/* One owner for the shell geometry; chat and tools share the same available width. */
(function () {
  'use strict';
  const root = document.documentElement;
  const side = document.querySelector('.side');
  const drawer = document.getElementById('studyDrawer');
  const scrim = document.getElementById('studyScrim');
  const backdrop = document.createElement('div');
  backdrop.className = 'drawer-backdrop';
  document.body.appendChild(backdrop);
  const api = window.verimath = window.verimath || {};
  const read = (key, fallback) => { try { return localStorage.getItem(key) ?? fallback; } catch (_) { return fallback; } };
  const save = (key, value) => { try { localStorage.setItem(key, String(value)); } catch (_) {} };
  const state = { width: Number(read('verimath-side-w', 264)) || 264,
    collapsed: read('verimath-side-collapsed', '0') === '1', mobileOpen: false, toolsOpen: false };

  function render() {
    const mobile = innerWidth < 1024;
    const width = Math.max(200, Math.min(420, state.width, innerWidth - 640));
    const left = mobile || state.collapsed ? 0 : width;
    const dockTools = state.toolsOpen && !mobile && innerWidth - left - 360 >= 640;
    root.style.setProperty('--side-w', left + 'px');
    root.style.setProperty('--drawer-w', (mobile ? Math.min(300, innerWidth - 40) : width) + 'px');
    root.style.setProperty('--tools-w', dockTools ? '360px' : '0px');
    root.classList.toggle('side-collapsed', !mobile && state.collapsed);
    root.classList.toggle('tools-open', state.toolsOpen);
    root.classList.toggle('tools-docked', dockTools);
    root.classList.toggle('tools-overlay', state.toolsOpen && !dockTools);
    side.classList.toggle('open', mobile && state.mobileOpen);
    side.inert = mobile ? !state.mobileOpen : state.collapsed;
    backdrop.classList.toggle('show', mobile && state.mobileOpen);
    drawer.classList.toggle('open', state.toolsOpen);
    drawer.setAttribute('aria-hidden', String(!state.toolsOpen));
    drawer.inert = !state.toolsOpen;
    scrim.hidden = !state.toolsOpen || dockTools;
    for (const id of ['sideCollapse', 'sideReveal', 'drawerToggle']) {
      document.getElementById(id)?.setAttribute('aria-expanded', String(mobile ? state.mobileOpen : !state.collapsed));
    }
    document.getElementById('studyToggle')?.setAttribute('aria-expanded', String(state.toolsOpen));
  }
  function collapse(on) { state.collapsed = on; save('verimath-side-collapsed', on ? 1 : 0); render(); }
  function tools(on, tab) {
    state.toolsOpen = on;
    if (on) state.mobileOpen = false;
    render();
    if (tab) document.dispatchEvent(new CustomEvent('verimath:tools-tab', { detail: tab }));
    if (on && !root.classList.contains('tools-docked')) document.getElementById('studyClose')?.focus({ preventScroll: true });
    if (!on) document.getElementById('studyToggle')?.focus({ preventScroll: true });
  }
  api.layout = { state, render, openTools: tab => tools(true, tab), closeTools: () => tools(false),
    closeSide: () => { state.mobileOpen = false; render(); } };
  window.verimathSide = { collapse: () => collapse(true), expand: () => collapse(false),
    setWidth: value => { state.width = Math.max(200, Math.min(420, Number(value) || 264)); save('verimath-side-w', state.width); render(); return state.width; } };
  document.getElementById('sideCollapse')?.addEventListener('click', () => collapse(true));
  document.getElementById('sideReveal')?.addEventListener('click', () => collapse(false));
  document.getElementById('drawerToggle')?.addEventListener('click', () => {
    if (innerWidth >= 1024) return collapse(!state.collapsed);
    state.mobileOpen = !state.mobileOpen;
    if (state.mobileOpen) state.toolsOpen = false;
    render();
  });
  document.getElementById('drawerClose')?.addEventListener('click', api.layout.closeSide);
  backdrop.addEventListener('click', api.layout.closeSide);
  document.getElementById('studyToggle')?.addEventListener('click', () => tools(!state.toolsOpen));
  document.getElementById('studyClose')?.addEventListener('click', () => tools(false));
  scrim.addEventListener('click', () => tools(false));
  document.addEventListener('keydown', event => {
    if ((event.ctrlKey || event.metaKey) && event.key.toLowerCase() === 'b' && innerWidth >= 1024) {
      event.preventDefault(); collapse(!state.collapsed);
    }
    if (event.key === 'Escape') {
      if (state.toolsOpen) tools(false);
      if (state.mobileOpen) api.layout.closeSide();
    }
  });
  const resizer = document.getElementById('sideResizer');
  let drag = null;
  resizer?.addEventListener('pointerdown', event => {
    if (innerWidth < 1024 || state.collapsed) return;
    drag = { x: event.clientX, width: side.getBoundingClientRect().width };
    resizer.setPointerCapture(event.pointerId);
    root.classList.add('side-resizing');
    event.preventDefault();
  });
  resizer?.addEventListener('pointermove', event => {
    if (drag) window.verimathSide.setWidth(drag.width + event.clientX - drag.x);
  });
  function finishDrag() { drag = null; root.classList.remove('side-resizing'); }
  resizer?.addEventListener('pointerup', finishDrag);
  resizer?.addEventListener('pointercancel', finishDrag);
  resizer?.addEventListener('lostpointercapture', finishDrag);
  resizer?.addEventListener('dblclick', () => window.verimathSide.setWidth(264));
  resizer?.addEventListener('keydown', event => {
    if (!['ArrowLeft', 'ArrowRight', 'Home'].includes(event.key)) return;
    event.preventDefault();
    window.verimathSide.setWidth(event.key === 'Home' ? 264 : state.width + (event.key === 'ArrowRight' ? 16 : -16));
  });
  const settings = document.getElementById('settingsModal');
  document.getElementById('openSettings')?.addEventListener('click', () => { api.layout.closeSide(); settings.showModal(); });
  document.getElementById('settingsClose')?.addEventListener('click', () => settings.close());
  settings?.addEventListener('click', event => { if (event.target === settings) settings.close(); });
  addEventListener('resize', render);
  render();
})();
