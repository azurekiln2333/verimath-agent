/**
 * parity 的 JS 半边：从 stdin 读调用清单，求值，把结果按 JSON 吐回 stdout。
 *
 * 刻意做成哑管道 —— 不做任何容差判断、不知道 Python 侧算出了什么。
 * 比对全部在 pytest 里做，避免 JS 侧"自己判自己及格"。
 *
 * 数值序列化用 toString()，JS 的默认双精度往返表示是无损的
 * （最短能唯一还原的十进制），Python 的 float() 能精确读回。
 * Infinity / NaN 用字符串标记，因为 JSON 不支持。
 */
'use strict';

const statlib = require('../app/static/statlib.js');

function enc(v) {
  if (typeof v !== 'number') return v;
  if (Number.isNaN(v)) return '__nan__';
  if (v === Infinity) return '__inf__';
  if (v === -Infinity) return '__-inf__';
  return v;
}

function encResult(r) {
  const out = {};
  for (const k of Object.keys(r)) {
    const v = r[k];
    if (Array.isArray(v)) out[k] = v.map(enc);
    else if (v && typeof v === 'object') out[k] = encResult(v);
    else out[k] = enc(v);
  }
  return out;
}

let raw = '';
process.stdin.on('data', (d) => { raw += d; });
process.stdin.on('end', () => {
  const req = JSON.parse(raw);
  const out = { scalars: [], tests: {}, anova: null, power: [], sampleSize: [], rng: [] };

  for (const [name, args] of req.scalars) {
    try {
      out.scalars.push(enc(statlib[name].apply(null, args)));
    } catch (e) {
      out.scalars.push('__error__:' + e.message);
    }
  }

  for (const [jsName, args] of req.tests) {
    out.tests[jsName] = encResult(statlib[jsName].apply(null, args));
  }

  if (req.anova) out.anova = encResult(statlib.anovaOneway(req.anova));

  for (const args of req.power) {
    out.power.push(encResult(statlib.powerTwoSampleT.apply(null, args)));
  }
  for (const args of req.sampleSize) {
    out.sampleSize.push(encResult(statlib.sampleSizeTwoSampleT.apply(null, args)));
  }

  for (const spec of req.rng) {
    const r = new statlib.PCG32(spec.seed, spec.stream);
    const vals = [];
    for (let i = 0; i < spec.n; i++) {
      if (spec.method === 'random') vals.push(r.random());
      else if (spec.method === 'normal') vals.push(r.normal());
      else if (spec.method === 'exponential') vals.push(r.exponential(2.5));
      else if (spec.method === 'randint') vals.push(r.randint(1, 6));
      else if (spec.method === 'bernoulli') vals.push(r.bernoulli(0.3));
      else throw new Error('unknown method ' + spec.method);
    }
    out.rng.push(vals.map(enc));
  }

  process.stdout.write(JSON.stringify(out));
});
