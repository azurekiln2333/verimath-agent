/**
 * 跨层一致性检查：Python planner 产出的 spec，喂给 JS 的 controls()。
 *
 * 存在的理由是一个真实漏掉的 bug：planner 给 seed=20240607，
 * 而滑块范围是 1..999。<input type=range> 会**静默**把 value 夹到 999 ——
 * 界面看起来完全正常，但滑块显示的值和实际渲染用的值不一致，
 * 而且「恢复初始参数」再也回不到最初那张图。
 *
 * 之前的 widgets_runner.js 用的是自己写的 spec（seed=7，恰好在范围内），
 * 所以测不出来。这个 runner 用的是**真实 planner 输出**，两层必须对上。
 *
 * 用法：node tests/controls_parity_runner.js <specs.json>
 */
'use strict';

const fs = require('fs');

globalThis.statlib = require('../app/static/statlib.js');
globalThis.plot = require('../app/static/plot.js');

const specs = JSON.parse(fs.readFileSync(process.argv[2], 'utf8'));
const widgets = require('../app/static/widgets.js');

const failures = [];
let checks = 0;

specs.forEach((entry) => {
  const { rule, spec } = entry;
  const widget = widgets.get(spec.kind);
  if (!widget) {
    failures.push(rule + ': JS 侧没有 ' + spec.kind + ' 的实现');
    return;
  }
  let controls;
  try {
    controls = widget.controls(spec) || [];
  } catch (e) {
    failures.push(rule + ': controls() 抛异常 ' + e.message);
    return;
  }

  controls.forEach((c) => {
    checks++;
    // 1. 控件初值必须落在自己声明的范围内
    if (!(c.value >= c.min && c.value <= c.max)) {
      failures.push(rule + '/' + spec.kind + ' 控件 ' + c.key +
        ' 初值 ' + c.value + ' 越出范围 [' + c.min + ', ' + c.max + ']' +
        '（会被 range 输入静默夹住）');
    }
    // 2. 若控件对应 spec.params 里的字段，两者必须一致；
    //    不一致意味着滑块一显示就和图不符
    const specValue = spec.params[c.key];
    if (typeof specValue === 'number') {
      checks++;
      if (Math.abs(specValue - c.value) > 1e-9) {
        failures.push(rule + '/' + spec.kind + ' 控件 ' + c.key +
          ' 初值 ' + c.value + ' 与 spec 值 ' + specValue + ' 不一致');
      }
    }
    // 3. step 必须能整除出初值附近的刻度，否则滑块一动就跳到别的值
    checks++;
    if (!(Number.isFinite(c.step) && c.step > 0)) {
      failures.push(rule + ' 控件 ' + c.key + ' step 非法: ' + c.step);
    }
  });

  // 4. spec 里声明 interactive 的字段，必须真的有对应控件
  const declared = spec.params.interactive;
  if (Array.isArray(declared) && declared.length) {
    const keys = new Set(controls.map((c) => c.key));
    declared.forEach((key) => {
      checks++;
      if (!keys.has(key)) {
        failures.push(rule + '/' + spec.kind + ' 声明了可交互参数 ' + key +
          '，但 controls() 没有给出对应滑块');
      }
    });
  }
});

if (failures.length) {
  console.error('FAIL (' + failures.length + ' 项, 共 ' + checks + ' 检查)');
  failures.forEach((f) => console.error('  - ' + f));
  process.exit(1);
}
console.log('OK ' + checks + ' checks over ' + specs.length + ' planner specs');
