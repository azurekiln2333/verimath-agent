/* Background Canvas jobs never hold the chat composer or capture the active session. */
(function () {
  'use strict';
  const api = window.verimath = window.verimath || {};
  const entries = new Map();
  let timer = null;
  let generation = 0;
  let polling = false;
  let pendingDiscovery = false;
  const active = status => status === 'queued' || status === 'running';
  const labels = { queued: '排队中', running: '正在生成可视化，你可以继续聊天', succeeded: '已完成',
    failed: '生成失败', cancelled: '已取消', interrupted: '生成已中断' };
  async function request(url, options) {
    const response = await fetch(url, options);
    const data = await response.json();
    if (!response.ok) throw new Error(data.detail || '暂时无法连接服务');
    return data;
  }
  function post(url, body) { return request(url, { method: 'POST', headers: { 'Content-Type': 'application/json' }, body: JSON.stringify(body) }); }
  function preserveReading(action) {
    const box = document.getElementById('messages');
    const anchor = [...box.querySelectorAll('.msg-row')].find(node => node.getBoundingClientRect().bottom > box.getBoundingClientRect().top);
    const top = anchor?.getBoundingClientRect().top;
    const scroll = box.scrollTop;
    action();
    if (anchor?.isConnected) box.scrollTop += anchor.getBoundingClientRect().top - top;
    else box.scrollTop = scroll;
  }
  function schedule() {
    clearTimeout(timer);
    if (document.hidden) return;
    if (pendingDiscovery || [...entries.values()].some(entry => active(entry.job?.status))) timer = setTimeout(poll, 2000);
  }
  async function poll() {
    if (polling) return schedule();
    const sid = api.getSessionId?.();
    if (!sid) return;
    const version = generation;
    polling = true;
    try {
      const data = await request('/api/panel/artifact-jobs?session_id=' + encodeURIComponent(sid));
      if (version !== generation || sid !== api.getSessionId()) return;
      pendingDiscovery = data.checking.length > 0 || (data.suggestions_checking || []).length > 0;
      preserveReading(() => {
        for (const offer of data.offers) {
          const row = document.querySelector('[data-message-id="' + CSS.escape(offer.message_id) + '"]');
          if (row) api.artifacts.offer(api.ensureCompanion(row.querySelector('.msg-col')), offer);
        }
        for (const job of data.jobs) {
          const entry = entries.get(job.offer_id);
          if (entry && (!entry.job || job.created_at >= entry.job.created_at)) update(entry, job);
        }
        for (const item of data.suggestions || []) {
          const row = document.querySelector('[data-message-id="' + CSS.escape(item.message_id) + '"]');
          if (row && row.dataset.sessionId === sid) followups(row, item);
        }
      });
      document.getElementById('artifactConnectionStatus')?.remove();
    } catch (_) {
      const host = document.querySelector('.artifact-task[data-active="true"], .message-followups[data-state="checking"]');
      if (host && !document.getElementById('artifactConnectionStatus')) {
        const note = document.createElement('small'); note.id = 'artifactConnectionStatus';
        note.textContent = '连接中断，正在自动重连。后台任务仍会继续。'; host.appendChild(note);
      }
    } finally { polling = false; schedule(); }
  }
  function update(entry, job) {
    if (entry.job?.job_id === job.job_id && entry.job.status === job.status && (job.status !== 'succeeded' || entry.rendered)) return;
    if (entry.job?.job_id !== job.job_id) {
      api.disposeArtifacts?.(entry.result);
      entry.result.replaceChildren();
      entry.rendered = false;
      entry.renderFailed = false;
      entry.host.classList.remove('is-complete');
    }
    entry.job = job;
    entry.host.dataset.active = String(active(job.status));
    entry.status.textContent = labels[job.status] || job.status;
    entry.action.hidden = active(job.status) || job.status === 'succeeded';
    entry.action.textContent = job.status === 'failed' || job.status === 'interrupted' || job.status === 'cancelled' ? '重新生成' : '生成可视化';
    entry.cancel.hidden = !active(job.status);
    entry.host.classList.toggle('is-running', active(job.status));
    entry.error.textContent = job.error || '';
    if (job.status === 'succeeded' && job.artifact && !entry.rendered) {
      entry.result.dataset.jobId = job.job_id;
      entry.result.replaceChildren();
      let card;
      try { card = api.mountArtifact(job.artifact, entry.result); } catch (_) {}
      if (card && !card.querySelector('.artifact-error')) {
        entry.rendered = true;
        const collapse = document.createElement('button'); collapse.type = 'button';
        collapse.className = 'artifact-action'; collapse.textContent = '收起';
        collapse.setAttribute('aria-expanded', 'true');
        collapse.addEventListener('click', () => {
          const folded = card.classList.toggle('artifact-folded');
          collapse.textContent = folded ? '展开' : '收起'; collapse.setAttribute('aria-expanded', String(!folded));
        });
        card.querySelector('.artifact-actions')?.prepend(collapse);
        entry.host.classList.add('is-complete');
      } else {
        renderFailed(entry);
      }
    }
  }
  function renderFailed(entry) {
    entry.rendered = true; // Do not remount the same broken result on every poll.
    entry.renderFailed = true;
    entry.host.classList.remove('is-complete');
    entry.status.textContent = '画布运行异常';
    entry.error.textContent = '这份画布未能正常运行，可以重新生成。';
    entry.action.hidden = false; entry.action.textContent = '重新生成';
  }
  function offer(host, data) {
    if (!data?.offer_id || !host) return null;
    if (entries.has(data.offer_id)) return entries.get(data.offer_id).action;
    const section = document.createElement('section'); section.className = 'artifact-task';
    section.dataset.offerId = data.offer_id;
    const head = document.createElement('div'); head.className = 'artifact-task-head';
    const title = document.createElement('strong'); title.textContent = data.title || '可视化';
    const status = document.createElement('span'); status.className = 'artifact-task-status'; status.setAttribute('role', 'status');
    const action = document.createElement('button'); action.type = 'button'; action.className = 'artifact-offer-btn'; action.textContent = '生成可视化';
    const cancel = document.createElement('button'); cancel.type = 'button'; cancel.className = 'artifact-cancel'; cancel.textContent = '取消'; cancel.hidden = true;
    const error = document.createElement('small'); error.className = 'artifact-job-error';
    const result = document.createElement('div'); result.className = 'artifact-result';
    head.append(title, status, action, cancel); section.append(head, error, result); host.appendChild(section);
    const entry = { offer: data, host: section, status, action, cancel, error, result, job: null, rendered: false };
    entries.set(data.offer_id, entry);
    section.addEventListener('verimath:artifact-error', event => {
      if (event.detail?.jobId === entry.job?.job_id) renderFailed(entry);
    });
    action.addEventListener('click', async () => {
      action.disabled = true; error.textContent = '';
      try {
        const job = await post('/api/panel/artifact-jobs', { session_id: data.session_id, message_id: data.message_id,
          offer_id: data.offer_id, retry_of: entry.job && !active(entry.job.status) ? entry.job.job_id : null });
        if (entries.get(data.offer_id) === entry) { update(entry, job); schedule(); }
      } catch (problem) { error.textContent = problem.message; }
      finally { action.disabled = false; }
    });
    cancel.addEventListener('click', async () => {
      cancel.disabled = true;
      try { update(entry, await post('/api/panel/artifact-jobs/' + entry.job.job_id + '/cancel', { session_id: data.session_id })); }
      catch (problem) { error.textContent = problem.message; }
      finally { cancel.disabled = false; schedule(); }
    });
    return action;
  }
  function followups(row, data) {
    if (!row || row.dataset.sessionId !== api.getSessionId?.()) return;
    const host = api.ensureCompanion(row.querySelector('.msg-col'));
    let section = host.querySelector('.message-followups');
    const state = data.followups_state || (data.followups?.length ? 'completed' : 'none');
    const suggestions = (data.followups || []).filter(item => typeof item.label === 'string' && typeof item.query === 'string').slice(0, 4);
    if (!['checking', 'failed', 'interrupted'].includes(state) && !suggestions.length) {
      section?.remove(); return;
    }
    const signature = JSON.stringify([state, data.followups_stage, data.followups_error, suggestions]);
    if (section?.dataset.signature === signature) return;
    if (!section) {
      section = document.createElement('section'); section.className = 'message-followups';
      section.setAttribute('aria-label', '继续探究'); host.appendChild(section);
    }
    section.dataset.signature = signature; section.dataset.state = state; section.replaceChildren();
    const label = document.createElement('small'); label.textContent = '继续探究'; section.appendChild(label);
    if (state === 'checking') {
      const note = document.createElement('span'); note.className = 'followup-state'; note.setAttribute('role', 'status');
      note.textContent = data.followups_stage === 'reviewing' ? '正在核对追问建议…' : '正在结合对话整理追问…';
      section.appendChild(note);
      return;
    }
    if (state === 'failed' || state === 'interrupted') {
      const note = document.createElement('span'); note.className = 'followup-state';
      note.textContent = data.followups_error || '追问建议未完成，你可以继续提问或重试';
      const retry = document.createElement('button'); retry.type = 'button'; retry.className = 'followup-retry'; retry.textContent = '重试建议';
      retry.addEventListener('click', async () => {
        const sid = row.dataset.sessionId, mid = row.dataset.messageId;
        if (sid !== api.getSessionId?.()) return;
        retry.disabled = true;
        try {
          const updated = await post('/api/panel/sessions/' + encodeURIComponent(sid) + '/messages/' + encodeURIComponent(mid) + '/recommendations', {});
          if (!row.isConnected || sid !== api.getSessionId?.()) return;
          preserveReading(() => followups(row, updated));
          pendingDiscovery = true; schedule();
        } catch (problem) { note.textContent = problem.message; }
        finally { retry.disabled = false; }
      });
      section.append(note, retry);
      return;
    }
    for (const item of suggestions) {
      const button = document.createElement('button'); button.type = 'button';
      button.className = 'followup-question'; button.textContent = item.label; button.title = item.query;
      button.setAttribute('aria-label', item.label);
      button.disabled = !!api.isChatBusy?.();
      button.addEventListener('click', () => {
        if (api.isChatBusy?.() || row.dataset.sessionId !== api.getSessionId?.()) return;
        api.ask(item.query);
      });
      section.appendChild(button);
    }
  }
  api.artifacts = { offer, followups,
    setBusy(value) { document.querySelectorAll('.followup-question').forEach(button => { button.disabled = value; }); },
    reset() { generation++; entries.clear(); pendingDiscovery = false; clearTimeout(timer); },
    restore(host, offers, jobs) {
      for (const item of offers || []) offer(host, item);
      for (const job of jobs || []) { const entry = entries.get(job.offer_id); if (entry) update(entry, job); }
      schedule();
    },
    watchDiscovery(value) { pendingDiscovery = value || pendingDiscovery; schedule(); },
    sync: poll,
  };
  addEventListener('online', poll);
  document.addEventListener('visibilitychange', () => { if (document.hidden) clearTimeout(timer); else poll(); });
})();
