/**
 * statlib.js 的加载冒烟测试：无 DOM、无 window 也必须可用。
 * 顺带核对几个人工可验证的锚点，快速发现"加载成功但算错"。
 */
'use strict';

const s = require('../app/static/statlib.js');

const failures = [];
function ok(cond, msg) { if (!cond) failures.push(msg); }
function close(a, b, msg, tol) {
  tol = tol === undefined ? 1e-10 : tol;
  if (!(Math.abs(a - b) <= tol * Math.max(1, Math.abs(b)))) {
    failures.push(msg + ' (got ' + a + ', want ' + b + ')');
  }
}

ok(typeof s.normCdf === 'function', '应导出 normCdf');
ok(typeof s.PCG32 === 'function', '应导出 PCG32');

// 人工可验证的锚点
close(s.normCdf(0), 0.5, 'normCdf(0)=0.5');
close(s.normPpf(0.5), 0, 'normPpf(0.5)=0', 1e-9);
close(s.erf(0), 0, 'erf(0)=0');
close(s.erfc(0), 1, 'erfc(0)=1');
close(s.lgamma(1), 0, 'lgamma(1)=0');
close(s.lgamma(5), Math.log(24), 'lgamma(5)=ln(4!)');
close(s.tCdf(0, 10), 0.5, 'tCdf(0)=0.5');
close(s.chi2Cdf(0, 3), 0, 'chi2Cdf(0)=0');
close(s.betainc(1, 1, 0.37), 0.37, 'I_x(1,1)=x');
close(s.binomCdf(10, 10, 0.5), 1, 'binomCdf(n,n,p)=1');

// 双侧 95% 临界值 ≈ 1.959964
close(s.normPpf(0.975), 1.959963984540054, 'z_{0.975}', 1e-9);

// d=0 时功效恰为 alpha
close(s.powerTwoSampleT(0, 200, 0.05).power, 0.05, 'd=0 → power=alpha', 1e-9);

// F(1,df) = t²
close(s.fCdf(4, 1, 10), 2 * s.tCdf(2, 10) - 1, 'F(1,df)=t²');

// 同种子同序列
const a = new s.PCG32(42, 54), b = new s.PCG32(42, 54);
for (let i = 0; i < 50; i++) {
  if (a.random() !== b.random()) { failures.push('同种子序列不一致'); break; }
}

if (failures.length) {
  console.error('FAIL');
  failures.forEach((f) => console.error('  - ' + f));
  process.exit(1);
}
console.log('OK statlib smoke');
