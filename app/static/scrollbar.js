// 面板启动时量一次真实滚动条宽度，写进 --sbw。
// 不同浏览器/缩放下滚动条宽度不同（Windows Chrome 常为 10-17px），
// 写死数字会让右侧始终差几个像素——这就是"对话列与输入框对不齐"的最后一点。
(function () {
  function measure() {
    var probe = document.createElement('div');
    probe.style.cssText =
      'position:absolute;top:-9999px;left:-9999px;width:100px;height:100px;overflow:scroll;';
    document.body.appendChild(probe);
    var w = probe.offsetWidth - probe.clientWidth;
    probe.remove();
    if (w > 0) document.documentElement.style.setProperty('--sbw', w + 'px');
  }
  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', measure);
  } else {
    measure();
  }
  window.addEventListener('resize', measure);
})();
