/**
 * plot.js 的纯函数测试（在 node 里跑，无 DOM）。
 *
 * 只测能脱离 canvas 验证的部分：坐标映射、刻度算法、分箱。
 * 绘图调用本身用一个最小的 ctx 桩来验证"不抛异常 + 调了预期的 API"，
 * 像素级正确性靠人眼审，不在这里假装能自动验证。
 */
'use strict';

const plot = require('../app/static/plot.js');
const statlib = require('../app/static/statlib.js');

const failures = [];
let checks = 0;

function ok(cond, msg) {
  checks++;
  if (!cond) failures.push(msg);
}

function close(a, b, msg, tol) {
  checks++;
  tol = tol === undefined ? 1e-12 : tol;
  if (!(Math.abs(a - b) <= tol * Math.max(1, Math.abs(b)))) {
    failures.push(msg + ' (got ' + a + ', want ' + b + ')');
  }
}

// ---------------------------------------------------------------- Scale
(function testScale() {
  const s = new plot.Scale({
    xMin: -4, xMax: 4, yMin: 0, yMax: 0.4, width: 640, height: 360
  });
  close(s.px(-4), s.pad.left, 'px(xMin) 应贴左边距');
  close(s.px(4), 640 - s.pad.right, 'px(xMax) 应贴右边距');
  close(s.py(0.4), s.pad.top, 'py(yMax) 应贴上边距 (y 轴翻转)');
  ok(s.py(0) > s.py(0.4), 'y 轴必须翻转：小值在下方');
  // 往返映射必须是恒等的，否则拖拽交互会漂移
  [-3.5, -1, 0, 2.25, 3.9].forEach((x) => {
    close(s.dataX(s.px(x)), x, 'dataX(px(x)) 往返 x=' + x);
  });
  [0.01, 0.15, 0.39].forEach((y) => {
    close(s.dataY(s.py(y)), y, 'dataY(py(y)) 往返 y=' + y);
  });
  // 退化区间不能产生 NaN/Infinity
  const deg = new plot.Scale({
    xMin: 5, xMax: 5, yMin: 1, yMax: 1, width: 200, height: 100
  });
  ok(isFinite(deg.px(5)) && isFinite(deg.py(1)), '退化区间不应产生非有限值');
})();

// ------------------------------------------------------------ niceTicks
(function testTicks() {
  const t1 = plot.niceTicks(0, 1);
  ok(t1.length >= 3 && t1.length <= 12, '刻度数量应适中, 得 ' + t1.length);
  ok(t1[0] === 0, '0..1 的首刻度应为 0');
  ok(Math.abs(t1[t1.length - 1] - 1) < 1e-9, '0..1 的末刻度应为 1');

  // 步长必须是 1/2/5 × 10^k
  [[0, 1], [-3, 3], [0, 0.4], [0, 1e6], [1.7, 9.3], [-0.05, 0.05]].forEach((r) => {
    const t = plot.niceTicks(r[0], r[1]);
    if (t.length < 2) return;
    const step = t[1] - t[0];
    const mag = Math.pow(10, Math.floor(Math.log10(step) + 1e-9));
    const norm = step / mag;
    const isNice = [1, 2, 5, 10].some((m) => Math.abs(norm - m) < 1e-6);
    ok(isNice, '步长应为 1/2/5×10^k, 区间 ' + JSON.stringify(r) + ' 得 ' + step);
    t.forEach((v) => ok(v >= r[0] - 1e-9 && v <= r[1] + 1e-9,
      '刻度 ' + v + ' 越出区间 ' + JSON.stringify(r)));
  });

  // 浮点脏值：不能出现 0.30000000000000004
  plot.niceTicks(0, 1).concat(plot.niceTicks(0, 0.7)).forEach((v) => {
    ok(String(v).length <= 8, '刻度值应已清理浮点噪声, 得 ' + v);
  });

  ok(plot.niceTicks(5, 5).length >= 1, '退化区间应返回至少一个刻度');
  ok(plot.niceTicks(NaN, 1).length >= 1, 'NaN 输入不应崩溃');
})();

// -------------------------------------------------------------- fmtTick
(function testFmt() {
  ok(plot.fmtTick(0) === '0', 'fmtTick(0) 应为 "0"');
  ok(!/e/.test(plot.fmtTick(0.5)), '常见量级不该用科学计数法');
  ok(/e/.test(plot.fmtTick(1e6)), '极大值应用科学计数法');
  ok(/e/.test(plot.fmtTick(1e-6)), '极小值应用科学计数法');
  ok(plot.fmtTick(150) === '150', '整数应无小数点');
})();

// -------------------------------------------------------------- makeBins
(function testBins() {
  // 密度积分必须为 1 —— 否则叠加理论 pdf 曲线时高度对不上
  const datasets = [
    [[1, 2, 2, 3, 3, 3, 4, 4, 5], { bins: 4 }],
    [[1, 2, 2, 3, 3, 3, 4, 4, 5], {}],
    [[1, 1, 1], {}],
    [[0.5], {}],
    [[-2, -1, 0, 1, 2], { rule: 'fd' }]
  ];
  datasets.forEach(([vals, opts]) => {
    const bins = plot.makeBins(vals, opts);
    const counted = bins.reduce((a, b) => a + b.count, 0);
    ok(counted === vals.length,
      '所有观测都应落入某一箱: n=' + vals.length + ' 计入 ' + counted);
    const integral = bins.reduce((a, b) => a + b.density * (b.x1 - b.x0), 0);
    close(integral, 1.0, '密度积分应为 1 (n=' + vals.length + ')', 1e-12);
    for (let i = 1; i < bins.length; i++) {
      close(bins[i].x0, bins[i - 1].x1, '相邻箱边界应连续');
    }
  });

  const r = new statlib.PCG32(3);
  const xs = [];
  for (let i = 0; i < 5000; i++) xs.push(r.normal());
  const fd = plot.makeBins(xs, { rule: 'fd' });
  ok(fd.length > 10 && fd.length < 200, 'FD 规则箱数应合理, 得 ' + fd.length);
  close(fd.reduce((a, b) => a + b.density * (b.x1 - b.x0), 0), 1.0,
    'FD 分箱密度积分应为 1');
  ok(plot.makeBins([], {}).length === 0, '空输入应返回空数组');
  ok(plot.makeBins([1, 2, 3], { bins: 10000 }).length <= 200, '箱数应有上限');
})();

// --------------------------------------------------- 绘图调用的冒烟测试
(function testDrawSmoke() {
  const calls = [];
  const ctx = new Proxy({}, {
    get(_, prop) {
      if (prop === 'measureText') return () => ({ width: 20 });
      if (prop === 'canvas') return { width: 640, height: 360 };
      return (...a) => { calls.push(prop); return undefined; };
    },
    set() { return true; }
  });
  const s = new plot.Scale({
    xMin: -4, xMax: 4, yMin: 0, yMax: 0.45, width: 640, height: 360
  });
  const pdf = (x) => statlib.normPdf(x);

  plot.axes(ctx, s, { xLabel: 'z', yLabel: '密度' });
  ok(calls.includes('stroke') && calls.includes('fillText'), 'axes 应描边并写标签');

  plot.curve(ctx, s, pdf);
  plot.shadeUnder(ctx, s, pdf, 1.96, 4);
  ok(calls.includes('fill'), 'shadeUnder 应填充');

  plot.histogram(ctx, s, plot.makeBins([1, 2, 2, 3], {}));
  plot.scatter(ctx, s, [{ x: 0, y: 0.2 }, [1, 0.24]]);
  plot.vline(ctx, s, 1.96, { label: 'z*' });
  plot.hline(ctx, s, 0.2, { label: '基线' });
  plot.errorBar(ctx, s, 0, 0.1, 0.3, { center: 0.2 });
  plot.intervalBar(ctx, s, 0.2, -1, 1, { center: 0 });
  plot.label(ctx, 10, 10, '注释', { background: '#fff' });
  plot.legend(ctx, s, [{ label: 'A' }, { label: 'B' }]);

  // 越界输入必须静默跳过而不是抛异常或画到画布外
  plot.vline(ctx, s, 999);
  plot.hline(ctx, s, -5);
  plot.shadeUnder(ctx, s, pdf, 10, 20);
  plot.curve(ctx, s, () => NaN);
  ok(true, '越界与 NaN 输入不应抛异常');

  // save/restore 必须配对，否则 ctx 状态会泄漏到后续绘制
  const saves = calls.filter((c) => c === 'save').length;
  const restores = calls.filter((c) => c === 'restore').length;
  ok(saves === restores, 'save/restore 应配对: ' + saves + ' vs ' + restores);
})();

if (failures.length) {
  console.error('FAIL (' + failures.length + '/' + checks + ')');
  failures.forEach((f) => console.error('  - ' + f));
  process.exit(1);
}
console.log('OK ' + checks + ' checks');
