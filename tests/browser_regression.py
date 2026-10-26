"""Explicit real-browser regression; no external models or production data.

Run: python tests/browser_regression.py --output build/chat-regression
Requires the browser extra and `python -m playwright install chromium`.
"""
from __future__ import annotations

import argparse
import base64
import gc
import hashlib
import asyncio
import json
import os
from pathlib import Path
import socket
import sys
import tempfile
import threading
import time
from types import SimpleNamespace


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))


def run(output: Path, generated_dir: Path | None = None):
    from playwright.sync_api import expect, sync_playwright
    import uvicorn

    with tempfile.TemporaryDirectory(prefix="chat-browser-") as data_dir:
        os.environ["DATA_DIR"] = data_dir
        os.environ["MODEL_ENABLED"] = "false"
        import app.main as main
        from app.ocr import OcrError
        from app.ocr.service import OcrResult

        ocr = {'mode': 'ok', 'cancelled': 0, 'gate': None}
        @main.app.post('/__browser/ocr/{mode}')
        async def configure_ocr(mode: str):
            ocr['mode'] = mode
            if ocr['gate']:
                ocr['gate'].set()
            return {'ok': True}

        async def recognize(*args):
            if ocr['mode'] == 'fail':
                raise OcrError('识图服务暂时不可用，请重试')
            if ocr['mode'] == 'slow':
                ocr['gate'] = asyncio.Event()
                try:
                    await ocr['gate'].wait()
                except asyncio.CancelledError:
                    ocr['cancelled'] += 1
                    raise
            return OcrResult(text='求解 $2x+3=11$。', question_type='计算错误', model='fixture')
        main.ocr_service = SimpleNamespace(enabled=True, model='fixture', recognize=recognize)

        @main.app.post('/__browser/suggestions/{state}/{session_id}/{message_id}')
        async def suggestions(state: str, session_id: str, message_id: str):
            main.panel_store.patch_metadata(session_id, message_id, {
                'followups_state': state, 'followups_stage': 'reviewing', 'followups_error': ''})
            return {'followups_state': state}

        gates = {}
        specs = {}
        attempts = {}
        original_generate = main.artifact_service._generate
        html = """<!doctype html><html><head><style>
        body{color:var(--vm-ink);background:var(--vm-bg);font:16px system-ui}
        main{padding:16px;box-sizing:border-box}#space{height:280px}
        input{width:min(260px,90%)}button{padding:6px}h3{margin:0 0 12px}
        </style></head><body><main><h3>交互图解 · 示例数据</h3>
        <label>参数 <input id="parameter" type="range" min="1" max="10" value="3"></label>
        <output id="value">3</output><button id="shrink">收缩内容</button><div id="space"></div></main>
        <script>parameter.oninput=()=>value.textContent=parameter.value;
        shrink.onclick=()=>space.style.height='20px';</script></body></html>"""

        @main.app.post("/__browser/seed/{kind}")
        async def seed(kind: str):
            sid = "browser-" + kind
            mid = main.panel_store.begin_turn(sid, sid, "请解释这个概念", {"route": "concept"})
            text = """这是第一轮的回答，画布属于这条消息。行内公式 `\\(\\mu = 0\\)` 使用数学排版。Unicode 公式 `4·sin⁴θ` 也应正常阅读。

```latex
\\bar X = \\frac{1}{n}\\sum_{i=1}^{n} X_i
```

| 参数 | 含义 |
| --- | --- |
| n | 样本量 |

```python
print('代码仍使用代码排版')
```
"""
            main.panel_store.finish_turn(mid, text, "completed", {"route": "concept", "followups_state": "completed",
                "followups": [{"label": "置信区间如何理解？", "query": "什么是置信区间"},
                              {"label": "<img src=x onerror=alert(1)>", "query": "这是一条纯文本问题"}]})
            spec = {"kind": "html_canvas", "title": "交互图解", "caption": "示例数据", "html": main._inject_canvas_bridge(html), "height": 360}
            offer = main.panel_store.add_offer(sid, mid, {"tier": "canvas", "title": "交互图解", "caption": "示例数据"})
            specs[offer["offer_id"]] = spec
            gates[offer["offer_id"]] = asyncio.Event()
            attempts[offer["offer_id"]] = 0
            return {"session_id": sid, "message_id": mid, "offer_id": offer["offer_id"]}

        @main.app.post('/__browser/generated/{number}')
        async def seed_generated(number: int):
            if generated_dir is None or number not in (1, 2):
                raise ValueError('Supply --generated-dir with a completed real-model acceptance run')
            item = await seed('generated-' + str(number))
            # Replay the actual, unedited model output; do not count this as a model call.
            source = (generated_dir / f'model-canvas-{number}.html').read_text(encoding='utf-8')
            evidence = json.loads((generated_dir / 'results.json').read_text(encoding='utf-8'))
            original = next(r for r in evidence['rounds'] if r['message_id'] == evidence['canvases'][number-1]['message_id'])
            main.panel_store.finish_turn(item['message_id'], original['content'], 'completed', {
                'route': 'concept', 'followups_state': original.get('followups_state', 'completed'),
                'followups': original.get('followups', [])})
            specs[item['offer_id']] = {'kind': 'html_canvas', 'title': '真实模型生成图形复测',
                                     'caption': '已保存的真实模型产物', 'html': source, 'height': 420}
            gates[item['offer_id']].set()
            return item

        @main.app.post("/__browser/release/{offer_id}")
        async def release(offer_id: str):
            gates[offer_id].set()
            return {"ok": True}

        async def generate(job):
            if job["offer_id"] not in specs:
                return await original_generate(job)
            attempts[job["offer_id"]] += 1
            await gates[job["offer_id"]].wait()
            if job["session_id"] == "browser-retry" and attempts[job["offer_id"]] == 1:
                raise ValueError("fixture failure")
            if job['session_id'] == 'browser-runtime' and attempts[job['offer_id']] == 1:
                broken = html.replace('<script>parameter.oninput', '<script>const = broken;</script><script>parameter.oninput')
                return {**specs[job['offer_id']], 'html': main._inject_canvas_bridge(broken)}
            return specs[job["offer_id"]]

        main.artifact_service._generate = generate
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
        assert server.started, "Isolated browser server did not start"
        output.mkdir(parents=True, exist_ok=True)
        base = f"http://127.0.0.1:{port}"
        summary = {"layouts": [], "checks": []}
        try:
            with sync_playwright() as pw:
                browser = pw.chromium.launch()
                context = browser.new_context(viewport={"width": 1440, "height": 900}, device_scale_factor=1)
                page = context.new_page()
                errors = []
                page.on("pageerror", lambda error: errors.append(str(error)))
                page.add_init_script("window.__resizeReports=0;addEventListener('message',e=>{if(e.data?.source==='verimath-canvas'&&e.data.type==='resize')window.__resizeReports++})")
                page.goto(base + "/dashboard")
                expect(page.locator("#query")).to_be_visible()
                page.wait_for_function("window.verimath?.restoreSession && !document.querySelector('#send').hidden")
                assert not page.evaluate("verimath.layout.state.toolsOpen")

                for width in (390, 768, 1024, 1280, 1440, 1920):
                    page.set_viewport_size({"width": width, "height": 900 if width > 768 else 844})
                    page.evaluate("verimathSide.expand();verimathSide.setWidth(420);verimath.layout.closeTools()")
                    for opened in (False, True):
                        if opened:
                            page.locator("#studyToggle").click()
                        page.wait_for_timeout(300)
                        geometry = page.evaluate("""() => {
                          const main=document.querySelector('.main-wrap').getBoundingClientRect();
                          const msg=document.querySelector('.messages');const m=msg.getBoundingClientRect(),s=getComputedStyle(msg);
                          const input=document.querySelector('.composer-row').getBoundingClientRect();
                          return {chat:main.width,input:input.width,left:input.left,right:input.right,
                            messageLeft:m.left+parseFloat(s.paddingLeft),messageRight:m.right-parseFloat(s.paddingRight),
                            toolsDocked:document.documentElement.classList.contains('tools-docked'),
                            overflow:document.documentElement.scrollWidth>innerWidth};
                        }""")
                        assert geometry["chat"] >= min(640, width) - 1, (width, geometry)
                        assert geometry["input"] >= min(600, width - 32) - 50, (width, geometry)
                        assert abs(geometry["left"] - geometry["messageLeft"]) < 1
                        assert abs(geometry["right"] - geometry["messageRight"]) < 1
                        assert not geometry["overflow"], (width, geometry)
                        summary["layouts"].append({"viewport": width, "toolsOpen": opened, **geometry})
                    if width == 390:
                        page.locator("#studyClose").click()
                        page.locator("#drawerToggle").click()
                        expect(page.locator(".side")).to_have_class("side open")
                        page.locator("#drawerClose").click()
                        page.wait_for_timeout(300)
                        page.screenshot(path=str(output / "chat-mobile.png"))
                    page.evaluate("verimath.layout.closeTools()")

                    # Empty input stays compact; multiline input grows, caps and
                    # shrinks back without obscuring the image/send controls.
                    query_box = page.locator('#query')
                    query_box.fill('')
                    empty_height = page.locator('#composer').bounding_box()['height']
                    assert 80 <= empty_height <= 98, (width, empty_height)
                    query_box.fill('第一行\n第二行\n第三行')
                    assert page.locator('#composer').bounding_box()['height'] > empty_height + 35, (width, empty_height, query_box.evaluate("el=>({height:el.getBoundingClientRect().height,scrollHeight:el.scrollHeight,style:el.style.cssText,flex:getComputedStyle(el).flex,formHeight:el.form.getBoundingClientRect().height})"))
                    query_box.fill('\n'.join(f'第 {i} 行：核对积分区域与坐标变换' for i in range(40)))
                    assert query_box.bounding_box()['height'] <= 181
                    assert query_box.evaluate('el=>el.scrollHeight>el.clientHeight && getComputedStyle(el).overflowY==="auto"')
                    expect(page.locator('#composerAdd')).to_be_in_viewport()
                    expect(page.locator('#send')).to_be_in_viewport()
                    query_box.fill('')
                    assert abs(page.locator('#composer').bounding_box()['height'] - empty_height) < 1
                summary['checks'].append('compact composer: multiline growth, internal scroll and shrink at six widths')

                page.set_viewport_size({'width': 1440, 'height': 900})
                page.evaluate('verimathSide.setWidth(264)')
                page.wait_for_timeout(300)
                query_box.fill('这是一个较长的问题，需要检查缩窄窗口后的自动换行和高度。' * 3)
                wide_height = query_box.bounding_box()['height']
                page.set_viewport_size({'width': 390, 'height': 560})
                page.wait_for_timeout(350)
                assert query_box.bounding_box()['height'] > wide_height
                assert query_box.bounding_box()['height'] <= 141
                expect(page.locator('#send')).to_be_in_viewport()
                page.set_viewport_size({'width': 1440, 'height': 900})
                page.wait_for_timeout(350)
                assert abs(query_box.bounding_box()['height'] - wide_height) <= 1
                query_box.fill('')
                summary['checks'].append('composer reflows on width and available-height changes')

                page.set_viewport_size({"width": 1440, "height": 900})
                page.evaluate("verimathSide.setWidth(264)")
                page.wait_for_timeout(300)
                handle = page.locator('#sideResizer').bounding_box()
                page.mouse.move(handle['x'] + handle['width'] / 2, 180)
                page.mouse.down()
                page.mouse.move(330, 180, steps=8)
                page.mouse.up()
                page.wait_for_timeout(300)
                assert 320 <= page.locator('.side').bounding_box()['width'] <= 340
                page.locator('#sideCollapse').click()
                page.wait_for_timeout(300)
                assert page.locator('.main-wrap').bounding_box()['x'] < 1
                page.locator('#sideReveal').click()
                page.evaluate("verimathSide.setWidth(264)")
                page.emulate_media(reduced_motion='reduce')
                assert page.locator('body').evaluate("el=>parseFloat(getComputedStyle(el).transitionDuration)") < .01
                page.emulate_media(reduced_motion='no-preference')
                summary['checks'].append('pointer drag + collapse/expand + reduced motion')
                page.locator("#studyToggle").click()
                page.locator('[data-study-tab="cases"]').click()
                expect(page.locator("#caseList .katex").first).to_be_visible()
                assert "SimSun" in page.locator(".case-expect").first.evaluate("el=>getComputedStyle(el).fontFamily")
                page.screenshot(path=str(output / "tools-reading.png"))
                page.locator('[data-study-tab="verify"]').click()
                expect(page.locator('#verifyInstructions .katex')).to_have_count(2)
                assert not page.locator('#verifyInstructions code').count()
                assert '^' not in page.locator('#verifyInput').get_attribute('placeholder')
                expect(page.locator('#verifyPreview .katex')).to_have_count(3)
                page.locator("#verifyExample").click()
                assert 'x²' in page.locator('#verifyInput').input_value()
                expect(page.locator('#verifyPreview .katex')).to_have_count(3)
                page.screenshot(path=str(output / 'verify-math-preview.png'))
                page.locator("#verifyRun").click()
                expect(page.locator("#verifyResult .katex").first).to_be_visible()
                expect(page.locator('#verifyResult .verify-tag').first).to_have_text('等价 ✓')
                expect(page.locator('#verifyResult .verify-tag').nth(1)).to_have_text('不等价 ✗')
                page.locator('#verifyInput').fill('x³\nx^3')
                expect(page.locator('#verifyPreview .katex')).to_have_count(2)
                page.locator("#studyClose").click()
                summary["checks"].append("right panel serif and rendered formulas")

                # Image input remains a draft, with a review step before it enters chat.
                png = base64.b64decode('iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAQAAAC1HAwCAAAAC0lEQVR42mP8/x8AAwMCAO+jFRsAAAAASUVORK5CYII=')
                photo = {'name': 'synthetic-question.png', 'mimeType': 'image/png', 'buffer': png}
                initial_sid = page.evaluate('verimath.getSessionId()')
                initial_messages = page.locator('.msg-row').count()
                page.locator('#query').fill('先帮我看思路')
                for width in (390, 1440):
                    page.set_viewport_size({'width': width, 'height': 900})
                    page.wait_for_timeout(300)
                    page.locator('#composerAdd').click()
                    expect(page.locator('#composerMenu')).to_be_visible()
                    rect = page.locator('#composerMenu').bounding_box()
                    assert rect['x'] >= 0 and rect['x'] + rect['width'] <= width and rect['y'] > 0
                    assert page.evaluate('verimath.getSessionId()') == initial_sid
                    page.keyboard.press('Escape')
                page.locator('#photoInput').set_input_files(photo)
                expect(page.locator('#ocrRendered .katex')).to_be_visible()
                expect(page.locator('#query')).to_have_value('先帮我看思路')
                page.locator('#ocrEdit').click()
                page.locator('#ocrText').fill('求解 $2x+3=11$，解释每一步。')
                page.locator('#ocrEdit').click()
                expect(page.locator('#ocrRendered .katex')).to_be_visible()
                page.screenshot(path=str(output / 'ocr-review.png'))
                page.locator('#ocrInsert').click()
                expect(page.locator('#query')).to_have_value('先帮我看思路\n\n题目内容：\n求解 $2x+3=11$，解释每一步。')
                expect(page.locator('#ocrDialog')).to_be_hidden()
                assert page.locator('.msg-row').count() == initial_messages

                context.request.post(base + '/__browser/ocr/fail')
                page.locator('#photoInput').set_input_files(photo)
                expect(page.locator('#ocrRetry')).to_be_visible()
                expect(page.locator('#ocrInsert')).to_be_disabled()
                context.request.post(base + '/__browser/ocr/ok')
                page.locator('#ocrRetry').click()
                expect(page.locator('#ocrInsert')).to_be_enabled()
                page.locator('#ocrClose').click()
                page.locator('#ocrAttachment').click()
                expect(page.locator('#ocrDialog')).to_be_visible()
                context.request.post(base + '/__browser/ocr/slow')
                page.locator('#photoInput').set_input_files(photo)
                expect(page.locator('#ocrCancel')).to_be_visible()
                page.locator('#ocrCancel').click()
                expect(page.locator('#ocrStatus')).to_contain_text('已取消')
                context.request.post(base + '/__browser/ocr/ok')
                page.locator('#ocrRetry').click()
                expect(page.locator('#ocrInsert')).to_be_enabled()

                context.request.post(base + '/__browser/ocr/slow')
                with page.expect_request(lambda req: req.url.endswith('/api/coach/ocr')):
                    page.locator('#photoInput').set_input_files(photo)
                page.locator('#ocrClose').click()
                page.locator('#newConversation').click()
                page.wait_for_function('(sid)=>verimath.getSessionId()!==sid', arg=initial_sid)
                page.locator('#query').fill('新会话草稿')
                context.request.post(base + '/__browser/ocr/ok')
                page.wait_for_timeout(350)
                expect(page.locator('#query')).to_have_value('新会话草稿')
                expect(page.locator('#ocrAttachment')).to_be_hidden()
                page.evaluate('''b64=>{const bytes=Uint8Array.from(atob(b64), c=>c.charCodeAt(0));
                    const dt=new DataTransfer();dt.items.add(new File([bytes], 'pasted.png', {type:'image/png'}));
                    document.querySelector('#query').dispatchEvent(new ClipboardEvent('paste',{bubbles:true,clipboardData:dt}));}''', base64.b64encode(png).decode())
                expect(page.locator('#ocrInsert')).to_be_enabled()
                page.set_viewport_size({'width': 390, 'height': 844})
                page.screenshot(path=str(output / 'ocr-mobile.png'))
                assert page.locator('#ocrDialog').bounding_box()['width'] <= 390
                page.locator('#ocrInsert').click()
                assert page.locator('#query').input_value().startswith('新会话草稿\n\n题目内容：')
                page.set_viewport_size({'width': 1440, 'height': 900})
                summary['checks'].append('image menu semantics + OCR preview/math/edit + preserved draft + failure/cancel/retry + paste + session isolation')

                first = context.request.post(base + "/__browser/seed/slow").json()
                page.evaluate("sid=>localStorage.setItem('agent-session-id',sid)", first["session_id"])
                page.reload()
                expect(page.locator(".artifact-offer-btn")).to_be_visible()
                assert not context.request.get(base + "/api/panel/artifact-jobs", params={"session_id": first["session_id"]}).json()["jobs"]
                expect(page.locator(".msg.assistant .katex").first).to_be_visible()
                assert not page.locator('.msg.assistant p code').count()
                expect(page.locator(".msg.assistant pre code.language-python")).to_be_visible()
                assert not page.locator("code.language-latex").count()
                page.locator(".artifact-offer-btn").click()
                expect(page.locator(".artifact-task-status")).to_contain_text("生成")
                page.reload()
                expect(page.locator(".artifact-task-status")).to_contain_text("生成")
                page.locator('#query').fill('输入法草稿')
                page.locator('#query').dispatch_event('keydown', {'key': 'Enter', 'isComposing': True})
                expect(page.locator('.msg.assistant')).to_have_count(1)
                page.locator('#query').press('Shift+Enter')
                assert '\n' in page.locator('#query').input_value()
                expect(page.locator('.followup-question')).to_have_count(2)
                for _ in range(4):
                    page.evaluate('verimath.artifacts.sync()')
                expect(page.locator('.message-followups')).to_have_count(1)
                expect(page.locator('.artifact-host')).to_have_count(1)
                def set_suggestions(state):
                    context.request.post(base + f"/__browser/suggestions/{state}/{first['session_id']}/{first['message_id']}")
                set_suggestions('failed')
                page.evaluate('verimath.artifacts.sync()')
                expect(page.locator('.followup-retry')).to_be_visible()
                def retry_suggestions(route):
                    set_suggestions('checking')
                    route.fulfill(json={'followups_state': 'checking'})
                page.route('**/recommendations', retry_suggestions)
                page.locator('.followup-retry').click()
                expect(page.locator('.followup-state')).to_contain_text('正在')
                set_suggestions('completed')
                page.evaluate('verimath.artifacts.sync()')
                expect(page.locator('.followup-question')).to_have_count(2)
                page.unroute('**/recommendations', retry_suggestions)
                summary['checks'].append('suggestions polling is idempotent; failure retries independently')
                assert not page.locator('.message-followups img').count()
                with page.expect_request(lambda request: request.url.endswith('/api/panel/chat/stream')) as follow_request:
                    page.get_by_role('button', name='置信区间如何理解？', exact=True).click()
                assert follow_request.value.post_data_json['session_id'] == first['session_id']
                assert follow_request.value.post_data_json['query'] == '什么是置信区间'
                expect(page.locator(".msg.assistant")).to_have_count(2)
                expect(page.locator("#stopGen")).to_be_hidden(timeout=15000)
                assert not page.locator(".artifact").count()
                page.locator("#query").focus()
                page.evaluate("document.querySelector('#messages').scrollTop=0")
                context.request.post(base + "/__browser/release/" + first["offer_id"])
                owner = page.locator('[data-message-id="' + first["message_id"] + '"]')
                expect(owner.locator("iframe")).to_be_visible(timeout=15000)
                assert page.locator(".msg-row.assistant").nth(1).locator("iframe").count() == 0
                assert page.locator("#query").evaluate("el=>document.activeElement===el")
                assert page.locator("#messages").evaluate("el=>el.scrollTop") < 3
                bubble = page.locator('.msg.user').first
                assert abs(bubble.bounding_box()['x'] + bubble.bounding_box()['width'] - bubble.locator('..').bounding_box()['x'] - bubble.locator('..').bounding_box()['width']) < 1
                assert page.locator('.msg.assistant p').first.evaluate("el=>getComputedStyle(el).fontSize") == '16px'
                summary["checks"].append("slow Canvas + next chat + refresh + original ownership + no focus/scroll capture")
                summary['checks'].append('followup button sends a new contextual chat; persisted on refresh; labels render as text')

                frame = owner.frame_locator("iframe")
                frame.locator("#parameter").fill("8")
                expect(frame.locator("#value")).to_have_text("8")
                owner.get_by_role("button", name="全屏查看").click()
                expect(frame.locator("#parameter")).to_have_value("8")
                owner.get_by_role("button", name="退出放大").click()
                expect(frame.locator("#parameter")).to_have_value("8")
                frame.locator("#shrink").click()
                page.wait_for_timeout(700)
                height = owner.locator("iframe").evaluate("el=>el.getBoundingClientRect().height")
                assert 60 <= height <= 150, height
                count = page.evaluate("__resizeReports")
                page.wait_for_timeout(700)
                assert page.evaluate("__resizeReports") == count
                assert count < 15, count
                page.reload()
                owner = page.locator('[data-message-id="' + first["message_id"] + '"]')
                frame = owner.frame_locator("iframe")
                expect(frame.locator("#parameter")).to_have_value("8")
                page.screenshot(path=str(output / "chat-canvas.png"))
                with page.expect_download() as dl:
                    owner.get_by_role("button", name="下载 HTML").click()
                assert dl.value.suggested_filename.endswith(".html")
                summary["checks"].append("same Canvas when expanded + parameter restore + stable shrink bridge + export")

                native_row = page.locator('.msg-row.assistant').nth(1)
                native_row.locator('.artifact-offer-btn').click()
                expect(native_row.locator('canvas')).to_be_visible(timeout=15000)
                native_row.locator('input[type="range"]').first.fill('50')
                value = native_row.locator('input[type="range"]').first.input_value()
                page.evaluate("document.querySelector('#messages').scrollTop=document.querySelector('#messages').scrollHeight")
                read_position = page.locator('#messages').evaluate('el=>el.scrollTop')
                control = native_row.locator('input[type="range"]').first
                control_top = control.bounding_box()['y']
                control.click(position={'x': 80, 'y': 12})
                page.wait_for_timeout(100)
                assert abs(page.locator('#messages').evaluate('el=>el.scrollTop') - read_position) < 2
                assert abs(control.bounding_box()['y'] - control_top) < 2
                native_row.get_by_role('button', name='恢复初始参数').click()
                page.wait_for_timeout(100)
                assert abs(page.locator('#messages').evaluate('el=>el.scrollTop') - read_position) < 2
                native_row.get_by_role('button', name='全屏查看').click()
                page.wait_for_timeout(100)
                assert abs(page.locator('#messages').evaluate('el=>el.scrollTop') - read_position) < 2
                native_row.get_by_role('button', name='退出放大').click()
                page.wait_for_timeout(150)
                assert abs(page.locator('#messages').evaluate('el=>el.scrollTop') - read_position) < 2
                summary['checks'].append('chart controls/reset/expand at chat bottom keep reading position')
                control.fill('50')
                value = control.input_value()
                for width in (1440, 768, 390, 1280):
                    page.set_viewport_size({'width': width, 'height': 900})
                    page.wait_for_timeout(350)
                    pixels = native_row.locator('canvas').first.evaluate("el=>({w:el.width,h:el.height,cw:el.clientWidth,ch:el.clientHeight,dpr:devicePixelRatio})")
                    assert abs(pixels['w'] - pixels['cw'] * pixels['dpr']) <= 2, pixels
                    assert abs(pixels['h'] - pixels['ch'] * pixels['dpr']) <= 2, pixels
                page.reload()
                native_row = page.locator('.msg-row.assistant').nth(1)
                expect(native_row.locator('input[type="range"]').first).to_have_value(value)
                native_row.scroll_into_view_if_needed()
                page.screenshot(path=str(output / 'chat-statistical-canvas.png'))
                summary['checks'].append('native statistics Canvas pixel resolution on resize + parameter restore')

                second = context.request.post(base + "/__browser/seed/retry").json()
                page.evaluate("sid=>verimath.restoreSession(sid)", second["session_id"])
                page.locator(".artifact-offer-btn").click()
                context.request.post(base + "/__browser/release/" + second["offer_id"])
                expect(page.locator(".artifact-task-status")).to_have_text("生成失败", timeout=15000)
                page.get_by_role("button", name="重新生成").click()
                expect(page.locator("iframe")).to_be_visible(timeout=15000)
                jobs = context.request.get(base + "/api/panel/artifact-jobs", params={"session_id": second["session_id"]}).json()["jobs"]
                assert len(jobs) == 2 and [j["status"] for j in jobs] == ["failed", "succeeded"]
                page.locator("#query").fill("保留这个草稿")
                page.reload()
                expect(page.locator('#query')).to_have_value('保留这个草稿')
                page.evaluate("sid=>verimath.restoreSession(sid)", first["session_id"])
                expect(page.locator(".msg.assistant")).to_have_count(2)
                page.evaluate("sid=>verimath.restoreSession(sid)", second["session_id"])
                expect(page.locator("#query")).to_have_value("保留这个草稿")
                summary["checks"].append("failure retry + complete session switch + draft preservation")

                cancelled = context.request.post(base + "/__browser/seed/cancel").json()
                page.evaluate("sid=>verimath.restoreSession(sid)", cancelled["session_id"])
                page.locator(".artifact-offer-btn").click()
                expect(page.locator(".artifact-cancel")).to_be_visible()
                page.locator(".artifact-cancel").click()
                expect(page.locator(".artifact-task-status")).to_have_text("已取消")
                assert errors == [], errors
                summary["checks"].append("independent cancel; no browser JS errors")

                network = context.request.post(base + '/__browser/seed/network').json()
                page.evaluate('sid=>verimath.restoreSession(sid)', network['session_id'])
                page.locator('.artifact-offer-btn').click()
                expect(page.locator('.artifact-task-status')).to_contain_text('生成')
                context.set_offline(True)
                expect(page.locator('#artifactConnectionStatus')).to_be_visible(timeout=6000)
                context.request.post(base + '/__browser/release/' + network['offer_id'])
                context.set_offline(False)
                expect(page.locator('iframe')).to_be_visible(timeout=10000)
                assert len(context.request.get(base + '/api/panel/artifact-jobs', params={'session_id': network['session_id']}).json()['jobs']) == 1
                summary['checks'].append('offline polling recovery without duplicate generation')

                runtime = context.request.post(base + '/__browser/seed/runtime').json()
                page.evaluate('sid=>verimath.restoreSession(sid)', runtime['session_id'])
                page.locator('.artifact-offer-btn').click()
                context.request.post(base + '/__browser/release/' + runtime['offer_id'])
                expect(page.locator('.artifact-task-status')).to_have_text('画布运行异常', timeout=15000)
                expect(page.get_by_role('button', name='重新生成', exact=True)).to_be_visible()
                page.screenshot(path=str(output / 'canvas-recoverable-error.png'))
                page.get_by_role('button', name='重新生成', exact=True).evaluate('el=>{el.click();el.click()}')
                expect(page.frame_locator('iframe').locator('#parameter')).to_be_visible(timeout=15000)
                assert not page.locator('.artifact-frame-error').count()
                jobs = context.request.get(base + '/api/panel/artifact-jobs', params={'session_id': runtime['session_id']}).json()['jobs']
                assert len(jobs) == 2 and jobs[1]['retry_of'] == jobs[0]['job_id']
                assert all('Unexpected token' in error for error in errors), errors
                errors.clear()  # The deliberately broken fixture is the only allowed script error.
                summary['checks'].append('early generated-script failure is visible; regenerate creates one new successful attempt')
                if generated_dir:
                    summary['generated_geometry'] = []
                    for number in (1, 2):
                        item = context.request.post(base + f'/__browser/generated/{number}').json()
                        page.evaluate('sid=>verimath.restoreSession(sid)', item['session_id'])
                        page.locator('.artifact-offer-btn').click()
                        expect(page.locator('iframe')).to_be_visible(timeout=15000)
                        for width in (390, 768, 1024, 1440):
                            page.set_viewport_size({'width': width, 'height': 900 if width > 768 else 844})
                            page.wait_for_timeout(350)
                            page.locator('iframe').scroll_into_view_if_needed()
                            current_frame = page.frame_locator('iframe')
                            current_frame.locator('canvas').first.scroll_into_view_if_needed()
                            assert not page.locator('.artifact-frame-error').count()
                            geometry = page.evaluate('''() => {
                              const iframe=document.querySelector('iframe').getBoundingClientRect();
                              const box=document.querySelector('#messages');
                              const input=document.querySelector('.composer-row').getBoundingClientRect();
                              return {viewport:innerWidth,page:document.documentElement.scrollWidth,
                                iframeLeft:iframe.left,iframeRight:iframe.right,iframeWidth:iframe.width,
                                messagesWidth:box.clientWidth,messagesScroll:box.scrollWidth,messagesLeft:box.scrollLeft,
                                inputLeft:input.left,inputRight:input.right};
                            }''')
                            summary['generated_geometry'].append({'canvas': number, **geometry})
                            print(json.dumps({'canvas': number, **geometry}), flush=True)
                            assert geometry['page'] <= width, geometry
                            assert geometry['iframeLeft'] >= 0 and geometry['iframeRight'] <= width, geometry
                            assert abs(geometry['messagesLeft']) < 1, geometry
                            assert geometry['inputLeft'] >= 0 and geometry['inputRight'] <= width, geometry
                            page.screenshot(path=str(output / f'generated-{number}-{width}.png'))
                        reports_before = page.evaluate('__resizeReports')
                        page.wait_for_timeout(400)
                        assert page.evaluate('__resizeReports') == reports_before, 'Canvas height must settle after resizing'
                        frame = page.frame_locator('iframe')
                        control = frame.locator('input[type=range],input[type=number]').first
                        control.scroll_into_view_if_needed()
                        before_position = page.locator('#messages').evaluate('el=>el.scrollTop')
                        original = control.input_value()
                        target = control.get_attribute('max') or '2'
                        frame_obj = page.locator('iframe').element_handle().content_frame()
                        original_graph = frame_obj.evaluate("Array.from(document.querySelectorAll('canvas')).map(c=>c.toDataURL()).join('')")
                        control.fill(target)
                        page.wait_for_timeout(200)
                        changed_graph = frame_obj.evaluate("Array.from(document.querySelectorAll('canvas')).map(c=>c.toDataURL()).join('')")
                        assert changed_graph != original_graph, 'A changed control must redraw the graph'
                        assert abs(page.locator('#messages').evaluate('el=>el.scrollTop') - before_position) < 2
                        control.fill(original)
                        if number == 2:
                            # Gate the saved model artifact itself, against independently known geometry.
                            # These selectors refer to its inspected, unedited output, not product code.
                            qx, qy = frame.get_by_label('Q 的横坐标 x'), frame.get_by_label('Q 的纵坐标 y')
                            summary['point_semantics'] = []
                            for x, y, expected_dot, expected_angle in ((1, 2, 0, 90), (2, 2, 2, 45),
                                                                       (0, 2, -2, 135), (1, 1, 0, None)):
                                qx.fill(str(x)); qy.fill(str(y))
                                assert float(qx.input_value()) == x and float(qy.input_value()) == y
                                observed = float(frame.locator('#rd').inner_text())
                                angle = frame.locator('#ra').inner_text()
                                assert abs(observed - expected_dot) < .001
                                if expected_angle is None:
                                    assert '未定义' in angle
                                else:
                                    assert abs(float(angle.rstrip('°')) - expected_angle) < .1
                                summary['point_semantics'].append({'Q': [x, y], 'dot': observed, 'angle': angle})
                            qx.fill('2'); qy.fill('2')
                            page.wait_for_timeout(100)
                            page.reload()
                            frame = page.frame_locator('iframe')
                            expect(frame.locator('#qx')).to_have_value('2')
                            expect(frame.locator('#qy')).to_have_value('2')
                            expect(frame.locator('#rd')).to_have_text('2.00')
                            summary['checks'].append('free Q: zero/positive/negative dot products; zero displacement angle undefined; coordinates survive refresh')
                            page.set_viewport_size({'width': 390, 'height': 844})
                            page.wait_for_timeout(350)
                            frame.locator('#qx').scroll_into_view_if_needed()
                            focused_geometry = page.evaluate('''() => ({page:document.documentElement.scrollWidth,
                                left:document.querySelector('#messages').scrollLeft,
                                input:document.querySelector('.composer-row').getBoundingClientRect().left})''')
                            assert focused_geometry['page'] <= 390 and focused_geometry['left'] == 0
                            assert focused_geometry['input'] >= 0
                            page.screenshot(path=str(output / 'free-point-mobile.png'))
                        summary.setdefault('source_hashes', {})[str(number)] = hashlib.sha256(
                            (generated_dir / f'model-canvas-{number}.html').read_bytes()).hexdigest()
                    summary['checks'].append('actual generated Canvases: host layout at four widths; controls redraw without moving the conversation')
                context.close()
                browser.close()
        finally:
            server.should_exit = True
            thread.join(timeout=10)
            gc.collect()
        (output / "results.json").write_text(json.dumps(summary, ensure_ascii=False, indent=2), encoding="utf-8")
        print(json.dumps(summary, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, default=ROOT / "build/chat-regression")
    parser.add_argument('--generated-dir', type=Path)
    args = parser.parse_args()
    run(args.output, args.generated_dir)
