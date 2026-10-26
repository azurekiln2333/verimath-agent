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
    const modelToggle = document.getElementById('modelToggle');
    const modelModeToggle = document.getElementById('modelModeToggle');
    const topStatus = document.getElementById('topStatus');
    const topbarSection = document.getElementById('topbarSection');
    const topbarMode = document.getElementById('topbarMode');
    const topSearch = document.getElementById('topSearch');
    const welcomeMarkup = document.getElementById('welcomeMessage').outerHTML;
    let answerStyle = 'concise';

    function resizeComposer() {
      const viewportHeight = window.visualViewport?.height || window.innerHeight;
      const maxHeight = Math.max(32, Math.min(180, Math.floor(viewportHeight * .25)));
      const scrollTop = queryInput.scrollTop;
      queryInput.style.maxHeight = maxHeight + 'px';
      queryInput.style.height = '0px';
      const height = Math.max(32, Math.min(queryInput.scrollHeight, maxHeight));
      queryInput.style.height = height + 'px';
      queryInput.style.overflowY = queryInput.scrollHeight > height + 1 ? 'auto' : 'hidden';
      queryInput.scrollTop = scrollTop;
    }

    function syncComposerState() {
      if (!sendButton) return;
      resizeComposer();
      sendButton.disabled = isStreaming || isRestoring || !queryInput.value.trim();
      window.verimath?.artifacts?.setBusy(isStreaming || isRestoring);
    }

    // 右侧诊断面板：显式滚轮支持，让 wheel 事件在子元素上也能滚动面板本身
    const inspectPanel = document.querySelector('.inspect');
    if (inspectPanel) {
      inspectPanel.addEventListener('wheel', function (e) {
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
    let abortController = null;
    let currentTaskId = null;
    let isStreaming = false;
    let chatSettled = Promise.resolve();
    const drafts = new Map();
    const savedScroll = new Map();
    let hasRestored = false;
    let restoreVersion = 0;
    let restoringHistory = false;
    let isRestoring = false;

    function rememberSessionUI() {
      if (!hasRestored) return;
      drafts.set(sessionId, queryInput.value); savedScroll.set(sessionId, messages.scrollTop);
      try { localStorage.setItem('verimath-session-ui-' + sessionId, JSON.stringify({ draft: queryInput.value, scroll: messages.scrollTop })); } catch (_) {}
    }
    function readSessionUI(id) {
      if (drafts.has(id)) return;
      try {
        const saved = JSON.parse(localStorage.getItem('verimath-session-ui-' + id) || '{}');
        if (typeof saved.draft === 'string') drafts.set(id, saved.draft);
        if (Number.isFinite(saved.scroll)) savedScroll.set(id, saved.scroll);
      } catch (_) {}
    }
    addEventListener('pagehide', rememberSessionUI);

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
        const inlineCode = _md.renderer.rules.code_inline;
        const fencedCode = _md.renderer.rules.fence;
        _md.renderer.rules.code_inline = function (tokens, index, options, env, self) {
          const text = restoreMathDelimiters(tokens[index].content);
          if (/^(?:\\\([\s\S]*\\\)|\\\[[\s\S]*\\\]|\$[^$]+\$|\$\$[\s\S]*\$\$)$/.test(text)) return escapeHtml(text);
          if (/^[\s0-9A-Za-zα-ωΑ-Ω⁰¹²³⁴⁵⁶⁷⁸⁹⁺⁻∇∫∑√∞≠≤≥≈·×÷−+*/^=().,|{}\[\]-]+$/u.test(text) &&
              /[α-ωΑ-Ω⁰¹²³⁴⁵⁶⁷⁸⁹∇∫∑√∞≠≤≥≈·×÷]/u.test(text)) {
            return '<span class="math-inline">' + escapeHtml(text) + '</span>';
          }
          return inlineCode(tokens, index, options, env, self);
        };
        _md.renderer.rules.fence = function (tokens, index, options, env, self) {
          if (/^(math|latex|tex)(\s|$)/i.test(tokens[index].info.trim())) {
            const formula = restoreMathDelimiters(tokens[index].content).trim()
              .replace(/^\$\$([\s\S]*)\$\$$/, '$1').replace(/^\\\[([\s\S]*)\\\]$/, '$1');
            return '<div class="math-block">\\[' + escapeHtml(formula) + '\\]</div>\n';
          }
          return fencedCode(tokens, index, options, env, self);
        };
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
      } catch (_) { }
    }

    // ------------------------------------------------ 消息渲染（头像 + 内容列）
    function addMessage(role, text, extraClass = '') {
      const row = document.createElement('div');
      row.className = 'msg-row ' + role;
      const avatar = document.createElement('div');
      avatar.className = 'avatar avatar-' + role;
      avatar.innerHTML = role === 'assistant'
        ? '<span class="avatar-mark">V</span>'
        : '<span data-icon="person" data-icon-size="20"></span>';
      const col = document.createElement('div');
      col.className = 'msg-col';
      const item = document.createElement('div');
      item.className = 'msg ' + role + (role === 'assistant' ? ' markdown' : '') + (extraClass ? ' ' + extraClass : '');
      if (role === 'assistant') {
        item.innerHTML = renderMarkdown(text);
        typesetMath(item);
      } else {
        item.textContent = text;
      }
      col.appendChild(item);
      row.appendChild(avatar);
      row.appendChild(col);
      messages.appendChild(row);
      if (window.renderIcons) renderIcons(row);
      if (!restoringHistory) messages.scrollTop = messages.scrollHeight;
      return item;
    }

    // ------------------------------------------------ 可视化件挂载
    function formatControlValue(value, step) {
      if (step >= 1) return String(Math.round(value));
      const decimals = Math.min(4, Math.max(0, Math.ceil(-Math.log10(step))));
      return value.toFixed(decimals);
    }

    function mountArtifact(spec, host) {
      if (!spec) return null;

      if (spec.kind === 'html_canvas') {
        const card = document.createElement('section');
        card.className = 'artifact artifact-gen';
        const inner = document.createElement('div');
        inner.className = 'artifact-inner';
        const head = document.createElement('div');
        head.className = 'artifact-head';
        const headLeft = document.createElement('div');
        headLeft.className = 'artifact-head-left';
        const type = document.createElement('span');
        type.className = 'artifact-type';
        type.textContent = 'Discovery Visualization · 模型生成';
        const caption = document.createElement('div');
        caption.className = 'artifact-caption';
        caption.textContent = spec.title || '交互式可视化组件';
        headLeft.appendChild(type);
        headLeft.appendChild(caption);
        head.appendChild(headLeft);
        const actions = document.createElement('div');
        actions.className = 'artifact-actions';
         const dl = document.createElement('button');
         dl.type = 'button'; dl.className = 'artifact-action'; dl.title = '下载 HTML'; dl.setAttribute('aria-label', '下载 HTML');
        dl.innerHTML = '<span data-icon="download" data-icon-size="16"></span>';
        dl.addEventListener('click', () => {
          const blob = new Blob([spec.html], { type: 'text/html' });
          const a = document.createElement('a');
          a.href = URL.createObjectURL(blob); a.download = (spec.title || 'canvas') + '.html'; a.click();
          URL.revokeObjectURL(a.href);
        });
         const expand = document.createElement('button');
         expand.type = 'button'; expand.className = 'artifact-action'; expand.title = '全屏查看'; expand.setAttribute('aria-label', '全屏查看');
        expand.innerHTML = '<span data-icon="fullscreen" data-icon-size="16"></span>';
        expand.addEventListener('click', () => {
          openArtifactModal(card, spec.title);
        });
        actions.appendChild(dl);
        actions.appendChild(expand);
        head.appendChild(actions);
        inner.appendChild(head);

        const canvasHost = document.createElement('div');
        canvasHost.className = 'artifact-canvas';
        // 先插入文档再建 iframe：postMessage 的 event.source 只有在 iframe 已入文档后
        // 才能与它自己的 contentWindow 对上，否则 bridge 报上来的高度查不到归属。
        inner.appendChild(canvasHost);
        const iframe = document.createElement('iframe');
        iframe.setAttribute('sandbox', 'allow-scripts');
        iframe.setAttribute('srcdoc', spec.html || '');
        iframe.className = 'html-canvas-iframe';
        iframe.style.width = '100%';
        iframe.style.border = '0';
        iframe.style.background = 'transparent';
        iframe.setAttribute('title', spec.title || '可视化组件');
        canvasHost.appendChild(iframe);
        card.appendChild(inner);
        host.appendChild(card);
        // 注册必须在 iframe 真正进入文档之后：离屏 iframe 的 contentWindow 是 null，
        // 提前注册会让它进不了 canvasFrames，之后所有高度汇报都被静默丢弃
        // （表现就是"永远是 420px"）。见 autoFitIframe 的说明。
        autoFitIframe(iframe, spec.height || 320);
        if (window.renderIcons) renderIcons(card);
        return card;
      }

      if (!window.widgets || !window.widgets.has(spec.kind)) return null;
      const widget = window.widgets.get(spec.kind);

      // canvasHost 必须先声明：下载/全屏按钮的闭包引用了它。
      // 放在按钮之后声明会触发 TDZ ReferenceError，整张图被 mountArtifact
      // 外层 try/catch 静默吞掉 —— 界面看起来"没报错但也没图"。
      const canvasHost = document.createElement('div');
      canvasHost.className = 'artifact-canvas';

      const card = document.createElement('section');
      card.className = 'artifact artifact-demo';
      const inner = document.createElement('div');
      inner.className = 'artifact-inner';
      const head = document.createElement('div');
      head.className = 'artifact-head';
      const headLeft = document.createElement('div');
      headLeft.className = 'artifact-head-left';
      const type = document.createElement('span');
      type.className = 'artifact-type';
      type.textContent = 'Discovery Visualization · 内置演示';
      const caption = document.createElement('div');
      caption.className = 'artifact-caption';
      caption.textContent = spec.title || '交互式可视化组件';
      headLeft.appendChild(type);
      headLeft.appendChild(caption);
       head.appendChild(headLeft);
       const actions = document.createElement('div');
       actions.className = 'artifact-actions';
       const download = document.createElement('button');
       download.type = 'button'; download.className = 'artifact-action'; download.title = '下载图片'; download.setAttribute('aria-label', '下载图片');
       download.innerHTML = '<span data-icon="download" data-icon-size="16"></span>';
       download.addEventListener('click', () => {
         const canvas = canvasHost.querySelector('canvas');
         if (!canvas) return;
         const link = document.createElement('a');
         link.href = canvas.toDataURL('image/png');
         link.download = (spec.title || 'visualization') + '.png';
         link.click();
       });
       const expand = document.createElement('button');
       expand.type = 'button'; expand.className = 'artifact-action'; expand.title = '全屏查看'; expand.setAttribute('aria-label', '全屏查看');
       expand.innerHTML = '<span data-icon="fullscreen" data-icon-size="16"></span>';
       expand.addEventListener('click', () => openArtifactModal(card, spec.title));
       actions.appendChild(download);
       actions.appendChild(expand);
      head.appendChild(actions);
      inner.appendChild(head);

      inner.appendChild(canvasHost);
      card.appendChild(inner);
      host.appendChild(card);

      let controls = [];
      try {
        controls = widget.controls(spec) || [];
      } catch (_) { controls = []; }

      const state = {};
      controls.forEach((c) => { state[c.key] = c.value; });
      const stateKey = 'verimath-artifact-state-' + (host.dataset.jobId || '');
      if (host.dataset.jobId) {
        try {
          const saved = JSON.parse(localStorage.getItem(stateKey) || '{}');
          controls.forEach(c => { if (Number.isFinite(saved[c.key])) state[c.key] = Math.max(c.min, Math.min(c.max, saved[c.key])); });
        } catch (_) {}
      }

      let failed = false;
      function draw() {
        if (host.dataset.jobId) { try { localStorage.setItem(stateKey, JSON.stringify(state)); } catch (_) {} }
        if (failed) return;
        // Widget renderers replace their children. Keep their occupied height while they measure
        // the new canvas so a layout read cannot clamp the chat scroll position to a shorter page.
        const previousMinHeight = canvasHost.style.minHeight;
        canvasHost.style.minHeight = canvasHost.getBoundingClientRect().height + 'px';
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
        } finally {
          canvasHost.style.minHeight = previousMinHeight;
        }
      }
      card._redraw = draw;
      draw();
      if (failed) return card;

      // 容器宽度随窗口 / 侧栏 / 全屏变化时重排：图应当随版面长大，而不是被裁掉
      if (window.ResizeObserver) {
        let lastW = 0;
        const ro = new ResizeObserver(() => {
          const w = canvasHost.clientWidth;
          // 合并同一帧的布局变化，同时让拖动侧栏与画布同步。
          if (!w || Math.abs(w - lastW) < 2) return;
          lastW = w;
          cancelAnimationFrame(card._resizeFrame);
          card._resizeFrame = requestAnimationFrame(draw);
        });
        ro.observe(canvasHost);
        card._resizeObserver = ro;
      }

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
          val.textContent = formatControlValue(state[c.key], c.step);
          row.appendChild(name);
          row.appendChild(val);
          const input = document.createElement('input');
          input.type = 'range';
          input.min = String(c.min);
          input.max = String(c.max);
          input.step = String(c.step);
          input.value = String(state[c.key]);
          input.setAttribute('aria-label', c.label);
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
        inner.appendChild(box);
      }
      return card;
    }

    function renderArtifacts(list, host) {
      if (!Array.isArray(list) || !list.length || !host) return;
      if (host.dataset.artifactsDone === '1') return;
      host.dataset.artifactsDone = '1';
      // 占位卡片立刻出现：等模型答案完整到达再挂图，中间会有上百毫秒的空档，
      // 学生会以为"没有图"。先亮标题，再补内容，视觉上是一张卡在变完整。
      const skeleton = document.createElement('div');
      skeleton.className = 'artifact artifact-pending';
      skeleton.innerHTML =
        '<div class="artifact-inner">' +
          '<div class="artifact-head"><div class="artifact-head-left">' +
            '<span class="artifact-type">Visualization · 准备中</span>' +
            '<div class="artifact-caption">' + escapeHtml(list[0].title || '可视化') + '</div>' +
          '</div><span class="artifact-spinner" aria-hidden="true"></span></div>' +
          '<div class="artifact-skel-chart" aria-hidden="true"></div>' +
        '</div>';
      host.appendChild(skeleton);
      let mounted = 0;
      list.forEach((spec) => {
        try {
          const card = mountArtifact(spec, host);
          if (card && card !== skeleton) { mounted += 1; card.classList.add('artifact-in'); }
        } catch (_) { }
      });
      skeleton.remove();
      messages.scrollTop = messages.scrollHeight;
      return mounted;
    }

    function renderArtifactButton(host, offer) {
      return window.verimath.artifacts.offer(host, offer);
    }

    function nearBottomSafe() {
      return messages.scrollTop + messages.clientHeight >= messages.scrollHeight - 80;
    }

    function renderPending(stage) {
      return `<strong>${escapeHtml(stage)}</strong><span class="typing-dots"><span></span><span></span><span></span></span>`;
    }

    function formatReasoningItems(text) {
      // 把思考文本按行/句子拆成项目符号列表，便于阅读
      return text.split(/\n+/).map(function (line) {
        return line.trim();
      }).filter(function (line) {
        return line.length > 0;
      });
    }

    var TOOL_LABELS = {
      calculate_calculus: '核对微积分计算',
      plot_distribution: '生成分布图',
      search_knowledge_base: '查阅本地知识库',
      generate_exercise: '生成练习题',
      recommend_method: '选择统计方法',
      build_canvas: '构建可视化组件',
    };

    // ============================================================
    // 对话区骨架：标题行 + 正文 + 伴随物（工具/可视化/反馈）
    //
    // 之前的三处割裂都在这里收口：
    //   1) 每次提问结束时，活动行、正文、可视化卡、反馈条各自被追加到不同祖先上，
    //      宽窄不一、上下错位，读起来像三块拼起来的布。
    //   2) 可视化卡排在整条回答的最下面，学生读到"可视化已生成"时图还在屏幕外。
    //   3) 图定高 420px，内容比框矮时下半截全是白。
    // 现在：一条回答 = 一个 body；图在正文之后、追问之前；图高按 iframe 内容自适应。
    // ============================================================
    function ensureAnswerBody(col) {
      let body = col.querySelector('.msg-body');
      if (!body) {
        body = document.createElement('div');
        body.className = 'msg-body';
        col.appendChild(body);
      }
      return body;
    }

    function ensureCompanion(col) {
      let wrap = col.querySelector('.msg-companion');
      if (!wrap) {
        wrap = document.createElement('div');
        wrap.className = 'msg-companion';
        col.appendChild(wrap);
      }
      const existing = wrap.querySelector('.artifact-host');
      if (existing) return existing;
      const host = document.createElement('div');
      host.className = 'artifact-host';
      wrap.appendChild(host);
      return host;
    }

    // iframe 内容高度自适应：组件自己绘多少，卡片就多高。
    // 固定 420px 会让「割分演示」下面留一大片空白，也会把长图切掉。
    //
    // 沙箱 iframe 没有 allow-same-origin，宿主读不到它的 DOM，所以高度只能由
    // 注入的 /static/bridge.js 通过 postMessage 回传（见 watchBridgeMessages）。
    const canvasFrames = new Map();   // iframe.contentWindow -> iframe
    const frameErrors = new WeakSet();

    function failCanvas(iframe, message) {
      if (!iframe.isConnected || frameErrors.has(iframe)) return;
      frameErrors.add(iframe);
      clearTimeout(iframe._readyTimer);
      const note = document.createElement('div');
      note.className = 'artifact-frame-error';
      note.textContent = '图形运行出现问题，请重新生成可视化。';
      iframe.parentNode?.appendChild(note);
      iframe.dispatchEvent(new CustomEvent('verimath:artifact-error', {
        bubbles: true, detail: { jobId: iframe.closest('[data-job-id]')?.dataset.jobId },
      }));
      reportRenderFail(message);
    }

    function autoFitIframe(iframe, fallback) {
      const min = 160;
      const max = 760;
      const initial = Math.max(min, Math.min(max, fallback || 320));
      iframe.style.height = initial + 'px';
      // 注册进 canvasFrames，postMessage 才能按 event.source 找到归属。
      // contentWindow 在离屏阶段是 null，所以这里既当场注册、又在 load 时补一次。
      function register() {
        try {
          if (iframe.contentWindow) canvasFrames.set(iframe.contentWindow, iframe);
        } catch (_) { }
      }
      register();
      iframe._readyTimer = setTimeout(() => failCanvas(iframe, 'canvas readiness timeout'), 12000);
      let probeTimer;
      function onLoad() {
        register();
        iframe.contentWindow?.postMessage({ source: 'verimath-host', type: 'theme', dark: document.documentElement.dataset.theme === 'dark' }, '*');
        const key = iframe.closest('[data-job-id]')?.dataset.jobId;
        if (key) {
          try {
            const state = JSON.parse(localStorage.getItem('verimath-frame-state-' + key) || 'null');
            if (state) iframe.contentWindow?.postMessage({ source: 'verimath-host', type: 'restore-controls', state }, '*');
          } catch (_) {}
        }
        // 组件自己在 load 前后都会汇报；这里再请它算一次，兜住"汇报早于注册"的竞态
        probeTimer = setTimeout(function () {
          try {
            if (iframe.contentWindow) iframe.contentWindow.postMessage({ source: 'verimath-probe' }, '*');
          } catch (_) { }
        }, 260);
      }
      iframe.addEventListener('load', onLoad);
      iframe._dispose = () => {
        clearTimeout(iframe._readyTimer); clearTimeout(probeTimer);
        iframe.removeEventListener('load', onLoad);
        for (const [key, frame] of canvasFrames) if (frame === iframe) canvasFrames.delete(key);
      };
    }

    function watchBridgeMessages() {
      window.addEventListener('message', function (event) {
        const data = event.data;
        if (!data || data.source !== 'verimath-canvas') return;
        const iframe = canvasFrames.get(event.source);
        if (!iframe || !iframe.isConnected) return;
        if (data.type === 'ready') {
          clearTimeout(iframe._readyTimer);
        } else if (data.type === 'controls') {
          const key = iframe.closest('[data-job-id]')?.dataset.jobId;
          if (key && Array.isArray(data.state) && JSON.stringify(data.state).length < 32000) {
            try { localStorage.setItem('verimath-frame-state-' + key, JSON.stringify(data.state)); } catch (_) {}
          }
        } else if (data.type === 'resize') {
          const raw = Number(data.height);
          if (!Number.isFinite(raw) || raw <= 0) return;
          clearTimeout(iframe._readyTimer);
          const h = Math.max(48, Math.min(Math.round(innerHeight * 0.7), Math.ceil(raw)));
          const current = parseFloat(iframe.style.height) || 0;
          if (Math.abs(current - h) < 3) return;
          // 高度变化用一个短过渡，避免"刷"地跳一下
          iframe.classList.add('iframe-resizing');
          iframe.style.height = h + 'px';
          setTimeout(function () { iframe.classList.remove('iframe-resizing'); }, 180);
        } else if (data.type === 'error') {
          // A deferred observer notification does not mean the component crashed.
          if (/^ResizeObserver loop (?:completed with undelivered notifications\.?|limit exceeded\.?)$/.test(data.message || '')) return;
          failCanvas(iframe, 'canvas iframe ' + data.kind + ': ' + data.message);
        }
      });
    }
    watchBridgeMessages();

    // ============================================================
    // 思考链（reasoning）：DeepSeek 真实 reasoning_content。
    // 形态学 Claude / Pi：只有一行"活动行"，随阶段原地变形
    //   思考中  →  Braille 转轮 + 最新一句想法 + 计时 + ▸（点开看全文）
    //   调用工具 →  转轮 + 工具名
    //   写回答  →  活动行自行收起，只留一个可展开的小尾巴
    // 而不是每条消息前面先撒一堆框（加载骨架 + 思考面板 + 工具条）。
    // ============================================================
    var SPINNER_FRAMES = ['⠋', '⠙', '⠹', '⠸', '⠼', '⠴', '⠦', '⠧', '⠇', '⠏'];

    function createActivityRow(host) {
      var row = document.createElement('div');
      row.className = 'activity-row idle';
      row.innerHTML =
        '<button class="activity-main" type="button" aria-expanded="false">' +
          '<span class="activity-spinner" aria-hidden="true">' + SPINNER_FRAMES[0] + '</span>' +
          '<span class="activity-verb">思考中</span>' +
          '<span class="activity-preview"></span>' +
          '<span class="activity-timer">0s</span>' +
          '<span class="activity-chevron" aria-hidden="true">›</span>' +
        '</button>' +
        '<div class="activity-body" hidden></div>';
      host.appendChild(row);

      var started = Date.now();
      var frame = 0;
      var spinner = row.querySelector('.activity-spinner');
      var verb = row.querySelector('.activity-verb');
      var preview = row.querySelector('.activity-preview');
      var timer = row.querySelector('.activity-timer');
      var chevron = row.querySelector('.activity-chevron');
      var body = row.querySelector('.activity-body');
      var main = row.querySelector('.activity-main');
      var raw = '';
      var bodyShown = false;

      var tick = setInterval(function () {
        frame = (frame + 1) % SPINNER_FRAMES.length;
        spinner.textContent = SPINNER_FRAMES[frame];
        var sec = Math.round((Date.now() - started) / 1000);
        timer.textContent = sec >= 60 ? Math.floor(sec / 60) + 'm' + (sec % 60) + 's' : sec + 's';
      }, 90);

      // 点开时显示全文；未开放区域永远不参与流式高度抖动
      main.addEventListener('click', function () {
        if (!row.classList.contains('has-body')) return;
        bodyShown = !bodyShown;
        body.hidden = !bodyShown;
        row.classList.toggle('open', bodyShown);
        main.setAttribute('aria-expanded', bodyShown ? 'true' : 'false');
        chevron.style.transform = bodyShown ? 'rotate(90deg)' : '';
        if (bodyShown) refreshBody();
      });

      function refreshBody() {
        // 展开时即便还没收到新 token 也要把已有内容铺上（否则点了箭头是空白）
        if (!bodyShown) return;
        body.innerHTML = '<ul class="reasoning-list">' + formatReasoningItems(raw).map(function (item) {
          return '<li><span class="bullet">›</span><span>' + escapeHtml(item) + '</span></li>';
        }).join('') + '</ul>';
        body.scrollTop = body.scrollHeight;
      }
      return {
        row: row,
        setPhase: function (label, spinning) {
          verb.textContent = label;
          row.classList.toggle('idle', !spinning);
          row.classList.toggle('running', !!spinning);
        },
        appendReasoning: function (text) {
          if (!text) return;
          raw += text;
          // 预览取最后一行有内容的想法：学生想知道"它在想什么"，而不是看了多少次
          var lines = raw.split(/\n+/).map(function (s) { return s.trim(); }).filter(Boolean);
          var last = lines.length ? lines[lines.length - 1] : '';
          preview.textContent = last.slice(-90);
          if (raw.length > 0) {
            row.classList.add('has-body');
            chevron.style.visibility = 'visible';
            refreshBody();
          }
        },
        finalize: function (reason) {
          clearInterval(tick);
          row.classList.remove('running');
          row.classList.add(reason === 'stopped' ? 'stopped' : 'done');
          spinner.textContent = reason === 'stopped' ? '■' : '✓';
          verb.textContent = reason === 'stopped' ? '已停止' : '思考完成';
          if (reason !== 'stopped') preview.textContent = '';
          if (!bodyShown) body.hidden = true;
          if (raw && row.classList.contains('has-body')) { raw = raw; } else { row.classList.remove('has-body'); }
          if (!raw) row.classList.add('empty');
          if (window.renderIcons) renderIcons(row);
        }
      };
    }

    function renderStatus(data) {
      statusGrid.innerHTML = `
        <div class="metric"><b>服务</b><span>${escapeHtml(data.status)}</span></div>
        <div class="metric"><b>模型</b><span>${escapeHtml(data.model.name)}</span></div>
        <div class="metric"><b>索引 Chunk</b><span>${escapeHtml(data.corpus.chunks)}</span></div>
      `;
      if (topStatus) {
        const healthy = data.status === 'ok';
        topStatus.classList.toggle('is-error', !healthy);
        topStatus.innerHTML = '<span class="status-dot" aria-hidden="true"></span><span>' +
          (healthy ? '服务正常' : '需要检查') + '</span>';
      }
      modelToggle.checked = Boolean(data.model.enabled);
      window._statusData = data;
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
        <div class="insight-card">
          <div class="insight-card-head">
            <span data-icon="analytics" data-icon-size="16"></span>
            <span class="label">Execution Metadata</span>
          </div>
          <div class="insight-meta-row"><span class="k">Route</span><span class="v">${escapeHtml(result.route)}</span></div>
          <div class="insight-meta-row"><span class="k">状态</span><span class="v">${escapeHtml(result.status)}</span></div>
          <div class="insight-meta-row"><span class="k">模型调用</span><span class="v">${flags.model_used ? '是' : '否'}</span></div>
          <div class="insight-meta-row"><span class="k">是否追问</span><span class="v">${result.requires_clarification ? '是' : '否'}</span></div>
          <details class="insight-raw-details">
            <summary>原始数据</summary>
            <pre class="raw" id="raw">${escapeHtml(JSON.stringify(result, null, 2))}</pre>
          </details>
        </div>
      `;
      if (window.renderIcons) renderIcons(diagnostics);
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
        const excerpt = (source.excerpt || source.text || '').slice(0, 160);
        return `
          <div class="insight-card" style="margin-bottom:12px">
            <div class="insight-card-head">
              <span data-icon="menu_book" data-icon-size="16"></span>
              <span class="label">RAG Source</span>
            </div>
            <div class="insight-card-title">[${index + 1}] ${escapeHtml(title)}</div>
            <div class="insight-card-text">${escapeHtml(excerpt)}</div>
            <div class="insight-meta-row" style="margin-top:8px;border-top:1px solid rgba(194,201,187,0.3);padding-top:8px">
              <span class="k">${escapeHtml(metadata.course || 'unknown')} · ${escapeHtml(tags)}</span>
              <span class="v ok">score ${escapeHtml(source.score)}</span>
            </div>
          </div>
        `;
      }).join('');
      if (window.renderIcons) renderIcons(sourcesBox);
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
      window._historyItems = items;
      if (!items.length) {
        historyList.innerHTML = '<div class="subtle">暂无聊天记录</div>';
        return;
      }
      historyList.innerHTML = items.map(item => `
        <div class="record-item" data-record-id="${escapeHtml(item.session_id)}">
          <div class="record-title">${escapeHtml(item.title || '新对话')}</div>
          <div class="record-meta">
            <span>${escapeHtml(formatTime(item.updated_at))}</span>
          </div>
        </div>
      `).join('');
      historyList.querySelectorAll('.record-item').forEach((node, index) => {
        node.addEventListener('click', () => {
          restoreSession(items[index].session_id);
        });
      });
      // 若搜索框有值，重新应用过滤
      if (topSearch && topSearch.value) filterHistory(topSearch.value);
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
          renderDiagnostics({ route: 'test_run', status: 'saved', flags: {}, requires_clarification: false, ...items[index] });
        });
      });
    }

    async function loadStatus() {
      const response = await fetch('/api/panel/status');
      if (!response.ok) throw new Error(`status ${response.status}`);
      renderStatus(await response.json());
    }

    async function loadHistory() {
      const response = await fetch('/api/panel/sessions?limit=100');
      if (!response.ok) throw new Error(`history ${response.status}`);
      renderHistory((await response.json()).items || []);
      historyList.querySelectorAll('.record-item').forEach((node, index) => {
        node.classList.toggle('active', window._historyItems[index].session_id === sessionId);
      });
    }

    function disposeArtifacts(host) {
      host.querySelectorAll('.artifact').forEach(card => {
        card._resizeObserver?.disconnect(); cancelAnimationFrame(card._resizeFrame);
      });
      host.querySelectorAll('.html-canvas-iframe').forEach(frame => frame._dispose?.());
    }

    function disposeMessages() {
      closeExpandedArtifact();
      disposeArtifacts(messages);
    }

    function restoreMessage(item) {
      const text = item.status === 'streaming' ? (item.content || '回答正在生成…') : item.content;
      const bubble = addMessage(item.role, text);
      const row = bubble.closest('.msg-row'); row.dataset.messageId = item.message_id;
      row.dataset.sessionId = item.session_id;
      if (item.role === 'assistant') {
        if (['cancelled', 'interrupted'].includes(item.status)) {
          const note = document.createElement('small'); note.className = 'message-status';
          note.textContent = item.status === 'cancelled' ? '已停止生成' : '回答已中断'; bubble.appendChild(note);
        }
        appendSourcesToMessage(bubble, item);
        window.verimath.artifacts.restore(ensureCompanion(bubble.parentNode), item.visualization_offers, item.artifact_jobs);
        window.verimath.artifacts.followups(row, item);
        window.verimath.artifacts.watchDiscovery(item.visualization_state === 'checking' || item.followups_state === 'checking');
      }
      return row;
    }

    async function restoreSession(nextId, { fresh = false } = {}) {
      const version = ++restoreVersion;
      isRestoring = true; syncComposerState();
      if (isStreaming) { abortController?.abort(); await chatSettled; }
      if (version !== restoreVersion) return;
      rememberSessionUI(); hasRestored = true;
      sessionId = nextId;
      document.dispatchEvent(new CustomEvent('verimath:session-change', { detail: { sessionId } }));
      readSessionUI(nextId);
      try { localStorage.setItem('agent-session-id', nextId); } catch (_) {}
      queryInput.value = drafts.get(nextId) || '';
      resizeComposer();
      window.verimath.artifacts.reset(); window.verimath.resetCoach?.(); disposeMessages();
      messages.innerHTML = '';
      document.getElementById('quickChips')?.classList.toggle('chips-hidden', !fresh);
      window.verimath.layout?.closeSide();
      restoringHistory = true;
      try {
        const response = fresh ? null : await fetch('/api/panel/sessions/' + encodeURIComponent(nextId) + '/messages?limit=100');
        if (response && !response.ok) throw new Error('无法读取会话');
        const data = response ? await response.json() : { items: [] };
        if (version !== restoreVersion) return;
        if (!data.items.length) {
          messages.innerHTML = welcomeMarkup;
          document.getElementById('quickChips')?.classList.remove('chips-hidden');
        } else {
          data.items.forEach(restoreMessage);
          const last = [...data.items].reverse().find(item => item.role === 'assistant');
          if (last) {
            renderSources(last); renderDiagnostics(last);
            if (last.coach) window.verimath.onCoachEvent?.(last.coach);
            window.verimath._coachNote = null;
          }
          if (data.has_more) {
            const older = document.createElement('button'); older.type = 'button'; older.className = 'load-older'; older.textContent = '加载更早消息';
            let cursor = data.before;
            older.addEventListener('click', async () => {
              older.disabled = true;
              const anchor = older.nextElementSibling;
              const top = anchor?.getBoundingClientRect().top;
              try {
                const res = await fetch('/api/panel/sessions/' + encodeURIComponent(nextId) + '/messages?before=' + cursor);
                if (!res.ok) throw new Error('读取失败');
                const page = await res.json(); if (version !== restoreVersion) return;
                restoringHistory = true;
                const fragment = document.createDocumentFragment();
                page.items.forEach(item => fragment.appendChild(restoreMessage(item)));
                older.after(fragment); cursor = page.before;
                if (!page.has_more) older.remove();
                if (anchor?.isConnected) messages.scrollTop += anchor.getBoundingClientRect().top - top;
              } catch (_) { older.textContent = '加载失败，点击重试'; }
              finally { restoringHistory = false; older.disabled = false; }
            });
            messages.prepend(older);
          }
        }
        if (window.renderIcons) renderIcons(messages);
        messages.scrollTop = savedScroll.get(nextId) ?? messages.scrollHeight;
        if (topbarSection) topbarSection.textContent = (data.items.find(item => item.role === 'user')?.content || '新对话').slice(0, 35);
        loadContext().catch(() => {});
        loadHistory().catch(() => {});
      } catch (_) {
        if (version !== restoreVersion) return;
        const retry = document.createElement('button'); retry.type = 'button'; retry.className = 'load-older';
        retry.textContent = '会话读取失败，点击重试'; retry.onclick = () => restoreSession(nextId); messages.appendChild(retry);
      } finally {
        if (version === restoreVersion) { restoringHistory = false; isRestoring = false; }
        syncComposerState();
      }
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
      } catch (_) { }
    }

    function renderContext(ctx) {
      const turns = ctx.turns || [];
      const count = ctx.turn_count || 0;
      const max = ctx.max_turns || 16;
      const pillClass = count > 0 ? 'ctx-badge' : 'ctx-badge empty';

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
      if (isStreaming || isRestoring || !String(query || '').trim()) return;
      const welcome = document.getElementById('welcomeMessage');
      if (welcome) welcome.remove();
      // 快捷提问 chips 只服务"空对话"；对话开始后它们既没人点，又把输入条顶高、
      // 让注意力从"你刚问的问题"上飘走。这里只在有历史消息时收起。
      const chips = document.getElementById('quickChips');
      if (chips) chips.classList.add('chips-hidden');
      addMessage('user', query);
      isStreaming = true;
      let settle;
      chatSettled = new Promise(resolve => { settle = resolve; });
      const requestSession = sessionId;
      abortController = new AbortController();
      currentTaskId = null;
      syncComposerState();
      sendButton.hidden = true;       /* 发送/停止互斥：流式时只显示停止 */
      stopButton.hidden = false;
      const pending = addMessage('assistant', '', 'pending');
      pending.innerHTML = renderPending('正在思考');
      // 提问后输入条回到单行，否则光标停在上一轮的多行高度上，像"没清干净"
      resizeComposer();
      // 一条回答的全部内容都留在这一列里：活动行 → 正文 → 伴随物（工具/可视化）。
      // 之前 artifactHost 挂在 messages 上，会和正文分家、宽度也不一致。
      const column = pending.parentNode;
      const thinkHost = document.createElement('div');
      thinkHost.className = 'think-host';
      column.insertBefore(thinkHost, pending);
      const activity = createActivityRow(thinkHost);
      if (!settings.get('showThinking')) activity.row.classList.add('muted');
      let activityDone = false;
      function closeActivity(reason) {
        if (activityDone) return;
        activityDone = true;
        activity.finalize(reason);
      }
      let toolCount = 0;
      const artifactHost = ensureCompanion(column);
      let acc = '';
      let finalData = null;
      let streaming = false;
      let aborted = false;
      try {
        const response = await fetch('/api/panel/chat/stream', {
          method: 'POST',
          headers: {'Content-Type': 'application/json'},
          body: JSON.stringify({query, use_model: modelToggle.checked, answer_style: answerStyle, session_id: requestSession}),
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
              currentTaskId = evt.data.taskId || null;
              pending.closest('.msg-row').dataset.messageId = evt.data.message_id;
              pending.closest('.msg-row').dataset.sessionId = requestSession;
              renderSources(evt.data);
              pending.innerHTML = renderPending(modelToggle.checked ? '正在生成回答' : '整理答案');
            } else if (evt.event === 'thinking') {
              activity.appendReasoning(evt.data.text || '');
              if (nearBottomSafe()) messages.scrollTop = messages.scrollHeight;
            } else if (evt.event === 'delta') {
              activity.setPhase('撰写回答', true);
              if (!streaming) { streaming = true; pending.classList.remove('pending'); pending.style.display = ''; }
              acc += (evt.data.text || '');
              pending.textContent = acc;
              if (nearBottomSafe()) messages.scrollTop = messages.scrollHeight;
            } else if (evt.event === 'tool_call') {
              activity.setPhase(TOOL_LABELS[evt.data.name] || ('调用 ' + (evt.data.name || '工具')), true);
              renderToolStep(artifactHost, evt.data, 'call');
            } else if (evt.event === 'tool_result') {
              toolCount += 1;
              activity.setPhase('整理工具结果', true);
              renderToolStep(artifactHost, evt.data, 'result');
            } else if (evt.event === 'sources') {
              finalData = { ...finalData, sources: evt.data.sources || [] };
              renderSources(finalData);
            } else if (evt.event === 'artifact_offer') {
              // Offers are rendered after final; Canvas jobs have their own lifecycle.
            } else if (evt.event === 'artifact') {
              renderArtifacts([evt.data.artifact], artifactHost);
            } else if (evt.event === 'coach') {
              // 教学脚手架事件：帮助阶梯 + 误概念。侧栏卡片 + 回答下方旁注。
              if (window.verimath && window.verimath.onCoachEvent) {
                window.verimath.onCoachEvent(evt.data);
              }
            } else if (evt.event === 'final') {
              finalData = evt.data;
            }
          }
        }
        const data = finalData || {content: acc};
        closeActivity('done');
        pending.classList.remove('pending');
        pending.innerHTML = renderMarkdown(data.content || acc || '');
        typesetMath(pending);
        renderDiagnostics(data);
        renderSources(data);
        appendSourcesToMessage(pending, data);
        renderArtifacts(data.artifacts, artifactHost);
        (data.visualization_offers || []).forEach(offer => renderArtifactButton(artifactHost, offer));
        window.verimath.artifacts.followups(pending.closest('.msg-row'), data);
        window.verimath.artifacts.watchDiscovery(data.visualization_state === 'checking' || data.followups_state === 'checking');
        appendFeedbackBar(pending, query, data);
        // 帮助阶梯旁注：插在本条回答之后、反馈条之后，作为可点击的追问入口
        if (window.verimath && window.verimath._coachNote) {
          pending.appendChild(window.verimath._coachNote);
          window.verimath._coachNote = null;
        }
        loadHistory().catch(() => {});
        loadStatus().catch(() => {});
        loadContext().catch(() => {});
        if (window.verimath && window.verimath.refreshProfile) {
          try { window.verimath.refreshProfile(); } catch (_) { }
        }
      } catch (error) {
        aborted = (error && error.name === 'AbortError');
        pending.classList.remove('pending');
        if (aborted) {
          closeActivity('stopped');
          pending.innerHTML = renderMarkdown((acc || '（已停止）') + '\n\n> ⏹ 已停止生成。');
        } else {
          closeActivity('stopped');
          pending.innerHTML = renderMarkdown(`请求失败：${error.message}`);
        }
        typesetMath(pending);
        if (finalData) appendSourcesToMessage(pending, finalData);
      } finally {
        isStreaming = false;
        abortController = null;
        currentTaskId = null;
        sendButton.hidden = false;    /* 恢复发送按钮 */
        stopButton.hidden = true;
        syncComposerState();
        settle();
      }
    }

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
        const iconSpan = step.querySelector('.tool-step-icon');
        if (iconSpan && window.icon) iconSpan.innerHTML = window.icon('check_circle', 14);
        step.querySelector('.tool-step-text').textContent =
          name + (ok ? ' ✓' : '（完成）');
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
      if (isStreaming || isRestoring) return;
      const query = queryInput.value.trim();
      if (!query) return;
      queryInput.value = '';
      syncComposerState();
      ask(query);
    });

    document.getElementById('newConversation').addEventListener('click', async () => {
      const next = 'panel-' + crypto.randomUUID();
      await restoreSession(next, { fresh: true });
    });

    document.querySelectorAll('.quick').forEach(button => {
      button.addEventListener('click', () => {
        queryInput.value = button.dataset.q;
        queryInput.focus();
        queryInput.dispatchEvent(new Event('input', {bubbles: true}));
      });
    });
    messages.addEventListener('click', event => {
      const button = event.target.closest('.welcome-prompt');
      if (button?.dataset.q) { queryInput.value = button.dataset.q; queryInput.focus(); syncComposerState(); }
    });

    document.querySelectorAll('#styleSelector .segment').forEach(button => {
      button.addEventListener('click', () => {
        answerStyle = button.dataset.style || 'concise';
        document.querySelectorAll('#styleSelector .segment').forEach(item => item.classList.remove('active'));
        button.classList.add('active');
        try { window.localStorage.setItem('agent-answer-style', answerStyle); } catch (_) {}
      });
    });
    // 恢复已保存的输出模式
    (function initAnswerStyle() {
      let s = 'concise';
      try { s = window.localStorage.getItem('agent-answer-style') || 'concise'; } catch (_) {}
      answerStyle = s;
      document.querySelectorAll('#styleSelector .segment').forEach(item => {
        item.classList.toggle('active', item.dataset.style === s);
      });
    })();

    // ------------------------------------------------------------
    // 导航切换：4 项导航点击切换侧栏下半分区，localStorage 记忆
    // ------------------------------------------------------------
    function setNav(name) {
      const navTitles = { manuscripts: '对话', computations: '计算', archives: '归档', settings: '设置' };
      document.querySelectorAll('.nav-item').forEach(b => {
        b.classList.toggle('active', b.dataset.nav === name);
      });
      document.querySelectorAll('.nav-panel').forEach(p => {
        const match = p.dataset.navPanel === name;
        p.classList.toggle('active', match);
        if (match) p.removeAttribute('hidden'); else p.setAttribute('hidden', '');
      });
      if (topbarSection) topbarSection.textContent = navTitles[name] || '对话';
      try { window.localStorage.setItem('agent-nav', name); } catch (_) {}
    }
    (function initNav() {
      let n = 'manuscripts';
      try { n = window.localStorage.getItem('agent-nav') || 'manuscripts'; } catch (_) {}
      setNav(n);
    })();
    document.querySelectorAll('.nav-item').forEach(b => {
      b.addEventListener('click', () => {
        setNav(b.dataset.nav);
        if (window.innerWidth <= 860 && typeof closeDrawer === 'function') closeDrawer();
      });
    });

    // ------------------------------------------------------------
    // 双模式切换（开发者 / 用户）：Developer Mode 卡片开关
    // ------------------------------------------------------------
    function setMode(mode) {
      document.body.setAttribute('data-mode', mode);
      document.documentElement.setAttribute('data-mode', mode);
      if (modelModeToggle) modelModeToggle.checked = (mode === 'dev');
      if (topbarMode) topbarMode.textContent = mode === 'dev' ? '开发视图' : '专注模式';
      try { window.localStorage.setItem('agent-ui-mode', mode); } catch (_) {}
    }
    (function initMode() {
      let m = 'user';
      try { m = window.localStorage.getItem('agent-ui-mode') || 'user'; } catch (_) {}
      setMode(m);
    })();
    if (modelModeToggle) {
      modelModeToggle.addEventListener('change', () => {
        setMode(modelModeToggle.checked ? 'dev' : 'user');
      });
    }

    // ------------------------------------------------------------
    // 顶栏搜索框：过滤历史记录（输入即切到归档视图）
    // ------------------------------------------------------------
    function filterHistory(keyword) {
      const kw = (keyword || '').trim().toLowerCase();
      const items = window._historyItems || [];
      historyList.querySelectorAll('.record-item').forEach((node, i) => {
        const item = items[i];
        if (!item) return;
        const hay = item.title || '';
        node.style.display = (!kw || hay.toLowerCase().includes(kw)) ? '' : 'none';
      });
    }
    if (topSearch) {
      topSearch.addEventListener('input', () => {
        filterHistory(topSearch.value);
      });
    }

    function closeDrawer() { window.verimath.layout.closeSide(); }

    // ------------------------------------------------------------
    // 输入条快捷 chips：data-q 直接发送
    // ------------------------------------------------------------
    document.querySelectorAll('#quickChips button[data-q]').forEach(button => {
      button.addEventListener('click', () => {
        const q = button.dataset.q;
        if (!q || isStreaming) return;
        queryInput.value = q;
        ask(q);
        queryInput.value = '';
        syncComposerState();
      });
    });

    // ------------------------------------------------------------
    // 用户模式：把来源以引文卡片附在 AI 气泡后
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
      if (window.renderIcons) renderIcons(wrap);
    }

    function appendFeedbackBar(msgEl, query, data) {
      const existing = msgEl.querySelector('.feedback-bar');
      if (existing) existing.remove();
      const traceId = (data && data.flags && data.flags.trace_id) || '';
      const route = (data && data.route) || '';
      const bar = document.createElement('div');
      bar.className = 'feedback-bar';
      bar.innerHTML =
        '<button class="fb-btn" type="button" data-fb="up" title="有帮助"><span data-icon="thumb_up" data-icon-size="15"></span></button>' +
        '<span class="fb-divider"></span>' +
        '<button class="fb-btn" type="button" data-fb="down" title="需改进"><span data-icon="thumb_down" data-icon-size="15"></span></button>';
      msgEl.appendChild(bar);
      if (window.renderIcons) renderIcons(bar);
      bar.querySelectorAll('.fb-btn').forEach(btn => {
        btn.addEventListener('click', () => {
          const val = btn.dataset.fb;
          const wasActive = btn.classList.contains('active');
          bar.querySelectorAll('.fb-btn').forEach(b => b.classList.remove('active'));
          if (!wasActive) btn.classList.add('active');
          const final = wasActive ? 'none' : val;
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
    let expandedArtifact = null;
    function closeExpandedArtifact() {
      if (!expandedArtifact) return;
      const { card, close, focus, scroll, slot, minHeight } = expandedArtifact;
      expandedArtifact = null;
      if (card.matches(':popover-open')) card.hidePopover();
      card.removeAttribute('popover'); card.classList.remove('artifact-expanded'); close.remove();
      card._redraw?.();
      slot.style.minHeight = minHeight;
      messages.scrollTop = scroll;
      focus?.focus({ preventScroll: true });
    }
    function openArtifactModal(card, title) {
      closeExpandedArtifact();
      const close = document.createElement('button'); close.type = 'button';
      close.className = 'artifact-action artifact-close'; close.textContent = '退出放大';
      close.addEventListener('click', closeExpandedArtifact);
      const slot = card.parentElement;
      const minHeight = slot.style.minHeight;
      slot.style.minHeight = slot.getBoundingClientRect().height + 'px';
      expandedArtifact = { card, close, focus: document.activeElement, scroll: messages.scrollTop, slot, minHeight };
      card.querySelector('.artifact-actions').appendChild(close);
      card.classList.add('artifact-expanded');
      card.classList.remove('artifact-folded');
      // Popover keeps the same DOM and iframe browsing context, preserving all controls.
      card.setAttribute('popover', 'manual'); card.showPopover();
      close.focus({ preventScroll: true });
    }
    document.addEventListener('keydown', event => {
      if (event.key === 'Escape' && expandedArtifact) { event.preventDefault(); closeExpandedArtifact(); }
    });
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
    function openWidgetModal(title, render) {
      canvasModalTitle.textContent = title || '可视化组件';
      canvasModalBody.innerHTML = '';
      const host = document.createElement('div');
      host.className = 'artifact-modal-widget';
      canvasModalBody.appendChild(host);
      try {
        render(host);
      } catch (error) {
        host.textContent = '组件暂时无法在全屏视图中渲染。';
        reportRenderFail('fullscreen widget: ' + (error && error.message));
      }
      canvasModal.classList.add('open');
      canvasModal.setAttribute('aria-hidden', 'false');
    }
    function closeModal(modal) {
      modal.classList.remove('open');
      modal.setAttribute('aria-hidden', 'true');
      const body = modal.querySelector('.canvas-modal-body');
      if (body) body.innerHTML = '';
    }
    document.getElementById('canvasModalClose').addEventListener('click', () => closeModal(canvasModal));
    canvasModal.addEventListener('click', e => { if (e.target === canvasModal) closeModal(canvasModal); });

    window.__openCanvasModal = openCanvasModal;
    window.__openWidgetModal = openWidgetModal;
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

    // textarea 自适应高度
    queryInput.addEventListener('input', function () {
      syncComposerState();
    });
    // Only width changes trigger this observer; resizing the textarea itself
    // must not create a height feedback loop.
    let composerWidth = 0, composerResizeFrame = 0;
    const scheduleComposerResize = () => {
      cancelAnimationFrame(composerResizeFrame);
      composerResizeFrame = requestAnimationFrame(resizeComposer);
    };
    const composerObserver = new ResizeObserver(entries => {
      const width = entries[0].contentRect.width;
      if (Math.abs(width - composerWidth) > .5) {
        composerWidth = width;
        scheduleComposerResize();
      }
    });
    composerObserver.observe(composer);
    window.addEventListener('resize', scheduleComposerResize);
    window.visualViewport?.addEventListener('resize', scheduleComposerResize);
    queryInput.addEventListener('keydown', event => {
      if (event.key !== 'Enter' || event.shiftKey || event.isComposing || event.keyCode === 229) return;
      event.preventDefault();
      if (!sendButton.disabled) composer.requestSubmit();
    });

    // 渲染所有 [data-icon] 占位为内联 SVG + MutationObserver 动态补渲染
    if (window.renderIcons) renderIcons();
    if (window.renderIcons && 'MutationObserver' in window) {
      new MutationObserver(function (mutations) {
        for (var i = 0; i < mutations.length; i++) {
          mutations[i].addedNodes.forEach(function (node) {
            if (node.nodeType !== 1) return;
            if (node.hasAttribute && node.hasAttribute('data-icon')) {
              renderIcons(node.parentElement || node);
            } else if (node.querySelector && node.querySelector('[data-icon]')) {
              renderIcons(node);
            }
          });
        }
      }).observe(document.body, { childList: true, subtree: true });
    }

    // ============================================================
    // 设置中心：主题 / 字体大小 / 字体族 / 语言 / 背景动效 / 思考链 / 自动组件
    // localStorage 持久化，实时生效，无需刷新
    // ============================================================
    const I18N = {
      zh: {
        'nav.conversation': '对话', 'nav.computation': '计算', 'nav.archives': '归档', 'nav.settings': '设置',
        'settings.appearance': '外观', 'settings.theme': '主题', 'settings.theme.hint': '浅色 / 深色 / 跟随系统',
        'theme.light': '浅色', 'theme.dark': '深色', 'theme.auto': '自动',
        'settings.font_size': '字体大小', 'settings.font_size.hint': '正文字号缩放',
        'font_size.sm': '小', 'font_size.md': '中', 'font_size.lg': '大', 'font_size.xl': '特大',
        'settings.font_family': '界面字体', 'settings.font_family.hint': '统一字形，提升阅读稳定性',
        'font_family.serif': '衬线', 'font_family.sans': '无衬线',
        'settings.bg_animation': '背景动效', 'settings.bg_animation.hint': 'WebGL 网格动画',
        'settings.agent': '智能体', 'settings.use_model': '使用模型', 'settings.use_model.hint': '关闭时只用离线路由答案',
        'settings.output_mode': '输出模式', 'settings.output_mode.hint': '回答风格偏好',
        'output.rigorous': '严谨', 'output.examples': '举例', 'output.concise': '简洁', 'output.caveman': '极简',
        'settings.show_thinking': '显示思考链', 'settings.show_thinking.hint': '展示模型推理过程',
        'settings.auto_artifact': '自动展开可视化', 'settings.auto_artifact.hint': '关闭后只显示「生成可视化」按钮',
        'settings.language': '语言', 'settings.ui_language': '界面语言',
        'settings.service_status': '服务状态', 'settings.notes': '笔记'
      },
      en: {
        'nav.conversation': 'Chat', 'nav.computation': 'Compute', 'nav.archives': 'Archive', 'nav.settings': 'Settings',
        'settings.appearance': 'Appearance', 'settings.theme': 'Theme', 'settings.theme.hint': 'Light / Dark / System',
        'theme.light': 'Light', 'theme.dark': 'Dark', 'theme.auto': 'Auto',
        'settings.font_size': 'Font Size', 'settings.font_size.hint': 'Body text scaling',
        'font_size.sm': 'Sm', 'font_size.md': 'Md', 'font_size.lg': 'Lg', 'font_size.xl': 'XL',
        'settings.font_family': 'Interface Font', 'settings.font_family.hint': 'One clear type system for reading',
        'font_family.serif': 'Serif', 'font_family.sans': 'Sans',
        'settings.bg_animation': 'Background', 'settings.bg_animation.hint': 'WebGL grid animation',
        'settings.agent': 'Agent', 'settings.use_model': 'Use Model', 'settings.use_model.hint': 'Offline routing only when off',
        'settings.output_mode': 'Output Mode', 'settings.output_mode.hint': 'Answer style preference',
        'output.rigorous': 'Rigorous', 'output.examples': 'Examples', 'output.concise': 'Concise', 'output.caveman': 'Terse',
        'settings.show_thinking': 'Show Thinking', 'settings.show_thinking.hint': 'Display model reasoning',
        'settings.auto_artifact': 'Auto-expand visuals', 'settings.auto_artifact.hint': 'Off: show a button instead',
        'settings.language': 'Language', 'settings.ui_language': 'UI Language',
        'settings.service_status': 'Service Status', 'settings.notes': 'Notes'
      }
    };

    const settings = {
      _store: {},
      _key: 'agent-settings-v1',
      _defaults: {
        theme: 'light', fontScale: '1', fontFamily: 'sans', language: 'zh',
        bgAnimation: false, showThinking: false, autoArtifact: false
      },
      _listeners: {},
      load() {
        try {
          const raw = window.localStorage.getItem(this._key);
          if (raw) this._store = Object.assign({}, this._defaults, JSON.parse(raw));
          else this._store = Object.assign({}, this._defaults);
        } catch (_) { this._store = Object.assign({}, this._defaults); }
      },
      save() {
        try { window.localStorage.setItem(this._key, JSON.stringify(this._store)); } catch (_) {}
      },
      get(key) {
        if (!(key in this._store)) return this._defaults[key];
        return this._store[key];
      },
      set(key, value) {
        this._store[key] = value;
        this.save();
        if (this._listeners[key]) this._listeners[key].forEach(fn => { try { fn(value); } catch (_) {} });
      },
      on(key, fn) {
        if (!this._listeners[key]) this._listeners[key] = [];
        this._listeners[key].push(fn);
      }
    };
    settings.load();
    settings._store.autoArtifact = false;
    settings._store.bgAnimation = false;
    // 未支持的旧字号值迁移到默认中字号。
    (function migrateFontScale() {
      const valid = ['0.85', '1', '1.1', '1.25'];
      if (!valid.includes(String(settings.get('fontScale')))) {
        settings._store.fontScale = '1';
        settings.save();
      }
    })();

    // ---- 应用各设置项 ----
    function resolveTheme(theme) {
      if (theme === 'auto') {
        return window.matchMedia && window.matchMedia('(prefers-color-scheme: dark)').matches ? 'dark' : 'light';
      }
      return theme;
    }
    function applyTheme(theme) {
      const resolved = resolveTheme(theme);
      document.documentElement.setAttribute('data-theme', resolved);
      for (const frame of canvasFrames.values()) {
        frame.contentWindow?.postMessage({ source: 'verimath-host', type: 'theme', dark: resolved === 'dark' }, '*');
      }
      if (window.bgCanvas) window.bgCanvas.setDark(resolved === 'dark');
    }
    function applyFontScale(scale) {
      document.documentElement.style.setProperty('--fs-scale', String(scale));
    }
    function applyFontFamily(family) {
      document.body.setAttribute('data-font', family);
    }
    function applyLanguage(lang) {
      document.documentElement.setAttribute('lang', lang === 'en' ? 'en' : 'zh-CN');
      applyI18n(lang);
    }
    function applyI18n(lang) {
      const dict = I18N[lang] || I18N.zh;
      document.querySelectorAll('[data-i18n]').forEach(el => {
        const key = el.getAttribute('data-i18n');
        if (dict[key]) el.textContent = dict[key];
      });
    }
    function applyBgAnimation(on) {
      if (window.bgCanvas) { on ? window.bgCanvas.start() : window.bgCanvas.stop(); }
    }
    function applyShowThinking(on) {
      document.body.setAttribute('data-thinking', on ? 'on' : 'off');
    }
    function applyAutoArtifact() { /* 读取时由 settings.get 实时判断，无需预处理 */ }

    // ---- 设置控件激活态同步 ----
    function syncSegmented(key) {
      const val = settings.get(key);
      document.querySelectorAll('.segmented[data-setting="' + key + '"] .segment').forEach(seg => {
        seg.classList.toggle('active', seg.dataset.value === String(val));
      });
    }
    function syncSwitch(key) {
      const val = settings.get(key);
      const input = document.querySelector('input[data-setting-input="' + key + '"]');
      if (input) input.checked = Boolean(val);
    }

    // ---- 绑定 segmented 控件 ----
    document.querySelectorAll('.segmented[data-setting]').forEach(group => {
      const key = group.dataset.setting;
      group.querySelectorAll('.segment').forEach(seg => {
        seg.addEventListener('click', () => {
          let val = seg.dataset.value;
          // 数值型设置转回数字
          if (key === 'fontScale') val = parseFloat(val);
          settings.set(key, val);
        });
      });
      settings.on(key, () => syncSegmented(key));
    });

    // ---- 绑定 switch 控件 ----
    document.querySelectorAll('input[data-setting-input]').forEach(input => {
      const key = input.dataset.settingInput;
      input.addEventListener('change', () => {
        settings.set(key, input.checked);
      });
      settings.on(key, () => syncSwitch(key));
    });

    // ---- 各设置项变更回调 ----
    settings.on('theme', applyTheme);
    settings.on('fontScale', applyFontScale);
    settings.on('fontFamily', applyFontFamily);
    settings.on('language', applyLanguage);
    settings.on('bgAnimation', applyBgAnimation);
    settings.on('showThinking', applyShowThinking);
    settings.on('autoArtifact', applyAutoArtifact);

    // 系统主题变化时，若为 auto 模式则跟随
    if (window.matchMedia) {
      window.matchMedia('(prefers-color-scheme: dark)').addEventListener('change', () => {
        if (settings.get('theme') === 'auto') applyTheme('auto');
      });
    }

    // ---- 初始化：应用所有已保存设置 ----
    applyTheme(settings.get('theme'));
    applyFontScale(settings.get('fontScale'));
    applyFontFamily(settings.get('fontFamily'));
    applyLanguage(settings.get('language'));
    applyBgAnimation(settings.get('bgAnimation'));
    applyShowThinking(settings.get('showThinking'));
    syncSegmented('theme'); syncSegmented('fontScale'); syncSegmented('fontFamily'); syncSegmented('language');
    syncSwitch('bgAnimation'); syncSwitch('showThinking'); syncSwitch('autoArtifact');

    loadStatus().catch(error => {
      statusGrid.innerHTML = `<div class="metric"><b>服务</b><span>状态读取失败</span></div>`;
    });
    loadHistory().catch(() => {
      historyList.innerHTML = '<div class="subtle">聊天记录读取失败</div>';
    });
    loadTestRuns().catch(() => {
      testRunList.innerHTML = '<div class="subtle">测试记录读取失败</div>';
    });
    loadContext().catch(() => {});
    syncComposerState();

    // 学习助手（study.js）的接口：提问与当前会话 id。
    // 放在 IIFE 末尾赋值，此时 ask / sessionId 都已初始化。
    window.verimath = window.verimath || {};
    window.verimath.ask = ask;
    window.verimath.getSessionId = () => sessionId;
    window.verimath.isChatBusy = () => isStreaming || isRestoring;
    window.verimath.mountArtifact = mountArtifact;
    window.verimath.disposeArtifacts = disposeArtifacts;
    window.verimath.ensureCompanion = ensureCompanion;
    window.verimath.restoreSession = restoreSession;
    window.verimath.typesetMath = typesetMath;
    window.verimath.renderMarkdown = renderMarkdown;
    restoreSession(sessionId);
