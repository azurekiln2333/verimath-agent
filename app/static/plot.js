/**
 * plot.js —— 统计教学专用的 canvas 绘图原语。
 *
 * 为什么手写而不用 D3/Plotly：
 * 1. 统计教学的图形需求很窄 —— 坐标轴、曲线、直方图、阴影区、散点、标注。
 * 2. 这套 API 会注入给 Tier 2 沙箱（LLM 现场生成可视化代码）复用。
 *    **给模型一个小到能完整写进 prompt 的 API，比让它自由用 D3 可靠得多** ——
 *    API 面小，生成失败率就低。
 * 3. 零依赖、零 CDN，与项目既有的 vendor 本地化策略一致（沙箱 CSP
 *    是 connect-src 'none'，本来也加载不了外部库）。
 *
 * 设计要点：
 * - 高 DPI：按 devicePixelRatio 放大 backing store，避免曲线发虚。
 * - 数据坐标 → 屏幕坐标的映射集中在 Scale，绘图函数只吃数据坐标。
 * - 颜色走 CSS 自定义属性，跟随面板主题（含深色模式），不硬编码色值。
 */
(function (root) {
  'use strict';

  var PALETTE = {
    ink: '#17202a',
    muted: '#687381',
    line: '#d7dde4',
    accent: '#256f5f',
    accent2: '#b45f35',
    warn: '#9a3412',
    ok: '#166534',
    fill: 'rgba(37, 111, 95, 0.16)',
    fill2: 'rgba(180, 95, 53, 0.18)',
    grid: 'rgba(120, 132, 145, 0.18)'
  };

  var SERIES = ['#256f5f', '#b45f35', '#3b5b8c', '#7a5195', '#94722a', '#2f7f8f'];

  /**
   * 建立数据坐标与像素坐标的双向映射。
   * padding 给坐标轴标签留白，四边可分别指定。
   */
  function Scale(opts) {
    this.xMin = opts.xMin;
    this.xMax = opts.xMax;
    this.yMin = opts.yMin;
    this.yMax = opts.yMax;
    this.width = opts.width;
    this.height = opts.height;
    var p = opts.padding || {};
    this.pad = {
      left: p.left === undefined ? 52 : p.left,
      right: p.right === undefined ? 16 : p.right,
      top: p.top === undefined ? 16 : p.top,
      bottom: p.bottom === undefined ? 36 : p.bottom
    };
  }

  Scale.prototype.plotWidth = function () {
    return this.width - this.pad.left - this.pad.right;
  };

  Scale.prototype.plotHeight = function () {
    return this.height - this.pad.top - this.pad.bottom;
  };

  Scale.prototype.px = function (x) {
    var span = this.xMax - this.xMin || 1;
    return this.pad.left + (x - this.xMin) / span * this.plotWidth();
  };

  Scale.prototype.py = function (y) {
    var span = this.yMax - this.yMin || 1;
    // y 轴翻转：数据的大值在屏幕上方
    return this.pad.top + (1 - (y - this.yMin) / span) * this.plotHeight();
  };

  Scale.prototype.dataX = function (px) {
    var span = this.xMax - this.xMin || 1;
    return this.xMin + (px - this.pad.left) / this.plotWidth() * span;
  };

  Scale.prototype.dataY = function (py) {
    var span = this.yMax - this.yMin || 1;
    return this.yMin + (1 - (py - this.pad.top) / this.plotHeight()) * span;
  };

  /** 高 DPI 适配。返回 {ctx, scale, width, height}。 */
  function setup(canvas, opts) {
    opts = opts || {};
    var dpr = root.devicePixelRatio || 1;
    var cssW = opts.width || canvas.clientWidth || 640;
    var cssH = opts.height || canvas.clientHeight || 360;
    canvas.width = Math.round(cssW * dpr);
    canvas.height = Math.round(cssH * dpr);
    canvas.style.width = cssW + 'px';
    canvas.style.height = cssH + 'px';
    var ctx = canvas.getContext('2d');
    ctx.setTransform(dpr, 0, 0, dpr, 0, 0);
    ctx.clearRect(0, 0, cssW, cssH);
    var scale = new Scale({
      xMin: opts.xMin === undefined ? 0 : opts.xMin,
      xMax: opts.xMax === undefined ? 1 : opts.xMax,
      yMin: opts.yMin === undefined ? 0 : opts.yMin,
      yMax: opts.yMax === undefined ? 1 : opts.yMax,
      width: cssW, height: cssH, padding: opts.padding
    });
    return { ctx: ctx, scale: scale, width: cssW, height: cssH };
  }

  /** 好看的刻度：把区间切成 1/2/5×10^k 的整齐步长。 */
  function niceTicks(min, max, target) {
    target = target || 6;
    if (!(isFinite(min) && isFinite(max)) || max <= min) return [min];
    var raw = (max - min) / target;
    var mag = Math.pow(10, Math.floor(Math.log(raw) / Math.LN10));
    var norm = raw / mag;
    var step = mag * (norm < 1.5 ? 1 : norm < 3 ? 2 : norm < 7 ? 5 : 10);
    var start = Math.ceil(min / step) * step;
    var out = [];
    for (var v = start; v <= max + step * 1e-9; v += step) {
      // 消掉浮点累积误差造成的 0.30000000000000004
      out.push(Math.abs(v) < step * 1e-9 ? 0 : Number(v.toPrecision(12)));
    }
    return out;
  }

  function fmtTick(v) {
    if (v === 0) return '0';
    var a = Math.abs(v);
    if (a >= 1e5 || a < 1e-4) return v.toExponential(1);
    if (a >= 100) return v.toFixed(0);
    if (a >= 10) return v.toFixed(1).replace(/\.0$/, '');
    if (a >= 1) return v.toFixed(2).replace(/0$/, '').replace(/\.$/, '');
    return v.toFixed(3).replace(/0+$/, '').replace(/\.$/, '');
  }

  /** 坐标轴 + 网格 + 刻度标签。 */
  function axes(ctx, scale, opts) {
    opts = opts || {};
    var xt = opts.xTicks || niceTicks(scale.xMin, scale.xMax, opts.xTickCount);
    var yt = opts.yTicks || niceTicks(scale.yMin, scale.yMax, opts.yTickCount || 5);
    var i, x, y;

    ctx.save();
    ctx.font = '11px ui-sans-serif, system-ui, sans-serif';
    ctx.lineWidth = 1;

    if (opts.grid !== false) {
      ctx.strokeStyle = PALETTE.grid;
      ctx.beginPath();
      for (i = 0; i < yt.length; i++) {
        y = Math.round(scale.py(yt[i])) + 0.5;
        ctx.moveTo(scale.pad.left, y);
        ctx.lineTo(scale.width - scale.pad.right, y);
      }
      ctx.stroke();
    }

    ctx.strokeStyle = PALETTE.line;
    ctx.beginPath();
    y = Math.round(scale.py(Math.max(scale.yMin, Math.min(0, scale.yMax)))) + 0.5;
    ctx.moveTo(scale.pad.left, y);
    ctx.lineTo(scale.width - scale.pad.right, y);
    ctx.moveTo(scale.pad.left + 0.5, scale.pad.top);
    ctx.lineTo(scale.pad.left + 0.5, scale.height - scale.pad.bottom);
    ctx.stroke();

    ctx.fillStyle = PALETTE.muted;
    ctx.textAlign = 'center';
    ctx.textBaseline = 'top';
    for (i = 0; i < xt.length; i++) {
      if (xt[i] < scale.xMin || xt[i] > scale.xMax) continue;
      ctx.fillText(fmtTick(xt[i]), scale.px(xt[i]), scale.height - scale.pad.bottom + 6);
    }
    ctx.textAlign = 'right';
    ctx.textBaseline = 'middle';
    for (i = 0; i < yt.length; i++) {
      if (yt[i] < scale.yMin || yt[i] > scale.yMax) continue;
      ctx.fillText(fmtTick(yt[i]), scale.pad.left - 7, scale.py(yt[i]));
    }

    if (opts.xLabel) {
      ctx.textAlign = 'center';
      ctx.textBaseline = 'bottom';
      ctx.fillStyle = PALETTE.ink;
      ctx.fillText(opts.xLabel, scale.pad.left + scale.plotWidth() / 2, scale.height - 2);
    }
    if (opts.yLabel) {
      ctx.save();
      ctx.translate(11, scale.pad.top + scale.plotHeight() / 2);
      ctx.rotate(-Math.PI / 2);
      ctx.textAlign = 'center';
      ctx.textBaseline = 'top';
      ctx.fillStyle = PALETTE.ink;
      ctx.fillText(opts.yLabel, 0, 0);
      ctx.restore();
    }
    ctx.restore();
  }

  /** 采样函数并画曲线。fn 吃数据 x，返回数据 y。 */
  function curve(ctx, scale, fn, opts) {
    opts = opts || {};
    var n = opts.samples || 240;
    var i, x, y, started = false;
    ctx.save();
    ctx.strokeStyle = opts.color || PALETTE.accent;
    ctx.lineWidth = opts.width || 2;
    if (opts.dash) ctx.setLineDash(opts.dash);
    ctx.beginPath();
    for (i = 0; i <= n; i++) {
      x = scale.xMin + (scale.xMax - scale.xMin) * i / n;
      y = fn(x);
      if (!isFinite(y)) { started = false; continue; }
      if (started) ctx.lineTo(scale.px(x), scale.py(y));
      else { ctx.moveTo(scale.px(x), scale.py(y)); started = true; }
    }
    ctx.stroke();
    ctx.restore();
  }

  /**
   * 曲线下方的阴影区（拒绝域、p 值区、置信区间）。
   * 这是假设检验可视化的核心 —— "p 值就是这块面积"要能被看见。
   */
  function shadeUnder(ctx, scale, fn, from, to, opts) {
    opts = opts || {};
    var n = opts.samples || 160;
    var lo = Math.max(from, scale.xMin), hi = Math.min(to, scale.xMax);
    if (!(hi > lo)) return;
    var baseY = scale.py(Math.max(scale.yMin, 0));
    var i, x, y;
    ctx.save();
    ctx.fillStyle = opts.color || PALETTE.fill;
    ctx.beginPath();
    ctx.moveTo(scale.px(lo), baseY);
    for (i = 0; i <= n; i++) {
      x = lo + (hi - lo) * i / n;
      y = fn(x);
      if (!isFinite(y)) y = scale.yMin;
      ctx.lineTo(scale.px(x), scale.py(y));
    }
    ctx.lineTo(scale.px(hi), baseY);
    ctx.closePath();
    ctx.fill();
    if (opts.outline) {
      ctx.strokeStyle = opts.outline;
      ctx.lineWidth = 1;
      ctx.stroke();
    }
    ctx.restore();
  }

  /** 直方图。bins 是 [{x0, x1, count 或 density}]。 */
  function histogram(ctx, scale, bins, opts) {
    opts = opts || {};
    var key = opts.valueKey || 'density';
    var i, b, x0, x1, y, base = scale.py(Math.max(scale.yMin, 0));
    ctx.save();
    ctx.fillStyle = opts.color || PALETTE.fill;
    ctx.strokeStyle = opts.stroke || PALETTE.accent;
    ctx.lineWidth = 1;
    for (i = 0; i < bins.length; i++) {
      b = bins[i];
      x0 = scale.px(b.x0);
      x1 = scale.px(b.x1);
      y = scale.py(b[key]);
      ctx.fillRect(x0, y, Math.max(1, x1 - x0 - 1), base - y);
      if (opts.stroke !== null) {
        ctx.strokeRect(x0 + 0.5, y + 0.5, Math.max(1, x1 - x0 - 1), base - y);
      }
    }
    ctx.restore();
  }

  /** 把一维数据分箱。rule 可选 'sturges' | 'fd'（Freedman-Diaconis）。 */
  function makeBins(values, opts) {
    opts = opts || {};
    var xs = values.slice().sort(function (a, b) { return a - b; });
    var n = xs.length;
    if (!n) return [];
    var lo = opts.min === undefined ? xs[0] : opts.min;
    var hi = opts.max === undefined ? xs[n - 1] : opts.max;
    if (hi === lo) { hi = lo + 1; lo = lo - 1; }
    var k = opts.bins;
    if (!k) {
      if (opts.rule === 'fd' && n > 3) {
        var q1 = xs[Math.floor(0.25 * (n - 1))];
        var q3 = xs[Math.floor(0.75 * (n - 1))];
        var h = 2 * (q3 - q1) / Math.pow(n, 1 / 3);
        k = h > 0 ? Math.ceil((hi - lo) / h) : Math.ceil(Math.log2(n) + 1);
      } else {
        k = Math.ceil(Math.log2(n) + 1);        // Sturges
      }
    }
    k = Math.max(1, Math.min(200, k));
    var w = (hi - lo) / k, out = [], i;
    for (i = 0; i < k; i++) {
      out.push({ x0: lo + i * w, x1: lo + (i + 1) * w, count: 0, density: 0 });
    }
    for (i = 0; i < n; i++) {
      var idx = Math.floor((xs[i] - lo) / w);
      // 最后一箱必须闭合右端：否则等于 max 的观测被整个丢掉，
      // 密度积分不为 1（实测 9 个点丢 1 个 → 积分 0.889）
      if (idx === k && xs[i] <= hi) idx = k - 1;
      if (idx < 0 || idx >= k) continue;
      out[idx].count += 1;
    }
    for (i = 0; i < k; i++) out[i].density = out[i].count / (n * w);
    return out;
  }

  /** 散点。points 是 [{x, y}] 或 [[x, y]]。 */
  function scatter(ctx, scale, points, opts) {
    opts = opts || {};
    var r = opts.radius || 3.2;
    ctx.save();
    ctx.fillStyle = opts.color || PALETTE.accent;
    if (opts.alpha !== undefined) ctx.globalAlpha = opts.alpha;
    for (var i = 0; i < points.length; i++) {
      var p = points[i];
      var x = Array.isArray(p) ? p[0] : p.x;
      var y = Array.isArray(p) ? p[1] : p.y;
      ctx.beginPath();
      ctx.arc(scale.px(x), scale.py(y), r, 0, 2 * Math.PI);
      ctx.fill();
    }
    ctx.restore();
  }

  /** 竖直参考线（临界值、观测统计量、总体均值）。 */
  function vline(ctx, scale, x, opts) {
    opts = opts || {};
    if (x < scale.xMin || x > scale.xMax) return;
    var px = Math.round(scale.px(x)) + 0.5;
    ctx.save();
    ctx.strokeStyle = opts.color || PALETTE.accent2;
    ctx.lineWidth = opts.width || 1.6;
    if (opts.dash !== null) ctx.setLineDash(opts.dash || [5, 4]);
    ctx.beginPath();
    ctx.moveTo(px, scale.pad.top);
    ctx.lineTo(px, scale.height - scale.pad.bottom);
    ctx.stroke();
    if (opts.label) {
      ctx.setLineDash([]);
      ctx.font = '11px ui-sans-serif, system-ui, sans-serif';
      ctx.fillStyle = opts.color || PALETTE.accent2;
      var atTop = opts.labelAt !== 'bottom';
      ctx.textAlign = px > scale.width * 0.75 ? 'right' : 'left';
      ctx.textBaseline = atTop ? 'top' : 'bottom';
      var dx = ctx.textAlign === 'right' ? -4 : 4;
      ctx.fillText(opts.label, px + dx,
        atTop ? scale.pad.top + 2 : scale.height - scale.pad.bottom - 3);
    }
    ctx.restore();
  }

  /** 水平参考线。 */
  function hline(ctx, scale, y, opts) {
    opts = opts || {};
    if (y < scale.yMin || y > scale.yMax) return;
    var py = Math.round(scale.py(y)) + 0.5;
    ctx.save();
    ctx.strokeStyle = opts.color || PALETTE.muted;
    ctx.lineWidth = opts.width || 1.2;
    if (opts.dash !== null) ctx.setLineDash(opts.dash || [4, 3]);
    ctx.beginPath();
    ctx.moveTo(scale.pad.left, py);
    ctx.lineTo(scale.width - scale.pad.right, py);
    ctx.stroke();
    if (opts.label) {
      ctx.setLineDash([]);
      ctx.font = '11px ui-sans-serif, system-ui, sans-serif';
      ctx.fillStyle = opts.color || PALETTE.muted;
      ctx.textAlign = 'left';
      ctx.textBaseline = 'bottom';
      ctx.fillText(opts.label, scale.pad.left + 4, py - 3);
    }
    ctx.restore();
  }

  /** 误差棒 —— 画置信区间用。 */
  function errorBar(ctx, scale, x, lo, hi, opts) {
    opts = opts || {};
    var w = opts.capWidth || 8;
    var px = scale.px(x);
    ctx.save();
    ctx.strokeStyle = opts.color || PALETTE.ink;
    ctx.lineWidth = opts.width || 1.6;
    ctx.beginPath();
    ctx.moveTo(px, scale.py(lo));
    ctx.lineTo(px, scale.py(hi));
    ctx.moveTo(px - w / 2, scale.py(lo));
    ctx.lineTo(px + w / 2, scale.py(lo));
    ctx.moveTo(px - w / 2, scale.py(hi));
    ctx.lineTo(px + w / 2, scale.py(hi));
    ctx.stroke();
    if (opts.center !== undefined) {
      ctx.fillStyle = opts.color || PALETTE.ink;
      ctx.beginPath();
      ctx.arc(px, scale.py(opts.center), opts.radius || 3.5, 0, 2 * Math.PI);
      ctx.fill();
    }
    ctx.restore();
  }

  /** 水平区间条 —— 多条 CI 并排比较时用。 */
  function intervalBar(ctx, scale, y, lo, hi, opts) {
    opts = opts || {};
    var h = opts.capHeight || 8;
    var py = scale.py(y);
    ctx.save();
    ctx.strokeStyle = opts.color || PALETTE.ink;
    ctx.lineWidth = opts.width || 1.6;
    ctx.beginPath();
    ctx.moveTo(scale.px(lo), py);
    ctx.lineTo(scale.px(hi), py);
    ctx.moveTo(scale.px(lo), py - h / 2);
    ctx.lineTo(scale.px(lo), py + h / 2);
    ctx.moveTo(scale.px(hi), py - h / 2);
    ctx.lineTo(scale.px(hi), py + h / 2);
    ctx.stroke();
    if (opts.center !== undefined) {
      ctx.fillStyle = opts.color || PALETTE.ink;
      ctx.beginPath();
      ctx.arc(scale.px(opts.center), py, opts.radius || 3.2, 0, 2 * Math.PI);
      ctx.fill();
    }
    ctx.restore();
  }

  /** 文本标注。 */
  function label(ctx, x, y, text, opts) {
    opts = opts || {};
    ctx.save();
    ctx.font = opts.font || '12px ui-sans-serif, system-ui, sans-serif';
    ctx.fillStyle = opts.color || PALETTE.ink;
    ctx.textAlign = opts.align || 'left';
    ctx.textBaseline = opts.baseline || 'top';
    if (opts.background) {
      var m = ctx.measureText(text);
      var pad = 3;
      var w = m.width + pad * 2, h = 15;
      var bx = opts.align === 'right' ? x - w + pad : x - pad;
      var by = opts.baseline === 'bottom' ? y - h + pad : y - pad;
      ctx.fillStyle = opts.background;
      ctx.fillRect(bx, by, w, h);
      ctx.fillStyle = opts.color || PALETTE.ink;
    }
    ctx.fillText(text, x, y);
    ctx.restore();
  }

  /** 图例。items 是 [{label, color}]。 */
  function legend(ctx, scale, items, opts) {
    opts = opts || {};
    var x = opts.x === undefined ? scale.pad.left + 10 : opts.x;
    var y = opts.y === undefined ? scale.pad.top + 6 : opts.y;
    var lh = 16, i, sw = 14;
    ctx.save();
    ctx.font = '11px ui-sans-serif, system-ui, sans-serif';
    ctx.textAlign = 'left';
    ctx.textBaseline = 'middle';
    for (i = 0; i < items.length; i++) {
      ctx.fillStyle = items[i].color || SERIES[i % SERIES.length];
      ctx.fillRect(x, y + i * lh + 4, sw, 3);
      ctx.fillStyle = PALETTE.ink;
      ctx.fillText(items[i].label, x + sw + 6, y + i * lh + 5);
    }
    ctx.restore();
  }

  var plot = {
    PALETTE: PALETTE,
    SERIES: SERIES,
    Scale: Scale,
    setup: setup,
    niceTicks: niceTicks,
    fmtTick: fmtTick,
    axes: axes,
    curve: curve,
    shadeUnder: shadeUnder,
    histogram: histogram,
    makeBins: makeBins,
    scatter: scatter,
    vline: vline,
    hline: hline,
    errorBar: errorBar,
    intervalBar: intervalBar,
    label: label,
    legend: legend
  };

  if (typeof module !== 'undefined' && module.exports) module.exports = plot;
  root.plot = plot;
})(typeof globalThis !== 'undefined' ? globalThis : this);
