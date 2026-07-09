PANEL_HTML = r"""<!doctype html>
<html lang="zh-CN">
<head>
  <meta charset="utf-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1" />
  <title>数学与统计学习导师</title>
  <link rel="icon" href="data:," />
  <link rel="stylesheet" href="/static/vendor/katex.min.css" />
  <script defer src="/static/vendor/markdown-it.min.js"></script>
  <script defer src="/static/vendor/purify.min.js"></script>
  <script defer src="/static/vendor/katex.min.js"></script>
  <script defer src="/static/vendor/auto-render.min.js"></script>
  <style>
    :root {
      --bg: #f6f7f9;
      --surface: #ffffff;
      --surface-2: #f0f3f6;
      --ink: #17202a;
      --muted: #687381;
      --line: #d7dde4;
      --accent: #256f5f;
      --accent-2: #b45f35;
      --warn: #9a3412;
      --ok: #166534;
      --radius: 8px;
      --shadow: 0 12px 28px rgba(22, 32, 42, 0.08);
    }

    * { box-sizing: border-box; }

    body {
      margin: 0;
      min-height: 100vh;
      background: var(--bg);
      color: var(--ink);
      font: 14px/1.55 system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
    }

    button, textarea, input { font: inherit; }

    .shell {
      height: 100vh;
      display: grid;
      grid-template-columns: 280px minmax(420px, 1fr) 360px;
      overflow: hidden;
    }

    .side, .inspect {
      background: var(--surface);
      border-right: 1px solid var(--line);
      padding: 18px;
      overflow: auto;
    }

    .inspect {
      border-right: 0;
      border-left: 1px solid var(--line);
    }

    .main {
      display: grid;
      grid-template-rows: auto 1fr auto;
      min-width: 0;
    }

    .topbar {
      height: 62px;
      background: var(--surface);
      border-bottom: 1px solid var(--line);
      display: flex;
      align-items: center;
      justify-content: space-between;
      padding: 0 20px;
    }

    .brand {
      display: flex;
      flex-direction: column;
      gap: 2px;
    }

    h1 {
      margin: 0;
      font-size: 18px;
      font-weight: 700;
      letter-spacing: 0;
    }

    .subtle { color: var(--muted); font-size: 12px; }

    .section { margin-bottom: 18px; }
    .section h2 {
      margin: 0 0 10px;
      font-size: 13px;
      font-weight: 700;
      color: #2d3845;
      letter-spacing: 0;
    }

    .status-grid {
      display: grid;
      gap: 8px;
    }

    .metric {
      border: 1px solid var(--line);
      border-radius: var(--radius);
      padding: 10px;
      background: var(--surface);
    }

    .metric b {
      display: block;
      font-size: 12px;
      color: var(--muted);
      font-weight: 600;
    }

    .metric span {
      display: block;
      margin-top: 3px;
      font-size: 15px;
      font-weight: 700;
      overflow-wrap: anywhere;
    }

    .pill {
      display: inline-flex;
      align-items: center;
      min-height: 26px;
      padding: 3px 8px;
      border: 1px solid var(--line);
      border-radius: 999px;
      background: var(--surface-2);
      color: #2f3a45;
      font-size: 12px;
      white-space: nowrap;
    }

    .pill.ok { color: var(--ok); border-color: #a7d5b4; background: #eef8f0; }
    .pill.warn { color: var(--warn); border-color: #edc4a7; background: #fff4ec; }

    .quick-list {
      display: grid;
      gap: 8px;
    }

    .quick {
      width: 100%;
      min-height: 38px;
      border: 1px solid var(--line);
      border-radius: var(--radius);
      background: var(--surface);
      color: var(--ink);
      text-align: left;
      padding: 8px 10px;
      cursor: pointer;
    }

    .quick:hover { border-color: var(--accent); }

    .toggle-row {
      display: flex;
      align-items: center;
      justify-content: space-between;
      gap: 10px;
      padding: 10px;
      border: 1px solid var(--line);
      border-radius: var(--radius);
      background: var(--surface);
    }

    .segmented {
      display: grid;
      grid-template-columns: repeat(3, 1fr);
      border: 1px solid var(--line);
      border-radius: var(--radius);
      overflow: hidden;
      background: var(--surface);
    }

    .segment {
      min-height: 36px;
      border: 0;
      border-right: 1px solid var(--line);
      background: var(--surface);
      color: #334155;
      cursor: pointer;
      font-weight: 650;
    }

    .segment:last-child {
      border-right: 0;
    }

    .segment.active {
      background: var(--accent);
      color: #fff;
    }

    .switch {
      position: relative;
      width: 44px;
      height: 24px;
      flex: 0 0 auto;
    }

    .switch input {
      opacity: 0;
      width: 0;
      height: 0;
    }

    .slider {
      position: absolute;
      inset: 0;
      cursor: pointer;
      background: #c8d0d9;
      border-radius: 999px;
      transition: 0.15s ease;
    }

    .slider:before {
      content: "";
      position: absolute;
      width: 18px;
      height: 18px;
      left: 3px;
      top: 3px;
      background: #fff;
      border-radius: 50%;
      box-shadow: 0 1px 4px rgba(0,0,0,0.2);
      transition: 0.15s ease;
    }

    .switch input:checked + .slider { background: var(--accent); }
    .switch input:checked + .slider:before { transform: translateX(20px); }

    .messages {
      padding: 20px;
      overflow: auto;
      display: flex;
      flex-direction: column;
      gap: 14px;
      min-height: 0;
    }

    .msg {
      max-width: 920px;
      border: 1px solid var(--line);
      border-radius: var(--radius);
      background: var(--surface);
      box-shadow: 0 2px 10px rgba(22, 32, 42, 0.04);
      padding: 14px 16px;
      white-space: pre-wrap;
      overflow-wrap: anywhere;
    }

    .msg.user {
      align-self: flex-end;
      background: #eef7f4;
      border-color: #bddbd1;
    }

    .msg.assistant {
      align-self: flex-start;
    }

    .msg.pending {
      color: #405061;
      background: #fbfcfd;
      border-style: dashed;
    }

    .typing-dots {
      display: inline-flex;
      gap: 3px;
      margin-left: 4px;
      vertical-align: middle;
    }

    .typing-dots span {
      width: 5px;
      height: 5px;
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

    .markdown {
      white-space: normal;
    }

    .markdown h1,
    .markdown h2,
    .markdown h3,
    .markdown h4 {
      margin: 12px 0 8px;
      line-height: 1.35;
      letter-spacing: 0;
    }

    .markdown h1 { font-size: 20px; }
    .markdown h2 { font-size: 18px; }
    .markdown h3 { font-size: 16px; }
    .markdown h4 { font-size: 15px; }

    .markdown p {
      margin: 8px 0;
    }

    .markdown ul,
    .markdown ol {
      margin: 8px 0;
      padding-left: 22px;
    }

    .markdown li {
      margin: 5px 0;
    }

    .markdown blockquote {
      margin: 10px 0;
      padding: 8px 12px;
      border-left: 4px solid var(--accent);
      background: #f0f7f4;
      color: #334155;
      border-radius: 0 6px 6px 0;
    }

    .markdown pre {
      margin: 10px 0;
      padding: 12px;
      background: #16202a;
      color: #eef4f8;
      border-radius: var(--radius);
      overflow: auto;
      white-space: pre;
      font-size: 13px;
      line-height: 1.5;
    }

    .markdown code {
      font-family: ui-monospace, SFMono-Regular, Consolas, "Liberation Mono", monospace;
      font-size: 0.92em;
    }

    .markdown :not(pre) > code {
      background: #edf2f7;
      border: 1px solid #dbe3ea;
      border-radius: 5px;
      padding: 1px 5px;
      color: #26323e;
    }

    .markdown table {
      width: 100%;
      border-collapse: collapse;
      margin: 10px 0;
      font-size: 13px;
      display: block;
      overflow-x: auto;
    }

    .markdown th,
    .markdown td {
      border: 1px solid var(--line);
      padding: 7px 8px;
      text-align: left;
      vertical-align: top;
    }

    .markdown th {
      background: #eef3f6;
      font-weight: 700;
    }

    .markdown a {
      color: var(--accent);
      text-decoration: none;
      border-bottom: 1px solid rgba(37, 111, 95, 0.35);
    }

    .markdown hr {
      border: 0;
      border-top: 1px solid var(--line);
      margin: 14px 0;
    }

    .math-block {
      margin: 10px 0;
      padding: 10px 12px;
      overflow-x: auto;
      background: #fbfcfd;
      border: 1px solid #dde5ec;
      border-radius: var(--radius);
      font-family: ui-monospace, SFMono-Regular, Consolas, "Liberation Mono", monospace;
      color: #26323e;
      white-space: pre;
    }

    .markdown mjx-container {
      font-size: 102%;
      line-height: 1.35;
      color: #17202a;
      max-width: 100%;
      overflow-x: auto;
      overflow-y: hidden;
      padding: 2px 0;
    }

    .markdown mjx-container[display="true"] {
      font-size: 104%;
      margin: 12px 0 !important;
      padding: 10px 12px;
      background: #fbfcfd;
      border: 1px solid #dde5ec;
      border-radius: var(--radius);
    }

    .markdown mjx-container > mjx-math {
      max-width: 100%;
    }

    .math-inline {
      font-family: ui-monospace, SFMono-Regular, Consolas, "Liberation Mono", monospace;
      background: #f4f7fa;
      border-radius: 4px;
      padding: 0 4px;
    }

    .composer {
      background: var(--surface);
      border-top: 1px solid var(--line);
      padding: 14px 20px 18px;
      display: grid;
      grid-template-columns: 1fr auto auto;
      gap: 10px;
      align-items: end;
    }

    .composer textarea { grid-column: 1 / -1; }

    #clearContext {
      background: #eef2f5;
      color: #33414f;
      border: 1px solid var(--line);
    }
    #clearContext:hover { background: #e2e8ee; }

    textarea {
      width: 100%;
      min-height: 72px;
      max-height: 180px;
      resize: vertical;
      border: 1px solid var(--line);
      border-radius: var(--radius);
      padding: 11px 12px;
      color: var(--ink);
      background: #fff;
      outline: none;
    }

    textarea:focus { border-color: var(--accent); box-shadow: 0 0 0 3px rgba(37, 111, 95, 0.14); }

    .send {
      min-width: 88px;
      min-height: 42px;
      border: 0;
      border-radius: var(--radius);
      background: var(--accent);
      color: #fff;
      font-weight: 700;
      cursor: pointer;
      padding: 10px 14px;
    }

    .send:disabled {
      background: #9aa6b2;
      cursor: wait;
    }

    .inspector-block {
      border: 1px solid var(--line);
      border-radius: var(--radius);
      background: var(--surface);
      padding: 12px;
      margin-bottom: 12px;
      box-shadow: 0 2px 10px rgba(22, 32, 42, 0.04);
    }

    .source {
      border-top: 1px solid var(--line);
      padding-top: 10px;
      margin-top: 10px;
    }

    .source:first-child {
      border-top: 0;
      padding-top: 0;
      margin-top: 0;
    }

    .source-title {
      font-weight: 700;
      margin-bottom: 5px;
      overflow-wrap: anywhere;
    }

    .source-text {
      color: #3f4b58;
      font-size: 12px;
      max-height: 120px;
      overflow: auto;
      white-space: pre-wrap;
      background: #f7f9fb;
      border: 1px solid #e2e7ed;
      border-radius: 6px;
      padding: 8px;
    }

    pre.raw {
      margin: 0;
      white-space: pre-wrap;
      overflow-wrap: anywhere;
      font-size: 12px;
      color: #2f3a45;
      background: #f7f9fb;
      border: 1px solid #e2e7ed;
      border-radius: 6px;
      padding: 8px;
      max-height: 240px;
      overflow: auto;
    }

    .course-list {
      display: grid;
      gap: 6px;
    }

    .course-row {
      display: flex;
      justify-content: space-between;
      gap: 10px;
      border-bottom: 1px solid #edf1f5;
      padding-bottom: 6px;
    }

    .course-row span:first-child {
      overflow-wrap: anywhere;
    }

    .record-list {
      display: grid;
      gap: 8px;
    }

    .record-item {
      border: 1px solid var(--line);
      border-radius: var(--radius);
      background: #fff;
      padding: 9px 10px;
      cursor: pointer;
    }

    .record-item:hover {
      border-color: var(--accent);
      background: #f7fbf9;
    }

    .record-title {
      font-weight: 700;
      font-size: 12px;
      color: #26323e;
      overflow: hidden;
      display: -webkit-box;
      -webkit-line-clamp: 2;
      -webkit-box-orient: vertical;
    }

    .record-meta {
      margin-top: 4px;
      display: flex;
      gap: 6px;
      flex-wrap: wrap;
      color: var(--muted);
      font-size: 11px;
    }

    @media (max-width: 1100px) {
      .shell {
        grid-template-columns: 240px minmax(360px, 1fr);
      }
      .inspect {
        grid-column: 1 / -1;
        border-left: 0;
        border-top: 1px solid var(--line);
      }
    }

    @media (max-width: 760px) {
      .shell {
        grid-template-columns: 1fr;
        height: auto;
        min-height: 100vh;
        overflow: visible;
      }
      .side, .inspect {
        border: 0;
        border-bottom: 1px solid var(--line);
        max-height: none;
      }
      .main {
        min-height: 70vh;
      }
      .messages {
        min-height: 40vh;
      }
      .composer {
        grid-template-columns: 1fr 1fr;
        position: sticky;
        bottom: 0;
      }
      .composer textarea { grid-column: 1 / -1; }
    }

    @media (max-width: 420px) {
      .composer { grid-template-columns: 1fr; }
      .send { width: 100%; }
    }
  </style>
</head>
<body>
  <div class="shell">
    <aside class="side">
      <div class="section">
        <h1>数学与统计学习导师</h1>
        <div class="subtle">小艺 A2A 本地调试面板</div>
      </div>

      <div class="section">
        <h2>运行状态</h2>
        <div class="status-grid" id="statusGrid">
          <div class="metric"><b>服务</b><span>加载中</span></div>
        </div>
      </div>

      <div class="section">
        <h2>模型控制</h2>
        <div class="toggle-row">
          <div>
            <b>DeepSeek 增强</b>
            <div class="subtle">关闭时只用离线路由答案</div>
          </div>
          <label class="switch" title="切换本次面板请求是否调用模型">
            <input id="modelToggle" type="checkbox" checked>
            <span class="slider"></span>
          </label>
        </div>
      </div>

      <div class="section">
        <h2>回答偏好</h2>
        <div class="segmented" id="styleSelector" aria-label="回答偏好">
          <button class="segment active" type="button" data-style="rigorous">严谨</button>
          <button class="segment" type="button" data-style="examples">举例</button>
          <button class="segment" type="button" data-style="concise">简洁</button>
        </div>
        <div class="subtle" style="margin-top:8px">默认面向理学专业，严谨优先。</div>
      </div>

      <div class="section">
        <h2>快捷指令</h2>
        <div class="quick-list">
          <button class="quick" data-q="给我制定一个四周的数理统计学习路线">制定学习路线</button>
          <button class="quick" data-q="两组成绩比较应该用什么统计方法？">统计方法选择</button>
          <button class="quick" data-q="中心极限定理是什么？">解释一个概念</button>
          <button class="quick" data-q="出一道关于 Welch t 检验的原创练习题">出一道练习题</button>
        </div>
      </div>

      <div class="section">
        <h2>语料分布</h2>
        <div id="courseList" class="course-list subtle">等待索引信息</div>
      </div>

      <div class="section">
        <h2>最近聊天</h2>
        <div id="historyList" class="record-list subtle">等待聊天记录</div>
      </div>

      <div class="section">
        <h2>测试记录</h2>
        <div id="testRunList" class="record-list subtle">等待测试记录</div>
      </div>
    </aside>

    <main class="main">
      <header class="topbar">
        <div class="brand">
          <h1>Agent 工作台</h1>
          <div class="subtle">查看回答、路由、来源和模型状态</div>
        </div>
        <div id="topPills">
          <span class="pill">A2A Local</span>
        </div>
      </header>

      <section id="messages" class="messages">
        <div class="msg assistant">输入一个真实学生问题，面板会返回答案，并在右侧显示路由、模型调用状态和 RAG 来源。</div>
      </section>

      <form id="composer" class="composer">
        <textarea id="query" placeholder="例如：中心极限定理是什么？两组成绩比较应该用什么统计方法？"></textarea>
        <button id="clearContext" class="send" type="button" title="清空多轮上下文，开始新对话">新对话</button>
        <button id="send" class="send" type="submit">发送</button>
      </form>
    </main>

    <aside class="inspect">
      <div class="section">
        <h2>本轮诊断</h2>
        <div class="inspector-block" id="diagnostics">
          <div class="subtle">还没有请求</div>
        </div>
      </div>

      <div class="section">
        <h2>RAG 来源</h2>
        <div class="inspector-block" id="sources">
          <div class="subtle">暂无来源</div>
        </div>
      </div>

      <div class="section">
        <h2>原始结果</h2>
        <pre class="raw" id="raw">{}</pre>
      </div>
    </aside>
  </div>

  <script>
    const statusGrid = document.getElementById('statusGrid');
    const courseList = document.getElementById('courseList');
    const messages = document.getElementById('messages');
    const historyList = document.getElementById('historyList');
    const testRunList = document.getElementById('testRunList');
    const composer = document.getElementById('composer');
    const queryInput = document.getElementById('query');
    const sendButton = document.getElementById('send');
    const diagnostics = document.getElementById('diagnostics');
    const sourcesBox = document.getElementById('sources');
    const rawBox = document.getElementById('raw');
    const modelToggle = document.getElementById('modelToggle');
    const topPills = document.getElementById('topPills');
    const clearContextButton = document.getElementById('clearContext');
    let answerStyle = 'rigorous';

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

    function renderPending(stage) {
      return `<strong>${escapeHtml(stage)}</strong><span class="typing-dots"><span></span><span></span><span></span></span>`;
    }

    function renderStatus(data) {
      const modelClass = data.model.enabled ? 'ok' : 'warn';
      statusGrid.innerHTML = `
        <div class="metric"><b>服务</b><span>${escapeHtml(data.status)}</span></div>
        <div class="metric"><b>模型</b><span>${escapeHtml(data.model.name)}</span></div>
        <div class="metric"><b>索引 Chunk</b><span>${escapeHtml(data.corpus.chunks)}</span></div>
      `;
      topPills.innerHTML = `
        <span class="pill ok">A2A Local</span>
        <span class="pill ${modelClass}">DeepSeek ${data.model.enabled ? '已启用' : '未启用'}</span>
        <span class="pill">RAG ${escapeHtml(data.corpus.chunks)} chunks</span>
      `;
      modelToggle.checked = Boolean(data.model.enabled);
      courseList.innerHTML = (data.corpus.courses || []).map(row => `
        <div class="course-row">
          <span>${escapeHtml(row.course)}</span>
          <b>${escapeHtml(row.chunks)}</b>
        </div>
      `).join('') || '<div class="subtle">尚未建立索引</div>';
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
          rawBox.textContent = JSON.stringify(item, null, 2);
          renderSources({sources: item.sources || []});
          renderDiagnostics({
            route: item.route,
            status: 'saved',
            flags: item.flags || {},
            requires_clarification: false,
          });
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

    async function ask(query) {
      addMessage('user', query);
      sendButton.disabled = true;
      sendButton.textContent = modelToggle.checked ? '生成中' : '检索中';
      const pending = addMessage('assistant', '', 'pending');
      pending.innerHTML = renderPending('检索知识库');
      let acc = '';
      let finalData = null;
      let streaming = false;
      try {
        const response = await fetch('/api/panel/chat/stream', {
          method: 'POST',
          headers: {'Content-Type': 'application/json'},
          body: JSON.stringify({query, use_model: modelToggle.checked, answer_style: answerStyle, session_id: sessionId}),
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
              renderSources(evt.data);
              pending.innerHTML = renderPending(modelToggle.checked ? '正在生成回答' : '整理答案');
            } else if (evt.event === 'delta') {
              if (!streaming) { streaming = true; pending.classList.remove('pending'); }
              acc += (evt.data.text || '');
              pending.textContent = acc;          // 流式阶段用纯文本，避免半截 Markdown/公式
              messages.scrollTop = messages.scrollHeight;
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
        rawBox.textContent = JSON.stringify(data, null, 2);
        loadHistory().catch(() => {});
        loadStatus().catch(() => {});
      } catch (error) {
        pending.classList.remove('pending');
        pending.innerHTML = renderMarkdown(`请求失败：${error.message}`);
      } finally {
        sendButton.disabled = false;
        sendButton.textContent = '发送';
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
  </script>
</body>
</html>"""
