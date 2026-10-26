/* Image input belongs to a session draft; OCR never writes into a different chat. */
(function () {
  'use strict';
  const api = window.verimath;
  const byId = id => document.getElementById(id);
  const query = byId('query'), form = byId('composer');
  const add = byId('composerAdd'), menu = byId('composerMenu');
  const fileInput = byId('photoInput'), cameraInput = byId('cameraInput');
  const dialog = byId('ocrDialog'), editor = byId('ocrText'), rendered = byId('ocrRendered');
  const status = byId('ocrStatus'), error = byId('ocrError'), insert = byId('ocrInsert');
  let current = null, version = 0;

  function closeMenu(focus = false) {
    menu.hidden = true; add.setAttribute('aria-expanded', 'false');
    if (focus) add.focus();
  }
  add.addEventListener('click', () => {
    menu.hidden = !menu.hidden; add.setAttribute('aria-expanded', String(!menu.hidden));
    if (!menu.hidden) menu.querySelector('button').focus();
  });
  document.addEventListener('click', event => {
    if (!event.target.closest('.composer-add-wrap')) closeMenu();
    if (event.target.closest('[data-open-photo]')) { closeMenu(); fileInput.click(); }
  });
  document.addEventListener('keydown', event => {
    if (event.key === 'Escape' && !menu.hidden) { event.preventDefault(); closeMenu(true); }
  });
  byId('composerPhoto').addEventListener('click', () => { closeMenu(); fileInput.click(); });
  byId('composerCamera').addEventListener('click', () => { closeMenu(); cameraInput.click(); });
  byId('ocrChange').addEventListener('click', () => fileInput.click());
  byId('ocrClose').addEventListener('click', () => dialog.close());
  byId('ocrAttachment').addEventListener('click', () => { if (!dialog.open) dialog.showModal(); });

  function showError(message) { error.textContent = message; error.hidden = !message; }
  function previewText() {
    rendered.innerHTML = api.renderMarkdown(editor.value);
    api.typesetMath(rendered);
  }
  function display(phase, text) {
    if (!current) return;
    current.phase = phase;
    status.textContent = text;
    byId('ocrAttachment').hidden = false;
    byId('ocrAttachmentStatus').textContent = phase === 'ready' ? '题目已识别 · 点击核对' : text;
    byId('ocrCancel').hidden = phase !== 'reading';
    byId('ocrRetry').hidden = !['failed', 'cancelled'].includes(phase) || !current.file;
    byId('ocrEdit').hidden = phase !== 'ready';
    insert.disabled = phase !== 'ready' || !editor.value.trim();
    dialog.setAttribute('aria-busy', String(phase === 'reading'));
  }
  function reset() {
    version++;
    current?.controller?.abort();
    current = null;
    if (dialog.open) dialog.close();
    byId('ocrAttachment').hidden = true;
    byId('ocrImage').removeAttribute('src'); byId('ocrAttachmentThumb').removeAttribute('src');
    editor.value = ''; rendered.replaceChildren(); showError('');
    editor.hidden = true; rendered.hidden = true;
    closeMenu();
  }
  document.addEventListener('verimath:session-change', reset);
  byId('ocrCancel').addEventListener('click', () => {
    version++; current?.controller?.abort();
    display('cancelled', '已取消识别，图片仍可重新识别');
  });
  byId('ocrEdit').addEventListener('click', () => {
    editor.hidden = !editor.hidden; rendered.hidden = !editor.hidden;
    byId('ocrEdit').textContent = editor.hidden ? '编辑文字' : '预览公式';
    if (editor.hidden) previewText(); else editor.focus();
  });
  editor.addEventListener('input', () => { insert.disabled = !editor.value.trim(); });

  async function recognize() {
    if (!current?.file) return;
    const job = current, token = ++version;
    job.controller?.abort(); job.controller = new AbortController();
    const owns = () => token === version && current === job && job.sid === api.getSessionId();
    showError(''); editor.hidden = true; rendered.hidden = true;
    display('reading', '正在识别题目与公式…');
    let timedOut = false;
    const deadline = setTimeout(() => { timedOut = true; job.controller.abort(); }, 75000);
    try {
      if (!job.dataUri) job.dataUri = await new Promise((resolve, reject) => {
        const reader = new FileReader();
        reader.onload = () => resolve(reader.result);
        reader.onerror = () => reject(new Error('图片读取失败，请重新选择'));
        reader.readAsDataURL(job.file);
      });
      if (!owns()) return;
      byId('ocrImage').src = job.dataUri; byId('ocrAttachmentThumb').src = job.dataUri;
      const response = await fetch('/api/coach/ocr', {
        method: 'POST', headers: { 'Content-Type': 'application/json' }, signal: job.controller.signal,
        body: JSON.stringify({ image: job.dataUri, session_id: job.sid }),
      });
      const data = await response.json();
      if (!response.ok || !data.ok) throw new Error(data.error || (typeof data.detail === 'string' ? data.detail : '识别未完成，请重试'));
      if (!owns()) return;
      if (typeof data.text !== 'string' || !data.text.trim()) throw new Error('没有识别到文字，请换一张清晰图片');
      editor.value = data.text.trim(); previewText(); rendered.hidden = false;
      byId('ocrEdit').textContent = '编辑文字';
      display('ready', '已识别。请核对数字、公式和看不清的符号。');
    } catch (problem) {
      if (!owns()) return;
      const message = timedOut ? '识别超时，可以重试或换一张图片' : problem.message;
      display('failed', '识别未完成'); showError(message || '无法连接识图服务，请重试');
    } finally { clearTimeout(deadline); }
  }
  byId('ocrRetry').addEventListener('click', recognize);
  function selectFile(file) {
    if (!file) return;
    reset();
    current = { file, sid: api.getSessionId(), phase: 'reading', controller: null, dataUri: null };
    byId('ocrFilename').textContent = file.name || '粘贴的题目照片';
    if (!dialog.open) dialog.showModal();
    if (!/^image\/(png|jpeg|webp|gif)$/.test(file.type) || file.size > 8 * 1024 * 1024) {
      current.file = null;
      display('failed', '无法读取这张图片');
      showError(file.size > 8 * 1024 * 1024 ? '图片超过 8 MB，请压缩后重试' : '请选择 PNG、JPEG、WebP 或 GIF 图片');
      return;
    }
    recognize();
  }
  for (const input of [fileInput, cameraInput]) input.addEventListener('change', () => {
    const file = input.files?.[0]; input.value = ''; selectFile(file);
  });
  document.addEventListener('paste', event => {
    if (event.target.closest('input,textarea,[contenteditable="true"]') && event.target !== query) return;
    const image = [...(event.clipboardData?.items || [])].find(item => item.type.startsWith('image/'));
    if (image) { event.preventDefault(); selectFile(image.getAsFile()); }
  });
  document.addEventListener('dragover', event => {
    if (![...(event.dataTransfer?.types || [])].includes('Files')) return;
    event.preventDefault(); form.classList.add('is-dragging');
  });
  document.addEventListener('dragleave', event => { if (!event.relatedTarget) form.classList.remove('is-dragging'); });
  document.addEventListener('drop', event => {
    form.classList.remove('is-dragging');
    if (!event.dataTransfer?.files.length) return;
    event.preventDefault(); selectFile(event.dataTransfer.files[0]);
  });
  insert.addEventListener('click', () => {
    if (!current || current.sid !== api.getSessionId() || current.phase !== 'ready') return;
    const text = editor.value.trim();
    const draft = query.value.trim();
    const combined = draft ? draft + '\n\n题目内容：\n' + text : text;
    if (combined.length > query.maxLength) { showError('文字超过输入长度，请删减识别结果后再放入'); return; }
    query.value = combined;
    query.dispatchEvent(new Event('input', { bubbles: true }));
    reset(); query.focus();
  });
})();
