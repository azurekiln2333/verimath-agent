/**
 * side-panel.js —— 左侧栏的宽度与折叠。
 *
 * 为什么单独一段：左边栏宽度是**全局布局输入**（--side-w），
 * 对话列、顶栏、输入条都靠它定位。把它做成可调，等于给整个版面
 * 加了一个自由度，必须持久化 + 有上下限 + 拖动时锁住 iframe。
 *
 * 交互约定（与主流编辑器一致）：
 *   - 拖右边缘调宽，双击边缘复位
 *   - 底部按钮 / Ctrl+B 收起，收起后顶栏左侧出现展开按钮
 *   - 宽度写入 localStorage，刷新后保持
 *   - 窄屏（≤860）交回原有抽屉逻辑，本模块不介入
 */
(function () {
  'use strict';

  var aside = document.querySelector('.side');
  var resizer = document.getElementById('sideResizer');
  var collapseBtn = document.getElementById('sideCollapse');
  var revealBtn = document.getElementById('sideReveal');
  if (!aside || !resizer) return;

  var MIN = 200;
  var MAX = 420;
  var DEFAULT = 264;
  var KEY = 'verimath-side-w';
  var COLLAPSE_KEY = 'verimath-side-collapsed';
  var root = document.documentElement;

  function clamp(w) {
    return Math.max(MIN, Math.min(MAX, Math.round(w)));
  }

  function applyWidth(w) {
    var width = clamp(w);
    root.style.setProperty('--side-w', width + 'px');
    return width;
  }

  function loadWidth() {
    var saved = 0;
    try { saved = parseInt(window.localStorage.getItem(KEY) || '0', 10); } catch (_) { }
    return saved > 0 ? clamp(saved) : DEFAULT;
  }

  function saveWidth(w) {
    try { window.localStorage.setItem(KEY, String(w)); } catch (_) { }
  }

  applyWidth(loadWidth());

  // ---------------------------------------------------------------- 拖拽

  var dragging = false;
  var startX = 0;
  var startW = 0;

  function onMove(e) {
    if (!dragging) return;
    var clientX = e.touches ? e.touches[0].clientX : e.clientX;
    applyWidth(startW + (clientX - startX));
    if (e.cancelable) e.preventDefault();
  }

  function onUp() {
    if (!dragging) return;
    dragging = false;
    root.classList.remove('side-resizing');
    document.removeEventListener('mousemove', onMove);
    document.removeEventListener('mouseup', onUp);
    document.removeEventListener('touchmove', onMove);
    document.removeEventListener('touchend', onUp);
    var w = parseInt(getComputedStyle(root).getPropertyValue('--side-w'), 10);
    if (w > 0) saveWidth(w);
  }

  function onDown(e) {
    if (window.innerWidth <= 860) return;
    dragging = true;
    startX = e.touches ? e.touches[0].clientX : e.clientX;
    startW = aside.getBoundingClientRect().width;
    root.classList.add('side-resizing');
    document.addEventListener('mousemove', onMove);
    document.addEventListener('mouseup', onUp);
    document.addEventListener('touchmove', onMove, { passive: false });
    document.addEventListener('touchend', onUp);
    if (e.cancelable) e.preventDefault();
  }

  resizer.addEventListener('mousedown', onDown);
  resizer.addEventListener('touchstart', onDown, { passive: false });

  // 双击复位；键盘 ←/→ 微调，Home 复位
  resizer.addEventListener('dblclick', function () {
    applyWidth(DEFAULT);
    saveWidth(DEFAULT);
  });
  resizer.addEventListener('keydown', function (e) {
    var current = aside.getBoundingClientRect().width;
    if (e.key === 'ArrowLeft') { applyWidth(current - 16); saveWidth(clamp(current - 16)); e.preventDefault(); }
    else if (e.key === 'ArrowRight') { applyWidth(current + 16); saveWidth(clamp(current + 16)); e.preventDefault(); }
    else if (e.key === 'Home') { applyWidth(DEFAULT); saveWidth(DEFAULT); e.preventDefault(); }
  });

  // ---------------------------------------------------------------- 折叠

  function setCollapsed(on) {
    root.classList.toggle('side-collapsed', !!on);
    try { window.localStorage.setItem(COLLAPSE_KEY, on ? '1' : '0'); } catch (_) { }
    if (collapseBtn) {
      collapseBtn.setAttribute('aria-expanded', on ? 'false' : 'true');
    }
  }

  function isCollapsed() {
    return root.classList.contains('side-collapsed');
  }

  if (collapseBtn) collapseBtn.addEventListener('click', function () { setCollapsed(true); });
  if (revealBtn) revealBtn.addEventListener('click', function () { setCollapsed(false); });

  document.addEventListener('keydown', function (e) {
    if ((e.ctrlKey || e.metaKey) && (e.key === 'b' || e.key === 'B')) {
      if (window.innerWidth <= 860) return;
      e.preventDefault();
      setCollapsed(!isCollapsed());
    }
  });

  // 恢复上次的折叠状态（窄屏一律不折叠，交给抽屉）
  try {
    if (window.innerWidth > 860 && window.localStorage.getItem(COLLAPSE_KEY) === '1') {
      setCollapsed(true);
    }
  } catch (_) { }

  // 窗口从窄变宽时，若之前是折叠状态，保持折叠
  window.addEventListener('resize', function () {
    if (window.innerWidth <= 860) {
      root.classList.remove('side-collapsed');
      root.style.removeProperty('--side-w');
    } else {
      applyWidth(loadWidth());
      try {
        if (window.localStorage.getItem(COLLAPSE_KEY) === '1') root.classList.add('side-collapsed');
      } catch (_) { }
    }
  });

  window.verimathSide = {
    collapse: function () { setCollapsed(true); },
    expand: function () { setCollapsed(false); },
    setWidth: function (w) { var v = applyWidth(w); saveWidth(v); return v; }
  };
})();
