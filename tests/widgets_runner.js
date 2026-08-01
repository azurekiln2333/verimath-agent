/**
 * widgets.js 的无头测试。
 *
 * 用最小 DOM/canvas 桩把每个 widget 真跑一遍。这不是"语法检查"——
 * 它能抓到真实缺陷：NaN 坐标、非有限的 scale 边界、save/restore 失衡、
 * 缺失 aria-label、以及交互参数变化后渲染崩掉。
 *
 * 断言里最关键的一条是"绘图坐标必须全部有限"：NaN 传给 canvas API
 * 不会抛异常，只会静默画不出东西 —— 在真浏览器里表现为空白图，
 * 极难定位。这里把它变成可自动捕获的失败。
 */
'use strict';

globalThis.statlib = require('../app/static/statlib.js');
globalThis.plot = require('../app/static/plot.js');

const failures = [];
let checks = 0;

function ok(cond, msg) {
  checks++;
  if (!cond) failures.push(msg);
}

// ------------------------------------------------------------- DOM 桩

const NUMERIC_CTX_METHODS = new Set([
  'moveTo', 'lineTo', 'rect', 'fillRect', 'strokeRect', 'clearRect',
  'arc', 'fillText', 'strokeText', 'translate', 'setTransform'
]);

function makeCtx(record) {
  const state = { saves: 0, restores: 0 };
  const handler = {
    get(_, prop) {
      if (prop === 'canvas') return { width: 640, height: 360 };
      if (prop === 'measureText') return () => ({ width: 24 });
      return (...args) => {
        if (prop === 'save') state.saves++;
        if (prop === 'restore') state.restores++;
        if (NUMERIC_CTX_METHODS.has(prop)) {
          args.forEach((a, i) => {
            if (typeof a === 'number' && !Number.isFinite(a)) {
              record.badCoords.push(prop + ' 第' + (i + 1) + '个参数为 ' + a);
            }
          });
        }
        return undefined;
      };
    },
    set(_, prop, value) {
      if (prop === 'fillStyle' || prop === 'strokeStyle') {
        if (typeof value === 'string' && /NaN|undefined/.test(value)) {
          record.badStyles.push(prop + ' = ' + value);
        }
      }
      return true;
    }
  };
  const ctx = new Proxy({}, handler);
  return { ctx, state };
}

function makeElement(tag, record) {
  const el = {
    tagName: tag.toUpperCase(),
    children: [],
    style: {},
    attrs: {},
    _text: '',
    set innerHTML(v) { if (v === '') this.children = []; },
    get innerHTML() { return ''; },
    set textContent(v) { this._text = String(v); },
    get textContent() { return this._text; },
    set className(v) { this.attrs['class'] = v; },
    get className() { return this.attrs['class'] || ''; },
    appendChild(c) { this.children.push(c); return c; },
    setAttribute(k, v) { this.attrs[k] = v; },
    getAttribute(k) { return this.attrs[k]; }
  };
  if (tag === 'canvas') {
    el.width = 640;
    el.height = 360;
    el.clientWidth = 640;
    el.clientHeight = 320;
    const made = makeCtx(record);
    el._ctxState = made.state;
    el.getContext = () => made.ctx;
    record.canvases.push(el);
  }
  return el;
}

function installDom(record) {
  globalThis.devicePixelRatio = 2;
  globalThis.document = {
    createElement: (tag) => makeElement(tag, record)
  };
}

function freshRecord() {
  const record = { canvases: [], badCoords: [], badStyles: [] };
  installDom(record);
  return record;
}

const widgets = require('../app/static/widgets.js');

// ------------------------------------------------------------ 测试样例
// 与 tests/test_artifacts.py 的 _VALID 保持一致的形状

const SPECS = {
  distribution_explorer: {
    kind: 'distribution_explorer', title: '正态分布', caption: '拖动看形状变化',
    params: { family: 'normal', params: { mu: 0, sigma: 1 }, show: 'pdf', mark_x: [1.96], interactive: [] }
  },
  hypothesis_test: {
    kind: 'hypothesis_test', title: 't 检验', caption: '阴影是 p 值',
    params: {
      test: 't', df: 18, df2: null, statistic: 2.31, alpha: 0.05,
      alternative: 'two-sided', show_p_area: true, show_rejection: true
    }
  },
  sampling_distribution: {
    kind: 'sampling_distribution', title: 'CLT', caption: '看均值分布变正态',
    params: {
      population: 'expon', sample_size: 30, n_samples: 300,
      statistic: 'mean', seed: 7, overlay_normal: true, interactive: []
    }
  },
  confidence_interval: {
    kind: 'confidence_interval', title: 'CI 覆盖率', caption: '红色未覆盖真值',
    params: {
      true_mean: 0, true_sd: 1, sample_size: 25, n_intervals: 30,
      ci_level: 0.95, seed: 7, interactive: []
    }
  },
  power_curve: {
    kind: 'power_curve', title: '功效曲线', caption: '样本量与功效',
    params: {
      x_axis: 'n', effect_size: 0.5, n_per_group: 30, alpha: 0.05,
      alternative: 'two-sided', target_power: 0.8, compare: [0.2, 0.8], interactive: []
    }
  },
  scatter_regression: {
    kind: 'scatter_regression', title: '回归', caption: '看拟合与残差',
    params: {
      x: [1, 2, 3, 4, 5, 6], y: [2.1, 3.9, 6.2, 7.8, 10.1, 12.2],
      show_fit: true, show_residuals: true, show_ci_band: true,
      x_label: 'x', y_label: 'y'
    }
  },
  data_plot: {
    kind: 'data_plot', title: '数据分布', caption: '先看数据再做检验',
    params: {
      series: [
        { label: 'A', values: [1, 2, 2, 3, 3, 3, 4, 4, 5] },
        { label: 'B', values: [2, 3, 3, 4, 4, 5, 5, 6, 9] }
      ],
      kind: 'histogram', bins: null, overlay_normal: true, x_label: '分数'
    }
  },
  effect_size: {
    kind: 'effect_size', title: '效应量', caption: '别只看 p 值',
    params: {
      items: [
        { label: '研究 A', estimate: 0.5, ci_low: 0.1, ci_high: 0.9 },
        { label: '研究 B', estimate: 0.2, ci_low: -0.3, ci_high: 0.7 }
      ],
      null_value: 0, x_label: '效应量 d'
    }
  }
};

// ------------------------------------------------- 每个 widget 都要能渲染

Object.keys(SPECS).forEach((kind) => {
  ok(widgets.has(kind), '注册表应包含 ' + kind);
  const w = widgets.get(kind);
  if (!w) return;

  const record = freshRecord();
  const container = makeElement('div', record);
  let result;
  try {
    result = w.render(container, SPECS[kind]);
  } catch (e) {
    failures.push(kind + ' 渲染抛异常: ' + e.message + '\n' + e.stack);
    return;
  }
  ok(record.canvases.length >= 1, kind + ' 应至少创建一个 canvas');
  ok(record.badCoords.length === 0,
    kind + ' 出现非有限绘图坐标: ' + record.badCoords.slice(0, 3).join('; '));
  ok(record.badStyles.length === 0,
    kind + ' 出现非法颜色: ' + record.badStyles.slice(0, 3).join('; '));
  record.canvases.forEach((c, i) => {
    ok(!!c.getAttribute('aria-label'),
      kind + ' 的 canvas[' + i + '] 缺少 aria-label（无障碍必需）');
    ok(c.getAttribute('role') === 'img',
      kind + ' 的 canvas[' + i + '] 应有 role=img');
    ok(c._ctxState.saves === c._ctxState.restores,
      kind + ' 的 canvas[' + i + '] save/restore 不配对: ' +
      c._ctxState.saves + ' vs ' + c._ctxState.restores);
  });
});

// ----------------------------------------------- controls 声明的正确性

Object.keys(SPECS).forEach((kind) => {
  const w = widgets.get(kind);
  if (!w) return;
  const controls = w.controls(SPECS[kind]);
  ok(Array.isArray(controls), kind + '.controls 应返回数组');
  controls.forEach((c) => {
    ok(typeof c.key === 'string' && c.key, kind + ' 控件缺少 key');
    ok(typeof c.label === 'string' && c.label, kind + ' 控件 ' + c.key + ' 缺少 label');
    ok(Number.isFinite(c.min) && Number.isFinite(c.max),
      kind + ' 控件 ' + c.key + ' 的范围必须有限');
    ok(c.max > c.min, kind + ' 控件 ' + c.key + ' 的 max 必须大于 min');
    ok(Number.isFinite(c.value),
      kind + ' 控件 ' + c.key + ' 的初值必须有限, 得 ' + c.value);
    ok(c.value >= c.min && c.value <= c.max,
      kind + ' 控件 ' + c.key + ' 的初值 ' + c.value + ' 越出 [' + c.min + ',' + c.max + ']');
    ok(Number.isFinite(c.step) && c.step > 0,
      kind + ' 控件 ' + c.key + ' 的 step 必须为正');
  });
});

// ------------------------------------- 交互：改参数后必须仍能正确渲染

(function testInteraction() {
  const cases = [
    ['distribution_explorer', [{ mu: -3, sigma: 0.3 }, { mu: 4, sigma: 3.9 }]],
    ['hypothesis_test', [{ alpha: 0.001, statistic: 0 }, { alpha: 0.199, statistic: 5.5 },
      { statistic: -4 }, { df: 1 }, { df: 200 }]],
    ['sampling_distribution', [{ sample_size: 1 }, { sample_size: 200, n_samples: 100 },
      { seed: 999 }]],
    ['confidence_interval', [{ sample_size: 2 }, { ci_level: 0.995 }, { ci_level: 0.5 },
      { n_intervals: 10 }]],
    ['power_curve', [{ alpha: 0.001 }, { effect_size: 0.05 }, { effect_size: 2 },
      { n_per_group: 2 }, { n_per_group: 500 }]],
    ['data_plot', [{ bins: 2 }, { bins: 30 }]]
  ];
  cases.forEach(([kind, states]) => {
    const w = widgets.get(kind);
    states.forEach((state) => {
      const record = freshRecord();
      const container = makeElement('div', record);
      try {
        w.render(container, SPECS[kind], state);
      } catch (e) {
        failures.push(kind + ' 在参数 ' + JSON.stringify(state) +
          ' 下抛异常: ' + e.message);
        return;
      }
      checks++;
      ok(record.badCoords.length === 0,
        kind + ' 在参数 ' + JSON.stringify(state) + ' 下出现非有限坐标: ' +
        record.badCoords.slice(0, 2).join('; '));
    });
  });
})();

// ------------------------------------------ 各分布族与图类型的全覆盖

(function testAllFamilies() {
  ['normal', 't', 'chi2', 'f', 'beta', 'expon', 'binom', 'poisson'].forEach((fam) => {
    const record = freshRecord();
    const container = makeElement('div', record);
    const spec = {
      kind: 'distribution_explorer', title: fam, caption: 'c',
      params: { family: fam, params: {}, show: 'pdf', mark_x: [], interactive: [] }
    };
    try {
      widgets.get('distribution_explorer').render(container, spec);
      checks++;
      ok(record.badCoords.length === 0, fam + ' 分布出现非有限坐标: ' +
        record.badCoords.slice(0, 2).join('; '));
      // controls 必须为每个族给出可用滑块，否则该族无法交互
      const cs = widgets.get('distribution_explorer').controls(spec);
      ok(cs.length > 0, fam + ' 分布应至少有一个可调参数');
    } catch (e) {
      failures.push(fam + ' 分布渲染失败: ' + e.message);
    }
  });

  ['pdf', 'cdf', 'both'].forEach((show) => {
    const record = freshRecord();
    try {
      widgets.get('distribution_explorer').render(makeElement('div', record), {
        kind: 'distribution_explorer', title: 't', caption: 'c',
        params: { family: 'normal', params: {}, show: show, mark_x: [], interactive: [] }
      });
      checks++;
      ok(record.badCoords.length === 0, 'show=' + show + ' 出现非有限坐标');
    } catch (e) {
      failures.push('show=' + show + ' 渲染失败: ' + e.message);
    }
  });

  ['z', 't', 'chi2', 'f'].forEach((test) => {
    ['two-sided', 'greater', 'less'].forEach((alt) => {
      const record = freshRecord();
      try {
        widgets.get('hypothesis_test').render(makeElement('div', record), {
          kind: 'hypothesis_test', title: 't', caption: 'c',
          params: {
            test: test, df: 10, df2: 12, statistic: test === 'chi2' || test === 'f' ? 4 : 2.1,
            alpha: 0.05, alternative: alt, show_p_area: true, show_rejection: true
          }
        });
        checks++;
        ok(record.badCoords.length === 0,
          test + '/' + alt + ' 出现非有限坐标: ' + record.badCoords.slice(0, 2).join('; '));
      } catch (e) {
        failures.push(test + '/' + alt + ' 渲染失败: ' + e.message);
      }
    });
  });

  ['histogram', 'box', 'dot', 'violin'].forEach((kind) => {
    const record = freshRecord();
    try {
      widgets.get('data_plot').render(makeElement('div', record), {
        kind: 'data_plot', title: 't', caption: 'c',
        params: {
          series: [{ label: 'A', values: [1, 2, 3, 4, 5, 20] }],
          kind: kind, bins: null, overlay_normal: false, x_label: ''
        }
      });
      checks++;
      ok(record.badCoords.length === 0, 'data_plot/' + kind + ' 出现非有限坐标');
    } catch (e) {
      failures.push('data_plot/' + kind + ' 渲染失败: ' + e.message);
    }
  });

  ['normal', 'uniform', 'expon', 'bimodal', 'skewed'].forEach((pop) => {
    const record = freshRecord();
    try {
      widgets.get('sampling_distribution').render(makeElement('div', record), {
        kind: 'sampling_distribution', title: 't', caption: 'c',
        params: {
          population: pop, sample_size: 10, n_samples: 200,
          statistic: 'mean', seed: 3, overlay_normal: true, interactive: []
        }
      });
      checks++;
      ok(record.badCoords.length === 0, '总体 ' + pop + ' 出现非有限坐标');
    } catch (e) {
      failures.push('总体 ' + pop + ' 渲染失败: ' + e.message);
    }
  });

  ['mean', 'median', 'variance', 'max'].forEach((st) => {
    const record = freshRecord();
    try {
      widgets.get('sampling_distribution').render(makeElement('div', record), {
        kind: 'sampling_distribution', title: 't', caption: 'c',
        params: {
          population: 'normal', sample_size: 8, n_samples: 200,
          statistic: st, seed: 3, overlay_normal: true, interactive: []
        }
      });
      checks++;
      ok(record.badCoords.length === 0, '统计量 ' + st + ' 出现非有限坐标');
    } catch (e) {
      failures.push('统计量 ' + st + ' 渲染失败: ' + e.message);
    }
  });

  ['n', 'effect_size', 'alpha'].forEach((axis) => {
    const record = freshRecord();
    try {
      widgets.get('power_curve').render(makeElement('div', record), {
        kind: 'power_curve', title: 't', caption: 'c',
        params: {
          x_axis: axis, effect_size: 0.5, n_per_group: 30, alpha: 0.05,
          alternative: 'two-sided', target_power: 0.8, compare: [], interactive: []
        }
      });
      checks++;
      ok(record.badCoords.length === 0, 'power x_axis=' + axis + ' 出现非有限坐标');
    } catch (e) {
      failures.push('power x_axis=' + axis + ' 渲染失败: ' + e.message);
    }
  });
})();

// ----------------------------------- 数值正确性：CLT 与 CI 的行为必须对

(function testStatisticalBehavior() {
  const sd = widgets.get('sampling_distribution');
  // 标准误应随 n 增大而缩小，且贴近 1/sqrt(n)
  const r1 = sd.render(makeElement('div', freshRecord()), SPECS.sampling_distribution, { sample_size: 4, n_samples: 2000 });
  const r2 = sd.render(makeElement('div', freshRecord()), SPECS.sampling_distribution, { sample_size: 64, n_samples: 2000 });
  ok(r2.sd < r1.sd, 'n 增大时抽样分布标准差应变小');
  const ratio = r1.sd / r2.sd;
  ok(ratio > 2.5 && ratio < 5.5,
    '标准误应约按 1/sqrt(n) 缩小（n 从 4 到 64 预期约 4 倍），得 ' + ratio.toFixed(2));

  // CI 覆盖率应接近名义水平
  const ci = widgets.get('confidence_interval');
  const cov = ci.render(makeElement('div', freshRecord()), SPECS.confidence_interval,
    { n_intervals: 300, sample_size: 20, ci_level: 0.95, seed: 21 });
  ok(cov.coverage > 0.88 && cov.coverage < 1.0,
    '95% CI 的模拟覆盖率应接近 0.95，得 ' + cov.coverage.toFixed(3));

  // 回归斜率必须与解析解一致
  const reg = widgets.get('scatter_regression').render(
    makeElement('div', freshRecord()), SPECS.scatter_regression);
  ok(Math.abs(reg.slope - 2.0) < 0.15,
    '已知近似 y=2x 的数据斜率应接近 2，得 ' + reg.slope.toFixed(4));
  ok(reg.r2 > 0.99, '强线性数据的 R² 应接近 1，得 ' + reg.r2.toFixed(4));

  // 假设检验的 p 值必须与 statlib 一致（widget 不能自己算错）
  const ht = widgets.get('hypothesis_test');
  const out = ht.render(makeElement('div', freshRecord()), SPECS.hypothesis_test);
  const expected = 2 * globalThis.statlib.tSf(2.31, 18);
  ok(Math.abs(out.pValue - expected) < 1e-12,
    'widget 的 p 值应与 statlib 一致: ' + out.pValue + ' vs ' + expected);
  ok(Math.abs(out.critHi - globalThis.statlib.tPpf(0.975, 18)) < 1e-12,
    '临界值应与 statlib 一致');
})();

// ------------------------------------------------------ 渲染的确定性

(function testDeterminism() {
  // 同 seed 两次渲染必须给出同样的统计结果 —— 复现性是教学要求
  const sd = widgets.get('sampling_distribution');
  const a = sd.render(makeElement('div', freshRecord()), SPECS.sampling_distribution, { seed: 123 });
  const b = sd.render(makeElement('div', freshRecord()), SPECS.sampling_distribution, { seed: 123 });
  ok(a.sd === b.sd && a.mean === b.mean, '同 seed 渲染结果必须完全一致');
  const c = sd.render(makeElement('div', freshRecord()), SPECS.sampling_distribution, { seed: 124 });
  ok(c.sd !== a.sd, '不同 seed 应给出不同结果');
})();

if (failures.length) {
  console.error('FAIL (' + failures.length + '/' + checks + ')');
  failures.forEach((f) => console.error('  - ' + f));
  process.exit(1);
}
console.log('OK ' + checks + ' checks');
