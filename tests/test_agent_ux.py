"""Failure boundaries for OCR, contextual suggestions and generated Canvas recovery."""
from __future__ import annotations

import asyncio
import base64
import json
from types import SimpleNamespace
from unittest.mock import AsyncMock

import httpx
import pytest

import app.main as main
from app.artifact_jobs import ArtifactService
from app.model_client import ModelMessage, OpenAICompatibleClient
from app.ocr.service import OcrError, OcrService, _decode_image
from app.panel_store import PanelStore
from app.settings import Settings
from app.skills.canvas_builder import _model_generate, validate_canvas


PNG = base64.b64decode('iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAQAAAC1HAwCAAAAC0lEQVR42mP8/x8AAwMCAO+jFRsAAAAASUVORK5CYII=')
IMAGE = 'data:image/png;base64,' + base64.b64encode(PNG).decode()
HTML = '<!doctype html><html><head></head><body><button>演示</button><script>let x=1;</script></body></html>'


def seed(store):
    mid = store.begin_turn('one', 'first', '如何理解正态分布？', {'route': 'concept'})
    store.finish_turn(mid, '均值决定中心，标准差决定分散程度。', 'completed', {'route': 'concept'})
    return mid


def test_ocr_uses_shared_multimodal_client_and_keeps_classification_out_of_draft(tmp_path):
    client = SimpleNamespace(enabled=True, complete=AsyncMock(return_value='求解 $2x+3=11$。\n疑问类型：计算错误'))
    service = OcrService(Settings(data_dir=tmp_path, ocr_model_name='vision-test'), client=client)
    result = asyncio.run(service.recognize(IMAGE))
    assert result.text == '求解 $2x+3=11$。' and result.question_type == '计算错误'
    args, kwargs = client.complete.call_args
    assert args[0][0].content[1]['image_url']['url'] == IMAGE
    assert kwargs['model'] == 'vision-test' and kwargs['thinking'] is False
    assert kwargs['max_tokens'] == 4096
    assert list((tmp_path / 'ocr').rglob('*.json'))
    assert not list(tmp_path.rglob('*.png'))


@pytest.mark.parametrize('image', [
    'data:image/jpeg;base64,' + base64.b64encode(PNG).decode(),
    'data:image/png;base64,' + base64.b64encode(b'not an image').decode(),
    'data:image/png;base64,' + 'A' * 11_184_816,
], ids=['mime-mismatch', 'invalid-content', 'too-large'])
def test_invalid_images_never_reach_the_model(tmp_path, image):
    client = SimpleNamespace(enabled=True, complete=AsyncMock())
    with pytest.raises(OcrError):
        asyncio.run(OcrService(Settings(data_dir=tmp_path), client=client).recognize(image))
    client.complete.assert_not_called()


def test_bare_base64_detects_actual_image_format():
    assert _decode_image(base64.b64encode(b'GIF89a' + b'fixture').decode())[1] == 'image/gif'


@pytest.mark.parametrize('status', [400, 401, 429, 503])
def test_ocr_upstream_errors_do_not_leak_response_or_connection_details(tmp_path, status):
    request = httpx.Request('POST', 'https://private.invalid/api')
    failure = httpx.HTTPStatusError('private diagnostic', request=request,
                                   response=httpx.Response(status, text='private diagnostic', request=request))
    client = SimpleNamespace(enabled=True, complete=AsyncMock(side_effect=failure))
    with pytest.raises(OcrError) as caught:
        asyncio.run(OcrService(Settings(data_dir=tmp_path), client=client).recognize(IMAGE))
    assert 'private' not in str(caught.value) and 'http' not in str(caught.value)


def test_ocr_disconnect_cancels_model_call(monkeypatch):
    async def run():
        cancelled = asyncio.Event()
        async def recognize(*args):
            try:
                await asyncio.Event().wait()
            finally:
                cancelled.set()
        monkeypatch.setattr(main, 'ocr_service', SimpleNamespace(recognize=recognize))
        result = await main.coach_ocr(main.OcrRequest(image=IMAGE), SimpleNamespace(is_disconnected=AsyncMock(return_value=True)))
        assert not result['ok'] and cancelled.is_set()
    asyncio.run(run())


@pytest.mark.parametrize('reason', ['length', 'content_filter'])
def test_incomplete_nonstream_output_is_not_accepted(monkeypatch, reason):
    def respond(request):
        return httpx.Response(200, json={'choices': [{'message': {'content': HTML}, 'finish_reason': reason}]})
    monkeypatch.setattr(httpx, 'AsyncHTTPTransport', lambda **kwargs: httpx.MockTransport(respond))
    async def run():
        client = OpenAICompatibleClient(Settings(model_enabled=True, model_api_key='fixture'))
        await client.start()
        try:
            with pytest.raises(RuntimeError, match='model_output_incomplete'):
                await client.complete([ModelMessage('user', '演示')])
        finally:
            await client.aclose()
    asyncio.run(run())


def test_canvas_repairs_truncation_once_and_preserves_valid_javascript():
    complete = AsyncMock(side_effect=['```html\n<html><body><script>let x=', f'```html\n{HTML}\n```'])
    spec = asyncio.run(_model_generate('演示参数', '', SimpleNamespace(complete=complete), None))
    assert spec['html'] == HTML and complete.await_count == 2
    incomplete = SimpleNamespace(complete=AsyncMock(return_value='<html><body><script>'))
    assert asyncio.run(_model_generate('演示参数', '', incomplete, None)) is None
    assert incomplete.complete.await_count == 2
    valid = HTML.replace('let x=1;', 'const parent = document.body; parent.dataset.ok="1";')
    assert 'parent.dataset.ok' in validate_canvas({'kind': 'html_canvas', 'html': valid})['html']


def test_canvas_network_failure_does_not_trigger_blind_regeneration():
    client = SimpleNamespace(complete=AsyncMock(side_effect=httpx.ConnectError('fixture')))
    assert asyncio.run(_model_generate('演示参数', '', client, None)) is None
    assert client.complete.await_count == 1


def test_saved_canvas_gets_one_early_bridge_without_mutating_stored_result():
    old = HTML.replace('</body>', '<script data-verimath-bridge>/* old bridge */</script></body>')
    job = {'artifact': {'kind': 'html_canvas', 'html': old}}
    prepared = main._prepare_client_job(job)['artifact']['html']
    assert prepared.count('<script data-verimath-bridge>') == 1
    assert prepared.count('data-verimath-policy') == 1
    assert prepared.index('data-verimath-bridge') < prepared.index('let x=1;')
    assert main._inject_canvas_bridge(prepared) == prepared
    assert job['artifact']['html'] == old


def test_successful_but_broken_canvas_can_be_regenerated_idempotently(tmp_path):
    store = PanelStore(tmp_path / 'panel.sqlite')
    mid = seed(store)
    offer = store.add_offer('one', mid, {'tier': 'canvas', 'title': '图解'})
    job = store.create_job('one', mid, offer['offer_id'])
    store.claim_job()
    store.finish_job(job['job_id'], 'succeeded', {'kind': 'html_canvas', 'html': HTML})
    assert store.create_job('one', mid, offer['offer_id'])['job_id'] == job['job_id']
    retried = store.create_job('one', mid, offer['offer_id'], job['job_id'])
    assert retried['job_id'] != job['job_id']
    assert store.create_job('one', mid, offer['offer_id'], job['job_id'])['job_id'] == retried['job_id']


def test_queued_recommendations_cancel_to_a_terminal_state(tmp_path):
    async def run():
        store = PanelStore(tmp_path / 'panel.sqlite')
        mid = seed(store)
        complete = AsyncMock()
        service = ArtifactService(store, SimpleNamespace(enabled=True, complete=complete))
        service.discovery_slots = asyncio.Semaphore(0)
        service.discover('one', mid)
        await asyncio.sleep(0)
        assert store.artifact_state('one')['pending']
        await service.stop()
        assert store.message('one', mid)['followups_state'] == 'interrupted'
        assert not store.artifact_state('one')['pending']
        complete.assert_not_called()
    asyncio.run(run())


def test_completed_recommendations_only_regenerate_on_explicit_retry(tmp_path):
    async def run():
        store = PanelStore(tmp_path / 'panel.sqlite')
        mid = seed(store)
        complete = AsyncMock(return_value=json.dumps({'suitable': False, 'followups': []}))
        service = ArtifactService(store, SimpleNamespace(enabled=True, complete=complete))
        service.discover('one', mid)
        await asyncio.gather(*service.discoveries.values())
        calls = complete.await_count
        service.discover('one', mid)
        assert not service.discoveries and complete.await_count == calls
        service.discover('one', mid, retry=True)
        service.discover('one', mid, retry=True)
        await asyncio.gather(*service.discoveries.values())
        assert complete.await_count == calls + 1
        await service.stop()
    asyncio.run(run())


def test_recommendation_retry_checks_message_ownership_and_status(tmp_path, monkeypatch):
    store = PanelStore(tmp_path / 'panel.sqlite')
    mid = seed(store)
    service = ArtifactService(store, SimpleNamespace(enabled=True, complete=AsyncMock(return_value='{"suitable":false,"followups":[]}')))
    monkeypatch.setattr(main, 'panel_store', store)
    monkeypatch.setattr(main, 'artifact_service', service)
    monkeypatch.setattr(main, 'model_client', service.client)
    async def run():
        async with httpx.AsyncClient(transport=httpx.ASGITransport(app=main.app), base_url='http://test') as client:
            assert (await client.post(f'/api/panel/sessions/other/messages/{mid}/recommendations')).status_code == 404
            assert (await client.post('/api/panel/sessions/one/messages/first:user/recommendations')).status_code == 404
            response = await client.post(f'/api/panel/sessions/one/messages/{mid}/recommendations')
            assert response.status_code == 202 and response.json()['followups_state'] == 'checking'
            await asyncio.gather(*service.discoveries.values())
            store.finish_turn(mid, 'partial', 'interrupted', {})
            assert (await client.post(f'/api/panel/sessions/one/messages/{mid}/recommendations')).status_code == 409
        await service.stop()
    asyncio.run(run())
