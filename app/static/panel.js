    (function () {
      const canvas = document.getElementById('glcanvas');
      const gl = canvas && canvas.getContext('webgl');
      if (!gl) { if (canvas) canvas.style.display = 'none'; return; }
      const vs = `attribute vec2 a_position; varying vec2 v_uv;
        void main(){ gl_Position=vec4(a_position,0.0,1.0); v_uv=a_position*0.5+0.5; }`;
      const fs = `precision highp float; uniform vec2 u_res; uniform vec2 u_mouse; uniform float u_dark; varying vec2 v_uv;
        void main(){
          vec2 uv=v_uv; float aspect=u_res.x/u_res.y; vec2 g=uv*vec2(aspect,1.0);
          float density=30.0; vec2 f=fract(g*density);
          vec2 m=u_mouse/u_res; m.x*=aspect; m.y=1.0-m.y;
          float dist=distance(g*density, m*density);
          float active=smoothstep(6.0,0.0,dist);
          float thick=0.02+active*0.05;
          vec2 grid=smoothstep(0.5-thick,0.5,abs(f-0.5));
          float line=max(grid.x,grid.y);
          vec3 bgL=vec3(0.980,0.976,0.957);
          vec3 bgD=vec3(0.078,0.090,0.066);
          vec3 bg=mix(bgL,bgD,u_dark);
          vec3 lcL=mix(vec3(0.90,0.89,0.85), vec3(0.176,0.353,0.153), active*0.4);
          vec3 lcD=mix(vec3(0.13,0.15,0.12), vec3(0.25,0.50,0.30), active*0.55);
          vec3 lc=mix(lcL,lcD,u_dark);
          vec3 color=mix(bg,lc,line*0.18);
          float vignette=1.0-smoothstep(0.5,1.5,length(uv-0.5));
          color*=mix(0.97,1.0,vignette);
          gl_FragColor=vec4(color,1.0);
        }`;
      function sh(t,s){
        const x=gl.createShader(t); gl.shaderSource(x,s); gl.compileShader(x);
        if(!gl.getShaderParameter(x,gl.COMPILE_STATUS)){ console.warn(gl.getShaderInfoLog(x)); return null; }
        return x;
      }
      const vsh=sh(gl.VERTEX_SHADER,vs), fsh=sh(gl.FRAGMENT_SHADER,fs);
      if(!vsh||!fsh){ if(canvas) canvas.style.display='none'; return; }
      const prog=gl.createProgram();
      gl.attachShader(prog, vsh); gl.attachShader(prog, fsh);
      gl.linkProgram(prog);
      if(!gl.getProgramParameter(prog,gl.LINK_STATUS)){ console.warn(gl.getProgramInfoLog(prog)); if(canvas) canvas.style.display='none'; return; }
      const buf=gl.createBuffer(); gl.bindBuffer(gl.ARRAY_BUFFER,buf);
      gl.bufferData(gl.ARRAY_BUFFER, new Float32Array([-1,-1, 1,-1, -1,1, -1,1, 1,-1, 1,1]), gl.STATIC_DRAW);
      const pL=gl.getAttribLocation(prog,"a_position"), rL=gl.getUniformLocation(prog,"u_res"), mL=gl.getUniformLocation(prog,"u_mouse"), dL=gl.getUniformLocation(prog,"u_dark");
      let mx=0,my=0;
      let darkMode = document.documentElement.getAttribute('data-theme') === 'dark';
      document.addEventListener('mousemove', e=>{ mx=e.clientX; my=e.clientY; });
      function resize(){ const w=canvas.clientWidth,h=canvas.clientHeight; if(canvas.width!==w||canvas.height!==h){canvas.width=w;canvas.height=h;} }
      let rafId = null;
      function render(){ resize(); gl.viewport(0,0,canvas.width,canvas.height); gl.clearColor(0,0,0,0); gl.clear(gl.COLOR_BUFFER_BIT);
        gl.useProgram(prog); gl.enableVertexAttribArray(pL); gl.bindBuffer(gl.ARRAY_BUFFER,buf);
        gl.vertexAttribPointer(pL,2,gl.FLOAT,false,0,0); gl.uniform2f(rL,canvas.width,canvas.height); gl.uniform2f(mL,mx,my); gl.uniform1f(dL, darkMode?1.0:0.0);
        gl.drawArrays(gl.TRIANGLES,0,6); rafId = requestAnimationFrame(render); }
      // 暴露开关：设置面板可控制背景动效启停 + 主题切换
      window.bgCanvas = {
        start: function () { if (rafId === null) { canvas.style.display = ''; rafId = requestAnimationFrame(render); } },
        stop: function () { if (rafId !== null) { cancelAnimationFrame(rafId); rafId = null; canvas.style.display = 'none'; } },
        setDark: function (on) { darkMode = !!on; }
      };
      rafId = requestAnimationFrame(render);
    })();

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
    const clearContextButton = document.getElementById('clearContext');
    let answerStyle = 'rigorous';

    function syncComposerState() {
      if (!sendButton) return;
      sendButton.disabled = isStreaming || !queryInput.value.trim();
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
      messages.scrollTop = messages.scrollHeight;
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
          if (window.__openCanvasModal) window.__openCanvasModal(spec.html, spec.title);
        });
        actions.appendChild(dl);
        actions.appendChild(expand);
        head.appendChild(actions);
        inner.appendChild(head);

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
        inner.appendChild(canvasHost);
        card.appendChild(inner);
        host.appendChild(card);
        if (window.renderIcons) renderIcons(card);
        return card;
      }

      if (!window.widgets || !window.widgets.has(spec.kind)) return null;
      const widget = window.widgets.get(spec.kind);

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
       expand.addEventListener('click', () => {
         if (window.__openWidgetModal) {
           window.__openWidgetModal(spec.title, (modalHost) => widget.render(modalHost, spec, state));
         }
       });
       actions.appendChild(download);
       actions.appendChild(expand);
      head.appendChild(actions);
      inner.appendChild(head);

      const canvasHost = document.createElement('div');
      canvasHost.className = 'artifact-canvas';
      inner.appendChild(canvasHost);
      card.appendChild(inner);
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
      list.forEach((spec) => {
        try {
          mountArtifact(spec, host);
        } catch (_) { }
      });
      messages.scrollTop = messages.scrollHeight;
    }

    function renderArtifactButton(host, offer) {
      if (!offer || !host) return null;
      if (host.dataset.offerDone === '1') return null;
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
        const skel = document.createElement('div');
        skel.className = 'canvas-skeleton';
        skel.innerHTML =
          '<div class="canvas-skel-spinner"></div>' +
          '<div class="canvas-skel-text">正在制作可视化组件…</div>' +
          '<div class="canvas-skel-hint">模型正在生成可交互组件，请稍候片刻</div>' +
          '<div class="canvas-skel-bars"><span></span><span></span><span></span><span></span><span></span><span></span></div>';
        host.appendChild(skel);
        messages.scrollTop = messages.scrollHeight;
        try {
          await new Promise(r => setTimeout(r, 600));
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
          await new Promise(r => setTimeout(r, 300));
          skel.remove();
          btn.remove();
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
      return btn;
    }

    function nearBottomSafe() {
      return messages.scrollTop + messages.clientHeight >= messages.scrollHeight - 80;
    }

    function renderPending(stage) {
      return `<strong>${escapeHtml(stage)}</strong><span class="typing-dots"><span></span><span></span><span></span></span>`;
    }

    // ============================================================
    // 思考链（reasoning）：DeepSeek 真实 reasoning_content，暖黄可折叠面板。
    // ============================================================
    var TOOL_LABELS = {
      plot_distribution: '生成分布图',
      search_knowledge_base: '查阅本地知识库',
      generate_exercise: '生成练习题',
      recommend_method: '选择统计方法',
      build_canvas: '构建可视化组件',
    };

    function createReasoningBlock(host) {
      var block = document.createElement('div');
      block.className = 'reasoning-block streaming open';
      block.innerHTML =
        '<div class="reasoning-head">' +
          '<span class="reasoning-arrow">' + (window.icon ? window.icon('chevron_right', 16) : '▶') + '</span>' +
          '<span class="reasoning-label">Thought Process</span>' +
          '<span class="reasoning-status">thinking…</span>' +
        '</div>' +
        '<div class="reasoning-body"><ul class="reasoning-list"></ul></div>';
      host.appendChild(block);
      if (window.renderIcons) renderIcons(block);
      block.querySelector('.reasoning-head').addEventListener('click', function (e) {
        e.stopPropagation();
        block.classList.toggle('open');
      });
      block._rawReasoning = '';
      return block;
    }

    function formatReasoningItems(text) {
      // 把思考文本按行/句子拆成项目符号列表，便于阅读
      return text.split(/\n+/).map(function (line) {
        return line.trim();
      }).filter(function (line) {
        return line.length > 0;
      });
    }

    function appendReasoning(block, text) {
      if (!block || !text) return;
      block._rawReasoning += text;
      var body = block.querySelector('.reasoning-body');
      var list = body.querySelector('.reasoning-list');
      var items = formatReasoningItems(block._rawReasoning);
      list.innerHTML = items.map(function (item) {
        return '<li><span class="bullet">→</span><span>' + escapeHtml(item) + '</span></li>';
      }).join('');
      var cnt = block._rawReasoning.length;
      var status = block.querySelector('.reasoning-status');
      if (status && block.classList.contains('streaming')) {
        status.textContent = 'thinking · ' + cnt + ' chars';
      }
    }

    function finalizeReasoning(block, reason) {
      if (!block) return;
      block.classList.remove('streaming');
      var cnt = block._rawReasoning ? block._rawReasoning.length : 0;
      var status = block.querySelector('.reasoning-status');
      if (status) {
        status.textContent = reason === 'stopped'
          ? 'stopped · ' + cnt + ' chars'
          : 'done · ' + cnt + ' chars';
      }
      block.classList.remove('open');
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
          if (item.session_id && item.session_id !== sessionId) {
            sessionId = item.session_id;
            try { window.localStorage.setItem('agent-session-id', sessionId); } catch (_) {}
          }
          messages.innerHTML = '';
          addMessage('user', item.query || '');
          if (item.answer) addMessage('assistant', item.answer);
          renderSources({sources: item.sources || []});
          renderDiagnostics({
            route: item.route,
            status: 'saved',
            flags: item.flags || {},
            requires_clarification: false,
            sources: item.sources || [],
          });
          loadContext().catch(() => {});
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
      if (isStreaming || !String(query || '').trim()) return;
      const welcome = document.getElementById('welcomeMessage');
      if (welcome) welcome.remove();
      addMessage('user', query);
      isStreaming = true;
      abortController = new AbortController();
      currentTaskId = null;
      syncComposerState();
      sendButton.hidden = true;       /* 发送/停止互斥：流式时只显示停止 */
      stopButton.hidden = false;
      const pending = addMessage('assistant', '', 'pending');
      pending.innerHTML = renderPending('Thinking');
      const reasoningHost = document.createElement('div');
      reasoningHost.className = 'think-host';
      pending.parentNode.insertBefore(reasoningHost, pending);
      let currentReasoning = null;
      let toolCount = 0;
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
              currentTaskId = evt.data.taskId || null;
              renderSources(evt.data);
              renderArtifacts(evt.data.artifacts, artifactHost);
              pending.innerHTML = renderPending(modelToggle.checked ? '正在生成回答' : '整理答案');
            } else if (evt.event === 'thinking') {
              if (!currentReasoning && settings.get('showThinking')) {
                currentReasoning = createReasoningBlock(reasoningHost);
                pending.style.display = 'none';
              }
              if (currentReasoning) appendReasoning(currentReasoning, evt.data.text || '');
              const nearBottom = messages.scrollTop + messages.clientHeight >= messages.scrollHeight - 80;
              if (nearBottom) messages.scrollTop = messages.scrollHeight;
            } else if (evt.event === 'delta') {
              if (currentReasoning) { finalizeReasoning(currentReasoning); currentReasoning = null; }
              if (!streaming) { streaming = true; pending.classList.remove('pending'); pending.style.display = ''; }
              const nearBottom = messages.scrollTop + messages.clientHeight >= messages.scrollHeight - 80;
              acc += (evt.data.text || '');
              pending.textContent = acc;
              if (nearBottom) messages.scrollTop = messages.scrollHeight;
            } else if (evt.event === 'tool_call') {
              if (currentReasoning) { finalizeReasoning(currentReasoning); currentReasoning = null; }
              renderToolStep(artifactHost, evt.data, 'call');
            } else if (evt.event === 'tool_result') {
              toolCount += 1;
              renderToolStep(artifactHost, evt.data, 'result');
            } else if (evt.event === 'artifact_offer') {
              const offerBtn = renderArtifactButton(artifactHost, evt.data);
              // 自动生成组件：开启时自动点击按钮触发制作
              if (offerBtn && settings.get('autoArtifact')) {
                setTimeout(() => { if (!offerBtn.disabled) offerBtn.click(); }, 400);
              }
            } else if (evt.event === 'artifact') {
              renderArtifacts([evt.data.artifact], artifactHost);
            } else if (evt.event === 'final') {
              finalData = evt.data;
            }
          }
        }
        const data = finalData || {content: acc};
        pending.classList.remove('pending');
        pending.innerHTML = renderMarkdown(data.content || acc || '');
        typesetMath(pending);
        renderDiagnostics(data);
        renderSources(data);
        appendSourcesToMessage(pending, data);
        renderArtifacts(data.artifacts, artifactHost);
        if (currentReasoning) { finalizeReasoning(currentReasoning); currentReasoning = null; }
        appendFeedbackBar(pending, query, data);
        loadHistory().catch(() => {});
        loadStatus().catch(() => {});
        loadContext().catch(() => {});
      } catch (error) {
        aborted = (error && error.name === 'AbortError');
        pending.classList.remove('pending');
        if (aborted) {
          pending.innerHTML = renderMarkdown((acc || '（已停止）') + '\n\n> ⏹ 已停止生成。');
          if (currentReasoning) { finalizeReasoning(currentReasoning, 'stopped'); currentReasoning = null; }
        } else {
          pending.innerHTML = renderMarkdown(`请求失败：${error.message}`);
          if (reasoningHost && reasoningHost.parentNode) reasoningHost.remove();
        }
        typesetMath(pending);
      } finally {
        isStreaming = false;
        abortController = null;
        currentTaskId = null;
        sendButton.hidden = false;    /* 恢复发送按钮 */
        stopButton.hidden = true;
        syncComposerState();
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
      if (isStreaming) return;
      const query = queryInput.value.trim();
      if (!query) return;
      queryInput.value = '';
      queryInput.style.height = 'auto';
      syncComposerState();
      ask(query);
    });

    clearContextButton.addEventListener('click', async () => {
      if (isStreaming) return;
      clearContextButton.disabled = true;
      try {
        await fetch('/api/panel/clear-context', {
          method: 'POST',
          headers: {'Content-Type': 'application/json'},
          body: JSON.stringify({session_id: sessionId}),
        });
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

    document.querySelectorAll('.quick, .welcome-prompt').forEach(button => {
      button.addEventListener('click', () => {
        queryInput.value = button.dataset.q;
        queryInput.focus();
        queryInput.dispatchEvent(new Event('input', {bubbles: true}));
      });
    });

    document.querySelectorAll('#styleSelector .segment').forEach(button => {
      button.addEventListener('click', () => {
        answerStyle = button.dataset.style || 'rigorous';
        document.querySelectorAll('#styleSelector .segment').forEach(item => item.classList.remove('active'));
        button.classList.add('active');
        try { window.localStorage.setItem('agent-answer-style', answerStyle); } catch (_) {}
      });
    });
    // 恢复已保存的输出模式
    (function initAnswerStyle() {
      let s = 'rigorous';
      try { s = window.localStorage.getItem('agent-answer-style') || 'rigorous'; } catch (_) {}
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
      b.addEventListener('click', () => setNav(b.dataset.nav));
    });

    // ------------------------------------------------------------
    // 双模式切换（开发者 / 用户）：Developer Mode 卡片开关
    // ------------------------------------------------------------
    function setMode(mode) {
      document.body.setAttribute('data-mode', mode);
      if (modelModeToggle) modelModeToggle.checked = (mode === 'dev');
      if (topbarMode) topbarMode.textContent = mode === 'dev' ? '开发视图' : '专注模式';
      try { window.localStorage.setItem('agent-ui-mode', mode); } catch (_) {}
      requestAnimationFrame(() => { messages.scrollTop = messages.scrollHeight; });
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
        const hay = (item.query || '') + ' ' + (item.route || '');
        node.style.display = (!kw || hay.toLowerCase().includes(kw)) ? '' : 'none';
      });
    }
    if (topSearch) {
      topSearch.addEventListener('input', () => {
        if (topSearch.value) setNav('archives');
        filterHistory(topSearch.value);
      });
    }

    // ------------------------------------------------------------
    // 左侧抽屉（移动端）：汉堡按钮开关
    // ------------------------------------------------------------
    const drawerToggle = document.getElementById('drawerToggle');
    const drawerClose = document.getElementById('drawerClose');
    const drawerBackdrop = document.createElement('div');
    drawerBackdrop.className = 'drawer-backdrop';
    document.body.appendChild(drawerBackdrop);
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
    drawerBackdrop.addEventListener('click', closeDrawer);
    // 切到开发者模式时收起抽屉（dev 模式 .side 是常驻栏）
    if (modelModeToggle) {
      modelModeToggle.addEventListener('change', () => { if (modelModeToggle.checked) closeDrawer(); });
    }
    document.addEventListener('keydown', (e) => {
      if (e.key === 'Escape' && sideEl && sideEl.classList.contains('open')) closeDrawer();
    });

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
        queryInput.style.height = 'auto';
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
    document.getElementById('composerNotes').addEventListener('click', openNotesModal);
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
      this.style.height = 'auto';
      this.style.height = Math.min(this.scrollHeight, 160) + 'px';
      syncComposerState();
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
        'settings.font_family': '正文字体', 'settings.font_family.hint': '衬线 / 无衬线',
        'font_family.serif': '衬线', 'font_family.sans': '无衬线',
        'settings.bg_animation': '背景动效', 'settings.bg_animation.hint': 'WebGL 网格动画',
        'settings.agent': '智能体', 'settings.use_model': '使用模型', 'settings.use_model.hint': '关闭时只用离线路由答案',
        'settings.output_mode': '输出模式', 'settings.output_mode.hint': '回答风格偏好',
        'output.rigorous': '严谨', 'output.examples': '举例', 'output.concise': '简洁', 'output.caveman': '极简',
        'settings.show_thinking': '显示思考链', 'settings.show_thinking.hint': '展示模型推理过程',
        'settings.auto_artifact': '自动生成组件', 'settings.auto_artifact.hint': '关闭后需手动点击生成',
        'settings.language': '语言', 'settings.ui_language': '界面语言',
        'settings.service_status': '服务状态', 'settings.notes': '笔记'
      },
      en: {
        'nav.conversation': 'Chat', 'nav.computation': 'Compute', 'nav.archives': 'Archive', 'nav.settings': 'Settings',
        'settings.appearance': 'Appearance', 'settings.theme': 'Theme', 'settings.theme.hint': 'Light / Dark / System',
        'theme.light': 'Light', 'theme.dark': 'Dark', 'theme.auto': 'Auto',
        'settings.font_size': 'Font Size', 'settings.font_size.hint': 'Body text scaling',
        'font_size.sm': 'Sm', 'font_size.md': 'Md', 'font_size.lg': 'Lg', 'font_size.xl': 'XL',
        'settings.font_family': 'Font Family', 'settings.font_family.hint': 'Serif / Sans-serif',
        'font_family.serif': 'Serif', 'font_family.sans': 'Sans',
        'settings.bg_animation': 'Background', 'settings.bg_animation.hint': 'WebGL grid animation',
        'settings.agent': 'Agent', 'settings.use_model': 'Use Model', 'settings.use_model.hint': 'Offline routing only when off',
        'settings.output_mode': 'Output Mode', 'settings.output_mode.hint': 'Answer style preference',
        'output.rigorous': 'Rigorous', 'output.examples': 'Examples', 'output.concise': 'Concise', 'output.caveman': 'Terse',
        'settings.show_thinking': 'Show Thinking', 'settings.show_thinking.hint': 'Display model reasoning',
        'settings.auto_artifact': 'Auto Artifact', 'settings.auto_artifact.hint': 'Manual click required when off',
        'settings.language': 'Language', 'settings.ui_language': 'UI Language',
        'settings.service_status': 'Service Status', 'settings.notes': 'Notes'
      }
    };

    const settings = {
      _store: {},
      _key: 'agent-settings-v1',
      _defaults: {
        theme: 'light', fontScale: '0.8', fontFamily: 'serif', language: 'zh',
        bgAnimation: true, showThinking: true, autoArtifact: true
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
    // 旧版 fontScale 值（如 1）已不在可选项内，迁移到新默认中字号
    (function migrateFontScale() {
      const valid = ['0.7', '0.8', '0.95', '1.15'];
      if (!valid.includes(String(settings.get('fontScale')))) {
        settings._store.fontScale = '0.8';
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