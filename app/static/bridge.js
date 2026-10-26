/* Measure actual content, never the iframe viewport: avoids host/child resize feedback. */
(function () {
  'use strict';
  if (window.__verimathBridge) return;
  window.__verimathBridge = true;
  let root;
  let last = -1;
  let scheduled = false;
  let force = false;
  let errors = 0;
  let restoring = false;
  const send = data => parent.postMessage(Object.assign({ source: 'verimath-canvas' }, data), '*');
  const controls = () => Array.from(document.querySelectorAll('input:not([type="password"]):not([type="file"]):not([type="hidden"]), select, textarea')).slice(0, 100);
  function saveControls() {
    if (restoring) return;
    send({ type: 'controls', state: controls().map((node, index) => ({
      key: node.id || node.name || String(index), value: String(node.value).slice(0, 500), checked: node.checked,
    })) });
  }
  function measure() {
    scheduled = false;
    if (!root) return;
    const height = Math.max(1, Math.ceil(root.getBoundingClientRect().height));
    if (force || Math.abs(height - last) >= 1) {
      last = height; force = false;
      send({ type: 'resize', height });
    }
  }
  function schedule() {
    if (scheduled) return;
    scheduled = true;
    requestAnimationFrame(measure);
  }
  function initialize() {
    const style = document.createElement('style');
    style.textContent = 'html,body{margin:0!important;padding:0!important;min-height:0!important;height:auto!important;background:transparent!important}' +
      'body{font-family:system-ui,"Microsoft YaHei",sans-serif;color:var(--vm-ink,#202124)}' +
      '[data-verimath-content]{display:flow-root;width:100%;box-sizing:border-box;min-height:0}';
    document.head.appendChild(style);
    root = document.querySelector('[data-verimath-content]');
    if (!root) {
      root = document.createElement('div'); root.dataset.verimathContent = '';
      for (const child of Array.from(document.body.childNodes)) {
        if (child.nodeType === 1 && ['SCRIPT', 'STYLE', 'LINK'].includes(child.tagName)) continue;
        root.appendChild(child);
      }
      document.body.prepend(root);
    }
    if (window.ResizeObserver) new ResizeObserver(schedule).observe(root);
    new MutationObserver(schedule).observe(root, { subtree: true, childList: true, attributes: true, characterData: true });
    document.fonts?.ready.then(schedule);
    send({ type: 'ready' });
    schedule();
  }
  window.addEventListener('message', event => {
    if (event.source !== parent) return;
    const data = event.data;
    if (data?.source === 'verimath-probe') { force = true; schedule(); }
    if (data?.source === 'verimath-host' && data.type === 'restore-controls' && Array.isArray(data.state)) {
      restoring = true;
      controls().forEach((node, index) => {
        const value = data.state.find(item => item.key === (node.id || node.name || String(index)));
        if (!value) return;
        node.value = value.value;
        if (typeof value.checked === 'boolean') node.checked = value.checked;
        node.dispatchEvent(new Event('input', { bubbles: true }));
        node.dispatchEvent(new Event('change', { bubbles: true }));
      });
      restoring = false; schedule();
    }
    if (data?.source === 'verimath-host' && data.type === 'theme') {
      document.documentElement.style.setProperty('--vm-ink', data.dark ? '#e8e9ed' : '#242a27');
      document.documentElement.style.setProperty('--vm-bg', data.dark ? '#252629' : '#fdfdfb');
      document.documentElement.style.setProperty('--vm-muted', data.dark ? '#a3a5ab' : '#747b76');
      document.documentElement.style.setProperty('--vm-line', data.dark ? '#3a3b40' : '#e4e7e2');
      document.documentElement.style.setProperty('--vm-accent', data.dark ? '#b4cebd' : '#365b46');
      document.documentElement.style.colorScheme = data.dark ? 'dark' : 'light';
      schedule();
    }
  });
  window.addEventListener('resize', schedule);
  document.addEventListener('input', saveControls);
  document.addEventListener('change', saveControls);
  window.addEventListener('load', schedule);
  window.addEventListener('error', event => {
    if (errors++ < 5) send({ type: 'error', kind: 'runtime', message: String(event.message || '组件运行错误').slice(0, 300) });
  });
  window.addEventListener('unhandledrejection', () => {
    if (errors++ < 5) send({ type: 'error', kind: 'promise', message: '组件异步运行失败' });
  });
  window.verimathResize = schedule;
  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', initialize, { once: true });
  else initialize();
})();
