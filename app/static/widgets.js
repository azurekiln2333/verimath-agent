/**
 * widgets.js —— artifact spec 的渲染器（Tier 1）。
 *
 * 与 app/artifacts/spec.py 的 WIDGET_REGISTRY 一一对应。后端校验过的 spec
 * 到这里只管画，不再做参数合法性判断 —— 但仍会防御性处理缺失字段，
 * 因为面板可能被旧版本 spec 复现（trace 回放）。
 *
 * 每个 widget 导出 {render(container, spec), controls(spec)}：
 *   render   把图画进容器
 *   controls 声明可交互参数，由 panel 生成滑块并在变更时重绘
 *
 * 交互是这套东西的核心价值：静态图讲不清"参数变了会怎样"。
 * 所以 controls 不是装饰，而是教学内容的载体。
 */
(function (root) {
  'use strict';

  var S = root.statlib;
  var P = root.plot;
  if (!S || !P) throw new Error('widgets.js 依赖 statlib.js 与 plot.js');

  // ---------------------------------------------------------------- 工具

  /** 按分布族取 pdf。params 缺失时给出教学上合理的默认值。 */
  function pdfFor(family, p) {
    p = p || {};
    switch (family) {
      case 'normal': return function (x) { return S.normPdf(x, p.mu || 0, p.sigma || 1); };
      case 't': return function (x) { return S.tPdf(x, p.df || 10); };
      case 'chi2': return function (x) { return S.chi2Pdf(x, p.df || 3); };
      case 'f': return function (x) { return S.fPdf(x, p.dfn || 3, p.dfd || 10); };
      case 'beta': return function (x) { return S.betaPdf(x, p.a || 2, p.b || 3); };
      case 'expon': return function (x) { return S.exponPdf(x, p.scale || 1); };
      default: return null;
    }
  }

  function cdfFor(family, p) {
    p = p || {};
    switch (family) {
      case 'normal': return function (x) { return S.normCdf(x, p.mu || 0, p.sigma || 1); };
      case 't': return function (x) { return S.tCdf(x, p.df || 10); };
      case 'chi2': return function (x) { return S.chi2Cdf(x, p.df || 3); };
      case 'f': return function (x) { return S.fCdf(x, p.dfn || 3, p.dfd || 10); };
      case 'beta': return function (x) { return S.betaCdf(x, p.a || 2, p.b || 3); };
      case 'expon': return function (x) { return S.exponCdf(x, p.scale || 1); };
      default: return null;
    }
  }

  /** 离散分布的 pmf 支撑点。 */
  function pmfPoints(family, p) {
    p = p || {};
    var out = [], k;
    if (family === 'binom') {
      var n = Math.max(1, Math.round(p.n || 20));
      for (k = 0; k <= n; k++) out.push({ k: k, v: S.binomPmf(k, n, p.p === undefined ? 0.5 : p.p) });
    } else if (family === 'poisson') {
      var lam = p.lam === undefined ? 4 : p.lam;
      var kMax = Math.max(10, Math.ceil(lam + 4 * Math.sqrt(lam) + 2));
      for (k = 0; k <= kMax; k++) out.push({ k: k, v: S.poissonPmf(k, lam) });
    }
    return out;
  }

  /** 给分布选一个合适的 x 范围（用分位数而非硬编码，适配任意参数）。 */
  function autoRange(family, p) {
    p = p || {};
    switch (family) {
      case 'normal': {
        var mu = p.mu || 0, sd = p.sigma || 1;
        return [mu - 4 * sd, mu + 4 * sd];
      }
      case 't': {
        var df = p.df || 10;
        var lim = Math.min(8, Math.max(4, S.tPpf(0.9995, df)));
        return [-lim, lim];
      }
      case 'chi2': return [0, Math.max(6, S.chi2Ppf(0.999, p.df || 3))];
      case 'f': return [0, Math.max(4, S.fPpf(0.995, p.dfn || 3, p.dfd || 10))];
      case 'beta': return [0, 1];
      case 'expon': return [0, Math.max(4, S.exponPpf(0.995, p.scale || 1))];
      default: return [0, 1];
    }
  }

  function maxOf(fn, lo, hi, n) {
    n = n || 200;
    var m = 0;
    for (var i = 0; i <= n; i++) {
      var v = fn(lo + (hi - lo) * i / n);
      if (isFinite(v) && v > m) m = v;
    }
    return m || 1;
  }

  function makeCanvas(container, h) {
    container.innerHTML = '';
    var c = document.createElement('canvas');
    c.style.display = 'block';
    c.style.width = '100%';
    c.style.height = (h || 320) + 'px';
    // 图形是信息载体，必须给屏幕阅读器一个等价描述
    c.setAttribute('role', 'img');
    container.appendChild(c);
    return c;
  }

  function fmtP(p) {
    if (p < 1e-4) return p.toExponential(2);
    return p.toFixed(4);
  }

  /**
   * 控件自洽化：初值必须落在 [min, max] 内。
   *
   * 不做这一步的后果是静默的：<input type=range> 会自己把越界的 value
   * 夹到边界上，于是「滑块显示的值」和「实际渲染用的值」不一致，
   * 而且「恢复初始参数」再也回不到最初那张图。
   * 界面看起来完全正常，只是数字是错的 —— 这类 bug 最难发现。
   */
  function ctl(key, label, min, max, step, value) {
    var v = Number(value);
    if (!isFinite(v)) v = min;
    return {
      key: key, label: label, min: min, max: max, step: step,
      value: Math.min(max, Math.max(min, v))
    };
  }

  // ------------------------------------------------- 1. 分布探索器

  var distributionExplorer = {
    controls: function (spec) {
      var p = spec.params || {};
      var fam = p.family;
      var wanted = p.interactive || [];
      var pp = p.params || {};
      var all = {
        normal: [
          ctl('mu', 'μ（均值）', -6, 6, 0.1, pp.mu || 0),
          ctl('sigma', 'σ（标准差）', 0.5, 4, 0.1, pp.sigma || 1)
        ],
        t: [ctl('df', 'df（自由度）', 1, 100, 1, pp.df || 10)],
        chi2: [ctl('df', 'df（自由度）', 1, 50, 1, pp.df || 3)],
        f: [
          ctl('dfn', 'dfn（分子自由度）', 1, 30, 1, pp.dfn || 3),
          ctl('dfd', 'dfd（分母自由度）', 1, 60, 1, pp.dfd || 10)
        ],
        beta: [
          ctl('a', 'α', 0.2, 10, 0.1, pp.a || 2),
          ctl('b', 'β', 0.2, 10, 0.1, pp.b || 3)
        ],
        expon: [ctl('scale', 'scale（尺度）', 0.2, 5, 0.1, pp.scale || 1)],
        binom: [
          ctl('n', 'n（试验次数）', 1, 60, 1, pp.n || 20),
          ctl('p', 'p（成功概率）', 0.01, 0.99, 0.01, pp.p === undefined ? 0.5 : pp.p)
        ],
        poisson: [ctl('lam', 'λ（平均发生率）', 0.2, 30, 0.2, pp.lam === undefined ? 4 : pp.lam)]
      };
      var list = all[fam] || [];
      // interactive 为空时默认全部可调 —— 交互是这个 widget 的主要价值
      if (!wanted.length) return list;
      return list.filter(function (c) { return wanted.indexOf(c.key) >= 0; });
    },

    render: function (container, spec, state) {
      var sp = spec.params || {};
      var fam = sp.family;
      var pars = Object.assign({}, sp.params, state || {});
      var canvas = makeCanvas(container, 320);

      if (fam === 'binom' || fam === 'poisson') {
        return renderDiscrete(canvas, fam, pars, sp);
      }

      var range = autoRange(fam, pars);
      var xMin = sp.x_min === null || sp.x_min === undefined ? range[0] : sp.x_min;
      var xMax = sp.x_max === null || sp.x_max === undefined ? range[1] : sp.x_max;
      var showCdf = sp.show === 'cdf';
      var both = sp.show === 'both';
      var fn = showCdf ? cdfFor(fam, pars) : pdfFor(fam, pars);
      var yMax = showCdf ? 1.05 : maxOf(fn, xMin, xMax) * 1.15;

      // 正态分布：用稳定参考轴（基于初始参数，不随滑块变）。
      // 修复「坐标轴随 μ/σ 自适应 → 看不出参数变化」的 bug：
      //   拖 μ → 曲线在固定网格上左右平移；拖 σ → 曲线明显变宽变矮 / 变窄变高（面积守恒）。
      var stableNormal = (fam === 'normal') &&
        (sp.x_min === null || sp.x_min === undefined) &&
        (sp.x_max === null || sp.x_max === undefined);
      if (stableNormal) {
        var refMu = (sp.params || {}).mu || 0;
        xMin = refMu - 10;
        xMax = refMu + 10;
        if (!showCdf) {
          // y 轴固定到 σ 下限(0.5)的峰值 ×1.15：σ 在 [0.5,4] 内变化时高度差异清晰且不裁剪
          yMax = (1 / (0.5 * Math.sqrt(2 * Math.PI))) * 1.15;
        }
      }

      var g = P.setup(canvas, {
        xMin: xMin, xMax: xMax, yMin: 0, yMax: yMax
      });
      P.axes(g.ctx, g.scale, {
        xLabel: 'x', yLabel: showCdf ? '累积概率' : '概率密度'
      });

      if (sp.shade_from !== null && sp.shade_from !== undefined ||
          sp.shade_to !== null && sp.shade_to !== undefined) {
        var from = sp.shade_from === null || sp.shade_from === undefined ? xMin : sp.shade_from;
        var to = sp.shade_to === null || sp.shade_to === undefined ? xMax : sp.shade_to;
        P.shadeUnder(g.ctx, g.scale, fn, from, to, { color: P.PALETTE.fill });
      }
      P.curve(g.ctx, g.scale, fn, { color: P.PALETTE.accent, width: 2 });
      // 正态分布：标注当前 μ 的位置线，让「μ 平移」一目了然
      if (stableNormal && !showCdf && pars.mu !== undefined) {
        P.vline(g.ctx, g.scale, pars.mu, { label: 'μ = ' + P.fmtTick(pars.mu) });
        // σ 参考标注：在右上角标出当前 σ 与峰值，强化「σ 变大→变矮变宽」的视觉映射
        var curSigma = pars.sigma === undefined ? 1 : pars.sigma;
        var curPeak = 1 / (curSigma * Math.sqrt(2 * Math.PI));
        P.label(g.ctx, g.width - g.scale.pad.right, g.scale.pad.top,
          'σ = ' + curSigma.toFixed(2) + '  峰值 ' + curPeak.toFixed(3),
          { align: 'right', color: P.PALETTE.muted,
            font: '600 12px ui-sans-serif, system-ui, sans-serif' });
      }
      if (both) {
        var cdf = cdfFor(fam, pars);
        // cdf 值域是 [0,1]，与 pdf 共轴时按 yMax 缩放，并标注这是缩放后的
        P.curve(g.ctx, g.scale, function (x) { return cdf(x) * yMax * 0.92; },
          { color: P.PALETTE.accent2, width: 1.6, dash: [6, 4] });
        P.legend(g.ctx, g.scale, [
          { label: '密度 pdf', color: P.PALETTE.accent },
          { label: '累积 cdf（已缩放）', color: P.PALETTE.accent2 }
        ]);
      }
      (sp.mark_x || []).forEach(function (mx) {
        P.vline(g.ctx, g.scale, mx, { label: 'x = ' + P.fmtTick(mx) });
      });

      canvas.setAttribute('aria-label', spec.title + '：' + spec.caption);
      return { xMin: xMin, xMax: xMax };
    }
  };

  function renderDiscrete(canvas, fam, pars, sp) {
    var pts = pmfPoints(fam, pars);
    if (!pts.length) return null;
    var kMax = pts[pts.length - 1].k;
    var yMax = 0;
    pts.forEach(function (d) { if (d.v > yMax) yMax = d.v; });
    var g = P.setup(canvas, {
      xMin: -0.5, xMax: kMax + 0.5, yMin: 0, yMax: yMax * 1.15
    });
    P.axes(g.ctx, g.scale, { xLabel: 'k', yLabel: '概率 P(X=k)' });
    var bins = pts.map(function (d) {
      return { x0: d.k - 0.42, x1: d.k + 0.42, density: d.v };
    });
    P.histogram(g.ctx, g.scale, bins, { valueKey: 'density' });
    (sp.mark_x || []).forEach(function (mx) {
      P.vline(g.ctx, g.scale, mx, { label: 'k = ' + mx });
    });
    canvas.setAttribute('aria-label', '离散分布 ' + fam + ' 的概率质量函数');
    return { xMin: -0.5, xMax: kMax + 0.5 };
  }

  // ------------------------------------------- 2. 假设检验（零分布 + p 值面积）

  var hypothesisTest = {
    controls: function (spec) {
      var p = spec.params || {};
      var out = [
        ctl('alpha', 'α（显著性水平）', 0.001, 0.2, 0.001, p.alpha || 0.05),
        ctl('statistic', '观测统计量', -6, 6, 0.01, p.statistic)
      ];
      if (p.test === 'chi2' || p.test === 'f') {
        // 卡方与 F 的统计量非负，滑块范围要跟着变；上界要能容纳观测值本身
        out[1] = ctl('statistic', '观测统计量', 0,
          Math.max(30, Math.ceil(p.statistic * 1.5)), 0.05, p.statistic);
      }
      if (p.test === 't') {
        out.push(ctl('df', 'df（自由度）', 1, 200, 1, p.df || 10));
      }
      return out;
    },

    render: function (container, spec, state) {
      var sp = Object.assign({}, spec.params, state || {});
      var test = sp.test;
      var alpha = sp.alpha === undefined ? 0.05 : sp.alpha;
      var alt = sp.alternative || 'two-sided';
      var stat = sp.statistic;
      var canvas = makeCanvas(container, 340);

      var pdf, cdf, sf, ppf, xLo, xHi, twoTailSymmetric;
      if (test === 'z') {
        pdf = function (x) { return S.normPdf(x); };
        cdf = function (x) { return S.normCdf(x); };
        sf = function (x) { return S.normSf(x); };
        ppf = function (q) { return S.normPpf(q); };
        xLo = -4.2; xHi = 4.2; twoTailSymmetric = true;
      } else if (test === 't') {
        var df = sp.df || 10;
        pdf = function (x) { return S.tPdf(x, df); };
        cdf = function (x) { return S.tCdf(x, df); };
        sf = function (x) { return S.tSf(x, df); };
        ppf = function (q) { return S.tPpf(q, df); };
        var lim = Math.max(4.2, Math.min(9, Math.abs(stat) + 1.5));
        xLo = -lim; xHi = lim; twoTailSymmetric = true;
      } else if (test === 'chi2') {
        var dfc = sp.df || 3;
        pdf = function (x) { return S.chi2Pdf(x, dfc); };
        cdf = function (x) { return S.chi2Cdf(x, dfc); };
        sf = function (x) { return S.chi2Sf(x, dfc); };
        ppf = function (q) { return S.chi2Ppf(q, dfc); };
        xLo = 0; xHi = Math.max(S.chi2Ppf(0.999, dfc), stat * 1.2, 1);
        twoTailSymmetric = false;
      } else {
        var dfn = sp.df || 3, dfd = sp.df2 || 10;
        pdf = function (x) { return S.fPdf(x, dfn, dfd); };
        cdf = function (x) { return S.fCdf(x, dfn, dfd); };
        sf = function (x) { return S.fSf(x, dfn, dfd); };
        ppf = function (q) { return S.fPpf(q, dfn, dfd); };
        xLo = 0; xHi = Math.max(S.fPpf(0.999, dfn, dfd), stat * 1.2, 1);
        twoTailSymmetric = false;
      }

      var yMax = maxOf(pdf, xLo, xHi) * 1.18;
      var g = P.setup(canvas, { xMin: xLo, xMax: xHi, yMin: 0, yMax: yMax });
      P.axes(g.ctx, g.scale, {
        xLabel: '检验统计量（' + test + '）', yLabel: '零分布密度'
      });

      // 拒绝域：先画，让它在 p 值区之下
      var critHi = null, critLo = null;
      if (sp.show_rejection !== false) {
        if (alt === 'two-sided' && twoTailSymmetric) {
          critHi = ppf(1 - alpha / 2); critLo = -critHi;
        } else if (alt === 'two-sided') {
          critHi = ppf(1 - alpha);      // 卡方/F 的双侧检验实践上用右尾
        } else if (alt === 'greater') {
          critHi = ppf(1 - alpha);
        } else {
          critLo = ppf(alpha);
        }
        if (critHi !== null) {
          P.shadeUnder(g.ctx, g.scale, pdf, critHi, xHi,
            { color: 'rgba(154, 52, 18, 0.20)' });
        }
        if (critLo !== null) {
          P.shadeUnder(g.ctx, g.scale, pdf, xLo, critLo,
            { color: 'rgba(154, 52, 18, 0.20)' });
        }
      }

      // p 值面积
      var pValue;
      if (alt === 'greater') pValue = sf(stat);
      else if (alt === 'less') pValue = cdf(stat);
      else if (twoTailSymmetric) pValue = 2 * Math.min(cdf(stat), sf(stat));
      else pValue = sf(stat);

      if (sp.show_p_area !== false) {
        if (alt === 'greater' || !twoTailSymmetric) {
          P.shadeUnder(g.ctx, g.scale, pdf, stat, xHi, { color: P.PALETTE.fill });
        } else if (alt === 'less') {
          P.shadeUnder(g.ctx, g.scale, pdf, xLo, stat, { color: P.PALETTE.fill });
        } else {
          P.shadeUnder(g.ctx, g.scale, pdf, Math.abs(stat), xHi, { color: P.PALETTE.fill });
          P.shadeUnder(g.ctx, g.scale, pdf, xLo, -Math.abs(stat), { color: P.PALETTE.fill });
        }
      }

      P.curve(g.ctx, g.scale, pdf, { color: P.PALETTE.ink, width: 1.8 });

      if (critHi !== null) {
        P.vline(g.ctx, g.scale, critHi, {
          color: P.PALETTE.warn, label: '临界值 ' + critHi.toFixed(3)
        });
      }
      if (critLo !== null) {
        P.vline(g.ctx, g.scale, critLo, {
          color: P.PALETTE.warn, label: critLo.toFixed(3), labelAt: 'bottom'
        });
      }
      P.vline(g.ctx, g.scale, stat, {
        color: P.PALETTE.accent, width: 2.2, dash: null,
        label: '观测值 ' + stat.toFixed(3), labelAt: 'bottom'
      });

      var reject = pValue < alpha;
      P.label(g.ctx, g.width - g.scale.pad.right, g.scale.pad.top,
        'p = ' + fmtP(pValue) + (reject ? '  <  ' : '  ≥  ') + 'α = ' + alpha,
        { align: 'right', color: reject ? P.PALETTE.warn : P.PALETTE.ok,
          font: '600 12px ui-sans-serif, system-ui, sans-serif' });
      P.label(g.ctx, g.width - g.scale.pad.right, g.scale.pad.top + 17,
        reject ? '在 α 水平下拒绝 H₀' : '不能拒绝 H₀（≠ H₀ 成立）',
        { align: 'right', color: P.PALETTE.muted });

      canvas.setAttribute('aria-label',
        spec.title + '：零分布下观测统计量 ' + stat.toFixed(3) +
        ' 对应 p 值 ' + fmtP(pValue) + '，' +
        (reject ? '小于' : '不小于') + '显著性水平 ' + alpha);
      return { pValue: pValue, critHi: critHi, critLo: critLo };
    }
  };

  // -------------------------------------- 3. 抽样分布（中心极限定理）

  /** 按总体类型采样。用 PCG32 保证可复现。 */
  function drawPopulation(rng, kind) {
    switch (kind) {
      case 'normal': return rng.normal(0, 1);
      case 'uniform': return rng.uniform(-1.732, 1.732);   // 方差 ≈ 1
      case 'expon': return rng.exponential(1) - 1;         // 中心化，强右偏
      case 'skewed': return Math.pow(rng.exponential(1), 1.5) - 1.33;
      case 'bimodal': return rng.random() < 0.5 ? rng.normal(-2, 0.5) : rng.normal(2, 0.5);
      default: return rng.normal(0, 1);
    }
  }

  function statOf(values, kind) {
    if (kind === 'mean') return S.mean(values);
    if (kind === 'variance') return values.length > 1 ? S.variance(values) : 0;
    if (kind === 'max') return Math.max.apply(null, values);
    var xs = values.slice().sort(function (a, b) { return a - b; });
    var m = Math.floor(xs.length / 2);
    return xs.length % 2 ? xs[m] : (xs[m - 1] + xs[m]) / 2;
  }

  var samplingDistribution = {
    controls: function (spec) {
      var p = spec.params || {};
      return [
        ctl('sample_size', 'n（每次抽样的样本量）', 1, 200, 1, p.sample_size),
        ctl('n_samples', '重复抽样次数', 100, 5000, 100, p.n_samples || 1000),
        ctl('seed', '随机种子（换个数看是否巧合）', 1, 999, 1, p.seed)
      ];
    },

    render: function (container, spec, state) {
      var sp = Object.assign({}, spec.params, state || {});
      var n = Math.max(1, Math.round(sp.sample_size));
      var reps = Math.max(10, Math.round(sp.n_samples || 1000));
      var rng = new S.PCG32(Math.round(sp.seed || 20240607), 54);
      var statKind = sp.statistic || 'mean';

      var stats = [], popSample = [], i, j, sample;
      for (i = 0; i < reps; i++) {
        sample = [];
        for (j = 0; j < n; j++) sample.push(drawPopulation(rng, sp.population));
        if (i < 40) popSample = popSample.concat(sample);
        stats.push(statOf(sample, statKind));
      }

      container.innerHTML = '';
      var wrap = document.createElement('div');
      wrap.className = 'artifact-dual';
      container.appendChild(wrap);
      var left = document.createElement('div');
      var right = document.createElement('div');
      wrap.appendChild(left);
      wrap.appendChild(right);

      // 左：总体形状 —— 关键教学点是"总体不正态也没关系"
      var cPop = makeCanvas(left, 190);
      var popBins = P.makeBins(popSample, { rule: 'fd' });
      var popMax = 0;
      popBins.forEach(function (b) { if (b.density > popMax) popMax = b.density; });
      var gp = P.setup(cPop, {
        xMin: popBins[0].x0, xMax: popBins[popBins.length - 1].x1,
        yMin: 0, yMax: popMax * 1.15
      });
      P.axes(gp.ctx, gp.scale, { xLabel: '总体分布（原始数据）', yLabel: '密度', yTickCount: 3 });
      P.histogram(gp.ctx, gp.scale, popBins, { color: 'rgba(120,132,145,0.28)', stroke: P.PALETTE.muted });
      cPop.setAttribute('aria-label', '总体分布的直方图，形状为 ' + sp.population);

      // 右：统计量的抽样分布 + 正态参考
      var cStat = makeCanvas(right, 190);
      var bins = P.makeBins(stats, { rule: 'fd' });
      var sMean = S.mean(stats);
      var sSd = stats.length > 1 ? S.stdev(stats) : 1;
      var yTop = 0;
      bins.forEach(function (b) { if (b.density > yTop) yTop = b.density; });
      var normPeak = sSd > 0 ? S.normPdf(sMean, sMean, sSd) : 0;
      yTop = Math.max(yTop, normPeak) * 1.18;
      var gs = P.setup(cStat, {
        xMin: bins[0].x0, xMax: bins[bins.length - 1].x1, yMin: 0, yMax: yTop
      });
      P.axes(gs.ctx, gs.scale, {
        xLabel: '样本' + ({ mean: '均值', median: '中位数', variance: '方差', max: '最大值' }[statKind]) + '的分布',
        yLabel: '密度', yTickCount: 3
      });
      P.histogram(gs.ctx, gs.scale, bins);
      if (sp.overlay_normal !== false && sSd > 0) {
        P.curve(gs.ctx, gs.scale, function (x) { return S.normPdf(x, sMean, sSd); },
          { color: P.PALETTE.accent2, width: 2 });
        P.legend(gs.ctx, gs.scale, [
          { label: '模拟结果', color: P.PALETTE.accent },
          { label: '正态参考曲线', color: P.PALETTE.accent2 }
        ]);
      }
      cStat.setAttribute('aria-label',
        '样本统计量的抽样分布，均值 ' + sMean.toFixed(3) + '，标准差 ' + sSd.toFixed(3));

      var note = document.createElement('div');
      note.className = 'artifact-note';
      note.textContent = 'n = ' + n + '：抽样分布标准差 ' + sSd.toFixed(4) +
        '（理论标准误 ≈ ' + (1 / Math.sqrt(n)).toFixed(4) + '）。' +
        '注意左图形状不变，右图随 n 增大越来越接近钟形 —— 这才是中心极限定理说的事。';
      container.appendChild(note);
      return { mean: sMean, sd: sSd };
    }
  };

  // ------------------------------------------ 4. 置信区间覆盖率

  var confidenceInterval = {
    controls: function (spec) {
      var p = spec.params || {};
      return [
        ctl('sample_size', 'n（每次抽样的样本量）', 2, 200, 1, p.sample_size),
        ctl('ci_level', '置信水平', 0.5, 0.995, 0.005, p.ci_level || 0.95),
        ctl('n_intervals', '重复实验次数', 10, 200, 5, p.n_intervals || 50),
        ctl('seed', '随机种子', 1, 999, 1, p.seed)
      ];
    },

    render: function (container, spec, state) {
      var sp = Object.assign({}, spec.params, state || {});
      var n = Math.max(2, Math.round(sp.sample_size));
      var reps = Math.max(5, Math.round(sp.n_intervals || 50));
      var level = sp.ci_level || 0.95;
      var trueMean = sp.true_mean || 0;
      var trueSd = sp.true_sd || 1;
      var rng = new S.PCG32(Math.round(sp.seed || 20240607), 54);
      var crit = S.tPpf(1 - (1 - level) / 2, n - 1);

      var rows = [], i, j, sample, m, se, covered = 0;
      for (i = 0; i < reps; i++) {
        sample = [];
        for (j = 0; j < n; j++) sample.push(rng.normal(trueMean, trueSd));
        m = S.mean(sample);
        se = S.stdev(sample) / Math.sqrt(n);
        var lo = m - crit * se, hi = m + crit * se;
        var ok = lo <= trueMean && trueMean <= hi;
        if (ok) covered++;
        rows.push({ lo: lo, hi: hi, mean: m, ok: ok });
      }

      container.innerHTML = '';
      var canvas = makeCanvas(container, Math.min(460, 60 + reps * 7));
      var allLo = Math.min.apply(null, rows.map(function (r) { return r.lo; }));
      var allHi = Math.max.apply(null, rows.map(function (r) { return r.hi; }));
      var g = P.setup(canvas, {
        xMin: allLo - 0.1, xMax: allHi + 0.1, yMin: -0.5, yMax: reps - 0.5,
        padding: { left: 40, right: 16, top: 26, bottom: 34 }
      });
      P.axes(g.ctx, g.scale, { xLabel: '参数估计值与置信区间', yTicks: [], grid: false });
      P.vline(g.ctx, g.scale, trueMean, {
        color: P.PALETTE.ink, dash: null, width: 1.6, label: '真值 μ = ' + trueMean
      });
      rows.forEach(function (r, idx) {
        P.intervalBar(g.ctx, g.scale, idx, r.lo, r.hi, {
          color: r.ok ? P.PALETTE.accent : P.PALETTE.warn,
          center: r.mean, width: r.ok ? 1.3 : 2.1
        });
      });

      var rate = covered / reps;
      P.label(g.ctx, g.scale.pad.left, 8,
        '覆盖 ' + covered + '/' + reps + ' = ' + (rate * 100).toFixed(1) +
        '%（名义 ' + (level * 100).toFixed(1) + '%）',
        { color: P.PALETTE.ink, font: '600 12px ui-sans-serif, system-ui, sans-serif' });

      canvas.setAttribute('aria-label',
        reps + ' 次重复实验的置信区间，其中 ' + covered + ' 条覆盖了真值 ' +
        trueMean + '，覆盖率 ' + (rate * 100).toFixed(1) + '%');

      var note = document.createElement('div');
      note.className = 'artifact-note';
      note.textContent = '红色区间没盖住真值。置信水平说的是"这个造区间的程序，' +
        '长期重复下有约 ' + (level * 100).toFixed(0) + '% 的区间会盖住真值"，' +
        '而不是"某一条给定区间有 ' + (level * 100).toFixed(0) + '% 的概率盖住真值"' +
        '—— 真值是固定的，随机的是区间。';
      container.appendChild(note);
      return { coverage: rate };
    }
  };

  // ------------------------------------------------- 5. 功效曲线

  var powerCurve = {
    controls: function (spec) {
      var p = spec.params || {};
      var out = [
        ctl('alpha', 'α（显著性水平）', 0.001, 0.2, 0.001, p.alpha || 0.05)
      ];
      if (p.x_axis !== 'effect_size') {
        out.push(ctl('effect_size', "效应量 Cohen's d", 0.05, 2, 0.05, p.effect_size));
      }
      if (p.x_axis !== 'n') {
        out.push(ctl('n_per_group', '每组样本量 n', 2, 500, 1, p.n_per_group || 30));
      }
      return out;
    },

    render: function (container, spec, state) {
      var sp = Object.assign({}, spec.params, state || {});
      var axis = sp.x_axis || 'n';
      var alpha = sp.alpha || 0.05;
      var alt = sp.alternative || 'two-sided';
      var target = sp.target_power || 0.8;
      var canvas = makeCanvas(container, 320);

      var xMin, xMax, fn, xLabel;
      if (axis === 'n') {
        xMin = 2; xMax = Math.max(40, (sp.n_per_group || 30) * 3);
        xLabel = '每组样本量 n';
        fn = function (x) {
          return S.powerTwoSampleT(sp.effect_size, Math.max(2, Math.round(x)), alpha, alt).power;
        };
      } else if (axis === 'effect_size') {
        xMin = 0; xMax = 2;
        xLabel = "效应量 Cohen's d";
        fn = function (x) {
          return x === 0 ? alpha
            : S.powerTwoSampleT(x, sp.n_per_group || 30, alpha, alt).power;
        };
      } else {
        xMin = 0.001; xMax = 0.2;
        xLabel = 'α（显著性水平）';
        fn = function (x) {
          return S.powerTwoSampleT(sp.effect_size, sp.n_per_group || 30,
            Math.max(1e-4, Math.min(0.999, x)), alt).power;
        };
      }

      var g = P.setup(canvas, { xMin: xMin, xMax: xMax, yMin: 0, yMax: 1.02 });
      P.axes(g.ctx, g.scale, { xLabel: xLabel, yLabel: '功效 (1 − β)' });
      P.hline(g.ctx, g.scale, target, {
        color: P.PALETTE.muted, label: '目标功效 ' + target
      });
      // α 水平线：功效不可能低于它（d=0 时功效恰等于 α）
      P.hline(g.ctx, g.scale, alpha, {
        color: P.PALETTE.warn, label: 'α = ' + alpha, dash: [2, 3]
      });

      (sp.compare || []).forEach(function (val, i) {
        var color = P.SERIES[(i + 1) % P.SERIES.length];
        P.curve(g.ctx, g.scale, function (x) {
          if (axis === 'n') return S.powerTwoSampleT(val, Math.max(2, Math.round(x)), alpha, alt).power;
          if (axis === 'effect_size') return S.powerTwoSampleT(x, val, alpha, alt).power;
          return S.powerTwoSampleT(sp.effect_size, val, Math.max(1e-4, x), alt).power;
        }, { color: color, width: 1.5, dash: [5, 3] });
      });

      P.curve(g.ctx, g.scale, fn, { color: P.PALETTE.accent, width: 2.2 });

      // 标出达到目标功效所需的样本量 —— 这是最实用的一个读数
      if (axis === 'n' && sp.effect_size) {
        try {
          var need = S.sampleSizeTwoSampleT(sp.effect_size, target, alpha, alt);
          if (need.n_per_group <= xMax) {
            P.vline(g.ctx, g.scale, need.n_per_group, {
              label: '需 n = ' + need.n_per_group, labelAt: 'bottom'
            });
          }
        } catch (e) { /* 达不到目标功效时不标注 */ }
      }

      var current = axis === 'n'
        ? S.powerTwoSampleT(sp.effect_size, sp.n_per_group || 30, alpha, alt)
        : null;
      if (current) {
        P.label(g.ctx, g.width - g.scale.pad.right, g.scale.pad.top,
          'n = ' + (sp.n_per_group || 30) + ' 时功效 ' + current.power.toFixed(3),
          { align: 'right', color: P.PALETTE.muted });
      }

      canvas.setAttribute('aria-label', spec.title + '：' + spec.caption);
      return {};
    }
  };

  // --------------------------------------------- 6. 散点 + 回归

  /** 最小二乘。返回斜率、截距、R²、残差。 */
  function linreg(x, y) {
    var n = x.length, mx = S.mean(x), my = S.mean(y);
    var sxy = 0, sxx = 0, syy = 0, i;
    for (i = 0; i < n; i++) {
      sxy += (x[i] - mx) * (y[i] - my);
      sxx += (x[i] - mx) * (x[i] - mx);
      syy += (y[i] - my) * (y[i] - my);
    }
    var slope = sxx === 0 ? 0 : sxy / sxx;
    var intercept = my - slope * mx;
    var ssRes = 0, resid = [];
    for (i = 0; i < n; i++) {
      var fit = intercept + slope * x[i];
      resid.push(y[i] - fit);
      ssRes += (y[i] - fit) * (y[i] - fit);
    }
    return {
      slope: slope, intercept: intercept,
      r2: syy === 0 ? 0 : 1 - ssRes / syy,
      resid: resid, mx: mx, sxx: sxx,
      seResid: n > 2 ? Math.sqrt(ssRes / (n - 2)) : 0, n: n
    };
  }

  var scatterRegression = {
    controls: function () { return []; },

    render: function (container, spec) {
      var sp = spec.params || {};
      var x = sp.x, y = sp.y;
      var fit = linreg(x, y);
      var canvas = makeCanvas(container, 320);
      var xLo = Math.min.apply(null, x), xHi = Math.max.apply(null, x);
      var yLo = Math.min.apply(null, y), yHi = Math.max.apply(null, y);
      var padX = (xHi - xLo) * 0.08 || 1, padY = (yHi - yLo) * 0.12 || 1;
      var g = P.setup(canvas, {
        xMin: xLo - padX, xMax: xHi + padX, yMin: yLo - padY, yMax: yHi + padY
      });
      P.axes(g.ctx, g.scale, { xLabel: sp.x_label || 'x', yLabel: sp.y_label || 'y' });

      if (sp.show_ci_band && fit.n > 2) {
        // 回归线的置信带：宽度随离 x̄ 的距离增大 —— 外推不可靠的可视化证据
        var tc = S.tPpf(0.975, fit.n - 2);
        var band = function (sign) {
          return function (xv) {
            var seFit = fit.seResid * Math.sqrt(1 / fit.n +
              Math.pow(xv - fit.mx, 2) / (fit.sxx || 1));
            return fit.intercept + fit.slope * xv + sign * tc * seFit;
          };
        };
        P.curve(g.ctx, g.scale, band(1), { color: P.PALETTE.muted, width: 1, dash: [4, 3] });
        P.curve(g.ctx, g.scale, band(-1), { color: P.PALETTE.muted, width: 1, dash: [4, 3] });
      }

      if (sp.show_residuals) {
        g.ctx.save();
        g.ctx.strokeStyle = 'rgba(154,52,18,0.5)';
        g.ctx.lineWidth = 1;
        for (var i = 0; i < x.length; i++) {
          g.ctx.beginPath();
          g.ctx.moveTo(g.scale.px(x[i]), g.scale.py(y[i]));
          g.ctx.lineTo(g.scale.px(x[i]), g.scale.py(fit.intercept + fit.slope * x[i]));
          g.ctx.stroke();
        }
        g.ctx.restore();
      }

      if (sp.show_fit !== false) {
        P.curve(g.ctx, g.scale, function (xv) {
          return fit.intercept + fit.slope * xv;
        }, { color: P.PALETTE.accent2, width: 2 });
      }
      P.scatter(g.ctx, g.scale, x.map(function (xv, i) {
        return { x: xv, y: y[i] };
      }), { color: P.PALETTE.accent, radius: 3.6 });

      var r = Math.sqrt(Math.max(0, fit.r2)) * (fit.slope < 0 ? -1 : 1);
      P.label(g.ctx, g.scale.pad.left + 8, g.scale.pad.top + 2,
        'ŷ = ' + fit.intercept.toFixed(3) + ' + ' + fit.slope.toFixed(3) + 'x' +
        '   r = ' + r.toFixed(3) + '   R² = ' + fit.r2.toFixed(3),
        { color: P.PALETTE.ink, background: 'rgba(255,255,255,0.82)' });

      canvas.setAttribute('aria-label',
        '散点图与回归线，斜率 ' + fit.slope.toFixed(3) + '，R² ' + fit.r2.toFixed(3));

      var note = document.createElement('div');
      note.className = 'artifact-note';
      note.textContent = 'R² 只说明线性模型解释了多少变异，不说明因果方向，' +
        '也不保证模型正确 —— 残差图和散点形状比 R² 更能暴露问题。';
      container.appendChild(note);
      return { slope: fit.slope, r2: fit.r2 };
    }
  };

  // ------------------------------------------------ 7. 原始数据分布图

  function quantile(sorted, q) {
    var pos = (sorted.length - 1) * q;
    var lo = Math.floor(pos), hi = Math.ceil(pos);
    if (lo === hi) return sorted[lo];
    return sorted[lo] + (sorted[hi] - sorted[lo]) * (pos - lo);
  }

  function boxStats(values) {
    var xs = values.slice().sort(function (a, b) { return a - b; });
    var q1 = quantile(xs, 0.25), q2 = quantile(xs, 0.5), q3 = quantile(xs, 0.75);
    var iqr = q3 - q1;
    var loFence = q1 - 1.5 * iqr, hiFence = q3 + 1.5 * iqr;
    var inliers = xs.filter(function (v) { return v >= loFence && v <= hiFence; });
    return {
      q1: q1, q2: q2, q3: q3,
      whiskLo: inliers.length ? inliers[0] : q1,
      whiskHi: inliers.length ? inliers[inliers.length - 1] : q3,
      outliers: xs.filter(function (v) { return v < loFence || v > hiFence; }),
      mean: S.mean(xs), n: xs.length
    };
  }

  var dataPlot = {
    controls: function (spec) {
      var p = spec.params || {};
      if (p.kind !== 'histogram') return [];
      var total = (p.series || []).reduce(function (a, s) { return a + s.values.length; }, 0);
      return [ctl('bins', '分箱数', 2,
        Math.max(4, Math.min(60, Math.ceil(total / 2))), 1,
        p.bins || Math.ceil(Math.log2(Math.max(2, total)) + 1))];
    },

    render: function (container, spec, state) {
      var sp = Object.assign({}, spec.params, state || {});
      var series = sp.series || [];
      var kind = sp.kind || 'histogram';
      var all = [];
      series.forEach(function (s) { all = all.concat(s.values); });
      var lo = Math.min.apply(null, all), hi = Math.max.apply(null, all);
      var pad = (hi - lo) * 0.08 || 1;
      var canvas = makeCanvas(container, kind === 'box' ? Math.max(160, 60 + series.length * 54) : 300);

      if (kind === 'box' || kind === 'violin') {
        var g = P.setup(canvas, {
          xMin: lo - pad, xMax: hi + pad, yMin: -0.6, yMax: series.length - 0.4,
          padding: { left: 78, right: 18, top: 18, bottom: 34 }
        });
        P.axes(g.ctx, g.scale, { xLabel: sp.x_label || '取值', yTicks: [], grid: false });
        series.forEach(function (s, i) {
          var b = boxStats(s.values);
          var color = P.SERIES[i % P.SERIES.length];
          var y = g.scale.py(i), h = 20;
          g.ctx.save();
          g.ctx.strokeStyle = color;
          g.ctx.fillStyle = hexAlpha(color, 0.16);
          g.ctx.lineWidth = 1.6;
          // 盒
          g.ctx.strokeRect(g.scale.px(b.q1), y - h / 2, g.scale.px(b.q3) - g.scale.px(b.q1), h);
          // 中位数
          g.ctx.beginPath();
          g.ctx.moveTo(g.scale.px(b.q2), y - h / 2);
          g.ctx.lineTo(g.scale.px(b.q2), y + h / 2);
          // 须
          g.ctx.moveTo(g.scale.px(b.whiskLo), y);
          g.ctx.lineTo(g.scale.px(b.q1), y);
          g.ctx.moveTo(g.scale.px(b.q3), y);
          g.ctx.lineTo(g.scale.px(b.whiskHi), y);
          g.ctx.stroke();
          g.ctx.restore();
          // 均值用点标出，与中位数区分 —— 偏态数据里两者差异是重点
          P.scatter(g.ctx, g.scale, [{ x: b.mean, y: i }], { color: color, radius: 3.4 });
          P.scatter(g.ctx, g.scale, b.outliers.map(function (v) {
            return { x: v, y: i };
          }), { color: P.PALETTE.warn, radius: 2.6, alpha: 0.85 });
          P.label(g.ctx, 70, y, (s.label || ('组' + (i + 1))),
            { align: 'right', baseline: 'middle', color: P.PALETTE.ink });
        });
        canvas.setAttribute('aria-label', '各组数据的箱线图，含中位数、四分位距与离群点');
      } else if (kind === 'dot') {
        var gd = P.setup(canvas, {
          xMin: lo - pad, xMax: hi + pad, yMin: -0.6, yMax: series.length - 0.4,
          padding: { left: 78, right: 18, top: 18, bottom: 34 }
        });
        P.axes(gd.ctx, gd.scale, { xLabel: sp.x_label || '取值', yTicks: [], grid: false });
        series.forEach(function (s, i) {
          var color = P.SERIES[i % P.SERIES.length];
          // 同值点上下抖动，避免完全重叠掩盖样本量
          var jitterRng = new S.PCG32(1000 + i, 7);
          P.scatter(gd.ctx, gd.scale, s.values.map(function (v) {
            return { x: v, y: i + (jitterRng.random() - 0.5) * 0.34 };
          }), { color: color, radius: 3.1, alpha: 0.72 });
          P.label(gd.ctx, 70, gd.scale.py(i), (s.label || ('组' + (i + 1))),
            { align: 'right', baseline: 'middle', color: P.PALETTE.ink });
        });
        canvas.setAttribute('aria-label', '各组数据的点图');
      } else {
        var binOpts = sp.bins ? { bins: Math.round(sp.bins), min: lo, max: hi }
          : { rule: 'fd', min: lo, max: hi };
        var allBins = series.map(function (s) { return P.makeBins(s.values, binOpts); });
        var yTop = 0;
        allBins.forEach(function (bs) {
          bs.forEach(function (b) { if (b.density > yTop) yTop = b.density; });
        });
        if (sp.overlay_normal) {
          series.forEach(function (s) {
            if (s.values.length < 2) return;
            var pk = S.normPdf(S.mean(s.values), S.mean(s.values), S.stdev(s.values));
            if (pk > yTop) yTop = pk;
          });
        }
        var gh = P.setup(canvas, {
          xMin: lo - pad, xMax: hi + pad, yMin: 0, yMax: yTop * 1.18
        });
        P.axes(gh.ctx, gh.scale, { xLabel: sp.x_label || '取值', yLabel: '密度' });
        allBins.forEach(function (bs, i) {
          var color = P.SERIES[i % P.SERIES.length];
          P.histogram(gh.ctx, gh.scale, bs, {
            color: hexAlpha(color, series.length > 1 ? 0.34 : 0.2), stroke: color
          });
        });
        if (sp.overlay_normal) {
          series.forEach(function (s, i) {
            if (s.values.length < 2) return;
            var m = S.mean(s.values), sd = S.stdev(s.values);
            if (sd <= 0) return;
            P.curve(gh.ctx, gh.scale, function (x) { return S.normPdf(x, m, sd); },
              { color: P.SERIES[i % P.SERIES.length], width: 1.8, dash: [6, 3] });
          });
        }
        if (series.length > 1) {
          P.legend(gh.ctx, gh.scale, series.map(function (s, i) {
            return { label: s.label || ('组' + (i + 1)), color: P.SERIES[i % P.SERIES.length] };
          }));
        }
        canvas.setAttribute('aria-label', '各组数据的直方图（纵轴为密度）');
      }

      var note = document.createElement('div');
      note.className = 'artifact-note';
      note.textContent = series.map(function (s) {
        var v = s.values;
        return (s.label || '数据') + '：n=' + v.length + '，均值 ' +
          S.mean(v).toFixed(3) + (v.length > 1 ? '，标准差 ' + S.stdev(v).toFixed(3) : '');
      }).join('　|　');
      container.appendChild(note);
      return {};
    }
  };

  function hexAlpha(hex, a) {
    var m = /^#?([0-9a-f]{2})([0-9a-f]{2})([0-9a-f]{2})$/i.exec(hex);
    if (!m) return hex;
    return 'rgba(' + parseInt(m[1], 16) + ',' + parseInt(m[2], 16) + ',' +
      parseInt(m[3], 16) + ',' + a + ')';
  }

  // -------------------------------------------- 8. 效应量并排比较

  var effectSize = {
    controls: function () { return []; },

    render: function (container, spec) {
      var sp = spec.params || {};
      var items = sp.items || [];
      var nullVal = sp.null_value === undefined ? 0 : sp.null_value;
      var canvas = makeCanvas(container, Math.max(150, 56 + items.length * 34));
      var lo = Math.min.apply(null, items.map(function (d) { return d.ci_low; }).concat([nullVal]));
      var hi = Math.max.apply(null, items.map(function (d) { return d.ci_high; }).concat([nullVal]));
      var pad = (hi - lo) * 0.12 || 0.5;
      var g = P.setup(canvas, {
        xMin: lo - pad, xMax: hi + pad, yMin: -0.6, yMax: items.length - 0.4,
        padding: { left: 108, right: 20, top: 18, bottom: 34 }
      });
      P.axes(g.ctx, g.scale, { xLabel: sp.x_label || '效应量', yTicks: [], grid: false });
      P.vline(g.ctx, g.scale, nullVal, {
        color: P.PALETTE.ink, dash: [4, 3], width: 1.4,
        label: '无效应 = ' + nullVal
      });
      items.forEach(function (d, i) {
        var crosses = d.ci_low <= nullVal && nullVal <= d.ci_high;
        P.intervalBar(g.ctx, g.scale, i, d.ci_low, d.ci_high, {
          color: crosses ? P.PALETTE.muted : P.PALETTE.accent,
          center: d.estimate, width: 1.9
        });
        P.label(g.ctx, 100, g.scale.py(i), String(d.label),
          { align: 'right', baseline: 'middle', color: P.PALETTE.ink });
      });
      canvas.setAttribute('aria-label',
        items.length + ' 项效应量及其置信区间的比较图');

      var note = document.createElement('div');
      note.className = 'artifact-note';
      note.textContent = '灰色区间跨过了"无效应"参考线（等价于在该水平下不显著）。' +
        '区间宽度反映估计精度 —— 一个"显著但区间极宽"的结果，实际信息量很低。';
      container.appendChild(note);
      return {};
    }
  };

  // ------------------------------------------------------------- 注册表

  var WIDGETS = {
    distribution_explorer: distributionExplorer,
    hypothesis_test: hypothesisTest,
    sampling_distribution: samplingDistribution,
    confidence_interval: confidenceInterval,
    power_curve: powerCurve,
    scatter_regression: scatterRegression,
    data_plot: dataPlot,
    effect_size: effectSize
  };

  var widgets = {
    WIDGETS: WIDGETS,
    has: function (kind) { return Object.prototype.hasOwnProperty.call(WIDGETS, kind); },
    get: function (kind) { return WIDGETS[kind]; },
    kinds: function () { return Object.keys(WIDGETS); },
    // 供测试与调试用的内部函数
    _internal: { linreg: linreg, boxStats: boxStats, quantile: quantile, hexAlpha: hexAlpha }
  };

  if (typeof module !== 'undefined' && module.exports) module.exports = widgets;
  root.widgets = widgets;
})(typeof globalThis !== 'undefined' ? globalThis : this);
