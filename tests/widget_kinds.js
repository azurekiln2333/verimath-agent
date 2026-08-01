/** 打印 JS 侧注册的 widget kind，供 pytest 与 Python 注册表比对。 */
'use strict';
globalThis.statlib = require('../app/static/statlib.js');
globalThis.plot = require('../app/static/plot.js');
process.stdout.write(require('../app/static/widgets.js').kinds().sort().join(','));
