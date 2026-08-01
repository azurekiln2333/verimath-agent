/**
 * statlib.js —— app/stats/ 的 JavaScript 镜像。
 *
 * 契约：与 Python 侧**逐函数同算法**，同输入必出同输出（parity 测试断言
 * 1e-12）。任何一侧改算法，另一侧必须同步改，否则 tests/test_statlib_parity
 * 会红。
 *
 * 与 Python 的唯一实质差异：erf/erfc/lgamma。Python 用 stdlib（libm），
 * JS 没有，所以这里自己实现：
 *   - erf/erfc  用 Cody 有理逼近（|ε| ~ 1e-16）
 *   - lgamma    用 Lanczos g=7, n=9 系数（|ε| ~ 1e-15）
 * 两者精度都接近机器 epsilon，parity 容差 1e-12 有充足余量。
 *
 * 无模块系统依赖：同时挂 window.statlib 和 module.exports，
 * 浏览器与 Node（parity 测试用）都能直接吃。
 */
(function (root) {
  'use strict';

  var SQRT2 = Math.SQRT2;
  var SQRT2PI = Math.sqrt(2 * Math.PI);
  var EPS = 3.0e-16;
  var FPMIN = 1.0e-300;
  var MAXIT = 300;

  // ------------------------------------------------------------ lgamma
  // Lanczos 逼近。g=7，9 项系数。
  var LANCZOS = [
    0.99999999999980993, 676.5203681218851, -1259.1392167224028,
    771.32342877765313, -176.61502916214059, 12.507343278686905,
    -0.13857109526572012, 9.9843695780195716e-6, 1.5056327351493116e-7
  ];

  function lgamma(x) {
    if (x < 0.5) {
      // 反射公式：Γ(x)Γ(1-x) = π/sin(πx)
      return Math.log(Math.PI / Math.sin(Math.PI * x)) - lgamma(1 - x);
    }
    x -= 1;
    var a = LANCZOS[0];
    var t = x + 7.5;
    for (var i = 1; i < 9; i++) a += LANCZOS[i] / (x + i);
    return 0.5 * Math.log(2 * Math.PI) + (x + 0.5) * Math.log(t) - t + Math.log(a);
  }

  // -------------------------------------------------------------- erf/erfc
  // Cody 1969 有理逼近，三段：|x|<0.5、0.5<=|x|<4、|x|>=4。
  var ERF_A = [3.16112374387056560e0, 1.13864154151050156e2,
               3.77485237685302021e2, 3.20937758913846947e3,
               1.85777706184603153e-1];
  var ERF_B = [2.36012909523441209e1, 2.44024637934444173e2,
               1.28261652607737228e3, 2.84423683343917062e3];
  var ERF_C = [5.64188496988670089e-1, 8.88314979438837594e0,
               6.61191906371416295e1, 2.98635138197400131e2,
               8.81952221241769090e2, 1.71204761263407058e3,
               2.05107837782607147e3, 1.23033935479799725e3,
               2.15311535474403846e-8];
  var ERF_D = [1.57449261107098347e1, 1.17693950891312499e2,
               5.37181101862009858e2, 1.62138957456669019e3,
               3.29079923573345963e3, 4.36261909014324716e3,
               3.43936767414372164e3, 1.23033935480374942e3];
  var ERF_P = [3.05326634961232344e-1, 3.60344899949804439e-1,
               1.25781726111229246e-1, 1.60837851487422766e-2,
               6.58749161529837803e-4, 1.63153871373020978e-2];
  var ERF_Q = [2.56852019228982242e0, 1.87295284992346047e0,
               5.27905102951428412e-1, 6.05183413124413191e-2,
               2.33520497626869185e-3];
  var SQRPI = 5.6418958354775628695e-1;   // 1/sqrt(pi)

  function _calerf(x, jint) {
    var y = Math.abs(x), ysq, xnum, xden, result, i, del;
    if (y <= 0.46875) {
      ysq = y > 1.11e-16 ? y * y : 0.0;
      xnum = ERF_A[4] * ysq;
      xden = ysq;
      for (i = 0; i < 3; i++) {
        xnum = (xnum + ERF_A[i]) * ysq;
        xden = (xden + ERF_B[i]) * ysq;
      }
      result = x * (xnum + ERF_A[3]) / (xden + ERF_B[3]);
      if (jint !== 0) result = 1 - result;
      if (jint === 2) result *= Math.exp(ysq);
      return result;
    }
    if (y <= 4.0) {
      xnum = ERF_C[8] * y;
      xden = y;
      for (i = 0; i < 7; i++) {
        xnum = (xnum + ERF_C[i]) * y;
        xden = (xden + ERF_D[i]) * y;
      }
      result = (xnum + ERF_C[7]) / (xden + ERF_D[7]);
      if (jint !== 2) {
        ysq = Math.floor(y * 16) / 16;
        del = (y - ysq) * (y + ysq);
        result *= Math.exp(-ysq * ysq) * Math.exp(-del);
      }
    } else {
      if (y >= 26.543) {
        result = 0.0;
      } else {
        ysq = 1 / (y * y);
        xnum = ERF_P[5] * ysq;
        xden = ysq;
        for (i = 0; i < 4; i++) {
          xnum = (xnum + ERF_P[i]) * ysq;
          xden = (xden + ERF_Q[i]) * ysq;
        }
        result = ysq * (xnum + ERF_P[4]) / (xden + ERF_Q[4]);
        result = (SQRPI - result) / y;
        if (jint !== 2) {
          ysq = Math.floor(y * 16) / 16;
          del = (y - ysq) * (y + ysq);
          result *= Math.exp(-ysq * ysq) * Math.exp(-del);
        }
      }
    }
    if (jint === 0) {
      result = 1 - result;
      return x < 0 ? -result : result;
    }
    if (jint === 1) return x < 0 ? 2 - result : result;
    // jint === 2 (scaled erfc)
    if (x < 0) {
      ysq = Math.floor(y * 16) / 16;
      del = (y - ysq) * (y + ysq);
      result = 2 * Math.exp(ysq * ysq) * Math.exp(del) - result;
    }
    return result;
  }

  function erf(x) { return _calerf(x, 0); }
  function erfc(x) { return _calerf(x, 1); }

  // ------------------------------------------------- 不完全 beta / gamma
  // 与 app/stats/special.py 同算法：修正 Lentz 连分数。

  function logBeta(a, b) { return lgamma(a) + lgamma(b) - lgamma(a + b); }

  function _betacf(a, b, x) {
    var qab = a + b, qap = a + 1, qam = a - 1;
    var c = 1.0;
    var d = 1 - qab * x / qap;
    if (Math.abs(d) < FPMIN) d = FPMIN;
    d = 1 / d;
    var h = d, m, m2, aa, delta;
    for (m = 1; m <= MAXIT; m++) {
      m2 = 2 * m;
      aa = m * (b - m) * x / ((qam + m2) * (a + m2));
      d = 1 + aa * d;
      if (Math.abs(d) < FPMIN) d = FPMIN;
      c = 1 + aa / c;
      if (Math.abs(c) < FPMIN) c = FPMIN;
      d = 1 / d;
      h *= d * c;
      aa = -(a + m) * (qab + m) * x / ((a + m2) * (qap + m2));
      d = 1 + aa * d;
      if (Math.abs(d) < FPMIN) d = FPMIN;
      c = 1 + aa / c;
      if (Math.abs(c) < FPMIN) c = FPMIN;
      d = 1 / d;
      delta = d * c;
      h *= delta;
      if (Math.abs(delta - 1) < EPS) break;
    }
    return h;
  }

  function betainc(a, b, x) {
    if (x <= 0) return 0.0;
    if (x >= 1) return 1.0;
    if (a <= 0 || b <= 0) throw new Error('betainc 需要 a > 0 且 b > 0');
    var front = Math.exp(a * Math.log(x) + b * Math.log1p(-x) - logBeta(a, b));
    if (x < (a + 1) / (a + b + 2)) return front * _betacf(a, b, x) / a;
    return 1 - Math.exp(b * Math.log1p(-x) + a * Math.log(x) - logBeta(b, a)) *
      _betacf(b, a, 1 - x) / b;
  }

  function _gser(a, x) {
    var ap = a, total = 1 / a, delta = total;
    for (var i = 0; i < MAXIT; i++) {
      ap += 1;
      delta *= x / ap;
      total += delta;
      if (Math.abs(delta) < Math.abs(total) * EPS) break;
    }
    return total * Math.exp(-x + a * Math.log(x) - lgamma(a));
  }

  function _gcf(a, x) {
    var b = x + 1 - a, c = 1 / FPMIN, d = 1 / b, h = d, i, an, delta;
    for (i = 1; i <= MAXIT; i++) {
      an = -i * (i - a);
      b += 2;
      d = an * d + b;
      if (Math.abs(d) < FPMIN) d = FPMIN;
      c = b + an / c;
      if (Math.abs(c) < FPMIN) c = FPMIN;
      d = 1 / d;
      delta = d * c;
      h *= delta;
      if (Math.abs(delta - 1) < EPS) break;
    }
    return Math.exp(-x + a * Math.log(x) - lgamma(a)) * h;
  }

  function gammainc(a, x) {
    if (x < 0 || a <= 0) throw new Error('gammainc 需要 a > 0 且 x >= 0');
    if (x === 0) return 0.0;
    if (x < a + 1) return _gser(a, x);
    return 1 - _gcf(a, x);
  }

  function gammaincc(a, x) { return 1 - gammainc(a, x); }

  // ------------------------------------------------------------- 反演器
  // 收敛判据只靠浮点相邻性，不用绝对容差 —— 与 Python 侧一致，
  // 否则极端分位数（1e-12）会在到达真值前就判定收敛。

  function invertCdf(cdf, p, low, high, grow) {
    if (p <= 0) return low;
    if (p >= 1) return high;
    var i, mid;
    if (grow !== false) {
      for (i = 0; i < 200; i++) {
        if (cdf(high) >= p) break;
        high = high > 0 ? high * 2 : 1.0;
      }
      for (i = 0; i < 200; i++) {
        if (cdf(low) <= p) break;
        low = low < 0 ? low * 2 : -1.0;
      }
    }
    for (i = 0; i < 200; i++) {
      mid = 0.5 * (low + high);
      if (mid <= low || mid >= high) break;
      if (cdf(mid) < p) low = mid; else high = mid;
    }
    return 0.5 * (low + high);
  }

  function invertSf(sf, q, low, high, grow) {
    if (q <= 0) return high;
    if (q >= 1) return low;
    var i, mid;
    if (grow !== false) {
      for (i = 0; i < 200; i++) {
        if (sf(high) <= q) break;
        high = high > 0 ? high * 2 : 1.0;
      }
      for (i = 0; i < 200; i++) {
        if (sf(low) >= q) break;
        low = low < 0 ? low * 2 : -1.0;
      }
    }
    for (i = 0; i < 200; i++) {
      mid = 0.5 * (low + high);
      if (mid <= low || mid >= high) break;
      if (sf(mid) > q) low = mid; else high = mid;
    }
    return 0.5 * (low + high);
  }

  // ---------------------------------------------------------------- 正态

  function normPdf(x, mu, sigma) {
    mu = mu === undefined ? 0 : mu;
    sigma = sigma === undefined ? 1 : sigma;
    if (sigma <= 0) throw new Error('sigma 必须大于 0');
    var z = (x - mu) / sigma;
    return Math.exp(-0.5 * z * z) / (sigma * SQRT2PI);
  }

  function normCdf(x, mu, sigma) {
    mu = mu === undefined ? 0 : mu;
    sigma = sigma === undefined ? 1 : sigma;
    if (sigma <= 0) throw new Error('sigma 必须大于 0');
    return 0.5 * erfc(-(x - mu) / (sigma * SQRT2));
  }

  function normSf(x, mu, sigma) {
    mu = mu === undefined ? 0 : mu;
    sigma = sigma === undefined ? 1 : sigma;
    if (sigma <= 0) throw new Error('sigma 必须大于 0');
    return 0.5 * erfc((x - mu) / (sigma * SQRT2));
  }

  // Acklam 逆正态系数 + 一步 Halley 精化（与 Python 侧同）
  var AK_A = [-3.969683028665376e+01, 2.209460984245205e+02,
              -2.759285104469687e+02, 1.383577518672690e+02,
              -3.066479806614716e+01, 2.506628277459239e+00];
  var AK_B = [-5.447609879822406e+01, 1.615858368580409e+02,
              -1.556989798598866e+02, 6.680131188771972e+01,
              -1.328068155288572e+01];
  var AK_C = [-7.784894002430293e-03, -3.223964580411365e-01,
              -2.400758277161838e+00, -2.549732539343734e+00,
              4.374664141464968e+00, 2.938163982698783e+00];
  var AK_D = [7.784695709041462e-03, 3.224671290700398e-01,
              2.445134137142996e+00, 3.754408661907416e+00];

  function normPpf(p, mu, sigma) {
    mu = mu === undefined ? 0 : mu;
    sigma = sigma === undefined ? 1 : sigma;
    if (sigma <= 0) throw new Error('sigma 必须大于 0');
    if (p <= 0) return -Infinity;
    if (p >= 1) return Infinity;
    var q, r, x;
    if (p < 0.02425) {
      q = Math.sqrt(-2 * Math.log(p));
      x = (((((AK_C[0] * q + AK_C[1]) * q + AK_C[2]) * q + AK_C[3]) * q +
        AK_C[4]) * q + AK_C[5]) /
        ((((AK_D[0] * q + AK_D[1]) * q + AK_D[2]) * q + AK_D[3]) * q + 1);
    } else if (p <= 1 - 0.02425) {
      q = p - 0.5;
      r = q * q;
      x = (((((AK_A[0] * r + AK_A[1]) * r + AK_A[2]) * r + AK_A[3]) * r +
        AK_A[4]) * r + AK_A[5]) * q /
        (((((AK_B[0] * r + AK_B[1]) * r + AK_B[2]) * r + AK_B[3]) * r +
          AK_B[4]) * r + 1);
    } else {
      q = Math.sqrt(-2 * Math.log1p(-p));
      x = -(((((AK_C[0] * q + AK_C[1]) * q + AK_C[2]) * q + AK_C[3]) * q +
        AK_C[4]) * q + AK_C[5]) /
        ((((AK_D[0] * q + AK_D[1]) * q + AK_D[2]) * q + AK_D[3]) * q + 1);
    }
    var e = 0.5 * erfc(-x / SQRT2) - p;
    var u = e * SQRT2PI * Math.exp(0.5 * x * x);
    x = x - u / (1 + 0.5 * x * u);
    return mu + sigma * x;
  }

  // -------------------------------------------------------------- Student t

  function tPdf(x, df) {
    if (df <= 0) throw new Error('df 必须大于 0');
    var half = 0.5 * (df + 1);
    var logC = lgamma(half) - lgamma(0.5 * df) - 0.5 * Math.log(df * Math.PI);
    return Math.exp(logC - half * Math.log(1 + x * x / df));
  }

  // 分支点取 |x|=1，与 Python 侧完全一致（理由见 distributions.py 的注释：
  // 判据要看结果落在哪，不是看自变量；x²<df 会在 df 大时误入中心区并抵消）
  function tCdf(x, df) {
    if (df <= 0) throw new Error('df 必须大于 0');
    if (x === 0) return 0.5;
    if (Math.abs(x) < 1) {
      var half = 0.5 * betainc(0.5, 0.5 * df, x * x / (df + x * x));
      return x > 0 ? 0.5 + half : 0.5 - half;
    }
    var tail = 0.5 * betainc(0.5 * df, 0.5, df / (df + x * x));
    return x > 0 ? 1 - tail : tail;
  }

  function tSf(x, df) { return tCdf(-x, df); }

  function tPpf(p, df) {
    if (p <= 0) return -Infinity;
    if (p >= 1) return Infinity;
    if (p === 0.5) return 0.0;
    if (p > 0.5) return -tPpf(1 - p, df);
    return invertCdf(function (v) { return tCdf(v, df); }, p, -1, 0, true);
  }

  // ------------------------------------------------------------------ 卡方

  function chi2Pdf(x, df) {
    if (df <= 0) throw new Error('df 必须大于 0');
    if (x < 0) return 0.0;
    if (x === 0) return df > 2 ? 0.0 : (df < 2 ? Infinity : 0.5);
    var k = 0.5 * df;
    return Math.exp((k - 1) * Math.log(x) - 0.5 * x - k * Math.LN2 - lgamma(k));
  }

  function chi2Cdf(x, df) {
    if (df <= 0) throw new Error('df 必须大于 0');
    if (x <= 0) return 0.0;
    return gammainc(0.5 * df, 0.5 * x);
  }

  function chi2Sf(x, df) {
    if (x <= 0) return 1.0;
    return gammaincc(0.5 * df, 0.5 * x);
  }

  function chi2Ppf(p, df) {
    if (p <= 0) return 0.0;
    if (p >= 1) return Infinity;
    if (p > 0.5) {
      return invertSf(function (v) { return chi2Sf(v, df); }, 1 - p,
        0, Math.max(1, df), true);
    }
    return invertCdf(function (v) { return chi2Cdf(v, df); }, p,
      0, Math.max(1, df), true);
  }

  // --------------------------------------------------------------------- F

  function fPdf(x, dfn, dfd) {
    if (dfn <= 0 || dfd <= 0) throw new Error('dfn 与 dfd 必须大于 0');
    if (x < 0) return 0.0;
    if (x === 0) return dfn > 2 ? 0.0 : (dfn < 2 ? Infinity : 1.0);
    var a = 0.5 * dfn, b = 0.5 * dfd;
    var logP = a * Math.log(dfn) + b * Math.log(dfd) + (a - 1) * Math.log(x) -
      (a + b) * Math.log(dfd + dfn * x) - logBeta(a, b);
    return Math.exp(logP);
  }

  function fCdf(x, dfn, dfd) {
    if (dfn <= 0 || dfd <= 0) throw new Error('dfn 与 dfd 必须大于 0');
    if (x <= 0) return 0.0;
    return betainc(0.5 * dfn, 0.5 * dfd, dfn * x / (dfn * x + dfd));
  }

  function fSf(x, dfn, dfd) {
    if (x <= 0) return 1.0;
    return betainc(0.5 * dfd, 0.5 * dfn, dfd / (dfn * x + dfd));
  }

  function fPpf(p, dfn, dfd) {
    if (p <= 0) return 0.0;
    if (p >= 1) return Infinity;
    if (p > 0.5) {
      return invertSf(function (v) { return fSf(v, dfn, dfd); }, 1 - p, 0, 2, true);
    }
    return invertCdf(function (v) { return fCdf(v, dfn, dfd); }, p, 0, 2, true);
  }

  // ------------------------------------------------------------------ Beta

  function betaPdf(x, a, b) {
    if (a <= 0 || b <= 0) throw new Error('a 与 b 必须大于 0');
    if (x < 0 || x > 1) return 0.0;
    if (x === 0 || x === 1) {
      var edge = (x === 0 && a < 1) || (x === 1 && b < 1);
      if (edge) return Infinity;
      return (a === 1 && b === 1) ? 1.0 : 0.0;
    }
    return Math.exp((a - 1) * Math.log(x) + (b - 1) * Math.log(1 - x) - logBeta(a, b));
  }

  function betaCdf(x, a, b) { return betainc(a, b, x); }

  function betaSf(x, a, b) { return betainc(b, a, 1 - x); }

  function betaPpf(p, a, b) {
    if (p <= 0) return 0.0;
    if (p >= 1) return 1.0;
    if (p > 0.5) {
      return invertSf(function (v) { return betaSf(v, a, b); }, 1 - p, 0, 1, false);
    }
    return invertCdf(function (v) { return betaCdf(v, a, b); }, p, 0, 1, false);
  }

  // ------------------------------------------------------------------ 指数

  function exponPdf(x, scale) {
    scale = scale === undefined ? 1 : scale;
    if (scale <= 0) throw new Error('scale 必须大于 0');
    if (x < 0) return 0.0;
    return Math.exp(-x / scale) / scale;
  }

  function exponCdf(x, scale) {
    scale = scale === undefined ? 1 : scale;
    if (scale <= 0) throw new Error('scale 必须大于 0');
    if (x <= 0) return 0.0;
    return -Math.expm1(-x / scale);
  }

  function exponPpf(p, scale) {
    scale = scale === undefined ? 1 : scale;
    if (p <= 0) return 0.0;
    if (p >= 1) return Infinity;
    return -scale * Math.log1p(-p);
  }

  // ------------------------------------------------------- 二项 / 泊松

  function binomPmf(k, n, p) {
    if (n < 0 || p < 0 || p > 1) throw new Error('需要 n >= 0 且 0 <= p <= 1');
    if (k < 0 || k > n) return 0.0;
    if (p === 0) return k === 0 ? 1.0 : 0.0;
    if (p === 1) return k === n ? 1.0 : 0.0;
    var logC = lgamma(n + 1) - lgamma(k + 1) - lgamma(n - k + 1);
    return Math.exp(logC + k * Math.log(p) + (n - k) * Math.log(1 - p));
  }

  function binomCdf(k, n, p) {
    if (k < 0) return 0.0;
    if (k >= n) return 1.0;
    return betainc(n - k, k + 1, 1 - p);
  }

  function poissonPmf(k, lam) {
    if (lam < 0) throw new Error('lam 必须 >= 0');
    if (k < 0) return 0.0;
    if (lam === 0) return k === 0 ? 1.0 : 0.0;
    return Math.exp(k * Math.log(lam) - lam - lgamma(k + 1));
  }

  function poissonCdf(k, lam) {
    if (k < 0) return 0.0;
    if (lam === 0) return 1.0;
    return gammaincc(k + 1, lam);
  }

  // ------------------------------------------------------- PCG32 可复现 RNG
  //
  // 用 BigInt 做 64 位状态运算。JS 的 Number 是 53 位有效位，装不下
  // 64 位乘法的精确结果，用 Number 会静默丢位、与 Python 侧对不上。
  // BigInt 慢一些，但 60fps 拖动滑块时每帧只取几百个数，实测无感。

  var MASK64 = (1n << 64n) - 1n;
  var MASK32 = (1n << 32n) - 1n;
  var PCG_MULT = 6364136223846793005n;
  var PCG_INC = 1442695040888963407n;

  function PCG32(seed, stream) {
    seed = seed === undefined ? 42 : seed;
    stream = stream === undefined ? 54 : stream;
    this.inc = ((BigInt(stream) << 1n) | 1n) & MASK64;
    this.state = 0n;
    this._nextUint32();
    this.state = (this.state + (BigInt(seed) & MASK64)) & MASK64;
    this._nextUint32();
    this._spare = null;
  }

  PCG32.prototype._nextUint32 = function () {
    var old = this.state;
    this.state = (old * PCG_MULT + this.inc) & MASK64;
    var xorshifted = (((old >> 18n) ^ old) >> 27n) & MASK32;
    var rot = (old >> 59n) & 31n;
    var res = ((xorshifted >> rot) | (xorshifted << ((-rot) & 31n))) & MASK32;
    return Number(res);
  };

  PCG32.prototype.random = function () {
    // 27 位 + 26 位拼成 53 位，与 Python 侧同构造
    var hi = this._nextUint32() >>> 5;
    var lo = this._nextUint32() >>> 6;
    return (hi * 67108864.0 + lo) / 9007199254740992.0;
  };

  PCG32.prototype.uniform = function (low, high) {
    low = low === undefined ? 0 : low;
    high = high === undefined ? 1 : high;
    return low + (high - low) * this.random();
  };

  PCG32.prototype.randint = function (low, high) {
    var span = high - low + 1;
    if (span <= 0) throw new Error('high 必须 >= low');
    var m32 = 4294967295;
    var limit = m32 - (m32 % span);
    for (;;) {
      var v = this._nextUint32();
      if (v <= limit) return low + (v % span);
    }
  };

  PCG32.prototype.normal = function (mu, sigma) {
    mu = mu === undefined ? 0 : mu;
    sigma = sigma === undefined ? 1 : sigma;
    if (this._spare !== null) {
      var z = this._spare;
      this._spare = null;
      return mu + sigma * z;
    }
    var u1;
    do { u1 = this.random(); } while (u1 <= 0);
    var u2 = this.random();
    var r = Math.sqrt(-2 * Math.log(u1));
    this._spare = r * Math.sin(2 * Math.PI * u2);
    return mu + sigma * r * Math.cos(2 * Math.PI * u2);
  };

  PCG32.prototype.exponential = function (scale) {
    scale = scale === undefined ? 1 : scale;
    for (;;) {
      var u = this.random();
      if (u > 0) return -scale * Math.log(u);
    }
  };

  PCG32.prototype.bernoulli = function (p) {
    return this.random() < (p === undefined ? 0.5 : p) ? 1 : 0;
  };

  PCG32.prototype.binomial = function (n, p) {
    var s = 0;
    for (var i = 0; i < n; i++) s += this.bernoulli(p);
    return s;
  };

  PCG32.prototype.poisson = function (lam) {
    if (lam <= 0) return 0;
    if (lam > 30) return Math.max(0, Math.round(this.normal(lam, Math.sqrt(lam))));
    var target = Math.exp(-lam), k = 0, prod = this.random();
    while (prod > target) { k += 1; prod *= this.random(); }
    return k;
  };

  PCG32.prototype.choice = function (items) {
    if (!items || !items.length) throw new Error('items 不能为空');
    return items[this.randint(0, items.length - 1)];
  };

  PCG32.prototype.sampleFrom = function (population, size) {
    var out = [];
    for (var i = 0; i < size; i++) out.push(this.choice(population));
    return out;
  };

  PCG32.prototype.shuffled = function (items) {
    var out = items.slice(), i, j, tmp;
    for (i = out.length - 1; i > 0; i--) {
      j = this.randint(0, i);
      tmp = out[i]; out[i] = out[j]; out[j] = tmp;
    }
    return out;
  };

  // -------------------------------------------------------- 描述统计与检验

  function mean(xs) {
    if (!xs.length) throw new Error('样本不能为空');
    var s = 0;
    for (var i = 0; i < xs.length; i++) s += xs[i];
    return s / xs.length;
  }

  function variance(xs, ddof) {
    ddof = ddof === undefined ? 1 : ddof;
    var n = xs.length;
    if (n - ddof <= 0) throw new Error('样本量不足以估计方差');
    var m = mean(xs), s = 0;
    for (var i = 0; i < n; i++) s += (xs[i] - m) * (xs[i] - m);
    return s / (n - ddof);
  }

  function stdev(xs, ddof) { return Math.sqrt(variance(xs, ddof)); }

  function pFromT(t, df, alternative) {
    if (alternative === 'greater') return 1 - tCdf(t, df);
    if (alternative === 'less') return tCdf(t, df);
    if (alternative && alternative !== 'two-sided') {
      throw new Error('alternative 只能是 two-sided / greater / less');
    }
    var c = tCdf(t, df);
    return 2 * Math.min(c, 1 - c);
  }

  function welchT(a, b, alternative, ciLevel) {
    alternative = alternative || 'two-sided';
    ciLevel = ciLevel === undefined ? 0.95 : ciLevel;
    var n1 = a.length, n2 = b.length;
    if (n1 < 2 || n2 < 2) throw new Error('两组样本量都必须 >= 2');
    var m1 = mean(a), m2 = mean(b), v1 = variance(a), v2 = variance(b);
    var se = Math.sqrt(v1 / n1 + v2 / n2);
    if (se === 0) throw new Error('两组方差都为 0，无法做 t 检验');
    var diff = m1 - m2, t = diff / se;
    var num = Math.pow(v1 / n1 + v2 / n2, 2);
    var den = Math.pow(v1 / n1, 2) / (n1 - 1) + Math.pow(v2 / n2, 2) / (n2 - 1);
    var df = num / den;
    var crit = tPpf(1 - (1 - ciLevel) / 2, df);
    return {
      name: 'Welch t 检验',
      statistic: t,
      p_value: pFromT(t, df, alternative),
      df: df,
      ci: [diff - crit * se, diff + crit * se],
      ci_level: ciLevel,
      effect_size: diff / Math.sqrt((v1 + v2) / 2),
      effect_name: "Cohen's d",
      estimate: diff,
      alternative: alternative,
      detail: { n1: n1, n2: n2, mean1: m1, mean2: m2, var1: v1, var2: v2, se: se }
    };
  }

  function oneSampleT(xs, mu0, alternative, ciLevel) {
    mu0 = mu0 === undefined ? 0 : mu0;
    alternative = alternative || 'two-sided';
    ciLevel = ciLevel === undefined ? 0.95 : ciLevel;
    var n = xs.length;
    if (n < 2) throw new Error('样本量必须 >= 2');
    var m = mean(xs), s = stdev(xs);
    if (s === 0) throw new Error('样本方差为 0，无法做 t 检验');
    var se = s / Math.sqrt(n), df = n - 1, t = (m - mu0) / se;
    var crit = tPpf(1 - (1 - ciLevel) / 2, df);
    return {
      name: '单样本 t 检验',
      statistic: t,
      p_value: pFromT(t, df, alternative),
      df: df,
      ci: [m - crit * se, m + crit * se],
      ci_level: ciLevel,
      effect_size: (m - mu0) / s,
      effect_name: "Cohen's d",
      estimate: m,
      alternative: alternative,
      detail: { n: n, mean: m, sd: s, se: se, mu0: mu0, mean_minus_mu0: m - mu0 }
    };
  }

  function anovaOneway(groups) {
    var k = groups.length, i, j;
    if (k < 2) throw new Error('至少需要 2 组');
    var nTotal = 0, sumAll = 0;
    for (i = 0; i < k; i++) {
      if (groups[i].length < 2) throw new Error('每组样本量都必须 >= 2');
      nTotal += groups[i].length;
      for (j = 0; j < groups[i].length; j++) sumAll += groups[i][j];
    }
    var grand = sumAll / nTotal, ssB = 0, ssW = 0, gm;
    for (i = 0; i < k; i++) {
      gm = mean(groups[i]);
      ssB += groups[i].length * (gm - grand) * (gm - grand);
      for (j = 0; j < groups[i].length; j++) ssW += Math.pow(groups[i][j] - gm, 2);
    }
    var dfB = k - 1, dfW = nTotal - k;
    if (dfW <= 0) throw new Error('组内自由度不足');
    var msB = ssB / dfB, msW = ssW / dfW;
    if (msW === 0) throw new Error('组内方差为 0，无法做 F 检验');
    var f = msB / msW, ssT = ssB + ssW;
    var eta2 = ssT > 0 ? ssB / ssT : 0;
    var omega2 = (ssT + msW) > 0 ? (ssB - dfB * msW) / (ssT + msW) : 0;
    var meansOut = [];
    for (i = 0; i < k; i++) meansOut.push(mean(groups[i]));
    return {
      name: '单因素 ANOVA',
      statistic: f,
      p_value: fSf(f, dfB, dfW),
      df: dfB,
      ci: null,
      effect_size: omega2,
      effect_name: 'omega²（偏差校正）',
      alternative: 'greater',
      detail: {
        k: k, n_total: nTotal, df_between: dfB, df_within: dfW,
        ms_between: msB, ms_within: msW, eta_squared: eta2,
        omega_squared: omega2, group_means: meansOut
      }
    };
  }

  function pearson(x, y, alternative, ciLevel) {
    alternative = alternative || 'two-sided';
    ciLevel = ciLevel === undefined ? 0.95 : ciLevel;
    var n = x.length;
    if (n !== y.length) throw new Error('两列长度必须相同');
    if (n < 3) throw new Error('样本量必须 >= 3');
    var mx = mean(x), my = mean(y), sxy = 0, sxx = 0, syy = 0, i;
    for (i = 0; i < n; i++) {
      sxy += (x[i] - mx) * (y[i] - my);
      sxx += (x[i] - mx) * (x[i] - mx);
      syy += (y[i] - my) * (y[i] - my);
    }
    if (sxx === 0 || syy === 0) throw new Error('有一列是常数，相关系数无定义');
    var r = Math.max(-1, Math.min(1, sxy / Math.sqrt(sxx * syy)));
    var df = n - 2, t, p, ci;
    if (Math.abs(r) >= 1) {
      t = r > 0 ? Infinity : -Infinity; p = 0.0; ci = [r, r];
    } else {
      t = r * Math.sqrt(df / (1 - r * r));
      p = pFromT(t, df, alternative);
      var z = Math.atanh(r);
      var seZ = n > 3 ? 1 / Math.sqrt(n - 3) : Infinity;
      var crit = normPpf(1 - (1 - ciLevel) / 2);
      ci = isFinite(seZ)
        ? [Math.tanh(z - crit * seZ), Math.tanh(z + crit * seZ)]
        : [-1, 1];
    }
    return {
      name: 'Pearson 相关',
      statistic: t, p_value: p, df: df, ci: ci, ci_level: ciLevel,
      effect_size: r * r, effect_name: 'R²（决定系数）',
      estimate: r, alternative: alternative,
      detail: { n: n, r: r, mean_x: mx, mean_y: my }
    };
  }

  // ------------------------------------------------------------ 功效与样本量
  // 非中心 t 近似成平移 t（不是平移正态），使 d=0 时功效恰等于 α。

  function powerTwoSampleT(effectSize, nPerGroup, alpha, alternative) {
    alpha = alpha === undefined ? 0.05 : alpha;
    alternative = alternative || 'two-sided';
    if (nPerGroup < 2) throw new Error('每组样本量必须 >= 2');
    if (!(alpha > 0 && alpha < 1)) throw new Error('alpha 必须在 (0,1)');
    var df = 2 * nPerGroup - 2;
    var ncp = Math.abs(effectSize) * Math.sqrt(nPerGroup / 2);
    var crit, power;
    if (alternative === 'two-sided') {
      crit = tPpf(1 - alpha / 2, df);
      power = tSf(crit - ncp, df) + tCdf(-crit - ncp, df);
    } else if (alternative === 'greater' || alternative === 'less') {
      crit = tPpf(1 - alpha, df);
      power = tSf(crit - ncp, df);
    } else {
      throw new Error('alternative 只能是 two-sided / greater / less');
    }
    power = Math.min(1, Math.max(0, power));
    return {
      power: power, beta: 1 - power, alpha: alpha,
      effect_size: effectSize, n_per_group: nPerGroup,
      test: '两独立样本 t 检验', alternative: alternative,
      approximation: '非中心 t 用平移 t 近似'
    };
  }

  function sampleSizeTwoSampleT(effectSize, power, alpha, alternative, maxN) {
    power = power === undefined ? 0.8 : power;
    alpha = alpha === undefined ? 0.05 : alpha;
    alternative = alternative || 'two-sided';
    maxN = maxN === undefined ? 100000 : maxN;
    if (effectSize === 0) throw new Error('效应量为 0 时任何样本量都达不到功效');
    if (!(power > 0 && power < 1)) throw new Error('power 必须在 (0,1)');
    var zA = normPpf(1 - alpha / (alternative === 'two-sided' ? 2 : 1));
    var zB = normPpf(power);
    var n = Math.max(2, Math.ceil(2 * Math.pow(zA + zB, 2) / (effectSize * effectSize)));
    while (n <= maxN) {
      var got = powerTwoSampleT(effectSize, n, alpha, alternative);
      if (got.power >= power) return got;
      n += 1;
    }
    throw new Error('在 n <= ' + maxN + ' 内无法达到功效 ' + power);
  }

  function criticalRegionTwoSampleT(nPerGroup, alpha, alternative) {
    alpha = alpha === undefined ? 0.05 : alpha;
    alternative = alternative || 'two-sided';
    var df = 2 * nPerGroup - 2, crit;
    if (alternative === 'two-sided') {
      crit = tPpf(1 - alpha / 2, df);
      return { df: df, alpha: alpha, lower: -crit, upper: crit, alternative: alternative };
    }
    crit = tPpf(1 - alpha, df);
    if (alternative === 'greater') {
      return { df: df, alpha: alpha, lower: crit, upper: null, alternative: alternative };
    }
    return { df: df, alpha: alpha, lower: null, upper: -crit, alternative: alternative };
  }

  // ---------------------------------------------------------------- 导出

  var statlib = {
    erf: erf, erfc: erfc, lgamma: lgamma, logBeta: logBeta,
    betainc: betainc, gammainc: gammainc, gammaincc: gammaincc,
    invertCdf: invertCdf, invertSf: invertSf,
    normPdf: normPdf, normCdf: normCdf, normSf: normSf, normPpf: normPpf,
    tPdf: tPdf, tCdf: tCdf, tSf: tSf, tPpf: tPpf,
    chi2Pdf: chi2Pdf, chi2Cdf: chi2Cdf, chi2Sf: chi2Sf, chi2Ppf: chi2Ppf,
    fPdf: fPdf, fCdf: fCdf, fSf: fSf, fPpf: fPpf,
    betaPdf: betaPdf, betaCdf: betaCdf, betaSf: betaSf, betaPpf: betaPpf,
    exponPdf: exponPdf, exponCdf: exponCdf, exponPpf: exponPpf,
    binomPmf: binomPmf, binomCdf: binomCdf,
    poissonPmf: poissonPmf, poissonCdf: poissonCdf,
    PCG32: PCG32,
    mean: mean, variance: variance, stdev: stdev,
    welchT: welchT, oneSampleT: oneSampleT, anovaOneway: anovaOneway,
    pearson: pearson,
    powerTwoSampleT: powerTwoSampleT,
    sampleSizeTwoSampleT: sampleSizeTwoSampleT,
    criticalRegionTwoSampleT: criticalRegionTwoSampleT
  };

  if (typeof module !== 'undefined' && module.exports) module.exports = statlib;
  root.statlib = statlib;
})(typeof globalThis !== 'undefined' ? globalThis : this);
