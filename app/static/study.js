/**
 * study.js —— 学习助手抽屉。
 *
 * 与 panel.js 的分工：panel.js 管对话主链，这里只做"怎么学"的辅助面板。
 * 两边通过两个约定接口通信：
 *   window.verimath.ask(query)            —— 向导师提问（复用主链的流式渲染）
 *   window.verimath.getSessionId()        —— 取当前会话 id（学情按会话隔离）
 *   window.verimath.onCoachEvent(data)    —— panel.js 收到 coach SSE 事件后回调
 *
 * 设计原则：辅助面板的任何失败都不能影响答题主链，所以全部用 try/catch 包裹，
 * 失败时只在该面板内部显示一行提示。
 */
(function () {
  'use strict';

  var api = window.verimath = window.verimath || {};

  var drawer = document.getElementById('studyDrawer');
  var toggle = document.getElementById('studyToggle');
  var closeBtn = document.getElementById('studyClose');
  var scrim = document.getElementById('studyScrim');
  if (!drawer || !toggle) return;

  var ladderTrack = document.getElementById('ladderTrack');
  var coachBox = document.getElementById('coachBox');
  var ladderBadge = document.getElementById('ladderBadge');
  var verifyInput = document.getElementById('verifyInput');
  var verifyResult = document.getElementById('verifyResult');
  var knowledgeMap = document.getElementById('knowledgeMap');
  var profileBox = document.getElementById('profileBox');

  var LEVELS = [
    { lv: 0, name: '复述' }, { lv: 1, name: '追问' }, { lv: 2, name: '提示' },
    { lv: 3, name: '示范' }, { lv: 4, name: '解答' }
  ];

  function esc(v) {
    return String(v == null ? '' : v).replace(/[&<>"']/g, function (c) {
      return { '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;' }[c];
    });
  }
  function mathSource(value) {
    var raised = '⁰¹²³⁴⁵⁶⁷⁸⁹⁺⁻';
    var plain = '0123456789+-';
    return String(value).replace(/[⁰¹²³⁴⁵⁶⁷⁸⁹⁺⁻]+/g, function (power) {
      return '^{' + Array.from(power, function (c) { return plain[raised.indexOf(c)]; }).join('') + '}';
    }).replace(/−/g, '-').replace(/\*\*/g, '^').replace(/\*/g, '\\cdot ');
  }
  function formula(value) {
    return '\\(' + esc(mathSource(value)) + '\\)';
  }
  function typeset(host) { if (api.typesetMath) api.typesetMath(host); }
  function questionHtml(item) {
    if (item.group === 'verify') return item.question.split(' / ').map(formula).join('<br>');
    return esc(item.question).replace(/((?:y\s*=\s*)?x\^2[^\u4e00-\u9fff？?]+|x\s*=\s*[-\d]+)/g,
      value => '\\(' + value.trim() + '\\)');
  }

  // ------------------------------------------------------------ 抽屉开合

  function openDrawer() {
    api.layout.openTools();
    loadProfile();
  }
  function closeDrawer() {
    api.layout.closeTools();
  }
  // 窗口缩到窄屏时取消布局占位，避免中栏被挤成一条
  document.addEventListener('verimath:tools-tab', function (event) { selectTab(event.detail); });
  api.openStudy = function (tab) {
    openDrawer();
    if (tab) selectTab(tab);
  };

  toggle.addEventListener('click', function () { if (drawer.classList.contains('open')) loadProfile(); });

  // ------------------------------------------------------------ 标签页

  function selectTab(name) {
    document.querySelectorAll('.study-tab').forEach(function (b) {
      b.classList.toggle('active', b.dataset.studyTab === name);
      b.setAttribute('aria-selected', String(b.dataset.studyTab === name));
      b.tabIndex = b.dataset.studyTab === name ? 0 : -1;
    });
    document.querySelectorAll('.study-panel').forEach(function (p) {
      p.classList.toggle('active', p.dataset.studyPanel === name);
    });
    if (name === 'profile') loadProfile();
    if (name === 'cases') loadCases();
  }
  document.querySelectorAll('.study-tab').forEach(function (b) {
    b.addEventListener('click', function () { selectTab(b.dataset.studyTab); });
  });

  // ------------------------------------------------------------ 帮助阶梯

  function renderLadder(level, maxLevel) {
    var cur = typeof level === 'number' ? level : 0;
    ladderTrack.innerHTML = LEVELS.map(function (L) {
      var cls = 'ladder-step';
      if (L.lv < cur) cls += ' reached';
      if (L.lv === cur) cls += ' reached current';
      return '<div class="' + cls + '"><b>L' + L.lv + '</b>' + esc(L.name) + '</div>';
    }).join('');
    if (ladderBadge) {
      ladderBadge.textContent = 'L' + cur;
      ladderBadge.hidden = false;
    }
    void maxLevel;
  }
  renderLadder(0, 4);

  /**
   * coach SSE 事件 → 抽屉里的帮助卡片 + 对话里的旁注。
   *
   * 为什么旁注要直接放在回答下方：帮助阶梯的价值在于"学生看到自己此刻
   * 处在哪一级"。藏在侧栏里，大多数人不会打开。
   */
  api.onCoachEvent = function (data) {
    try {
      renderLadder(data.level, data.max_level || 4);
      var parts = [];
      parts.push('<div class="coach-card' + (data.advanced ? ' warn' : '') + '">');
      parts.push('<div class="coach-card-title">' + (data.source === 'model' ? '本轮学习提示' : '离线学习提示') + '</div>');
      if (data.opener) parts.push('<div class="coach-card-text">' + esc(data.opener) + '</div>');
      if (data.question) parts.push('<div class="coach-question">❓ ' + esc(data.question) + '</div>');
      if (data.hints && data.hints.length) {
        parts.push('<ul class="coach-hints">' + data.hints.map(function (h) {
          return '<li>' + esc(h) + '</li>';
        }).join('') + '</ul>');
      }
      if (!data.question && data.source === 'model') parts.push('<div class="coach-card-text">可以继续追问刚才的解释，或告诉我具体卡在哪一步。</div>');
      parts.push('<div class="coach-reason">' + esc(data.reason) + '</div>');
      parts.push('<div class="coach-actions">');
      if (data.question) {
        parts.push('<button class="study-ghost" data-coach-reply="' + esc(data.question) + '">我来回答这个问题</button>');
      }
      parts.push('<button class="study-ghost" data-coach-ask="我没理解刚才的关键点，请承接上一轮，换一个更直观的例子，简短讲清楚。">换个例子讲</button>');
      parts.push('<button class="study-ghost" data-coach-ask="我还是卡住了，请沿着上一轮的问题展开必要步骤，并解释每一步为什么这样做。">展开关键步骤</button>');
      parts.push('</div></div>');

      (data.misconceptions || []).forEach(function (m) {
        parts.push('<div class="coach-card warn">');
        parts.push('<div class="coach-card-title">可能的概念混淆：' + esc(m.name) + '</div>');
        parts.push('<div class="coach-card-text">' + esc(m.why) + '</div>');
        if (m.probe) parts.push('<div class="coach-question">想一想：' + esc(m.probe) + '</div>');
        parts.push('</div>');
      });
      coachBox.innerHTML = parts.join('');
      typeset(coachBox);

      var note = document.createElement('details');
      note.className = 'coach-note';
      var noteParts = ['<summary>' + (data.source === 'model' ? '继续探究' : '离线学习提示') + '</summary>'];
      if (data.opener) noteParts.push('<div>' + esc(data.opener) + '</div>');
      if (data.question) noteParts.push('<div class="coach-note-q">❓ ' + esc(data.question) + '</div>');
      noteParts.push('<div class="coach-note-reason">' + esc(data.reason) + '</div>');
      note.innerHTML = noteParts.join('');
      typeset(note);
      api._coachNote = data.question || data.source !== 'model' ? note : null;
    } catch (e) {
      coachBox.innerHTML = '<p class="study-empty">帮助阶梯渲染失败：' + esc(e.message) + '</p>';
    }
  };

  api.resetCoach = function () {
    renderLadder(0, 4);
    coachBox.innerHTML = '<p class="subtle">继续对话后，这里会显示与当前问题相关的学习提示。</p>';
    api._coachNote = null;
  };

  document.addEventListener('click', function (e) {
    var reply = e.target.closest('[data-coach-reply]');
    var ask = e.target.closest('[data-coach-ask]');
    var node = e.target.closest('.km-node');
    if (reply) {
      var ta = document.getElementById('query');
      if (ta) {
        ta.value = '对于“' + reply.getAttribute('data-coach-reply') + '”，我的理解是：';
        ta.focus();
        ta.dispatchEvent(new Event('input', { bubbles: true }));
      }
    } else if (ask) {
      if (api.ask) api.ask(ask.getAttribute('data-coach-ask'));
    } else if (node) {
      if (api.ask) api.ask(node.getAttribute('data-km-query'));
      closeDrawer();
    }
  });

  // ------------------------------------------------------------ 推导核对

  var EXAMPLE = [
    'x² − 1',
    '(x − 1)(x + 1)',
    'x² + 2x + 1'
  ].join('\n');

  function lines() {
    return (verifyInput.value || '').split('\n')
      .map(function (s) { return s.trim(); })
      .filter(function (s) { return s.length > 0; });
  }
  var verifyPreview = document.getElementById('verifyPreview');
  function previewSteps() {
    if (!verifyPreview) return;
    var steps = lines();
    var example = !steps.length;
    var content = (example ? EXAMPLE.split('\n') : steps).slice(0, 30);
    // Keep the previous height until the new math has been typeset, including at the drawer bottom.
    verifyPreview.style.minHeight = verifyPreview.offsetHeight + 'px';
    verifyPreview.innerHTML = '<div class="verify-preview-label">' + (example ? '推导示例' : '公式预览') + '</div>';
    content.forEach(function (step, index) {
      var row = document.createElement('div'); row.className = 'verify-preview-row';
      var number = document.createElement('span'); number.className = 'verify-preview-index'; number.textContent = index + 1;
      var expression = document.createElement('span'); expression.className = 'verify-preview-formula';
      try {
        if (!window.katex) throw new Error('Math renderer unavailable');
        expression.innerHTML = window.katex.renderToString(mathSource(step), { throwOnError: true, strict: 'ignore' });
      } catch (_) { expression.textContent = '继续输入，完成后显示公式'; expression.classList.add('subtle'); }
      row.append(number, expression); verifyPreview.appendChild(row);
    });
    verifyPreview.style.minHeight = '';
  }
  verifyInput.addEventListener('input', previewSteps);

  async function runVerify() {
    var steps = lines();
    if (steps.length < 2) {
      verifyResult.innerHTML = '<p class="study-empty">至少需要两行，才能比较「这一步」和「下一步」。</p>';
      return;
    }
    verifyResult.innerHTML = '<p class="study-empty">核对中…</p>';
    try {
      var resp = await fetch('/api/coach/verify-steps', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ steps: steps })
      });
      var data = await resp.json();
      if (!data.ok) {
        verifyResult.innerHTML = '<p class="study-empty">' + esc(data.error || '核对失败') + '</p>';
        return;
      }
      var tagText = { ok: '等价 ✓', sampled: '采样一致', mismatch: '不等价 ✗', undecidable: '无法判定' };
      var html = data.checks.map(function (c) {
        var next = steps[c.index + 1] || '';
        var cls = c.status === 'ok' ? 'ok' : (c.status === 'mismatch' ? 'bad' : 'unknown');
        var counter = '';
        var keys = Object.keys(c.counterexample || {});
        if (keys.length) {
          counter = '<div class="verify-counter">反例：' + keys.map(function (k) {
            return k + ' = ' + c.counterexample[k];
          }).join('，') + ' —— 代入这一步与下一步，结果不同。请自己验证一下。</div>';
        }
        return '<div class="verify-row ' + cls + '">' +
          '<span class="verify-idx">' + (c.index + 1) + '→' + (c.index + 2) + '</span>' +
          '<div><div class="verify-expr">' + formula(steps[c.index]) + '</div>' +
          '<div class="verify-expr" style="color:var(--muted)">' + formula(next) + '</div>' +
          '<div class="subtle">' + esc(c.detail || '') + '</div>' + counter + '</div>' +
          '<span class="verify-tag ' + cls + '">' + tagText[c.status] + '</span>' +
          '</div>';
      }).join('');
      if (data.all_ok) {
        html = '<div class="coach-card"><div class="coach-card-title">每一步都成立</div>' +
          '<div class="coach-card-text">相邻两行已通过符号核对；仍需检查各步定义域。请记住：' +
          '每步成立 ≠ 整个推导正确 —— 还要检查第一步是否就是题目给的，以及最后一步是否回答了问题。</div></div>' + html;
      } else if (data.first_error_index !== null && data.first_error_index !== undefined) {
        html = '<div class="coach-card warn"><div class="coach-card-title">第 ' +
          (data.first_error_index + 1) + ' 步存在不等价</div>' +
          '<div class="coach-card-text">先别往下推。回到这一步，问自己：这一步用了哪条规则？' +
          '那条规则成立需要什么前提？</div></div>' + html;
      }
      verifyResult.innerHTML = html;
      typeset(verifyResult);
    } catch (err) {
      verifyResult.innerHTML = '<p class="study-empty">请求失败：' + esc(err.message) + '</p>';
    }
  }

  var runBtn = document.getElementById('verifyRun');
  var exBtn = document.getElementById('verifyExample');
  if (runBtn) runBtn.addEventListener('click', runVerify);
  if (exBtn) exBtn.addEventListener('click', function () {
    verifyInput.value = EXAMPLE;
    verifyResult.innerHTML = '';
    previewSteps();
  });

  // ------------------------------------------------------------ 知识图谱

  var MAP = [
    { id: 'prob', label: '概率与随机变量', sub: '基础', q: '什么是随机变量？期望和方差分别刻画什么？' },
    { id: 'sample', label: '抽样分布', sub: '桥梁', q: '样本均值的分布是什么样的？为什么它比原始数据更集中？' },
    { id: 'clt', label: '中心极限定理', sub: '核心', q: '中心极限定理是什么？它的适用条件有哪些容易被忽略的地方？' },
    { id: 'est', label: '点估计与置信区间', sub: '推断 I', q: '置信区间的含义到底是什么？为什么不能说参数有95%的概率落在区间内？' },
    { id: 'test', label: '假设检验', sub: '推断 II', q: '假设检验的完整逻辑是什么？p 值和显著性水平分别指什么？' },
    { id: 'power', label: '功效与样本量', sub: '设计', q: '检验功效是什么？样本量怎么估算？' },
    { id: 'reg', label: '回归分析', sub: '建模', q: '回归系数怎么解释？R² 高就说明模型好吗？' }
  ];

  knowledgeMap.innerHTML = MAP.map(function (m) {
    return '<div class="km-row"><button class="km-node" data-km-query="' + esc(m.q) + '">' +
      '<span class="km-dot"></span><span>' + esc(m.label) + '</span>' +
      '<span class="km-sub">' + esc(m.sub) + '</span></button></div>';
  }).join('');

  // ------------------------------------------------------------ 演示案例

  var caseList = document.getElementById('caseList');
  var caseLoaded = false;

  async function loadCases() {
    if (!caseList || caseLoaded) return;
    caseLoaded = true;
    try {
      var resp = await fetch('/api/coach/cases');
      var data = await resp.json();
      var groups = { ladder: '帮助阶梯', verify: '推导核对', viz: '可视化', photo: '拍照问疑' };
      var html = '';
      var current = '';
      (data.cases || []).forEach(function (c) {
        if (c.group !== current) {
          current = c.group;
          html += '<div class="case-group">' + esc(groups[c.group] || c.group) + '</div>';
        }
        html += '<div class="case-card">' +
          '<div class="case-title">' + esc(c.title) + '</div>' +
          '<div class="case-q">' + questionHtml(c) + '</div>' +
          '<div class="case-expect">' + esc(c.expect) + '</div>' +
          '<div class="case-actions">' +
          (c.group === 'photo'
            ? '<span class="subtle">拍照案例请用输入框左侧的相机按钮</span>'
            : '<button class="study-ghost" data-case-ask="' + esc(c.question) + '">提问</button>') +
          '<button class="study-ghost" data-case-run="' + esc(c.id) + '">查看机制</button>' +
          '</div><div class="case-out" id="case-out-' + esc(c.id) + '"></div></div>';
      });
      caseList.innerHTML = html;
      typeset(caseList);
    } catch (err) {
      caseList.innerHTML = '<p class="study-empty">案例加载失败：' + esc(err.message) + '</p>';
    }
  }

  async function runCase(id) {
    var out = document.getElementById('case-out-' + id);
    if (!out) return;
    out.textContent = '运行中…';
    try {
      var resp = await fetch('/api/coach/cases/' + encodeURIComponent(id));
      var data = await resp.json();
      if (!data.ok) throw new Error(data.error || '失败');
      out.innerHTML = (data.observations || []).map(function (o) {
        if (o.level !== undefined) {
          return '<div class="case-obs"><b>L' + o.level + ' · ' + esc(o.level_name) + '</b> ' +
            esc(o.reason) + '</div>';
        }
        if (o.checks) {
          return o.checks.map(function (c) {
            var tag = c.status === 'ok' ? '✓ 等价' : (c.status === 'mismatch' ? '✗ 不等价' : '? 无法判定');
            var cex = Object.keys(c.counterexample || {}).length
              ? '（反例 ' + Object.keys(c.counterexample).map(function (k) {
                  return k + '=' + c.counterexample[k];
                }).join(',') + '）' : '';
            return '<div class="case-obs">第 ' + (c.index + 1) + '→' + (c.index + 2) +
              ' 步 ' + tag + ' ' + esc(cex) + '</div>';
          }).join('');
        }
        return '<div class="case-obs subtle">' + esc(o.note || '') + '</div>';
      }).join('');
    } catch (err) {
      out.textContent = '运行失败：' + err.message;
    }
  }

  document.addEventListener('click', function (e) {
    var run = e.target.closest('[data-case-run]');
    var ask = e.target.closest('[data-case-ask]');
    if (run) runCase(run.getAttribute('data-case-run'));
    if (ask) {
      var q = ask.getAttribute('data-case-ask');
      var ta = document.getElementById('query');
      if (ta) {
        ta.value = q;
        ta.dispatchEvent(new Event('input', { bubbles: true }));
        if (api.ask) api.ask(q);
        ta.value = '';
        closeDrawer();
      }
    }
  });

  // ------------------------------------------------------------ 学情

  async function loadProfile() {
    try {
      var sid = (api.getSessionId && api.getSessionId()) || 'panel';
      var resp = await fetch('/api/coach/profile?session_id=' + encodeURIComponent(sid));
      var data = await resp.json();
      var p = (data && data.profile) || {};
      if (!p.turns) {
        profileBox.innerHTML = '<p class="study-empty">还没有过程记录。发一个问题后，' +
          '这里会显示你的帮助依赖度、独立推进率与反复出现的误区。</p>';
        return;
      }
      var depPct = Math.round((p.dependency || 0) * 100);
      var indPct = Math.round((p.independent_rate || 0) * 100);
      var html = '<div class="profile-grid">' +
        '<div class="profile-metric"><b>' + depPct + '%</b><span>帮助依赖度（越低越好）</span>' +
        '<div class="profile-bar"><i style="width:' + depPct + '%"></i></div></div>' +
        '<div class="profile-metric"><b>' + indPct + '%</b><span>独立推进率（越高越好）</span>' +
        '<div class="profile-bar"><i style="width:' + indPct + '%"></i></div></div>' +
        '<div class="profile-metric"><b>' + (p.turns || 0) + '</b><span>已记录轮次</span></div>' +
        '<div class="profile-metric"><b>L' + Math.round(p.avg_level || 0) + '</b><span>平均帮助等级</span></div>' +
        '</div>';
      if (p.recurring_misconceptions && p.recurring_misconceptions.length) {
        html += '<div class="profile-mis"><b>反复出现的误区</b><br>' +
          p.recurring_misconceptions.map(function (m) {
            return esc(m.id) + ' × ' + m.count + ' 次';
          }).join('；') +
          '<br><span class="subtle">建议：专门就这一类误区提问「为什么」，而不是继续做题。</span></div>';
      } else {
        html += '<p class="study-empty" style="margin-top:12px">暂未发现反复出现的误区。</p>';
      }
      profileBox.innerHTML = html;
    } catch (err) {
      profileBox.innerHTML = '<p class="study-empty">学情读取失败：' + esc(err.message) + '</p>';
    }
  }

  if (window.renderIcons) window.renderIcons(drawer);
  function renderStaticMath() {
    typeset(document.getElementById('verifyInstructions'));
    previewSteps();
  }
  // The math libraries are deferred; wait until they have loaded before rendering static content.
  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', renderStaticMath, { once: true });
  else renderStaticMath();

  api.refreshProfile = function () {
    if (drawer.classList.contains('open')) loadProfile();
  };
})();
