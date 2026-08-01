PANEL_HTML = r"""<!doctype html>
<html lang="zh-CN">
<head>
  <meta charset="utf-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1" />
  <title>VeriMath Agent · 数学与统计学习导师</title>
  <link rel="icon" href="data:," />
  <link rel="stylesheet" href="/static/vendor/katex.min.css" />
  <link rel="stylesheet" href="/static/vendor/fonts/fonts.css" />
  <!-- 图标改为内联 SVG（icons.js，同步加载确保内联脚本可用），主题字体本地托管 -->
  <script src="/static/icons.js"></script>
  <script defer src="/static/vendor/markdown-it.min.js"></script>
  <script defer src="/static/vendor/purify.min.js"></script>
  <script defer src="/static/vendor/katex.min.js"></script>
  <script defer src="/static/vendor/auto-render.min.js"></script>
  <!-- 可视化件：statlib 必须先加载（plot 与 widgets 都依赖它） -->
  <script defer src="/static/statlib.js"></script>
  <script defer src="/static/plot.js"></script>
  <script defer src="/static/widgets.js"></script>
  <style>
    :root {
      --bg: #faf9f4;
      --surface: #ffffff;
      --surface-2: #efeee9;
      --surface-3: #f5f4ef;
      --surface-4: #e9e8e3;
      --ink: #1b1c19;
      --muted: #42493e;
      --line: #c2c9bb;
      --line-soft: #e3e3de;
      --accent: #2d5a27;
      --accent-2: #3f6833;
      --accent-container: #bdedaa;
      --accent-soft: #eef4ea;
      --warn: #ba1a1a;
      --ok: #2d5a27;
      --radius: 8px;
      --radius-sm: 4px;
      --serif: 'Libre Caslon Text', Georgia, serif;
      --sans: 'Inter', system-ui, -apple-system, sans-serif;
      --mono: 'JetBrains Mono', ui-monospace, Consolas, monospace;
      --shadow: 0 1px 8px rgba(27, 28, 25, 0.05);
      --shadow-md: 0 6px 20px rgba(27, 28, 25, 0.08);
    }

    * { box-sizing: border-box; }

    body {
      margin: 0;
      min-height: 100vh;
      background: var(--bg);
      color: var(--ink);
      font: 15px/1.65 var(--sans);
      -webkit-font-smoothing: antialiased;
    }

    #glcanvas {
      position: fixed;
      top: 0; left: 0;
      width: 100vw;
      height: 100vh;
      z-index: -1;
      pointer-events: none;
    }

    button, textarea, input { font: inherit; }

    /* 内联 SVG 图标：继承父级 currentColor，随字号缩放 */
    .icon {
      display: inline-block;
      width: 1em;
      height: 1em;
      vertical-align: middle;
      fill: currentColor;
      flex-shrink: 0;
    }
    .icon-slot { display: inline-flex; align-items: center; justify-content: center; line-height: 1; }

    /* ---------- 顶栏 ---------- */
    .topbar {
      position: fixed;
      top: 0; left: 0; right: 0;
      height: 64px;
      background: rgba(250, 249, 244, 0.82);
      backdrop-filter: blur(14px);
      -webkit-backdrop-filter: blur(14px);
      border-bottom: 1px solid var(--line-soft);
      box-shadow: 0 1px 8px rgba(27, 28, 25, 0.03);
      z-index: 50;
      display: flex;
      align-items: center;
      gap: 20px;
      padding: 0 28px;
    }

    .brand {
      display: flex;
      align-items: center;
      gap: 10px;
      flex: 0 0 auto;
    }

    .logo {
      width: 34px;
      height: 34px;
      border-radius: var(--radius-sm);
      background: var(--accent);
      color: #fff;
      display: flex;
      align-items: center;
      justify-content: center;
      font-family: var(--serif);
      font-weight: 700;
      font-size: 17px;
      box-shadow: var(--shadow);
      flex-shrink: 0;
    }

    .brand h1 {
      margin: 0;
      font-family: var(--serif);
      font-size: 20px;
      font-weight: 600;
      color: var(--accent);
      letter-spacing: -0.01em;
      line-height: 1.1;
    }

    .brand .subtle {
      font-size: 11px;
      letter-spacing: 0.06em;
      text-transform: uppercase;
      color: var(--muted);
      font-family: var(--mono);
    }

    #topPills {
      display: flex;
      align-items: center;
      gap: 8px;
      flex-wrap: wrap;
      flex: 1 1 auto;
      justify-content: flex-end;
    }

    /* ---------- 三栏骨架 ---------- */
    .shell {
      display: grid;
      grid-template-columns: 282px minmax(0, 1fr) 340px;
      height: 100vh;
      padding-top: 64px;
      overflow: hidden;
    }

    .side, .inspect {
      background: rgba(255, 255, 255, 0.72);
      backdrop-filter: blur(6px);
      -webkit-backdrop-filter: blur(6px);
      overflow: auto;
      padding: 20px 18px;
      scrollbar-width: thin;
      scrollbar-color: var(--line) transparent;
    }

    .side { border-right: 1px solid var(--line-soft); }
    .inspect { border-left: 1px solid var(--line-soft); }

    .side::-webkit-scrollbar,
    .inspect::-webkit-scrollbar,
    .messages::-webkit-scrollbar { width: 7px; }
    .side::-webkit-scrollbar-thumb,
    .inspect::-webkit-scrollbar-thumb,
    .messages::-webkit-scrollbar-thumb { background: var(--line); border-radius: 4px; }

    .main {
      display: grid;
      grid-template-rows: 1fr auto;
      min-width: 0;
      overflow: hidden;
    }

    /* ---------- 消息区 ---------- */
    .messages {
      padding: 30px 36px;
      overflow: auto;
      display: flex;
      flex-direction: column;
      gap: 18px;
      min-height: 0;
      scrollbar-width: thin;
      scrollbar-color: var(--line) transparent;
    }

    .msg {
      max-width: 780px;
      padding: 15px 20px;
      border-radius: 12px;
      box-shadow: var(--shadow);
      overflow-wrap: anywhere;
      white-space: pre-wrap;
      animation: msgIn 0.18s ease;
    }

    @keyframes msgIn {
      from { opacity: 0; transform: translateY(4px); }
      to { opacity: 1; transform: translateY(0); }
    }

    .msg.user {
      align-self: flex-end;
      background: var(--accent);
      color: #fff;
      border-bottom-right-radius: 4px;
    }

    .msg.assistant {
      align-self: flex-start;
      background: var(--surface);
      color: var(--ink);
      border: 1px solid var(--line-soft);
      border-bottom-left-radius: 4px;
    }

    .msg.pending {
      background: var(--surface-3);
      border: 1px dashed var(--line);
      color: var(--muted);
    }

    .markdown { white-space: normal; }
    .markdown h1, .markdown h2, .markdown h3, .markdown h4 {
      font-family: var(--serif);
      margin: 14px 0 8px;
      line-height: 1.3;
      color: var(--ink);
    }
    .markdown h1 { font-size: 22px; }
    .markdown h2 { font-size: 19px; }
    .markdown h3 { font-size: 17px; }
    .markdown h4 { font-size: 15.5px; }
    .markdown p { margin: 9px 0; }
    .markdown ul, .markdown ol { margin: 8px 0; padding-left: 22px; }
    .markdown li { margin: 4px 0; }
    .markdown blockquote {
      margin: 10px 0;
      padding: 8px 14px;
      border-left: 3px solid var(--accent);
      background: var(--accent-soft);
      color: var(--muted);
      border-radius: 0 6px 6px 0;
    }
    .markdown pre {
      margin: 10px 0;
      padding: 12px;
      background: #1b1c19;
      color: #eef4e8;
      border-radius: var(--radius-sm);
      overflow: auto;
      font-size: 12.5px;
      line-height: 1.5;
      font-family: var(--mono);
    }
    .markdown code { font-family: var(--mono); font-size: 0.92em; }
    .markdown :not(pre) > code {
      background: var(--surface-2);
      border: 1px solid var(--line-soft);
      border-radius: 4px;
      padding: 1px 5px;
      color: var(--accent);
    }
    .markdown table {
      width: 100%;
      border-collapse: collapse;
      margin: 10px 0;
      font-size: 13px;
      display: block;
      overflow-x: auto;
    }
    .markdown th, .markdown td {
      border: 1px solid var(--line-soft);
      padding: 7px 9px;
      text-align: left;
      vertical-align: top;
    }
    .markdown th { background: var(--surface-3); font-weight: 700; }
    .markdown a {
      color: var(--accent);
      text-decoration: none;
      border-bottom: 1px solid rgba(45, 90, 39, 0.35);
    }
    .markdown hr { border: 0; border-top: 1px solid var(--line-soft); margin: 14px 0; }

    .markdown mjx-container {
      font-size: 102%;
      line-height: 1.35;
      max-width: 100%;
      overflow-x: auto;
      overflow-y: hidden;
      padding: 2px 0;
    }
    .markdown mjx-container[display="true"] {
      font-size: 104%;
      margin: 12px 0 !important;
      padding: 10px 12px;
      background: var(--surface-3);
      border: 1px solid var(--line-soft);
      border-radius: var(--radius-sm);
    }

    .typing-dots {
      display: inline-flex;
      gap: 3px;
      margin-left: 6px;
      vertical-align: middle;
    }
    .typing-dots span {
      width: 5px; height: 5px;
      border-radius: 50%;
      background: var(--accent);
      opacity: 0.35;
      animation: pulse 1s infinite ease-in-out;
    }
    .typing-dots span:nth-child(2) { animation-delay: 0.15s; }
    .typing-dots span:nth-child(3) { animation-delay: 0.3s; }
    @keyframes pulse {
      0%, 80%, 100% { opacity: 0.25; transform: translateY(0); }
      40% { opacity: 1; transform: translateY(-2px); }
    }

    /* ---------- 输入栏 ---------- */
    .composer {
      border-top: 1px solid var(--line-soft);
      background: rgba(255, 255, 255, 0.92);
      backdrop-filter: blur(8px);
      padding: 14px 32px 18px;
      display: flex;
      flex-direction: column;
      gap: 10px;
    }
    .composer-row {
      display: grid;
      grid-template-columns: 1fr auto auto;
      gap: 10px;
      align-items: end;
    }

    .composer textarea {
      grid-column: 1 / -1;
      width: 100%;
      min-height: 68px;
      max-height: 180px;
      resize: vertical;
      border: 1px solid var(--line-soft);
      border-radius: var(--radius);
      padding: 12px 14px;
      color: var(--ink);
      background: var(--surface);
      outline: none;
      font-family: var(--sans);
    }
    .composer textarea:focus {
      border-color: var(--accent);
      box-shadow: 0 0 0 3px rgba(45, 90, 39, 0.12);
    }

    .send {
      min-width: 92px;
      min-height: 42px;
      border: 0;
      border-radius: var(--radius);
      background: var(--accent);
      color: #fff;
      font-weight: 600;
      font-family: var(--sans);
      cursor: pointer;
      padding: 10px 16px;
      display: inline-flex;
      align-items: center;
      gap: 6px;
      box-shadow: var(--shadow);
      transition: transform 0.12s, background 0.15s;
    }
    .send:hover { background: var(--accent-2); transform: translateY(-1px); }
    .send:disabled { background: var(--muted); cursor: wait; transform: none; }
    /* 停止按钮：流式生成时出现，warn 色提示「中断」语义 */
    .send.stop { background: var(--warn); }
    .send.stop:hover { background: #8a1212; transform: translateY(-1px); }
    .send.stop[hidden] { display: none; }

    #clearContext {
      background: var(--surface-3);
      color: var(--muted);
      border: 1px solid var(--line-soft);
    }
    #clearContext:hover { background: var(--surface-2); color: var(--ink); }

    /* ---------- 侧栏通用 ---------- */
    .section { margin-bottom: 20px; }
    .section h2 {
      margin: 0 0 10px;
      font-family: var(--serif);
      font-size: 14px;
      font-weight: 600;
      color: var(--ink);
      letter-spacing: 0;
      display: flex;
      align-items: center;
      gap: 6px;
    }
    .section h2 .icon { font-size: 16px; color: var(--accent); }

    .subtle { color: var(--muted); font-size: 12px; }

    .status-grid { display: grid; gap: 8px; }
    .metric {
      border: 1px solid var(--line-soft);
      border-radius: var(--radius-sm);
      padding: 9px 11px;
      background: var(--surface);
    }
    .metric b {
      display: block;
      font-size: 10.5px;
      color: var(--muted);
      font-weight: 600;
      letter-spacing: 0.05em;
      text-transform: uppercase;
      font-family: var(--mono);
    }
    .metric span {
      display: block;
      margin-top: 3px;
      font-size: 14px;
      font-weight: 600;
      overflow-wrap: anywhere;
    }

    .pill {
      display: inline-flex;
      align-items: center;
      min-height: 26px;
      padding: 3px 10px;
      border: 1px solid var(--line-soft);
      border-radius: 999px;
      background: var(--surface);
      color: var(--muted);
      font-size: 11.5px;
      font-family: var(--mono);
      white-space: nowrap;
    }
    .pill.ok { color: var(--ok); border-color: var(--accent-container); background: var(--accent-soft); }
    .pill.warn { color: var(--warn); border-color: #edc4a7; background: #fdf3ec; }

    /* 开关 */
    .toggle-row {
      display: flex;
      align-items: center;
      justify-content: space-between;
      gap: 10px;
      padding: 10px 12px;
      border: 1px solid var(--line-soft);
      border-radius: var(--radius-sm);
      background: var(--surface);
    }
    .toggle-row .label-block { display: flex; flex-direction: column; }
    .toggle-row b { font-size: 13px; font-weight: 600; color: var(--ink); }
    .switch { position: relative; width: 42px; height: 24px; flex: 0 0 auto; }
    .switch input { opacity: 0; width: 0; height: 0; }
    .slider {
      position: absolute; inset: 0; cursor: pointer;
      background: var(--line); border-radius: 999px; transition: 0.15s;
    }
    .slider:before {
      content: ""; position: absolute;
      width: 18px; height: 18px; left: 3px; top: 3px;
      background: #fff; border-radius: 50%;
      box-shadow: 0 1px 4px rgba(0,0,0,0.2); transition: 0.15s;
    }
    .switch input:checked + .slider { background: var(--accent); }
    .switch input:checked + .slider:before { transform: translateX(18px); }

    /* 分段选择 */
    .segmented {
      display: grid;
      grid-template-columns: repeat(3, 1fr);
      border: 1px solid var(--line-soft);
      border-radius: var(--radius-sm);
      overflow: hidden;
      background: var(--surface);
    }
    .segment {
      min-height: 36px;
      border: 0;
      border-right: 1px solid var(--line-soft);
      background: var(--surface);
      color: var(--muted);
      cursor: pointer;
      font-weight: 550;
    }
    .segment:last-child { border-right: 0; }
    .segment.active { background: var(--accent); color: #fff; }

    /* 快捷指令 */
    .quick-list { display: grid; gap: 7px; }
    .quick {
      width: 100%;
      min-height: 38px;
      border: 1px solid var(--line-soft);
      border-radius: var(--radius-sm);
      background: var(--surface);
      color: var(--ink);
      text-align: left;
      padding: 8px 11px;
      cursor: pointer;
      font-size: 12.5px;
      transition: border-color 0.12s, background 0.12s;
    }
    .quick:hover { border-color: var(--accent); background: var(--accent-soft); }

    /* 语料分布 */
    .course-list { display: grid; gap: 6px; }
    .course-row {
      display: flex;
      justify-content: space-between;
      gap: 10px;
      border-bottom: 1px solid var(--line-soft);
      padding-bottom: 5px;
      font-size: 12.5px;
    }
    .course-row span { overflow-wrap: anywhere; }
    .course-row b { color: var(--accent); font-family: var(--mono); }

    /* 上下文 */
    .ctx-summary {
      display: flex;
      align-items: center;
      gap: 8px;
      margin-bottom: 10px;
    }
    .ctx-badge {
      display: inline-flex;
      align-items: center;
      justify-content: center;
      min-width: 30px;
      height: 26px;
      padding: 0 8px;
      border-radius: 999px;
      background: var(--accent);
      color: #fff;
      font-weight: 700;
      font-family: var(--mono);
      font-size: 13px;
    }
    .ctx-badge.empty { background: var(--surface-2); color: var(--muted); }
    .ctx-turns { display: grid; gap: 6px; max-height: 220px; overflow: auto; }
    .ctx-turn {
      border-left: 2px solid var(--line);
      padding: 5px 9px;
      font-size: 11.5px;
    }
    .ctx-turn.user { border-left-color: var(--accent); }
    .ctx-turn.assistant { border-left-color: var(--accent-container); }
    .ctx-turn-role {
      font-family: var(--mono);
      font-size: 10px;
      text-transform: uppercase;
      letter-spacing: 0.05em;
      color: var(--muted);
    }
    .ctx-turn-preview { color: var(--ink); margin-top: 2px; overflow-wrap: anywhere; }

    /* 记录列表 */
    .record-list { display: grid; gap: 6px; }
    .record-item {
      border: 1px solid var(--line-soft);
      border-radius: var(--radius-sm);
      background: var(--surface);
      padding: 8px 10px;
      cursor: pointer;
      transition: border-color 0.12s, background 0.12s;
    }
    .record-item:hover { border-color: var(--accent); background: var(--accent-soft); }
    .record-title {
      font-size: 12.5px;
      font-weight: 600;
      color: var(--ink);
      overflow-wrap: anywhere;
      line-height: 1.35;
    }
    .record-meta {
      display: flex;
      gap: 8px;
      flex-wrap: wrap;
      margin-top: 4px;
      font-size: 10.5px;
      color: var(--muted);
      font-family: var(--mono);
    }

    /* ---------- 右侧诊断 ---------- */
    .inspector-block {
      border: 1px solid var(--line-soft);
      border-radius: var(--radius-sm);
      background: var(--surface);
      padding: 11px;
      margin-bottom: 12px;
      box-shadow: var(--shadow);
    }
    .source {
      border-top: 1px solid var(--line-soft);
      padding-top: 10px;
      margin-top: 10px;
    }
    .source:first-child { border-top: 0; padding-top: 0; margin-top: 0; }
    .source-title { font-weight: 600; margin-bottom: 4px; overflow-wrap: anywhere; font-size: 12.5px; }
    .source-text {
      color: var(--muted);
      font-size: 11.5px;
      max-height: 110px;
      overflow: auto;
      white-space: pre-wrap;
      background: var(--surface-3);
      border: 1px solid var(--line-soft);
      border-radius: 4px;
      padding: 7px;
      margin-top: 5px;
    }
    pre.raw {
      margin: 0;
      white-space: pre-wrap;
      overflow-wrap: anywhere;
      font-size: 11px;
      color: var(--ink);
      background: var(--surface-3);
      border: 1px solid var(--line-soft);
      border-radius: 4px;
      padding: 8px;
      max-height: 240px;
      overflow: auto;
      font-family: var(--mono);
    }

    /* ---------- 可视化件（artifact 滑块卡片） ---------- */
    .artifact {
      align-self: flex-start;
      max-width: 720px;
      width: 100%;
      border: 1px solid var(--line-soft);
      border-radius: var(--radius);
      background: var(--surface);
      box-shadow: var(--shadow-md);
      overflow: hidden;
      margin-top: 4px;
    }
    .artifact-head {
      padding: 12px 16px;
      background: var(--accent-soft);
      border-bottom: 1px solid var(--line-soft);
    }
    .artifact-title {
      font-family: var(--serif);
      font-size: 15px;
      font-weight: 600;
      color: var(--accent);
    }
    .artifact-caption {
      font-size: 12px;
      color: var(--muted);
      margin-top: 3px;
      line-height: 1.5;
    }
    .artifact-canvas {
      padding: 14px 16px;
      background: var(--surface);
      min-height: 60px;
    }
    .artifact-canvas canvas { max-width: 100%; }
    .artifact-error {
      padding: 14px;
      color: var(--warn);
      background: #fdf3ec;
      border-radius: var(--radius-sm);
      font-size: 12.5px;
    }
    /* 按需组件按钮：对话生成后出现，点击才制作可视化 */
    .artifact-offer-btn {
      align-self: flex-start;
      max-width: 720px;
      width: 100%;
      display: flex;
      align-items: center;
      gap: 12px;
      padding: 12px 16px;
      border: 1px dashed var(--accent);
      border-radius: var(--radius);
      background: var(--accent-soft);
      color: var(--accent);
      cursor: pointer;
      text-align: left;
      transition: background 0.15s, border-color 0.15s;
      box-shadow: var(--shadow);
    }
    .artifact-offer-btn:hover:not(:disabled) { background: var(--accent-container); border-style: solid; }
    .artifact-offer-btn:disabled { cursor: progress; opacity: 0.85; }
    .artifact-offer-btn .icon { color: var(--accent); }
    .artifact-offer-text { display: flex; flex-direction: column; flex: 1 1 auto; min-width: 0; }
    .artifact-offer-text b { font-family: var(--serif); font-size: 14px; font-weight: 600; }
    .artifact-offer-text em { font-style: normal; font-size: 12px; color: var(--muted); overflow-wrap: anywhere; }
    .artifact-offer-hint { font-size: 11px; font-family: var(--mono); color: var(--muted); white-space: nowrap; }
    .artifact-offer-btn.loading .artifact-offer-hint { color: var(--accent); }
    /* 工具调用步骤提示（Agent 模式） */
    .tool-step {
      align-self: flex-start;
      max-width: 720px;
      display: inline-flex;
      align-items: center;
      gap: 7px;
      padding: 6px 12px;
      border: 1px solid var(--line-soft);
      border-radius: 999px;
      background: var(--surface-3);
      color: var(--muted);
      font-size: 12px;
      font-family: var(--mono);
      margin-top: 4px;
    }
    .tool-step .icon { color: var(--muted); }
    .tool-step.done { border-color: var(--accent-container); background: var(--accent-soft); color: var(--accent); }
    .tool-step.done .icon { color: var(--accent); }
    .artifact-controls {
      padding: 12px 16px;
      border-top: 1px solid var(--line-soft);
      background: var(--surface-3);
      display: grid;
      gap: 10px;
    }
    .artifact-control { display: grid; gap: 4px; }
    .artifact-control-row {
      display: flex;
      justify-content: space-between;
      align-items: center;
      font-size: 12px;
    }
    .artifact-control-row span { color: var(--muted); font-weight: 500; }
    .artifact-control-row b {
      color: var(--accent);
      font-family: var(--mono);
      font-size: 12.5px;
    }
    .artifact-control input[type="range"] {
      width: 100%;
      height: 5px;
      -webkit-appearance: none;
      appearance: none;
      background: var(--line);
      border-radius: 999px;
      outline: none;
    }
    .artifact-control input[type="range"]::-webkit-slider-thumb {
      -webkit-appearance: none;
      appearance: none;
      width: 18px; height: 18px;
      border-radius: 50%;
      background: var(--accent);
      border: 2px solid #fff;
      box-shadow: 0 1px 4px rgba(0,0,0,0.2);
      cursor: pointer;
    }
    .artifact-control input[type="range"]::-moz-range-thumb {
      width: 16px; height: 16px;
      border-radius: 50%;
      background: var(--accent);
      border: 2px solid #fff;
      cursor: pointer;
    }
    .artifact-reset {
      justify-self: start;
      border: 1px solid var(--line-soft);
      border-radius: var(--radius-sm);
      background: var(--surface);
      color: var(--muted);
      padding: 6px 12px;
      font-size: 12px;
      cursor: pointer;
    }
    .artifact-reset:hover { border-color: var(--accent); color: var(--accent); }

    /* ============================================================
       思考链（reasoning）：DeepSeek 真实 reasoning_content，暗色可折叠面板。
       默认收起（只显示头部条），点击展开看完整思维链。
       每轮 agent 迭代一个块：思考流式→首个 delta/tool_call 时自动收起→下一轮新建。
       仿 coding agent 的暗色思考块（参考 image copy 4.png）。
       ============================================================ */
    .think-host {
      align-self: flex-start;
      max-width: 720px;
      width: 100%;
      margin-bottom: 4px;
      display: flex;
      flex-direction: column;
      gap: 4px;
    }
    body[data-mode="user"] .think-host { max-width: 88%; }
    .reasoning-block {
      border-radius: 8px;
      overflow: hidden;
      border: 1px solid #3a3b37;
    }
    .reasoning-head {
      display: flex;
      align-items: center;
      gap: 8px;
      padding: 8px 12px;
      background: #2a2b28;
      color: #b8bcb4;
      cursor: pointer;
      font-size: 12px;
      font-family: var(--mono);
      user-select: none;
      transition: background 0.15s;
    }
    .reasoning-head:hover { background: #333431; }
    .reasoning-arrow {
      display: inline-flex; align-items: center; justify-content: center;
      transition: transform 0.15s;
      color: #8a8e85;
    }
    .reasoning-block.open .reasoning-arrow { transform: rotate(90deg); }
    .reasoning-label { font-weight: 600; color: #d4d8cf; letter-spacing: 0.02em; }
    .reasoning-status {
      margin-left: auto;
      font-size: 10.5px;
      color: #8a8e85;
      display: inline-flex;
      align-items: center;
      gap: 5px;
    }
    /* 流式期间的脉冲指示器 */
    .reasoning-block.streaming .reasoning-status::before {
      content: '';
      width: 8px; height: 8px;
      border: 1.5px solid #5a5d54;
      border-top-color: #d4d8cf;
      border-radius: 50%;
      animation: thinkSpin 0.8s linear infinite;
    }
    .reasoning-body {
      display: none;
      background: #1b1c19;
      color: #eef4e8;
      padding: 14px 16px;
      font-family: var(--mono);
      font-size: 12.5px;
      line-height: 1.7;
      white-space: pre-wrap;
      overflow-wrap: anywhere;
      max-height: 420px;
      overflow-y: auto;
      scrollbar-width: thin;
      scrollbar-color: #3a3b37 transparent;
    }
    .reasoning-block.open .reasoning-body { display: block; }
    .reasoning-body::-webkit-scrollbar { width: 6px; }
    .reasoning-body::-webkit-scrollbar-thumb { background: #3a3b37; border-radius: 3px; }
    /* 思考链里的关键词轻量高亮（可选，让长思维链更易扫读） */
    .reasoning-body { border-top: 1px solid #2a2b28; }
    @keyframes thinkSpin { to { transform: rotate(360deg); } }

    /* Canvas 制作中 skeleton 占位：点击「生成可视化」后先显示，
       告诉用户模型正在做，完成后替换为真实组件。 */
    .canvas-skeleton {
      width: 100%;
      padding: 22px 18px;
      border: 1px solid var(--line-soft);
      border-radius: 10px;
      background: var(--surface);
      display: flex;
      flex-direction: column;
      align-items: center;
      gap: 12px;
    }
    .canvas-skel-spinner {
      width: 30px; height: 30px;
      border: 3px solid var(--accent-container);
      border-top-color: var(--accent);
      border-radius: 50%;
      animation: thinkSpin 0.8s linear infinite;
    }
    .canvas-skel-text {
      font-family: var(--serif);
      font-size: 14px;
      font-weight: 600;
      color: var(--accent);
    }
    .canvas-skel-hint { font-size: 12px; color: var(--muted); }
    .canvas-skel-bars { display: flex; align-items: flex-end; gap: 6px; height: 46px; margin-top: 2px; }
    .canvas-skel-bars span {
      width: 10px; background: var(--accent-container);
      border-radius: 3px 3px 0 0;
      animation: skelPulse 1.2s ease-in-out infinite;
    }
    .canvas-skel-bars span:nth-child(2) { animation-delay: 0.1s; }
    .canvas-skel-bars span:nth-child(3) { animation-delay: 0.2s; }
    .canvas-skel-bars span:nth-child(4) { animation-delay: 0.3s; }
    .canvas-skel-bars span:nth-child(5) { animation-delay: 0.4s; }
    .canvas-skel-bars span:nth-child(6) { animation-delay: 0.5s; }
    @keyframes skelPulse {
      0%, 100% { height: 14px; opacity: 0.5; }
      50% { height: 42px; opacity: 1; }
    }

    /* 反馈条：AI 回答完成后挂在气泡下方 */
    .feedback-bar {
      display: flex;
      align-items: center;
      gap: 6px;
      margin-top: 10px;
      padding-top: 8px;
      border-top: 1px dashed var(--line-soft);
    }
    .feedback-bar .fb-label { font-size: 11.5px; color: var(--muted); margin-right: 4px; }
    .fb-btn {
      display: inline-flex; align-items: center; gap: 4px;
      padding: 4px 10px; border-radius: 999px;
      border: 1px solid var(--line-soft); background: var(--surface);
      color: var(--muted); font-size: 11.5px; cursor: pointer;
      transition: 0.15s;
    }
    .fb-btn:hover { border-color: var(--accent); color: var(--accent); }
    .fb-btn.active { background: var(--accent-soft); border-color: var(--accent); color: var(--accent); }
    .fb-btn .icon { font-size: 14px; }

    /* 用户模式抽屉遮罩 */
    .drawer-backdrop {
      display: none;
      position: fixed; inset: 64px 0 0 0;
      background: rgba(27,28,25,0.28);
      z-index: 39;
      opacity: 0;
      transition: opacity 0.25s;
    }
    .drawer-backdrop.show { display: block; opacity: 1; }
    /* 汉堡按钮（仅用户模式可见） */
    .drawer-toggle {
      display: none;
      width: 38px; height: 38px;
      border: 1px solid var(--line-soft); border-radius: var(--radius-sm);
      background: var(--surface); color: var(--ink);
      align-items: center; justify-content: center;
      cursor: pointer; flex-shrink: 0;
    }
    .drawer-toggle:hover { border-color: var(--accent); color: var(--accent); }
    body[data-mode="user"] .drawer-toggle { display: inline-flex; }
    /* 抽屉头：仅用户模式可见 */
    .drawer-head {
      display: none;
      align-items: center;
      justify-content: space-between;
      padding: 12px 16px 8px;
      border-bottom: 1px solid var(--line-soft);
      font-family: var(--serif);
    }
    body[data-mode="user"] .drawer-head { display: flex; }
    .drawer-head b { font-size: 15px; color: var(--accent); }
    .drawer-head button {
      border: 0; background: transparent; color: var(--muted);
      cursor: pointer; padding: 4px; border-radius: var(--radius-sm);
    }
    .drawer-head button:hover { color: var(--accent); background: var(--surface-3); }

    /* ============================================================
       双模式：开发者 / 用户。body[data-mode] 控制。
       用户模式 = 美观对话界面（参考 Scholastic Emerald DESIGN.md + code.html 对话框）
       ============================================================ */
    .mode-switch {
      display: inline-flex;
      align-items: center;
      background: var(--surface-2);
      border: 1px solid var(--line-soft);
      border-radius: 999px;
      padding: 3px;
      gap: 2px;
    }
    .mode-switch button {
      border: 0;
      background: transparent;
      color: var(--muted);
      font-family: var(--mono);
      font-size: 11.5px;
      letter-spacing: 0.04em;
      padding: 6px 14px;
      border-radius: 999px;
      cursor: pointer;
      display: inline-flex;
      align-items: center;
      gap: 5px;
      transition: 0.15s;
    }
    .mode-switch button .icon { font-size: 15px; }
    .mode-switch button.active {
      background: var(--accent);
      color: #fff;
      box-shadow: var(--shadow);
    }

    /* —— 用户模式布局：单列阅读画布 —— */
    body[data-mode="user"] .shell {
      grid-template-columns: 1fr;
      overflow-y: auto;
    }
    /* 用户模式：右栏隐藏，左栏变成可收起抽屉（点顶栏汉堡按钮展开） */
    body[data-mode="user"] .inspect { display: none; }
    body[data-mode="user"] .side {
      display: block;   /* 覆盖窄屏媒体查询的 display:none —— 抽屉在用户模式任何宽度都存在，只是 transform 收起 */
      position: fixed;
      top: 64px; left: 0; bottom: 0;
      width: 300px;
      max-width: 86vw;
      transform: translateX(-100%);
      transition: transform 0.25s ease;
      z-index: 40;
      background: var(--surface);
      box-shadow: var(--shadow-md);
      border-right: 1px solid var(--line-soft);
      overflow-y: auto;
    }
    body[data-mode="user"] .side.open { transform: translateX(0); }
    body[data-mode="user"] .main {
      grid-template-rows: 1fr auto;
      max-width: 840px;
      width: 100%;
      margin: 0 auto;
      min-height: calc(100vh - 64px);
    }
    body[data-mode="user"] .messages {
      padding: 28px 24px 8px;
      gap: 22px;
      background: transparent;
    }
    /* 用户模式气泡：参考 code.html 对话框 */
    body[data-mode="user"] .msg {
      max-width: 100%;
      border-radius: 16px;
      padding: 16px 20px;
      box-shadow: 0 1px 10px rgba(27,28,25,0.06);
      animation: msgIn 0.22s ease;
    }
    body[data-mode="user"] .msg.user {
      align-self: flex-end;
      max-width: 82%;
      background: var(--accent);
      color: #fff;
      border-bottom-right-radius: 5px;
    }
    body[data-mode="user"] .msg.assistant {
      align-self: flex-start;
      max-width: 88%;
      background: var(--surface-bright, #fff);
      color: var(--ink);
      border: 1px solid var(--line-soft);
      border-bottom-left-radius: 5px;
      /* 不用 flex：addMessage 把 markdown 块元素直接放进 .msg，
         flex 会让 <h2>/<p>/<ul> 变成横向排列的行项目而不是纵向堆叠。
         改用相对定位 + 左侧留白，头像绝对定位到左上，正文走正常 block 流。 */
      position: relative;
      padding-left: 56px;
    }
    /* AI 头像：绝对定位左上角，不参与正文流 */
    body[data-mode="user"] .msg.assistant::before {
      content: "";
      position: absolute;
      left: 14px;
      top: 16px;
      width: 30px; height: 30px;
      border-radius: var(--radius-sm);
      background-image: linear-gradient(135deg, var(--accent) 0%, var(--accent-2) 100%);
      border: 1px solid var(--accent-container);
      box-shadow: var(--shadow);
    }
    /* 知识点卡片：## 标题成视觉锚点 */
    body[data-mode="user"] .markdown h2,
    body[data-mode="user"] .markdown h3 {
      position: relative;
      padding-left: 14px;
      margin-top: 18px;
    }
    body[data-mode="user"] .markdown h2::before,
    body[data-mode="user"] .markdown h3::before {
      content: "";
      position: absolute;
      left: 0; top: 4px; bottom: 4px;
      width: 4px;
      background: var(--accent);
      border-radius: 2px;
    }
    body[data-mode="user"] .markdown p { line-height: 1.75; }
    body[data-mode="user"] .markdown blockquote {
      border-left-width: 4px;
      border-radius: 0 10px 10px 0;
      padding: 10px 16px;
    }
    body[data-mode="user"] .markdown mjx-container[display="true"] {
      margin: 14px auto !important;
      max-width: 92%;
    }

    /* 用户模式 composer：圆角容器 + chips */
    body[data-mode="user"] .composer {
      background: rgba(250,249,244,0.9);
      backdrop-filter: blur(8px);
      border-top: 0;
      padding: 10px 24px 22px;
      display: flex;
      flex-direction: column;
      gap: 10px;
      align-items: stretch;
    }
    body[data-mode="user"] .composer .composer-row {
      display: flex;
      gap: 10px;
      align-items: flex-end;
      background: var(--surface-2);
      border: 1px solid transparent;
      border-radius: 14px;
      padding: 8px 8px 8px 14px;
      transition: 0.15s;
    }
    body[data-mode="user"] .composer .composer-row:focus-within {
      background: var(--surface);
      border-color: var(--accent);
      box-shadow: 0 0 0 3px rgba(45,90,39,0.10);
    }
    body[data-mode="user"] .composer textarea {
      grid-column: auto;
      border: 0;
      background: transparent;
      box-shadow: none;
      padding: 8px 0;
      min-height: 44px;
      flex: 1;
    }
    body[data-mode="user"] .composer textarea:focus { box-shadow: none; }
    body[data-mode="user"] #clearContext {
      grid-column: auto;
      background: transparent;
      border: 0;
      color: var(--muted);
      box-shadow: none;
      min-width: 0;
      padding: 8px 10px;
    }
    body[data-mode="user"] #clearContext:hover { color: var(--accent); background: var(--surface-3); }
    body[data-mode="user"] #send {
      min-width: 86px;
      border-radius: 10px;
    }
    /* 快捷 chips 行（仅用户模式） */
    .quick-chips {
      display: none;
      flex-wrap: wrap;
      gap: 8px;
      justify-content: center;
    }
    body[data-mode="user"] .quick-chips { display: flex; }
    .quick-chips button {
      display: inline-flex;
      align-items: center;
      gap: 6px;
      padding: 7px 14px;
      border-radius: 999px;
      background: var(--surface);
      border: 1px solid var(--line-soft);
      color: var(--ink);
      font-family: var(--mono);
      font-size: 11.5px;
      letter-spacing: 0.03em;
      cursor: pointer;
      transition: 0.15s;
    }
    .quick-chips button:hover {
      border-color: var(--accent);
      color: var(--accent);
      transform: translateY(-1px);
      box-shadow: var(--shadow);
    }
    .quick-chips button .icon { font-size: 15px; color: var(--accent); }

    /* —— Canvas 三种呈现容器 —— */
    /* 全屏模态 */
    .canvas-modal {
      position: fixed; inset: 0;
      background: rgba(27,28,25,0.55);
      backdrop-filter: blur(4px);
      z-index: 100;
      display: none;
      align-items: center;
      justify-content: center;
      padding: 32px;
    }
    .canvas-modal.open { display: flex; }
    .canvas-modal-frame {
      width: 100%; max-width: 1100px; height: 80vh;
      background: var(--surface);
      border-radius: 14px;
      box-shadow: var(--shadow-md);
      overflow: hidden;
      display: flex;
      flex-direction: column;
    }
    .canvas-modal-head {
      display: flex; align-items: center; justify-content: space-between;
      padding: 10px 16px;
      border-bottom: 1px solid var(--line-soft);
      background: var(--surface-3);
    }
    .canvas-modal-head b { font-family: var(--serif); font-size: 15px; color: var(--accent); }
    .canvas-modal-head button {
      border: 0; background: transparent; cursor: pointer;
      color: var(--muted); display: inline-flex; align-items: center;
    }
    .canvas-modal-head button:hover { color: var(--ink); }
    .canvas-modal-body { flex: 1; min-height: 0; }
    .canvas-modal-body iframe { width: 100%; height: 100%; border: 0; background: #fff; }

    /* 用户模式：来源以引文卡片折叠在 AI 气泡后 */
    .msg-sources { margin-top: 14px; border-top: 1px dashed var(--line-soft); padding-top: 10px; }
    .msg-sources-toggle {
      display: inline-flex; align-items: center; gap: 6px;
      font-family: var(--mono); font-size: 11px; color: var(--muted);
      background: none; border: 0; cursor: pointer; padding: 2px 0;
    }
    .msg-sources-toggle:hover { color: var(--accent); }
    .msg-sources-list { display: none; margin-top: 8px; }
    .msg-sources-list.open { display: block; }
    .citation-card {
      border-left: 3px solid var(--accent);
      background: var(--accent-soft);
      border-radius: 0 8px 8px 0;
      padding: 8px 12px;
      margin: 6px 0;
      font-size: 12.5px;
    }
    .citation-card .cite-meta { font-family: var(--mono); font-size: 10.5px; color: var(--muted); letter-spacing: 0.03em; }
    .citation-card .cite-text { color: var(--muted); margin-top: 2px; }

    /* 用户模式：可视化件容器左对齐、与 AI 气泡等宽，不撑满整列 */
    body[data-mode="user"] .artifact-host {
      align-self: flex-start;
      max-width: 88%;
      width: 100%;
    }

    /* “已记住 N 轮” 小标（用户模式输入区上方） */
    .ctx-hint {
      display: none;
      align-self: center;
      font-family: var(--mono);
      font-size: 11px;
      color: var(--muted);
      gap: 5px;
      align-items: center;
    }
    body[data-mode="user"] .ctx-hint { display: inline-flex; }
    .ctx-hint .icon { font-size: 14px; color: var(--accent); }

    /* 响应式：窄屏收起右栏 */
    @media (max-width: 1100px) {
      .shell { grid-template-columns: 240px minmax(0, 1fr); }
      .inspect { display: none; }
    }
    @media (max-width: 720px) {
      .shell { grid-template-columns: 1fr; }
      .side { display: none; }
      .topbar { padding: 0 16px; }
      .messages { padding: 18px 16px; }
      .composer { padding: 12px 16px 16px; }
    }
  </style>
</head>
<body data-mode="user">
  <canvas id="glcanvas"></canvas>

  <header class="topbar">
    <button id="drawerToggle" class="drawer-toggle" type="button" title="打开侧栏（对话记录与设置）" aria-label="打开侧栏">
      <span data-icon="menu" data-icon-size="20"></span>
    </button>
    <div class="brand">
      <div class="logo">V</div>
      <div>
        <h1>VeriMath Agent</h1>
        <div class="subtle">数学与统计学习导师</div>
      </div>
    </div>
    <div id="modeSwitch" class="mode-switch" role="group" aria-label="界面模式">
      <button type="button" data-mode="user" class="active"><span data-icon="chat"></span>用户</button>
      <button type="button" data-mode="dev"><span data-icon="developer_board"></span>开发者</button>
    </div>
    <div id="topPills">
      <span class="pill ok">A2A Local</span>
    </div>
  </header>

  <div id="drawerBackdrop" class="drawer-backdrop"></div>

  <div class="shell">
    <!-- 左栏：导航与状态 -->
    <aside class="side">
      <!-- 抽屉头：仅用户模式可见，提供关闭入口 -->
      <div class="drawer-head">
        <b>侧栏</b>
        <button id="drawerClose" type="button" title="收起" aria-label="收起侧栏"><span data-icon="close" data-icon-size="18"></span></button>
      </div>
      <div class="section">
        <h2><span data-icon="tune"></span>服务状态</h2>
        <div id="statusGrid" class="status-grid">
          <div class="metric"><b>服务</b><span>读取中</span></div>
        </div>
      </div>

      <div class="section">
        <h2><span data-icon="model_training"></span>DeepSeek 增强</h2>
        <div class="toggle-row" title="切换是否调用模型">
          <div class="label-block">
            <b>使用模型</b>
            <span class="subtle">关闭时只用离线路由答案</span>
          </div>
          <label class="switch">
            <input id="modelToggle" type="checkbox" checked>
            <span class="slider"></span>
          </label>
        </div>
      </div>

      <div class="section">
        <h2><span data-icon="style"></span>回答偏好</h2>
        <div class="segmented" id="styleSelector" aria-label="回答偏好">
          <button class="segment active" type="button" data-style="rigorous">严谨</button>
          <button class="segment" type="button" data-style="examples">举例</button>
          <button class="segment" type="button" data-style="concise">简洁</button>
        </div>
        <div class="subtle" style="margin-top:8px">默认面向理学专业，严谨优先。</div>
      </div>

      <div class="section">
        <h2><span data-icon="bolt"></span>快捷指令</h2>
        <div class="quick-list">
          <button class="quick" data-q="给我制定一个四周的数理统计学习路线">制定学习路线</button>
          <button class="quick" data-q="两组成绩比较应该用什么统计方法？">统计方法选择</button>
          <button class="quick" data-q="什么是正态分布">正态分布可视化</button>
          <button class="quick" data-q="中心极限定理是什么？">解释一个概念</button>
          <button class="quick" data-q="出一道关于 Welch t 检验的原创练习题">出一道练习题</button>
        </div>
      </div>

      <div class="section">
        <h2><span data-icon="library_books"></span>语料分布</h2>
        <div id="courseList" class="course-list subtle">等待索引信息</div>
      </div>

      <div class="section">
        <h2><span data-icon="memory"></span>对话上下文</h2>
        <div id="contextPanel">
          <div class="subtle">暂无上下文</div>
        </div>
      </div>

      <div class="section">
        <h2><span data-icon="history"></span>最近聊天</h2>
        <div id="historyList" class="record-list subtle">等待聊天记录</div>
      </div>

      <div class="section">
        <h2><span data-icon="science"></span>测试记录</h2>
        <div id="testRunList" class="record-list subtle">等待测试记录</div>
      </div>
    </aside>

    <!-- 中栏：对话 -->
    <main class="main">
      <section id="messages" class="messages">
        <div class="msg assistant">输入一个真实学生问题，面板会返回答案，并在右侧显示路由、模型调用状态和 RAG 来源。试试「什么是正态分布」——会弹出一个可拖动参数的可视化组件。</div>
      </section>

      <form id="composer" class="composer">
        <div class="ctx-hint" id="ctxHint"><span data-icon="memory"></span><span id="ctxHintText">新对话</span></div>
        <div class="composer-row">
          <textarea id="query" placeholder="例如：什么是正态分布？中心极限定理是什么？两组成绩比较应该用什么统计方法？"></textarea>
          <button id="clearContext" class="send" type="button" title="清空多轮上下文，开始新对话">
            <span data-icon="add_comment" data-icon-size="18"></span>新对话
          </button>
          <button id="send" class="send" type="submit">
            发送<span data-icon="send" data-icon-size="18"></span>
          </button>
          <button id="stopGen" class="send stop" type="button" title="提前结束本次生成" hidden>
            停止<span data-icon="stop" data-icon-size="18"></span>
          </button>
        </div>
        <div class="quick-chips" id="quickChips">
          <button type="button" data-q="什么是正态分布"><span data-icon="show_chart"></span>正态分布</button>
          <button type="button" data-q="帮我整理一个方差分析的课件"><span data-icon="menu_book"></span>课件</button>
          <button type="button" data-q="出一道关于 Welch t 检验的练习题"><span data-icon="edit_note"></span>出题</button>
          <button type="button" data-q="画一个中心极限定理的演示，n 从 1 到 30 看样本均值分布收敛"><span data-icon="animation"></span>可视化</button>
          <button type="button" id="openNotes"><span data-icon="note_add"></span>更新笔记</button>
        </div>
      </form>
    </main>

    <!-- 右栏：洞察 -->
    <aside class="inspect">
      <div class="section">
        <h2><span data-icon="analytics"></span>本轮诊断</h2>
        <div class="inspector-block" id="diagnostics">
          <div class="subtle">还没有请求</div>
        </div>
      </div>

      <div class="section">
        <h2><span data-icon="source"></span>RAG 来源</h2>
        <div class="inspector-block" id="sources">
          <div class="subtle">暂无来源</div>
        </div>
      </div>

      <div class="section">
        <h2><span data-icon="code"></span>原始数据</h2>
        <pre class="raw" id="raw">点击左侧历史记录可查看当时的完整数据。</pre>
      </div>
    </aside>
  </div>

  <!-- Canvas 全屏模态（模型生成的 HTML 组件沉浸式查看） -->
  <div class="canvas-modal" id="canvasModal" aria-hidden="true">
    <div class="canvas-modal-frame">
      <div class="canvas-modal-head">
        <b id="canvasModalTitle">可视化组件</b>
        <button type="button" id="canvasModalClose" title="关闭"><span data-icon="close"></span></button>
      </div>
      <div class="canvas-modal-body" id="canvasModalBody"></div>
    </div>
  </div>

  <!-- 更新笔记弹窗 -->
  <div class="canvas-modal" id="notesModal" aria-hidden="true">
    <div class="canvas-modal-frame" style="max-width:640px;height:auto">
      <div class="canvas-modal-head">
        <b>更新我的笔记到知识库</b>
        <button type="button" id="notesModalClose" title="关闭"><span data-icon="close"></span></button>
      </div>
      <div style="padding:18px 20px;display:flex;flex-direction:column;gap:10px">
        <div style="display:flex;gap:10px">
          <input id="notesCourse" placeholder="课程（如 概率论）" style="flex:1;padding:9px 12px;border:1px solid var(--line-soft);border-radius:var(--radius);font-family:var(--sans)">
          <input id="notesTopic" placeholder="主题（如 中心极限定理）" style="flex:1;padding:9px 12px;border:1px solid var(--line-soft);border-radius:var(--radius);font-family:var(--sans)">
        </div>
        <textarea id="notesText" placeholder="粘贴你的笔记内容……支持 Markdown 与公式。入库后会优先用于后续检索。" style="min-height:180px;width:100%;resize:vertical;padding:12px;border:1px solid var(--line-soft);border-radius:var(--radius);font-family:var(--sans);line-height:1.6"></textarea>
        <div style="display:flex;align-items:center;justify-content:space-between;gap:10px">
          <span class="subtle" id="notesStatus"></span>
          <button id="notesSubmit" class="send" type="button" style="min-width:110px">提交入库</button>
        </div>
      </div>
    </div>
  </div>

  <!-- WebGL 网格背景（Scholastic Emerald 主题） -->
  <script>
    (function () {
      const canvas = document.getElementById('glcanvas');
      const gl = canvas && canvas.getContext('webgl');
      if (!gl) { if (canvas) canvas.style.display = 'none'; return; }
      const vs = `attribute vec2 a_position; varying vec2 v_uv;
        void main(){ gl_Position=vec4(a_position,0.0,1.0); v_uv=a_position*0.5+0.5; }`;
      const fs = `precision highp float; uniform vec2 u_res; uniform vec2 u_mouse; varying vec2 v_uv;
        void main(){
          vec2 uv=v_uv; float aspect=u_res.x/u_res.y; vec2 g=uv*vec2(aspect,1.0);
          float density=26.0; vec2 f=fract(g*density);
          vec2 m=u_mouse/u_res; m.x*=aspect; m.y=1.0-m.y;
          float dist=distance(g*density, m*density);
          float active=smoothstep(6.0,0.0,dist);
          float thick=0.015+active*0.05;
          vec2 grid=smoothstep(0.5-thick,0.5,abs(f-0.5));
          float line=max(grid.x,grid.y);
          vec3 bg=vec3(0.980,0.976,0.957);
          vec3 lc=mix(vec3(0.88,0.87,0.83), vec3(0.176,0.353,0.153), active*0.45);
          vec3 color=mix(bg,lc,line*0.16);
          float vignette=1.0-smoothstep(0.5,1.5,length(uv-0.5));
          color*=mix(0.97,1.0,vignette);
          gl_FragColor=vec4(color,1.0);
        }`;
      function sh(t,s){ const x=gl.createShader(t); gl.shaderSource(x,s); gl.compileShader(x); return x; }
      const prog=gl.createProgram();
      gl.attachShader(prog, sh(gl.VERTEX_SHADER,vs)); gl.attachShader(prog, sh(gl.FRAGMENT_SHADER,fs));
      gl.linkProgram(prog);
      const buf=gl.createBuffer(); gl.bindBuffer(gl.ARRAY_BUFFER,buf);
      gl.bufferData(gl.ARRAY_BUFFER, new Float32Array([-1,-1, 1,-1, -1,1, -1,1, 1,-1, 1,1]), gl.STATIC_DRAW);
      const pL=gl.getAttribLocation(prog,"a_position"), rL=gl.getUniformLocation(prog,"u_res"), mL=gl.getUniformLocation(prog,"u_mouse");
      let mx=0,my=0;
      document.addEventListener('mousemove', e=>{ mx=e.clientX; my=e.clientY; });
      function resize(){ const w=canvas.clientWidth,h=canvas.clientHeight; if(canvas.width!==w||canvas.height!==h){canvas.width=w;canvas.height=h;} }
      function render(){ resize(); gl.viewport(0,0,canvas.width,canvas.height); gl.clearColor(0,0,0,0); gl.clear(gl.COLOR_BUFFER_BIT);
        gl.useProgram(prog); gl.enableVertexAttribArray(pL); gl.bindBuffer(gl.ARRAY_BUFFER,buf);
        gl.vertexAttribPointer(pL,2,gl.FLOAT,false,0,0); gl.uniform2f(rL,canvas.width,canvas.height); gl.uniform2f(mL,mx,my);
        gl.drawArrays(gl.TRIANGLES,0,6); requestAnimationFrame(render); }
      requestAnimationFrame(render);
    })();
  </script>

  <script>
    const statusGrid = document.getElementById('statusGrid');
    const courseList = document.getElementById('courseList');
    const messages = document.getElementById('messages');
    const historyList = document.getElementById('historyList');
    const testRunList = document.getElementById('testRunList');
    const composer = document.getElementById('composer');
    const queryInput = document.getElementById('query');
    const sendButton = document.getElementById('send');
    const stopButton = document.getElementById('stopGen');
    const diagnostics = document.getElementById('diagnostics');
    const sourcesBox = document.getElementById('sources');
    const rawBox = document.getElementById('raw');
    const modelToggle = document.getElementById('modelToggle');
    const topPills = document.getElementById('topPills');
    const clearContextButton = document.getElementById('clearContext');
    let answerStyle = 'rigorous';

    // 右侧诊断面板：显式滚轮支持，让 wheel 事件在子元素上也能滚动面板本身
    const inspectPanel = document.querySelector('.inspect');
    if (inspectPanel) {
      inspectPanel.addEventListener('wheel', function (e) {
        // 如果目标是 input[type=range] 或 textarea，不拦截（让用户正常操作控件）
        if (e.target.tagName === 'INPUT' || e.target.tagName === 'TEXTAREA') return;
        e.preventDefault();
        inspectPanel.scrollTop += e.deltaY;
      }, { passive: false });
    }

    // 持久会话 id：让面板多轮对话共享上下文，刷新页面不丢
    function getSessionId() {
      let sid = null;
      try { sid = window.localStorage.getItem('agent-session-id'); } catch (_) {}
      if (!sid) {
        sid = 'panel-' + (window.crypto && crypto.randomUUID ? crypto.randomUUID() : Date.now() + '-' + Math.random().toString(16).slice(2));
        try { window.localStorage.setItem('agent-session-id', sid); } catch (_) {}
      }
      return sid;
    }
    let sessionId = getSessionId();

    // 流式生成状态：支持「提前结束对话」
    let abortController = null;      // 当前流式请求的 AbortController，停止时 abort()
    let currentTaskId = null;        // 当前任务 task_id，停止时上报后端取消
    let isStreaming = false;          // 是否正在流式生成中

    function escapeHtml(value) {
      return String(value ?? '')
        .replaceAll('&', '&amp;')
        .replaceAll('<', '&lt;')
        .replaceAll('>', '&gt;')
        .replaceAll('"', '&quot;')
        .replaceAll("'", '&#039;');
    }

    let _md = null;
    const MATH_TOKENS = {
      inlineOpen: '@@CODEX_MATH_INLINE_OPEN@@',
      inlineClose: '@@CODEX_MATH_INLINE_CLOSE@@',
      blockOpen: '@@CODEX_MATH_BLOCK_OPEN@@',
      blockClose: '@@CODEX_MATH_BLOCK_CLOSE@@'
    };

    function getMarkdown() {
      if (!_md && window.markdownit) {
        _md = window.markdownit({ html: false, linkify: true, breaks: false });
      }
      return _md;
    }

    function protectMathDelimiters(text) {
      return text
        .replaceAll('\\[', MATH_TOKENS.blockOpen)
        .replaceAll('\\]', MATH_TOKENS.blockClose)
        .replaceAll('\\(', MATH_TOKENS.inlineOpen)
        .replaceAll('\\)', MATH_TOKENS.inlineClose);
    }

    function restoreMathDelimiters(text) {
      return text
        .replaceAll(MATH_TOKENS.blockOpen, '\\[')
        .replaceAll(MATH_TOKENS.blockClose, '\\]')
        .replaceAll(MATH_TOKENS.inlineOpen, '\\(')
        .replaceAll(MATH_TOKENS.inlineClose, '\\)');
    }

    // markdown-it 渲染 -> DOMPurify 消毒。公式分隔符由 KaTeX 事后处理，故此处不解析 $。
    function renderMarkdown(markdown) {
      const src = String(markdown || '');
      const protectedSrc = protectMathDelimiters(src);
      const md = getMarkdown();
      const raw = md ? md.render(protectedSrc) : escapeHtml(protectedSrc).replace(/\n/g, '<br>');
      const restored = restoreMathDelimiters(raw);
      if (window.DOMPurify) {
        return window.DOMPurify.sanitize(restored, { ADD_ATTR: ['target', 'rel'] });
      }
      return restored;
    }

    // KaTeX auto-render 扫描 DOM。throwOnError:false 时把失败公式标红并上报 render_fail。
    function typesetMath(element) {
      if (!window.renderMathInElement) return;
      try {
        window.renderMathInElement(element, {
          delimiters: [
            { left: '\\[', right: '\\]', display: true },
            { left: '\\(', right: '\\)', display: false },
            { left: '$$', right: '$$', display: true },
            { left: '$', right: '$', display: false }
          ],
          throwOnError: false,
          errorCallback: function (msg, err) {
            console.warn('KaTeX render failed', msg);
            reportRenderFail(msg);
          }
        });
      } catch (error) {
        console.warn('renderMathInElement failed', error);
      }
    }

    function reportRenderFail(message) {
      try {
        fetch('/api/panel/render-fail', {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify({ message: String(message).slice(0, 500) })
        }).catch(() => {});
      } catch (_) { /* 上报失败静默，不影响渲染 */ }
    }

    function addMessage(role, text, extraClass = '') {
      const item = document.createElement('div');
      item.className = `msg ${role}${role === 'assistant' ? ' markdown' : ''}${extraClass ? ` ${extraClass}` : ''}`;
      if (role === 'assistant') {
        item.innerHTML = renderMarkdown(text);
        typesetMath(item);
      } else {
        item.textContent = text;
      }
      messages.appendChild(item);
      messages.scrollTop = messages.scrollHeight;
      return item;
    }

    // ------------------------------------------------ 可视化件挂载
    // 契约：后端已校验过 spec，这里只管渲染。任何异常都降级为一行提示，
    // 绝不影响已经渲染好的文字答案 —— 图是增强，不是答案的前提。

    function formatControlValue(value, step) {
      if (step >= 1) return String(Math.round(value));
      const decimals = Math.min(4, Math.max(0, Math.ceil(-Math.log10(step))));
      return value.toFixed(decimals);
    }

    function mountArtifact(spec, host) {
      if (!spec) return null;

      // ---- html_canvas：模型生成的自包含 HTML，沙箱 iframe 渲染 ----
      // 不走 widgets 注册表（那是 8 个固定 widget），独立通道：srcdoc + sandbox。
      // sandbox 只给 allow-scripts，不给 allow-same-origin → 彻底隔离，组件碰不到父页。
      if (spec.kind === 'html_canvas') {
        const card = document.createElement('section');
        card.className = 'artifact artifact-canvas';
        const head = document.createElement('div');
        head.className = 'artifact-head';
        const title = document.createElement('div');
        title.className = 'artifact-title';
        title.textContent = spec.title || '自定义可视化';
        const caption = document.createElement('div');
        caption.className = 'artifact-caption';
        caption.textContent = spec.caption || '模型生成的可交互 HTML 组件';
        head.appendChild(title);
        head.appendChild(caption);
        // 全屏按钮：复用 Canvas 模态，沉浸查看
        const expand = document.createElement('button');
        expand.type = 'button';
        expand.className = 'artifact-expand';
        expand.innerHTML = '<span data-icon="expand_more" data-icon-size="16"></span>全屏';
        expand.title = '全屏查看';
        expand.addEventListener('click', () => {
          if (window.__openCanvasModal) window.__openCanvasModal(spec.html, spec.title);
        });
        head.appendChild(expand);
        card.appendChild(head);

        const canvasHost = document.createElement('div');
        canvasHost.className = 'artifact-canvas';
        const iframe = document.createElement('iframe');
        iframe.setAttribute('sandbox', 'allow-scripts');
        iframe.setAttribute('srcdoc', spec.html || '');
        iframe.className = 'html-canvas-iframe';
        iframe.style.width = '100%';
        iframe.style.height = (spec.height || 420) + 'px';
        iframe.style.border = '0';
        iframe.style.background = '#fff';
        iframe.setAttribute('title', spec.title || '可视化组件');
        canvasHost.appendChild(iframe);
        card.appendChild(canvasHost);
        host.appendChild(card);
        if (window.renderIcons) renderIcons(card);   // 渲染全屏按钮里的图标
        return card;
      }

      if (!window.widgets || !window.widgets.has(spec.kind)) return null;
      const widget = window.widgets.get(spec.kind);

      const card = document.createElement('section');
      card.className = 'artifact';
      const head = document.createElement('div');
      head.className = 'artifact-head';
      const title = document.createElement('div');
      title.className = 'artifact-title';
      title.textContent = spec.title || '';
      const caption = document.createElement('div');
      caption.className = 'artifact-caption';
      caption.textContent = spec.caption || '';
      head.appendChild(title);
      head.appendChild(caption);
      card.appendChild(head);

      const canvasHost = document.createElement('div');
      canvasHost.className = 'artifact-canvas';
      card.appendChild(canvasHost);
      host.appendChild(card);

      let controls = [];
      try {
        controls = widget.controls(spec) || [];
      } catch (_) { controls = []; }

      const state = {};
      controls.forEach((c) => { state[c.key] = c.value; });

      let failed = false;
      function draw() {
        if (failed) return;
        try {
          widget.render(canvasHost, spec, Object.keys(state).length ? state : undefined);
        } catch (error) {
          failed = true;
          canvasHost.innerHTML = '';
          const msg = document.createElement('div');
          msg.className = 'artifact-error';
          msg.textContent = '这张图没能画出来（' + (error && error.message ? error.message : '未知错误') +
            '）。上面的文字答案不受影响。';
          canvasHost.appendChild(msg);
          reportRenderFail('artifact ' + spec.kind + ': ' + (error && error.message));
        }
      }
      draw();
      if (failed) return card;

      if (controls.length) {
        const box = document.createElement('div');
        box.className = 'artifact-controls';
        const inputs = [];
        controls.forEach((c) => {
          const wrap = document.createElement('label');
          wrap.className = 'artifact-control';
          const row = document.createElement('span');
          row.className = 'artifact-control-row';
          const name = document.createElement('span');
          name.textContent = c.label;
          const val = document.createElement('b');
          val.textContent = formatControlValue(c.value, c.step);
          row.appendChild(name);
          row.appendChild(val);
          const input = document.createElement('input');
          input.type = 'range';
          input.min = String(c.min);
          input.max = String(c.max);
          input.step = String(c.step);
          input.value = String(c.value);
          // 滑块必须有可读名称，否则屏幕阅读器只报「滑块」
          input.setAttribute('aria-label', c.label);
          // 滚轮微调：在滑块上滚动鼠标滚轮可步进调整参数值
          input.addEventListener('wheel', function (wheelEvt) {
            if (!input.matches(':focus') && !input.matches(':hover')) return;
            wheelEvt.preventDefault();
            var step = Number(input.step) || 1;
            var min = Number(input.min);
            var max = Number(input.max);
            var v = Number(input.value);
            var direction = wheelEvt.deltaY < 0 ? 1 : -1;
            v = Math.min(max, Math.max(min, v + direction * step));
            input.value = String(v);
            state[c.key] = v;
            val.textContent = formatControlValue(v, Number(input.step));
            draw();
          }, { passive: false });
          input.addEventListener('input', () => {
            const v = Number(input.value);
            state[c.key] = v;
            val.textContent = formatControlValue(v, c.step);
            // 重绘同步进行：本地计算在毫秒级，不需要节流也不会掉帧
            draw();
          });
          wrap.appendChild(row);
          wrap.appendChild(input);
          box.appendChild(wrap);
          inputs.push({ input, val, spec: c });
        });
        const reset = document.createElement('button');
        reset.type = 'button';
        reset.className = 'artifact-reset';
        reset.textContent = '恢复初始参数';
        reset.addEventListener('click', () => {
          inputs.forEach(({ input, val, spec: c }) => {
            input.value = String(c.value);
            state[c.key] = c.value;
            val.textContent = formatControlValue(c.value, c.step);
          });
          draw();
        });
        box.appendChild(reset);
        card.appendChild(box);
      }
      return card;
    }

    function renderArtifacts(list, host) {
      if (!Array.isArray(list) || !list.length || !host) return;
      // 幂等：meta 与 final 都带 artifacts，重复调用不应画出两份
      if (host.dataset.artifactsDone === '1') return;
      host.dataset.artifactsDone = '1';
      list.forEach((spec) => {
        try {
          mountArtifact(spec, host);
        } catch (_) { /* 单个图失败不影响其他图与文字 */ }
      });
      messages.scrollTop = messages.scrollHeight;
    }

    // 按需组件：对话生成后给出「生成可视化」按钮，用户点击才制作并渲染。
    // offer 形如 {tier, spec?, query, route, title, caption}：
    //   - 有 spec（Tier1 确定性规则命中）→ 直接 mountArtifact
    //   - 无 spec（Tier2/Canvas）→ POST /api/panel/artifact 让后端生成后再渲染
    function renderArtifactButton(host, offer) {
      if (!offer || !host) return;
      // 幂等：同一 host 已渲染过 offer 按钮则不再重复
      if (host.dataset.offerDone === '1') return;
      host.dataset.offerDone = '1';
      const btn = document.createElement('button');
      btn.type = 'button';
      btn.className = 'artifact-offer-btn';
      const title = offer.title || '可视化组件';
      btn.innerHTML = (window.icon ? window.icon('show_chart', 18) : '') +
        '<span class="artifact-offer-text"><b>生成可视化</b><em>' + escapeHtml(title) + '</em></span>' +
        '<span class="artifact-offer-hint">点击制作</span>';
      btn.addEventListener('click', async () => {
        btn.disabled = true;
        btn.classList.add('loading');
        const hint = btn.querySelector('.artifact-offer-hint');
        if (hint) hint.textContent = '制作中…';
        // 先放一个 skeleton 占位：让用户明确知道组件正在做，不是卡死
        const skel = document.createElement('div');
        skel.className = 'canvas-skeleton';
        skel.innerHTML =
          '<div class="canvas-skel-spinner"></div>' +
          '<div class="canvas-skel-text">正在制作可视化组件…</div>' +
          '<div class="canvas-skel-hint">模型正在生成可交互组件，请稍候片刻</div>' +
          '<div class="canvas-skel-bars"><span></span><span></span><span></span><span></span><span></span><span></span></div>';
        host.appendChild(skel);
        // 用户刚点击按钮，强制滚到底确保 skeleton 在视野内（不用 nearBottomSafe 判断）
        messages.scrollTop = messages.scrollHeight;
        try {
          // 阶段1：skeleton 单独显示至少 600ms，让用户明确看到「正在制作」反馈。
          // 确定性 spec 路径瞬时完成，若 mountArtifact 立刻执行，skeleton 与组件同帧出现
          // 又同帧移除，浏览器根本不绘制 skeleton —— 必须先等一拍。
          await new Promise(r => setTimeout(r, 600));
          // 阶段2：真正制作组件
          if (offer.spec) {
            mountArtifact(offer.spec, host);
          } else {
            const resp = await fetch('/api/panel/artifact', {
              method: 'POST',
              headers: {'Content-Type': 'application/json'},
              body: JSON.stringify({query: offer.query || '', route: offer.route || 'concept'}),
            });
            const data = await resp.json();
            if (!resp.ok) throw new Error(data.detail || `status ${resp.status}`);
            if (data.ok && data.artifact) {
              mountArtifact(data.artifact, host);
            } else {
              throw new Error(data.detail || '未生成组件');
            }
          }
          // 阶段3：组件已就位，再保留 skeleton 300ms 让用户看到「制作→完成」过渡
          await new Promise(r => setTimeout(r, 300));
          skel.remove();   // 制作完成：移除占位
          btn.remove();    // 移除按钮，让出空间给卡片
          messages.scrollTop = messages.scrollHeight;
        } catch (err) {
          skel.remove();
          btn.classList.remove('loading');
          btn.disabled = false;
          if (hint) hint.textContent = '失败：' + err.message;
        }
      });
      host.appendChild(btn);
      messages.scrollTop = messages.scrollHeight;
    }

    function nearBottomSafe() {
      return messages.scrollTop + messages.clientHeight >= messages.scrollHeight - 80;
    }

    function renderPending(stage) {
      return `<strong>${escapeHtml(stage)}</strong><span class="typing-dots"><span></span><span></span><span></span></span>`;
    }

    // ============================================================
    // 思考链（reasoning）：DeepSeek 真实 reasoning_content，暗色可折叠面板。
    // 每轮 agent 迭代一个块：thinking 事件流式追加→首个 delta/tool_call 时
    // 自动收起（finalizeReasoning）→下一轮 thinking 事件新建块。
    // 默认收起，点击头部条展开。仿 coding agent 暗色思考块。
    // ============================================================
    var TOOL_LABELS = {
      plot_distribution: '生成分布图',
      search_knowledge_base: '查阅本地知识库',
      generate_exercise: '生成练习题',
      recommend_method: '选择统计方法',
      build_canvas: '构建可视化组件',
    };

    // 创建一个思考块（流式期间默认展开）。返回该块 DOM 节点。
    function createReasoningBlock(host) {
      var block = document.createElement('div');
      block.className = 'reasoning-block streaming open';
      block.innerHTML =
        '<div class="reasoning-head">' +
          '<span class="reasoning-arrow">' + (window.icon ? window.icon('expand_more', 16) : '▶') + '</span>' +
          '<span class="reasoning-label">思考过程</span>' +
          '<span class="reasoning-status">思考中…</span>' +
        '</div>' +
        '<div class="reasoning-body"></div>';
      host.appendChild(block);
      if (window.renderIcons) renderIcons(block);
      block.querySelector('.reasoning-head').addEventListener('click', function (e) {
        e.stopPropagation();
        block.classList.toggle('open');
      });
      return block;
    }

    // 追加思考文本（流式增量）。同时更新头部状态字数。
    function appendReasoning(block, text) {
      if (!block || !text) return;
      var body = block.querySelector('.reasoning-body');
      body.appendChild(document.createTextNode(text));
      var cnt = body.textContent.length;
      var status = block.querySelector('.reasoning-status');
      if (status && block.classList.contains('streaming')) {
        status.textContent = '思考中 · ' + cnt + ' 字';
      }
    }

    // 结束本轮思考：去掉流式态、更新状态文案、自动收起。
    // reason: 'done'（正常完成）/ 'stopped'（用户中断）
    function finalizeReasoning(block, reason) {
      if (!block) return;
      block.classList.remove('streaming');
      var body = block.querySelector('.reasoning-body');
      var cnt = body ? body.textContent.length : 0;
      var status = block.querySelector('.reasoning-status');
      if (status) {
        status.textContent = reason === 'stopped'
          ? '已停止 · ' + cnt + ' 字'
          : '已完成 · ' + cnt + ' 字';
      }
      // 流式期间是展开的，完成后自动收起（用户可点头部重新展开）
      block.classList.remove('open');
    }

    function renderStatus(data) {
      statusGrid.innerHTML = `
        <div class="metric"><b>服务</b><span>${escapeHtml(data.status)}</span></div>
        <div class="metric"><b>模型</b><span>${escapeHtml(data.model.name)}</span></div>
        <div class="metric"><b>索引 Chunk</b><span>${escapeHtml(data.corpus.chunks)}</span></div>
      `;
      modelToggle.checked = Boolean(data.model.enabled);
      // 存储状态数据供 updateTopPills 统一渲染
      window._statusData = data;
      updateTopPills();
      courseList.innerHTML = (data.corpus.courses || []).map(row => `
        <div class="course-row">
          <span>${escapeHtml(row.course)}</span>
          <b>${escapeHtml(row.chunks)}</b>
        </div>
      `).join('') || '<div class="subtle">尚未建立索引</div>';
    }

    // 统一的顶栏 pill 渲染：合并服务状态 + 上下文轮次，避免多处覆盖竞争
    let _contextCount = 0;
    function updateTopPills() {
      const d = window._statusData;
      if (!d) return;
      const modelClass = d.model.enabled ? 'ok' : 'warn';
      const ctxClass = _contextCount > 0 ? 'ok' : '';
      topPills.innerHTML = `
        <span class="pill ok">A2A Local</span>
        <span class="pill ${modelClass}">DeepSeek ${d.model.enabled ? '已启用' : '未启用'}</span>
        <span class="pill">RAG ${escapeHtml(d.corpus.chunks)} chunks</span>
        <span class="pill ${ctxClass}">${_contextCount} 轮上下文</span>
      `;
    }

    function renderDiagnostics(result) {
      const flags = result.flags || {};
      diagnostics.innerHTML = `
        <div class="status-grid">
          <div class="metric"><b>Route</b><span>${escapeHtml(result.route)}</span></div>
          <div class="metric"><b>状态</b><span>${escapeHtml(result.status)}</span></div>
          <div class="metric"><b>模型调用</b><span>${flags.model_used ? '是' : '否'}</span></div>
          <div class="metric"><b>是否追问</b><span>${result.requires_clarification ? '是' : '否'}</span></div>
        </div>
      `;
    }

    function renderSources(result) {
      const sources = result.sources || [];
      if (!sources.length) {
        sourcesBox.innerHTML = '<div class="subtle">本轮未命中来源</div>';
        return;
      }
      sourcesBox.innerHTML = sources.map((source, index) => {
        const metadata = source.metadata || {};
        const title = metadata.title || metadata.topic || 'unknown';
        const tags = [
          metadata.source_category,
          metadata.doc_type,
          metadata.ingest_policy,
          metadata.language,
        ].filter(Boolean).join(' · ');
        return `
          <div class="source">
            <div class="source-title">[${index + 1}] ${escapeHtml(title)}</div>
            <div class="subtle">${escapeHtml(metadata.course || 'unknown')} · ${escapeHtml(tags)} · score ${escapeHtml(source.score)}</div>
            <div class="source-text">${escapeHtml(source.excerpt || source.text || '')}</div>
          </div>
        `;
      }).join('');
    }

    function formatTime(epochSeconds) {
      if (!epochSeconds) return '';
      return new Date(epochSeconds * 1000).toLocaleString('zh-CN', {
        month: '2-digit',
        day: '2-digit',
        hour: '2-digit',
        minute: '2-digit',
      });
    }

    function renderHistory(items) {
      if (!items.length) {
        historyList.innerHTML = '<div class="subtle">暂无聊天记录</div>';
        return;
      }
      historyList.innerHTML = items.map(item => `
        <div class="record-item" data-record-id="${escapeHtml(item.id)}">
          <div class="record-title">${escapeHtml(item.query)}</div>
          <div class="record-meta">
            <span>${escapeHtml(item.route)}</span>
            <span>${escapeHtml(formatTime(item.created_at))}</span>
            <span>${item.flags && item.flags.model_used ? 'DeepSeek' : '离线'}</span>
          </div>
        </div>
      `).join('');
      historyList.querySelectorAll('.record-item').forEach((node, index) => {
        node.addEventListener('click', () => {
          const item = items[index];
          // 切换到该记录所属会话，让后续对话与上下文面板基于这个 session
          if (item.session_id && item.session_id !== sessionId) {
            sessionId = item.session_id;
            try { window.localStorage.setItem('agent-session-id', sessionId); } catch (_) {}
          }
          // 在消息区重放当时的问答——否则点进去看不到对话内容
          messages.innerHTML = '';
          addMessage('user', item.query || '');
          if (item.answer) addMessage('assistant', item.answer);
          rawBox.textContent = JSON.stringify(item, null, 2);
          renderSources({sources: item.sources || []});
          renderDiagnostics({
            route: item.route,
            status: 'saved',
            flags: item.flags || {},
            requires_clarification: false,
          });
          loadContext().catch(() => {});
        });
      });
    }

    function renderTestRuns(items) {
      if (!items.length) {
        testRunList.innerHTML = '<div class="subtle">暂无测试记录</div>';
        return;
      }
      testRunList.innerHTML = items.map(item => {
        const report = item.report || {};
        return `
          <div class="record-item">
            <div class="record-title">评测 ${escapeHtml(report.total || 0)} 条 · 命中率 ${escapeHtml(report.source_hit_rate ?? 0)}</div>
            <div class="record-meta">
              <span>${escapeHtml(formatTime(item.created_at))}</span>
              <span>guard ${escapeHtml((report.route_counts || {}).guard || 0)}</span>
              <span>追问 ${escapeHtml(report.clarification_count || 0)}</span>
            </div>
          </div>
        `;
      }).join('');
      testRunList.querySelectorAll('.record-item').forEach((node, index) => {
        node.addEventListener('click', () => {
          rawBox.textContent = JSON.stringify(items[index], null, 2);
        });
      });
    }

    async function loadStatus() {
      const response = await fetch('/api/panel/status');
      if (!response.ok) throw new Error(`status ${response.status}`);
      renderStatus(await response.json());
    }

    async function loadHistory() {
      const response = await fetch('/api/panel/history?limit=12');
      if (!response.ok) throw new Error(`history ${response.status}`);
      renderHistory((await response.json()).items || []);
    }

    async function loadTestRuns() {
      const response = await fetch('/api/panel/test-runs?limit=8');
      if (!response.ok) throw new Error(`test-runs ${response.status}`);
      renderTestRuns((await response.json()).items || []);
    }

    // ------------------------------------------------ 对话上下文
    const contextPanel = document.getElementById('contextPanel');

    async function loadContext() {
      try {
        const response = await fetch('/api/panel/context?session_id=' + encodeURIComponent(sessionId));
        if (!response.ok) return;
        renderContext(await response.json());
      } catch (_) { /* 上下文加载失败静默 */ }
    }

    function renderContext(ctx) {
      const turns = ctx.turns || [];
      const count = ctx.turn_count || 0;
      const max = ctx.max_turns || 16;
      const pillClass = count > 0 ? 'ctx-badge' : 'ctx-badge empty';

      // 更新全局上下文计数，触发顶栏 pill 统一渲染
      _contextCount = count;
      updateTopPills();
      const hintEl = document.getElementById('ctxHintText');
      if (hintEl) hintEl.textContent = count > 0 ? `已记住 ${count} 轮对话，可继续深入` : '新对话';

      if (!turns.length) {
        contextPanel.innerHTML = `
          <div class="ctx-summary">
            <span class="${pillClass}">0</span>
            <span class="subtle">模型还没有看到历史对话</span>
          </div>
        `;
        return;
      }

      const turnsHtml = turns.map(t => `
        <div class="ctx-turn ${t.role}">
          <div class="ctx-turn-role">${t.role === 'user' ? '学生' : '导师'}</div>
          <div class="ctx-turn-preview">${escapeHtml(t.preview)}</div>
        </div>
      `).join('');

      contextPanel.innerHTML = `
        <div class="ctx-summary">
          <span class="${pillClass}">${count}</span>
          <span class="subtle">/${max} 条 · 模型可看到这些对话</span>
        </div>
        <div class="ctx-turns">${turnsHtml}</div>
      `;
    }

    async function ask(query) {
      addMessage('user', query);
      // 进入流式态：隐藏发送、显示停止，建立可中断的 AbortController
      isStreaming = true;
      abortController = new AbortController();
      currentTaskId = null;
      sendButton.disabled = true;
      stopButton.hidden = false;
      const pending = addMessage('assistant', '', 'pending');
      pending.innerHTML = renderPending('检索知识库');
      // 思考链容器：插在回答气泡之前，每轮 agent 迭代一个暗色可折叠思考块
      const reasoningHost = document.createElement('div');
      reasoningHost.className = 'think-host';
      messages.insertBefore(reasoningHost, pending);
      let currentReasoning = null;   // 当前未完成的思考块（新一轮 thinking 到来时新建）
      let toolCount = 0;
      // 图挂在气泡外的独立容器：文字气泡在流式期间会被反复重写
      // （textContent 覆盖），图必须不受影响，否则每来一个 token 就被抹掉
      const artifactHost = document.createElement('div');
      artifactHost.className = 'artifact-host';
      messages.appendChild(artifactHost);
      let acc = '';
      let finalData = null;
      let streaming = false;
      let aborted = false;
      try {
        const response = await fetch('/api/panel/chat/stream', {
          method: 'POST',
          headers: {'Content-Type': 'application/json'},
          body: JSON.stringify({query, use_model: modelToggle.checked, answer_style: answerStyle, session_id: sessionId}),
          signal: abortController.signal,
        });
        if (!response.ok || !response.body) {
          const detail = await response.text().catch(() => '');
          throw new Error(detail || `status ${response.status}`);
        }
        const reader = response.body.getReader();
        const decoder = new TextDecoder();
        let buffer = '';
        for (;;) {
          const {value, done} = await reader.read();
          if (done) break;
          buffer += decoder.decode(value, {stream: true});
          let sep;
          while ((sep = buffer.indexOf('\n\n')) !== -1) {
            const chunk = buffer.slice(0, sep);
            buffer = buffer.slice(sep + 2);
            const evt = parseSseChunk(chunk);
            if (!evt) continue;
            if (evt.event === 'meta') {
              finalData = evt.data;
              currentTaskId = evt.data.taskId || null;   // 记下 task_id 供停止上报
              renderSources(evt.data);
              // 图不依赖 LLM 文本，meta 一到就画 —— 学生在 token 还在流的
              // 时候已经能拖动图了
              renderArtifacts(evt.data.artifacts, artifactHost);
              pending.innerHTML = renderPending(modelToggle.checked ? '正在生成回答' : '整理答案');
            } else if (evt.event === 'thinking') {
              // DeepSeek 真实思考链：每轮 thinking 到来时若无活跃块则新建，流式追加文本
              if (!currentReasoning) {
                currentReasoning = createReasoningBlock(reasoningHost);
              }
              appendReasoning(currentReasoning, evt.data.text || '');
              // 粘底滚动（思考链流式期间也要跟到底）
              const nearBottom = messages.scrollTop + messages.clientHeight >= messages.scrollHeight - 80;
              if (nearBottom) messages.scrollTop = messages.scrollHeight;
            } else if (evt.event === 'delta') {
              // 首个回答 token：本轮思考结束，收起思考块
              if (currentReasoning) { finalizeReasoning(currentReasoning); currentReasoning = null; }
              if (!streaming) { streaming = true; pending.classList.remove('pending'); }
              // 粘底：仅当用户已在底部附近时才自动滚，避免向上查看历史时被每个 token 拉回
              const nearBottom = messages.scrollTop + messages.clientHeight >= messages.scrollHeight - 80;
              acc += (evt.data.text || '');
              pending.textContent = acc;          // 流式阶段用纯文本，避免半截 Markdown/公式
              if (nearBottom) messages.scrollTop = messages.scrollHeight;
            } else if (evt.event === 'tool_call') {
              // 工具调用：本轮思考结束，收起思考块；保留轻量步骤芯片
              if (currentReasoning) { finalizeReasoning(currentReasoning); currentReasoning = null; }
              renderToolStep(artifactHost, evt.data, 'call');
            } else if (evt.event === 'tool_result') {
              toolCount += 1;
              renderToolStep(artifactHost, evt.data, 'result');
            } else if (evt.event === 'artifact_offer') {
              // 按需组件：对话生成后给出「生成可视化」按钮，点击才制作
              renderArtifactButton(artifactHost, evt.data);
            } else if (evt.event === 'artifact') {
              // Tier 2 补发的可调组件：规则未命中时，模型在答案流完后补画一张图
              renderArtifacts([evt.data.artifact], artifactHost);
            } else if (evt.event === 'final') {
              finalData = evt.data;
            }
          }
        }
        const data = finalData || {content: acc};
        pending.classList.remove('pending');
        pending.innerHTML = renderMarkdown(data.content || acc || '');
        typesetMath(pending);                     // 收尾一次性渲染 Markdown + KaTeX
        renderDiagnostics(data);
        renderSources(data);
        appendSourcesToMessage(pending, data);   // 用户模式：来源以引文卡片附在 AI 气泡后
        renderArtifacts(data.artifacts, artifactHost);   // meta 缺失时的兜底（幂等）
        // 思考链收尾：若仍有未收起的思考块（如模型无 delta 直接 done），收起它
        if (currentReasoning) { finalizeReasoning(currentReasoning); currentReasoning = null; }
        // 反馈条：让用户对这条回答反馈
        appendFeedbackBar(pending, query, data);
        rawBox.textContent = JSON.stringify(data, null, 2);
        loadHistory().catch(() => {});
        loadStatus().catch(() => {});
        loadContext().catch(() => {});
      } catch (error) {
        aborted = (error && error.name === 'AbortError');
        pending.classList.remove('pending');
        if (aborted) {
          // 用户主动停止：保留已生成的文本，标注「已停止」
          pending.innerHTML = renderMarkdown((acc || '（已停止）') + '\n\n> ⏹ 已停止生成。');
          // 思考链：标注已停止
          if (currentReasoning) { finalizeReasoning(currentReasoning, 'stopped'); currentReasoning = null; }
        } else {
          pending.innerHTML = renderMarkdown(`请求失败：${error.message}`);
          // 失败时移除思考链容器（无内容可看）
          if (reasoningHost && reasoningHost.parentNode) reasoningHost.remove();
        }
        typesetMath(pending);
      } finally {
        // 退出流式态：恢复发送按钮、隐藏停止按钮
        isStreaming = false;
        abortController = null;
        currentTaskId = null;
        sendButton.disabled = false;
        stopButton.hidden = true;
      }
    }

    // 停止按钮：中断前端流式读取 + 通知后端取消当前任务
    stopButton.addEventListener('click', () => {
      if (!isStreaming) return;
      if (abortController) abortController.abort();
      if (currentTaskId) {
        fetch('/api/panel/cancel', {
          method: 'POST',
          headers: {'Content-Type': 'application/json'},
          body: JSON.stringify({task_id: currentTaskId, session_id: sessionId}),
        }).catch(() => {});
      }
    });

    // 工具调用步骤的轻量渲染（Agent 模式）：call → 进行中，result → 完成
    function renderToolStep(host, data, phase) {
      const name = data.name || data.tool || '';
      if (!name) return;
      let step = host.querySelector('.tool-step[data-tool="' + name + '"]');
      if (!step) {
        step = document.createElement('div');
        step.className = 'tool-step';
        step.setAttribute('data-tool', name);
        step.innerHTML = '<span class="tool-step-icon">' + (window.icon ? window.icon('science', 14) : '') + '</span>' +
          '<span class="tool-step-text">调用工具：' + escapeHtml(name) + '…</span>';
        host.appendChild(step);
      }
      if (phase === 'result') {
        step.classList.add('done');
        const ok = data && data.summary && !data.summary.error;
        step.querySelector('.tool-step-text').textContent =
          '工具 ' + name + (ok ? ' ✓' : '（完成）');
      }
    }

    function parseSseChunk(chunk) {
      let event = 'message';
      const dataLines = [];
      for (const line of chunk.split('\n')) {
        if (line.startsWith('event:')) event = line.slice(6).trim();
        else if (line.startsWith('data:')) dataLines.push(line.slice(5).trim());
      }
      if (!dataLines.length) return null;
      try { return {event, data: JSON.parse(dataLines.join('\n'))}; }
      catch (_) { return null; }
    }

    composer.addEventListener('submit', event => {
      event.preventDefault();
      const query = queryInput.value.trim();
      if (!query) return;
      queryInput.value = '';
      ask(query);
    });

    clearContextButton.addEventListener('click', async () => {
      clearContextButton.disabled = true;
      try {
        await fetch('/api/panel/clear-context', {
          method: 'POST',
          headers: {'Content-Type': 'application/json'},
          body: JSON.stringify({session_id: sessionId}),
        });
        // 起一个全新会话，界面清空当前对话
        try { window.localStorage.removeItem('agent-session-id'); } catch (_) {}
        sessionId = getSessionId();
        messages.innerHTML = '';
        addMessage('assistant', '已开始新对话，上文已清空。');
        loadContext().catch(() => {});
      } catch (error) {
        addMessage('assistant', `清空上下文失败：${error.message}`);
      } finally {
        clearContextButton.disabled = false;
      }
    });

    document.querySelectorAll('.quick').forEach(button => {
      button.addEventListener('click', () => {
        queryInput.value = button.dataset.q;
        queryInput.focus();
      });
    });

    document.querySelectorAll('#styleSelector .segment').forEach(button => {
      button.addEventListener('click', () => {
        answerStyle = button.dataset.style || 'rigorous';
        document.querySelectorAll('#styleSelector .segment').forEach(item => item.classList.remove('active'));
        button.classList.add('active');
      });
    });

    // ------------------------------------------------------------
    // 双模式切换（开发者 / 用户）
    // ------------------------------------------------------------
    function setMode(mode) {
      document.body.setAttribute('data-mode', mode);
      document.querySelectorAll('#modeSwitch button').forEach(b => {
        b.classList.toggle('active', b.dataset.mode === mode);
      });
      try { window.localStorage.setItem('agent-ui-mode', mode); } catch (_) {}
      // 切换后回到底部
      requestAnimationFrame(() => { messages.scrollTop = messages.scrollHeight; });
    }
    (function initMode() {
      let m = 'user';
      try { m = window.localStorage.getItem('agent-ui-mode') || 'user'; } catch (_) {}
      setMode(m);
    })();
    document.querySelectorAll('#modeSwitch button').forEach(b => {
      b.addEventListener('click', () => setMode(b.dataset.mode));
    });

    // ------------------------------------------------------------
    // 用户模式左侧抽屉：汉堡按钮开关，遮罩/关闭按钮收起。
    // 开发者模式下 .side 是 grid 列（非抽屉），切换模式时自动收起抽屉态。
    // ------------------------------------------------------------
    const drawerToggle = document.getElementById('drawerToggle');
    const drawerClose = document.getElementById('drawerClose');
    const drawerBackdrop = document.getElementById('drawerBackdrop');
    const sideEl = document.querySelector('.side');
    function openDrawer() {
      if (!sideEl) return;
      sideEl.classList.add('open');
      drawerBackdrop.classList.add('show');
    }
    function closeDrawer() {
      if (!sideEl) return;
      sideEl.classList.remove('open');
      drawerBackdrop.classList.remove('show');
    }
    if (drawerToggle) drawerToggle.addEventListener('click', () => {
      sideEl.classList.contains('open') ? closeDrawer() : openDrawer();
    });
    if (drawerClose) drawerClose.addEventListener('click', closeDrawer);
    if (drawerBackdrop) drawerBackdrop.addEventListener('click', closeDrawer);
    // 切到开发者模式时收起抽屉（dev 模式 .side 是常驻栏，不需要抽屉态）
    document.querySelectorAll('#modeSwitch button').forEach(b => {
      b.addEventListener('click', () => { if (b.dataset.mode === 'dev') closeDrawer(); });
    });
    // ESC 关抽屉
    document.addEventListener('keydown', (e) => {
      if (e.key === 'Escape' && sideEl && sideEl.classList.contains('open')) closeDrawer();
    });

    // ------------------------------------------------------------
    // 用户模式快捷 chips：data-q 直接发送；openNotes 打开笔记弹窗
    // ------------------------------------------------------------
    document.querySelectorAll('#quickChips button[data-q]').forEach(button => {
      button.addEventListener('click', () => {
        const q = button.dataset.q;
        if (!q) return;
        queryInput.value = q;
        ask(q);
        queryInput.value = '';
      });
    });

    // ------------------------------------------------------------
    // 用户模式：把来源以引文卡片附在 AI 气泡后（开发者模式仍看右栏）
    // ------------------------------------------------------------
    function appendSourcesToMessage(msgEl, result) {
      const existing = msgEl.querySelector('.msg-sources');
      if (existing) existing.remove();
      const sources = (result && result.sources) || [];
      if (!sources.length) return;
      const wrap = document.createElement('div');
      wrap.className = 'msg-sources';
      const toggle = document.createElement('button');
      toggle.type = 'button';
      toggle.className = 'msg-sources-toggle';
      toggle.innerHTML = `<span data-icon="format_quote" data-icon-size="14"></span>来源（${sources.length}）`;
      const list = document.createElement('div');
      list.className = 'msg-sources-list';
      list.innerHTML = sources.map((source, i) => {
        const m = source.metadata || {};
        const title = escapeHtml(m.title || m.topic || 'unknown');
        const meta = escapeHtml([m.course, m.doc_type].filter(Boolean).join(' · '));
        const text = escapeHtml((source.excerpt || source.text || '').slice(0, 160));
        return `<div class="citation-card"><div class="cite-meta">[${i + 1}] ${meta} · score ${escapeHtml(source.score)}</div><div class="cite-text"><strong>${title}</strong> — ${text}</div></div>`;
      }).join('');
      toggle.addEventListener('click', () => {
        list.classList.toggle('open');
      });
      wrap.appendChild(toggle);
      wrap.appendChild(list);
      msgEl.appendChild(wrap);
    }

    // 反馈条：AI 回答完成后挂在气泡下方，让用户标记有用/需改进。
    // 点击即上报到 /api/panel/feedback（fire-and-forget），并切换激活态。
    function appendFeedbackBar(msgEl, query, data) {
      const existing = msgEl.querySelector('.feedback-bar');
      if (existing) existing.remove();
      const traceId = (data && data.flags && data.flags.trace_id) || '';
      const route = (data && data.route) || '';
      const bar = document.createElement('div');
      bar.className = 'feedback-bar';
      bar.innerHTML =
        '<span class="fb-label">这个回答：</span>' +
        '<button class="fb-btn" type="button" data-fb="up"><span data-icon="thumb_up" data-icon-size="14"></span>有帮助</button>' +
        '<button class="fb-btn" type="button" data-fb="down"><span data-icon="thumb_down" data-icon-size="14"></span>需改进</button>';
      msgEl.appendChild(bar);
      if (window.renderIcons) renderIcons(bar);
      bar.querySelectorAll('.fb-btn').forEach(btn => {
        btn.addEventListener('click', () => {
          const val = btn.dataset.fb;
          // 再次点同一个 = 取消
          const wasActive = btn.classList.contains('active');
          bar.querySelectorAll('.fb-btn').forEach(b => b.classList.remove('active'));
          if (!wasActive) btn.classList.add('active');
          const final = wasActive ? 'none' : val;
          // 上报（失败静默，不阻塞交互）
          fetch('/api/panel/feedback', {
            method: 'POST',
            headers: {'Content-Type': 'application/json'},
            body: JSON.stringify({
              query: (query || '').slice(0, 500),
              route: route, trace_id: traceId, feedback: final,
            }),
          }).catch(() => {});
        });
      });
    }

    // ------------------------------------------------------------
    // Canvas 模态：沉浸式查看模型生成的 HTML 组件
    // ------------------------------------------------------------
    const canvasModal = document.getElementById('canvasModal');
    const canvasModalBody = document.getElementById('canvasModalBody');
    const canvasModalTitle = document.getElementById('canvasModalTitle');
    function openCanvasModal(html, title) {
      canvasModalTitle.textContent = title || '可视化组件';
      canvasModalBody.innerHTML = '';
      const iframe = document.createElement('iframe');
      iframe.setAttribute('sandbox', 'allow-scripts');
      iframe.setAttribute('srcdoc', html || '');
      canvasModalBody.appendChild(iframe);
      canvasModal.classList.add('open');
      canvasModal.setAttribute('aria-hidden', 'false');
    }
    function closeModal(modal) {
      modal.classList.remove('open');
      modal.setAttribute('aria-hidden', 'true');
      const body = modal.querySelector('.canvas-modal-body');
      if (body) body.innerHTML = '';  // 释放 iframe
    }
    document.getElementById('canvasModalClose').addEventListener('click', () => closeModal(canvasModal));
    canvasModal.addEventListener('click', e => { if (e.target === canvasModal) closeModal(canvasModal); });

    // 暴露给 mountArtifact 使用（模块1前端会调用）
    window.__openCanvasModal = openCanvasModal;
    // canvas 呈现方式偏好（inline / modal / right）—— 默认 inline
    window.__canvasMode = (function () {
      try { return window.localStorage.getItem('agent-canvas-mode') || 'inline'; } catch (_) { return 'inline'; }
    })();
    window.__setCanvasMode = function (m) {
      window.__canvasMode = m;
      try { window.localStorage.setItem('agent-canvas-mode', m); } catch (_) {}
    };

    // ------------------------------------------------------------
    // 更新笔记弹窗 → POST /api/panel/notes
    // ------------------------------------------------------------
    const notesModal = document.getElementById('notesModal');
    const notesSubmit = document.getElementById('notesSubmit');
    const notesStatus = document.getElementById('notesStatus');
    function openNotesModal() {
      notesStatus.textContent = '';
      notesModal.classList.add('open');
      notesModal.setAttribute('aria-hidden', 'false');
      setTimeout(() => document.getElementById('notesText').focus(), 50);
    }
    document.getElementById('openNotes').addEventListener('click', openNotesModal);
    document.getElementById('notesModalClose').addEventListener('click', () => closeModal(notesModal));
    notesModal.addEventListener('click', e => { if (e.target === notesModal) closeModal(notesModal); });
    notesSubmit.addEventListener('click', async () => {
      const text = document.getElementById('notesText').value.trim();
      if (!text) { notesStatus.textContent = '请先粘贴笔记内容'; return; }
      notesSubmit.disabled = true;
      notesStatus.textContent = '入库中…';
      try {
        const resp = await fetch('/api/panel/notes', {
          method: 'POST',
          headers: {'Content-Type': 'application/json'},
          body: JSON.stringify({
            text,
            course: document.getElementById('notesCourse').value.trim() || '我的笔记',
            topic: document.getElementById('notesTopic').value.trim() || '',
            doc_type: 'self_note',
          }),
        });
        const data = await resp.json();
        if (!resp.ok) throw new Error(data.detail || `status ${resp.status}`);
        notesStatus.textContent = `已入库 ${data.chunks || 0} 个片段`;
        document.getElementById('notesText').value = '';
        document.getElementById('notesCourse').value = '';
        document.getElementById('notesTopic').value = '';
        loadStatus().catch(() => {});
        setTimeout(() => closeModal(notesModal), 1200);
      } catch (err) {
        notesStatus.textContent = `失败：${err.message}`;
      } finally {
        notesSubmit.disabled = false;
      }
    });
    document.addEventListener('keydown', e => {
      if (e.key === 'Escape') { closeModal(canvasModal); closeModal(notesModal); }
    });

    // 渲染所有 [data-icon] 占位为内联 SVG（图标系统启动）
    if (window.renderIcons) renderIcons();
    // 动态插入的 [data-icon]（来源切换、工具调用芯片、历史项等）也要补渲染：
    // 用 MutationObserver 监听新增节点，凡含 [data-icon] 就就地渲染。
    // 修复「init 只渲染一次 → 后续动态图标显示为空」的 bug。
    if (window.renderIcons && 'MutationObserver' in window) {
      new MutationObserver(function (mutations) {
        for (var i = 0; i < mutations.length; i++) {
          mutations[i].addedNodes.forEach(function (node) {
            if (node.nodeType !== 1) return;            // 只看元素节点
            if (node.hasAttribute && node.hasAttribute('data-icon')) {
              renderIcons(node.parentElement || node);
            } else if (node.querySelector && node.querySelector('[data-icon]')) {
              renderIcons(node);
            }
          });
        }
      }).observe(document.body, { childList: true, subtree: true });
    }

    loadStatus().catch(error => {
      statusGrid.innerHTML = `<div class="metric"><b>服务</b><span>状态读取失败</span></div>`;
      rawBox.textContent = error.message;
    });
    loadHistory().catch(() => {
      historyList.innerHTML = '<div class="subtle">聊天记录读取失败</div>';
    });
    loadTestRuns().catch(() => {
      testRunList.innerHTML = '<div class="subtle">测试记录读取失败</div>';
    });
    loadContext().catch(() => {});
  </script>
</body>
</html>"""
