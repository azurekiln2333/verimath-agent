"""Opt-in real-model + browser acceptance using only the synthetic calculus case.

Run from the repository root: python scripts/calculus_acceptance.py
Uses the configured model and a temporary empty knowledge database. Never index notes.
Outputs omit credentials, machine paths, raw reasoning and private sources.
"""
from __future__ import annotations

import argparse
import gc
import json
import math
import os
from pathlib import Path
import re
import socket
import sys
import tempfile
import threading
import time

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))


def events(text):
    result = []
    for chunk in text.split("\n\n"):
        lines = chunk.splitlines()
        name = next((v[7:] for v in lines if v.startswith("event: ")), "")
        data = next((v[6:] for v in lines if v.startswith("data: ")), "{}")
        if name:
            result.append((name, json.loads(data)))
    return result


def regenerate_canvas(output: Path, number: int):
    """Revise only a rejected Canvas through the model and the normal job/retry path."""
    import asyncio
    import hashlib
    os.environ['DATA_DIR'] = tempfile.mkdtemp(prefix='canvas-recheck-')
    import app.main as main
    report = json.loads((output / 'results.json').read_text(encoding='utf-8'))
    result = report['rounds'][0 if number == 1 else 2]
    sid = 'acceptance-calculus'
    mid = main.panel_store.begin_turn(sid, result['message_id'].rsplit(':', 1)[0], result['query'], {'route': 'concept'})
    main.panel_store.finish_turn(mid, result['content'], 'completed', {'route': 'concept'})
    focus = ('展示圆盘、竖直切线与极坐标面积元，优先解释题目。' if number == 1 else
             'Q是平面任意测试点，不能限制在原圆上。固定P=(1,1)、梯度(2,0)，自由拖动Q，显示位移、点积与夹角。'
             'Q=(1,2)时点积0但Q不在圆上；Q=(2,2)时为2；Q=(0,2)时为-2；Q=P时点积0但夹角未定义。'
             '提供带label的Q的x、y原生数值输入，输入值忠实保留，不能吸附回圆。')
    offer = main.panel_store.add_offer(sid, mid, {'tier': 'canvas', 'title': report['canvases'][number-1]['title'],
        'query': focus, 'context_hint': report['rounds'][0]['query'] + '\n' + report['rounds'][0]['content']})

    async def generate():
        await main.model_client.start()
        started = time.monotonic()
        previous = None
        try:
            for attempt in range(2):
                job = main.artifact_service.submit(sid, mid, offer['offer_id'], previous)
                while (current := main.panel_store.job(job['job_id']))['status'] in {'queued', 'running'}:
                    await asyncio.sleep(.25)
                print(json.dumps({'attempt': attempt + 1, 'status': current['status']}), flush=True)
                if current['status'] == 'succeeded':
                    spec = current['artifact']
                    assert spec.get('generation_source') == 'model' and not spec.get('fallback_template')
                    path = output / f'model-canvas-{number}.html'
                    rejected = output / f'model-canvas-{number}-rejected.html'
                    if not rejected.exists():
                        rejected.write_bytes(path.read_bytes())
                    path.write_text(spec['html'], encoding='utf-8')
                    report['canvases'][number-1] = {'message_id': mid, 'title': spec['title'], 'source': 'model',
                        'html_chars': len(spec['html']), 'status': 'succeeded',
                        'generation_seconds': round(time.monotonic()-started, 2),
                        'sha256': hashlib.sha256(spec['html'].encode()).hexdigest()}
                    report['status'] = 'reviewing_canvas_semantics'
                    report['canvas_revision_reason'] = '模型原图把切线测试点限制在圆上；通过模型重新生成自由测试点版本，待数值复核。'
                    (output / 'results.json').write_text(json.dumps(report, ensure_ascii=False, indent=2), encoding='utf-8')
                    print(json.dumps({'source': 'model', 'chars': len(spec['html']), 'seconds': round(time.monotonic()-started, 2)}), flush=True)
                    return
                previous = job['job_id']
            raise AssertionError('Model Canvas generation failed after one retry')
        finally:
            await main.artifact_service.stop()
            await main.model_client.aclose()
    asyncio.run(generate())


def run(output):
    import httpx
    import mpmath as mp
    import uvicorn
    from playwright.sync_api import sync_playwright, expect

    output.mkdir(parents=True, exist_ok=True)
    report = {"case": "圆的切线、梯度与极坐标换元", "rounds": [], "canvases": [], "checks": []}

    def save():
        (output / "results.json").write_text(json.dumps(report, ensure_ascii=False, indent=2), encoding="utf-8")

    def record(query, text, started):
        parsed = events(text)
        final = next(d for n, d in parsed if n == "final")
        result = {"query": query, "content": final["content"], "chars": len(final["content"]),
                  "seconds": round(time.monotonic() - started, 2), "message_id": final["message_id"],
                  "model_used": final["flags"].get("model_used", False),
                  "model_error": final["flags"].get("model_error"),
                  "tools": [d for n, d in parsed if n in {"tool_call", "tool_result"}],
                  "status": final["status"]}
        report["rounds"].append(result)
        save()
        print(json.dumps({"round": len(report["rounds"]), "seconds": result["seconds"], "chars": result["chars"],
                          "tools": [d["name"] for n, d in parsed if n == "tool_call"]}), flush=True)
        assert result["model_used"] and result["status"] == "completed", "Real model answer did not complete"
        return result

    with tempfile.TemporaryDirectory(prefix="calculus-live-") as data_dir:
        os.environ["DATA_DIR"] = data_dir
        os.environ["MODEL_ENABLED"] = "true"
        import app.main as main
        from app.demo_cases import CASES

        assert main.model_client.enabled, "Configured model unavailable"
        report['model'] = main.settings.model_name
        report['thinking_enabled'] = main.settings.model_thinking
        sid = "acceptance-calculus"
        with socket.socket() as sock:
            sock.bind(("127.0.0.1", 0))
            port = sock.getsockname()[1]
        server = uvicorn.Server(uvicorn.Config(main.app, host="127.0.0.1", port=port, log_level="error"))
        thread = threading.Thread(target=server.run, daemon=True)
        thread.start()
        for _ in range(200):
            if server.started:
                break
            time.sleep(.05)
        assert server.started
        base = f"http://127.0.0.1:{port}"
        client = httpx.Client(base_url=base, timeout=240)

        def state():
            return client.get("/api/panel/artifact-jobs", params={"session_id": sid}).json()

        def recommendations(result):
            deadline = time.monotonic() + 35
            while time.monotonic() < deadline:
                data = state()
                item = next((i for i in data["suggestions"] if i["message_id"] == result["message_id"]), None)
                if item and item["followups_state"] != "checking":
                    result["followups"] = item["followups"]
                    result["followups_state"] = item['followups_state']
                    save()
                    return data
                time.sleep(.25)
            raise AssertionError("Recommendations did not terminate")

        def ask(query):
            started = time.monotonic()
            chunks, buffer, first_delta = [], '', None
            with client.stream('POST', '/api/panel/chat/stream', json={"query": query, "session_id": sid,
                                    "use_model": True, "answer_style": "concise"}) as response:
                response.raise_for_status()
                for chunk in response.iter_text():
                    chunks.append(chunk)
                    buffer += chunk
                    while '\n\n' in buffer:
                        frame, buffer = buffer.split('\n\n', 1)
                        for name, data in events(frame):
                            if name == 'delta' and first_delta is None:
                                first_delta = round(time.monotonic() - started, 2)
                            if name == 'tool_call':
                                print(json.dumps({'tool': data['name'], 'operation': data.get('arguments', {}).get('operation'),
                                                  'seconds': round(time.monotonic()-started, 2)}), flush=True)
            result = record(query, ''.join(chunks), started)
            result['first_text_seconds'] = first_delta
            save()
            return result

        def wait_job(job_id):
            deadline = time.monotonic() + 250
            while time.monotonic() < deadline:
                item = next(j for j in state()["jobs"] if j["job_id"] == job_id)
                if item["status"] not in {"queued", "running"}:
                    assert item["status"] == "succeeded", item.get("error")
                    return item
                time.sleep(.5)
            raise AssertionError("Canvas deadline exceeded")

        try:
            initial = ask(next(c.question for c in CASES if c.id == "viz-calculus"))
            data = recommendations(initial)
            sums = [t["summary"] for t in initial["tools"] if "summary" in t and t["name"] == "calculate_calculus"]
            tangent = next(s for s in sums if s.get("operation") == "implicit_tangent")
            integral = next(s for s in sums if s.get("operation") == "integrate")
            assert tangent["vertical"] and tangent["at_point"] == ["2", "0"]
            assert integral["exact"] == "3*pi/2"
            from app.tools.calculus import calculate
            jacobian = calculate(dict(operation="jacobian", variables=["r", "theta"],
                                      mapping=["r*cos(theta)", "r*sin(theta)"]))
            assert jacobian['exact'] == 'r'
            report['independent_jacobian'] = jacobian['exact']
            assert not re.search(r"x\s*\+\s*y\s*=\s*2", initial["content"])
            assert not re.search(r"该点.{0,8}y.{0,6}(最大|极大)", initial['content']), 'Incorrect geometric extremum'
            independent = mp.quad(lambda y: mp.quad(lambda x: x*x + y*y,
                [-mp.sqrt(2*y-y*y), mp.sqrt(2*y-y*y)]), [0, 1, 2])
            assert abs(float(independent) - integral["numeric"]) < 1e-9
            report["independent_integral"] = float(independent)
            report["checks"].append("切线、雅可比、二重积分经工具核对，直角坐标数值积分独立复核")
            assert len(initial.get("followups", [])) >= 3

            with sync_playwright() as pw:
                browser = pw.chromium.launch()
                context = browser.new_context(viewport={"width": 1440, "height": 1000})
                page = context.new_page()
                page.set_default_timeout(15000)
                errors = []
                page.on("pageerror", lambda error: errors.append(str(error)))
                page.goto(base + "/dashboard")
                page.wait_for_function("window.verimath?.restoreSession")
                page.evaluate("sid=>verimath.restoreSession(sid)", sid)
                owner = page.locator('[data-message-id="' + initial["message_id"] + '"]')
                expect(owner.locator('.followup-question')).to_have_count(len(initial["followups"]))
                assert not owner.locator('code.language-latex,code.language-math,.katex-error').count()
                expect(owner.locator('.katex').first).to_be_visible()
                page.screenshot(path=str(output / "answer-and-questions.png"))

                owner.locator('.artifact-offer-btn').first.click()
                expect(owner.locator('.artifact-task-status')).to_contain_text('生成')
                first_job = next(j for j in state()["jobs"] if j["message_id"] == initial["message_id"])
                # Click an actual model-authored recommendation; this must make a fresh request.
                buttons = owner.locator('.followup-question')
                index = next((i for i in range(buttons.count()) if '梯度' in (buttons.nth(i).get_attribute('title') or '')), 0)
                button = buttons.nth(index)
                follow_query = button.get_attribute('title')
                started = time.monotonic()
                with page.expect_response(lambda r: r.url.endswith('/api/panel/chat/stream'), timeout=180000) as pending:
                    button.click()
                response = pending.value
                expect(page.locator('#stopGen')).to_be_hidden(timeout=180000)
                second = record(follow_query, response.text(), started)
                overlap = next(j for j in state()["jobs"] if j["job_id"] == first_job["job_id"])["status"]
                report["overlap_canvas_status_when_followup_completed"] = overlap
                assert overlap in {"queued", "running"}, "Canvas completed too soon to demonstrate independent overlap"
                assert response.request.post_data_json["session_id"] == sid
                report["checks"].append("点击模型推荐问题发起新一轮API调用，上一轮Canvas仍在生成")
                recommendations(second)
                page.evaluate('verimath.artifacts.sync()')

                confusion = ask("我卡在 (2,0)·(x-1,y-1)=0 这一步。这里两个向量分别是什么，为什么等于0就得到切线？"
                                "请用短句接上刚才的题，并提供一张能拖动点Q、观察位移和点积的交互图。")
                confusion_state = recommendations(confusion)
                offer = next(o for o in confusion_state["offers"] if o["message_id"] == confusion["message_id"])
                second_job = client.post('/api/panel/artifact-jobs', json={k: offer[k] for k in ('session_id', 'message_id', 'offer_id')}).json()
                jac = ask("继续这道题：为什么换成极坐标后面积元要乘雅可比行列式的绝对值？"
                          "我只会套公式，请从小矩形变成什么图形讲起，说明这里为什么是r。")
                recommendations(jac)
                polar = ask("这里所谓的三角换元，具体是怎样换的？为什么θ从0到π、r从0到2sinθ？"
                            "还有sin⁴θ的积分怎么算？请区分坐标变换与三角恒等变形，简洁解释。")
                recommendations(polar)

                for number, job in enumerate((first_job, second_job), 1):
                    completed = wait_job(job["job_id"])
                    artifact = completed["artifact"]
                    assert artifact["kind"] == 'html_canvas' and artifact.get('generation_source') == 'model'
                    assert not artifact.get('fallback_template')
                    (output / f"model-canvas-{number}.html").write_text(artifact['html'], encoding='utf-8')
                    report['canvases'].append({"message_id": job['message_id'], "title": artifact['title'],
                        "source": artifact['generation_source'], "html_chars": len(artifact['html']), "status": completed['status']})
                    save()
                # Reload the complete transcript to verify ownership and persistence.
                page.reload()
                expect(page.locator('.msg-row.assistant')).to_have_count(5)
                expect(page.locator('.followup-question').first).to_be_visible()
                for i, job in enumerate((first_job, second_job), 1):
                    row = page.locator('[data-message-id="' + job['message_id'] + '"]')
                    expect(row.locator('iframe')).to_have_count(1)
                    frame = row.frame_locator('iframe')
                    expect(frame.locator('body')).to_be_visible()
                    row.locator('iframe').scroll_into_view_if_needed()
                    controls = frame.locator('input[type=range], input[type=number]')
                    assert controls.count() > 0, 'Model Canvas needs an accessible adjustable parameter'
                    control = controls.first
                    before = control.input_value()
                    minimum = float(control.get_attribute('min') or 0)
                    maximum = float(control.get_attribute('max') or 100)
                    target = minimum if float(before) != minimum else maximum
                    control.fill(format(target, 'g'))
                    page.wait_for_timeout(150)
                    assert float(control.input_value()) == target
                    control.fill(before)
                    row.get_by_role('button', name='全屏查看').click()
                    assert control.input_value() == before
                    row.get_by_role('button', name='退出放大').click()
                    assert control.input_value() == before
                    page.wait_for_timeout(200)
                    frame_element = page.locator('[data-message-id="' + job['message_id'] + '"] iframe').element_handle().content_frame()
                    geometry = frame_element.evaluate('({width:innerWidth,scroll:document.documentElement.scrollWidth,height:document.documentElement.scrollHeight})')
                    assert geometry['scroll'] <= geometry['width'] + 2, geometry
                    report['canvases'][i-1]['desktop_geometry'] = geometry
                    row.locator('iframe').scroll_into_view_if_needed()
                    page.screenshot(path=str(output / f'model-canvas-{i}.png'))
                page.set_viewport_size({'width': 390, 'height': 844})
                page.wait_for_timeout(350)
                row = page.locator('[data-message-id="' + second_job['message_id'] + '"]')
                row.locator('iframe').scroll_into_view_if_needed()
                frame_element = row.locator('iframe').element_handle().content_frame()
                geometry = frame_element.evaluate('({width:innerWidth,scroll:document.documentElement.scrollWidth})')
                assert geometry['scroll'] <= geometry['width'] + 2, geometry
                page.screenshot(path=str(output / 'model-canvas-mobile.png'))
                report['checks'].append('两张图均为模型生成，参数可操作，放大返回保留参数，刷新恢复原回答归属，390px无横向溢出')
                assert errors == [], errors
                report['checks'].append('浏览器无未捕获JS错误；公式正常排版')
                context.close()
                browser.close()
            report['status'] = 'passed'
        except Exception as exc:
            report['status'] = 'failed'
            report['error'] = type(exc).__name__ + ': ' + str(exc)[:1200]
            raise
        finally:
            save()
            client.close()
            server.should_exit = True
            thread.join(timeout=10)
            gc.collect()
            lines = ['# 综合微积分案例真实模型验收', '', f"结果：{report.get('status', 'incomplete')}", '',
                     '测试使用独立空知识库，仅发送本案例及合成追问；不读取私人笔记。', '',
                     '| 轮次 | 正文字数（含公式标记） | 完成耗时（秒） |', '| --- | ---: | ---: |']
            lines += [f"| {i} | {r['chars']} | {r['seconds']} |" for i, r in enumerate(report['rounds'], 1)]
            lines += ['', *('- ' + c for c in report['checks'])]
            for i, r in enumerate(report['rounds'], 1):
                lines += ['', f'## 第{i}轮', '', r['query'], '', r['content'], '', '模型推荐：' + '；'.join(q['label'] for q in r.get('followups', []))]
            (output / 'report.md').write_text('\n'.join(lines), encoding='utf-8')
    print(json.dumps({'status': report['status'], 'rounds': len(report['rounds']), 'canvases': len(report['canvases'])}), flush=True)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--output', type=Path, default=ROOT / 'build/calculus-acceptance')
    parser.add_argument('--regenerate-canvas', type=int, choices=(1, 2))
    args = parser.parse_args()
    if args.regenerate_canvas:
        regenerate_canvas(args.output, args.regenerate_canvas)
    else:
        run(args.output)
