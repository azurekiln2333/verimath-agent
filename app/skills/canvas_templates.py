"""canvas_templates：预制统计教学 HTML 可视化模板（skills/库）。

每个模板是一个返回完整 HTML 文档的函数：自包含、内联 CSS/JS、SVG 绘图、
无外部库（与 canvas_builder 规范一致），可在沙箱 iframe 中安全渲染。

用途：
1. 模型生成（canvas_builder.build）时，把命中的模板 HTML 作为「参考实现示例」
   塞进 system prompt，引导模型生成同风格、同交互模式的组件（脚手架）。
2. 模型生成失败（解析为空 / 清洗后为空 / 异常）时，直接用模板 HTML 兜底，
   保证「该有的可视化不丢」——参见 canvas_builder.build 的 fallback 分支。

设计约束：
- 720px 宽容器，高度自适应（300-420px）。背景透明，文字 #1b1c19，主色 #2d5a27。
- 必须可交互：滑块/选择器改变参数即时重绘。边界值不报错。
- 数学公式用纯文本/SVG，不依赖 KaTeX/MathJax（iframe 内没有这些库）。
"""
from __future__ import annotations

import re
from typing import Callable

# ============================================================
# 共享 CSS / JS（注入每个模板）
# ============================================================
_BASE_CSS = r"""
*{box-sizing:border-box}
body{margin:0;font-family:'Inter',system-ui,-apple-system,sans-serif;color:#1b1c19;background:transparent}
.card{width:720px;max-width:100%;padding:14px 16px;margin:0 auto}
h3{margin:0 0 4px;font-size:16px;color:#2d5a27;font-family:'Libre Caslon Text',Georgia,serif;font-weight:600}
.desc{font-size:12px;color:#42493e;margin:0 0 10px;line-height:1.55}
.controls{display:flex;flex-wrap:wrap;gap:16px;margin-bottom:8px;align-items:flex-end}
.ctrl{display:flex;flex-direction:column;gap:2px;font-size:11px;color:#42493e;font-family:'JetBrains Mono',ui-monospace,Consolas,monospace}
.ctrl b{color:#2d5a27;font-weight:600}
input[type=range]{width:150px;accent-color:#2d5a27;cursor:pointer;margin-top:2px}
select{font-family:inherit;font-size:11px;border:1px solid #c2c9bb;border-radius:4px;padding:2px 4px;background:#fff;color:#1b1c19}
.readout{font-size:11px;color:#2d5a27;font-family:'JetBrains Mono',monospace;background:#eef4ea;border:1px solid #c2c9bb;border-radius:4px;padding:2px 8px;font-weight:600}
svg{display:block;width:100%;height:auto;background:#fff;border:1px solid #e3e3de;border-radius:6px}
.legend{display:flex;gap:14px;font-size:11px;color:#42493e;margin-top:7px;flex-wrap:wrap}
.legend span{display:inline-flex;align-items:center;gap:5px}
.swatch{width:14px;height:3px;border-radius:2px;display:inline-block}
.note{font-size:11px;color:#42493e;margin-top:8px;font-family:'JetBrains Mono',monospace;line-height:1.6}
.decision{font-size:12px;font-weight:600;padding:3px 9px;border-radius:4px;display:inline-block;margin-top:6px}
.decision.reject{background:#fdecec;color:#ba1a1a;border:1px solid #edc4a7}
.decision.accept{background:#eef4ea;color:#2d5a27;border:1px solid #bdedaa}
"""

_JS_HELPERS = r"""
function logGamma(x){var g=7,c=[0.99999999999980993,676.5203681218851,-1259.1392167224028,771.32342877765313,-176.61502916214059,12.507343278686905,-0.13857109526572012,9.9843695780195716e-6,1.5056327351493116e-7];if(x<0.5)return Math.log(Math.PI/Math.sin(Math.PI*x))-logGamma(1-x);x-=1;var a=c[0],t=x+g+0.5;for(var i=1;i<g+2;i++)a+=c[i]/(x+i);return 0.5*Math.log(2*Math.PI*t)+(x+0.5)*Math.log(t)-t+Math.log(a);}
function betaPdf(x,a,b){if(x<=0||x>=1)return 0;return Math.exp((a-1)*Math.log(x)+(b-1)*Math.log(1-x)-logGamma(a)-logGamma(b)+logGamma(a+b));}
function normPdf(x,mu,sd){if(sd<=0)return 0;var z=(x-mu)/sd;return Math.exp(-0.5*z*z)/(sd*2.5066282746310002);}
function normCdf(z){var t=1/(1+0.2316419*Math.abs(z)),d=0.3989423*Math.exp(-z*z/2),p=d*t*(0.3193815+t*(-0.3565638+t*(1.781478+t*(-1.821256+t*1.330274))));return z>0?1-p:p;}
function normInv(p){if(p<=0)return -10;if(p>=1)return 10;var a=[-39.969683028665376,220.9460984245205,-275.9285104469687,138.3577518672690,-30.66479806614716,2.506628277459239],b=[-54.47609879822406,161.5858368580409,-155.6989798598866,66.80131188771972,-13.28068155288572],c=[-0.007784894002430293,-0.3223964580411365,-2.400758277161838,-2.549732539343734,4.374664141464968,2.938163982698783],d=[0.007784695709041462,0.3224671290700398,2.445134137142996,3.754408661907416],plow=0.02425,phigh=1-plow,q,r;if(p<plow){q=Math.sqrt(-2*Math.log(p));return (((((c[0]*q+c[1])*q+c[2])*q+c[3])*q+c[4])*q+c[5])/((((d[0]*q+d[1])*q+d[2])*q+d[3])*q+1);}if(p<=phigh){q=p-0.5;r=q*q;return (((((a[0]*r+a[1])*r+a[2])*r+a[3])*r+a[4])*r+a[5])*q/(((((b[0]*r+b[1])*r+b[2])*r+b[3])*r+b[4])*r+1);}q=Math.sqrt(-2*Math.log(1-p));return -(((((c[0]*q+c[1])*q+c[2])*q+c[3])*q+c[4])*q+c[5])/((((d[0]*q+d[1])*q+d[2])*q+d[3])*q+1);}
function lcg(seed){var s=seed>>>0;return function(){s=(s*1664525+1013904223)>>>0;return s/4294967296;};}
function randn(rng){var u=rng(),v=rng();return Math.sqrt(-2*Math.log(u+1e-12))*Math.cos(2*Math.PI*v);}
function el(id){return document.getElementById(id);}
function val(id){return +document.getElementById(id).value;}
"""


def _html_doc(title: str, body: str, js: str) -> str:
    """组装完整 HTML 文档（内联 CSS/JS）。"""
    return (
        "<!doctype html><html lang=\"zh-CN\"><head><meta charset=\"utf-8\"/>"
        "<meta name=\"viewport\" content=\"width=device-width,initial-scale=1\"/>"
        "<title>" + title + "</title><style>" + _BASE_CSS + "</style></head>"
        "<body><div class=\"card\">" + body + "</div>"
        "<script>" + _JS_HELPERS + js + "</script></body></html>"
    )


# ============================================================
# 模板 1：中心极限定理演示
# ============================================================
def clt_demo(query: str = "") -> str:
    body = (
        "<h3>中心极限定理演示</h3>"
        "<p class=\"desc\">总体为均匀分布 U(0,1)（虚线）。"
        "拖动 n 观察样本均值 X̄ 的分布（实线）如何趋近正态 N(μ, σ²/n)，"
        "同时方差随 1/√n 缩小、峰值升高。</p>"
        "<div class=\"controls\">"
        "<div class=\"ctrl\">样本量 n"
        "<input type=\"range\" id=\"n\" min=\"1\" max=\"30\" step=\"1\" value=\"2\">"
        "<b id=\"nv\">2</b></div>"
        "</div>"
        "<svg id=\"plt\" viewBox=\"0 0 680 300\" preserveAspectRatio=\"xMidYMid meet\"></svg>"
        "<div class=\"legend\">"
        "<span><i class=\"swatch\" style=\"background:#8a8e85\"></i>总体 U(0,1)</span>"
        "<span><i class=\"swatch\" style=\"background:#2d5a27\"></i>样本均值分布</span>"
        "</div>"
        "<div class=\"note\" id=\"nt\"></div>"
    )
    js = r"""
function cltRedraw(){
  var n=val('n');el('nv').textContent=n;
  var W=680,H=300,L=50,R=640,T=30,B=270,xmin=0,xmax=1,ymax=8.2;
  function sx(x){return L+(x-xmin)/(xmax-xmin)*(R-L);}
  function sy(v){return B-(v)/ymax*(B-T);}
  var p=[];
  p.push('<line x1="'+L+'" y1="'+B+'" x2="'+R+'" y2="'+B+'" stroke="#c2c9bb"/>');
  p.push('<line x1="'+L+'" y1="'+T+'" x2="'+L+'" y2="'+B+'" stroke="#c2c9bb"/>');
  for(var i=0;i<=5;i++){var xv=i/5,px=sx(xv);p.push('<line x1="'+px+'" y1="'+B+'" x2="'+px+'" y2="'+(B+4)+'" stroke="#c2c9bb"/>');p.push('<text x="'+px+'" y="'+(B+16)+'" font-size="10" fill="#42493e" text-anchor="middle">'+xv.toFixed(1)+'</text>');}
  p.push('<line x1="'+sx(0)+'" y1="'+sy(1)+'" x2="'+sx(1)+'" y2="'+sy(1)+'" stroke="#8a8e85" stroke-width="2" stroke-dasharray="4 3"/>');
  var sd=1/Math.sqrt(12*n);
  var path='';
  for(var i=0;i<=200;i++){var xv=i/200;var pv=normPdf(xv,0.5,sd);path+=(i?'L':'M')+sx(xv).toFixed(1)+' '+sy(pv).toFixed(1)+' ';}
  p.push('<path d="'+path+'" fill="none" stroke="#2d5a27" stroke-width="2.2"/>');
  p.push('<line x1="'+sx(0.5)+'" y1="'+T+'" x2="'+sx(0.5)+'" y2="'+B+'" stroke="#3f6833" stroke-width="1" stroke-dasharray="2 3"/>');
  p.push('<text x="'+sx(0.5)+'" y="'+(T-8)+'" font-size="10" fill="#3f6833" text-anchor="middle">μ=0.5</text>');
  el('plt').innerHTML=p.join('');
  el('nt').textContent='σ_X̄ = 1/√(12n) = '+sd.toFixed(3)+'   峰值 ≈ '+normPdf(0.5,0.5,sd).toFixed(2)+'   （n 越大越窄越高）';
}
el('n').addEventListener('input',cltRedraw);cltRedraw();
"""
    return _html_doc("中心极限定理演示", body, js)


# ============================================================
# 模板 2：假设检验拒绝域
# ============================================================
def hypothesis_test(query: str = "") -> str:
    body = (
        "<h3>假设检验 · 拒绝域与 p 值</h3>"
        "<p class=\"desc\">双侧 Z 检验。调整显著性水平 α 与观测统计量 z，"
        "红色为拒绝域，蓝线为观测值。|z| 越过临界值则拒绝 H₀。</p>"
        "<div class=\"controls\">"
        "<div class=\"ctrl\">显著性 α"
        "<input type=\"range\" id=\"alpha\" min=\"0.001\" max=\"0.2\" step=\"0.001\" value=\"0.05\">"
        "<b id=\"av\">0.05</b></div>"
        "<div class=\"ctrl\">观测 z"
        "<input type=\"range\" id=\"z\" min=\"-4\" max=\"4\" step=\"0.05\" value=\"2.1\">"
        "<b id=\"zv\">2.10</b></div>"
        "</div>"
        "<svg id=\"plt\" viewBox=\"0 0 680 300\" preserveAspectRatio=\"xMidYMid meet\"></svg>"
        "<div class=\"legend\">"
        "<span><i class=\"swatch\" style=\"background:#ba1a1a\"></i>拒绝域</span>"
        "<span><i class=\"swatch\" style=\"background:#1b1c19\"></i>标准正态</span>"
        "<span><i class=\"swatch\" style=\"background:#2d5a27\"></i>观测 z</span>"
        "</div>"
        "<div class=\"note\" id=\"nt\"></div>"
    )
    js = r"""
function htRedraw(){
  var a=val('alpha'),z=val('z');
  el('av').textContent=a.toFixed(3);el('zv').textContent=z.toFixed(2);
  var L=50,R=640,T=30,B=270,xmin=-4,xmax=4,ymax=0.45;
  function sx(x){return L+(x-xmin)/(xmax-xmin)*(R-L);}
  function sy(v){return B-(v)/ymax*(B-T);}
  var zc=normInv(1-a/2);
  var p=[];
  p.push('<line x1="'+L+'" y1="'+B+'" x2="'+R+'" y2="'+B+'" stroke="#c2c9bb"/>');
  p.push('<line x1="'+L+'" y1="'+T+'" x2="'+L+'" y2="'+B+'" stroke="#c2c9bb"/>');
  function curve(xa,xb,stroke,fill){
    var path='M'+sx(xa).toFixed(1)+' '+sy(0).toFixed(1);
    for(var i=0;i<=120;i++){var t=i/120;var xv=xa+(xb-xa)*t;path+=' L'+sx(xv).toFixed(1)+' '+sy(normPdf(xv,0,1)).toFixed(1);}
    if(fill){path+=' L'+sx(xb).toFixed(1)+' '+sy(0).toFixed(1)+' Z';p.push('<path d="'+path+'" fill="'+fill+'" opacity="0.45"/>');}
    else p.push('<path d="'+path+'" fill="none" stroke="'+stroke+'" stroke-width="2"/>');
  }
  curve(-zc,0,null,'#ba1a1a');curve(0,zc,null,'#ba1a1a');
  curve(xmin,xmax,'#1b1c19',null);
  // critical lines
  p.push('<line x1="'+sx(-zc)+'" y1="'+T+'" x2="'+sx(-zc)+'" y2="'+B+'" stroke="#ba1a1a" stroke-width="1" stroke-dasharray="3 3"/>');
  p.push('<line x1="'+sx(zc)+'" y1="'+T+'" x2="'+sx(zc)+'" y2="'+B+'" stroke="#ba1a1a" stroke-width="1" stroke-dasharray="3 3"/>');
  p.push('<text x="'+sx(zc)+'" y="'+(T-6)+'" font-size="10" fill="#ba1a1a" text-anchor="middle">z='+zc.toFixed(2)+'</text>');
  // observed
  p.push('<line x1="'+sx(z)+'" y1="'+T+'" x2="'+sx(z)+'" y2="'+B+'" stroke="#2d5a27" stroke-width="2"/>');
  p.push('<text x="'+sx(z)+'" y="'+(T-6)+'" font-size="10" fill="#2d5a27" text-anchor="middle">z='+z.toFixed(2)+'</text>');
  el('plt').innerHTML=p.join('');
  var pv=2*(1-normCdf(Math.abs(z)));
  var reject=Math.abs(z)>=zc;
  el('nt').innerHTML='临界值 ±'+zc.toFixed(3)+'   p 值 = '+pv.toFixed(4)+'   '+(reject?'<span class="decision reject">拒绝 H₀</span>':'<span class="decision accept">不拒绝 H₀</span>');
}
el('alpha').addEventListener('input',htRedraw);el('z').addEventListener('input',htRedraw);htRedraw();
"""
    return _html_doc("假设检验拒绝域", body, js)


# ============================================================
# 模板 3：线性回归拟合
# ============================================================
def regression_line(query: str = "") -> str:
    body = (
        "<h3>线性回归 · 最小二乘拟合</h3>"
        "<p class=\"desc\">固定数据点（灰）。拖动斜率 b₁ 与截距 b₀ 调整直线，"
        "尝试最小化残差平方和 SSE。绿色虚线为 OLS 最优解。</p>"
        "<div class=\"controls\">"
        "<div class=\"ctrl\">斜率 b₁"
        "<input type=\"range\" id=\"b1\" min=\"-2\" max=\"4\" step=\"0.05\" value=\"0.8\">"
        "<b id=\"b1v\">0.80</b></div>"
        "<div class=\"ctrl\">截距 b₀"
        "<input type=\"range\" id=\"b0\" min=\"-5\" max=\"8\" step=\"0.1\" value=\"4\">"
        "<b id=\"b0v\">4.0</b></div>"
        "</div>"
        "<svg id=\"plt\" viewBox=\"0 0 680 300\" preserveAspectRatio=\"xMidYMid meet\"></svg>"
        "<div class=\"legend\">"
        "<span><i class=\"swatch\" style=\"background:#1b1c19\"></i>你的直线</span>"
        "<span><i class=\"swatch\" style=\"background:#2d5a27\"></i>OLS 最优</span>"
        "</div>"
        "<div class=\"note\" id=\"nt\"></div>"
    )
    js = r"""
var DATA=[[1,3],[2,5],[3,7],[4,6],[5,9],[6,11],[7,12],[8,14]];
function regRedraw(){
  var b1=val('b1'),b0=val('b0');
  el('b1v').textContent=b1.toFixed(2);el('b0v').textContent=b0.toFixed(1);
  var L=50,R=640,T=30,B=270,xmin=0,xmax=9,ymin=0,ymax=18;
  function sx(x){return L+(x-xmin)/(xmax-xmin)*(R-L);}
  function sy(y){return B-(y-ymin)/(ymax-ymin)*(B-T);}
  // OLS
  var n=DATA.length,mx=0,my=0;for(var i=0;i<n;i++){mx+=DATA[i][0];my+=DATA[i][1];}mx/=n;my/=n;
  var sxy=0,sxx=0;for(var i=0;i<n;i++){sxy+=(DATA[i][0]-mx)*(DATA[i][1]-my);sxx+=(DATA[i][0]-mx)*(DATA[i][0]-mx);}
  var ob1=sxy/sxx,ob0=my-ob1*mx;
  var p=[];
  p.push('<line x1="'+L+'" y1="'+B+'" x2="'+R+'" y2="'+B+'" stroke="#c2c9bb"/>');
  p.push('<line x1="'+L+'" y1="'+T+'" x2="'+L+'" y2="'+B+'" stroke="#c2c9bb"/>');
  // grid
  for(var y=0;y<=ymax;y+=3)p.push('<line x1="'+L+'" y1="'+sy(y)+'" x2="'+R+'" y2="'+sy(y)+'" stroke="#f0f0ec"/>');
  // user line
  p.push('<line x1="'+sx(xmin)+'" y1="'+sy(b0+b1*xmin)+'" x2="'+sx(xmax)+'" y2="'+sy(b0+b1*xmax)+'" stroke="#1b1c19" stroke-width="2"/>');
  // OLS line
  p.push('<line x1="'+sx(xmin)+'" y1="'+sy(ob0+ob1*xmin)+'" x2="'+sx(xmax)+'" y2="'+sy(ob0+ob1*xmax)+'" stroke="#2d5a27" stroke-width="2" stroke-dasharray="5 3"/>');
  // points + residuals
  var sse=0;
  for(var i=0;i<n;i++){
    var x=DATA[i][0],y=DATA[i][1],yh=b0+b1*x;
    sse+=(y-yh)*(y-yh);
    p.push('<line x1="'+sx(x)+'" y1="'+sy(y)+'" x2="'+sx(x)+'" y2="'+sy(yh)+'" stroke="#ba1a1a" stroke-width="1" opacity="0.5"/>');
    p.push('<circle cx="'+sx(x)+'" cy="'+sy(y)+'" r="4" fill="#42493e" stroke="#fff" stroke-width="1"/>');
  }
  var osse=0;for(var i=0;i<n;i++){var yh=ob0+ob1*DATA[i][0];osse+=(DATA[i][1]-yh)*(DATA[i][1]-yh);}
  el('plt').innerHTML=p.join('');
  el('nt').textContent='你的 SSE = '+sse.toFixed(2)+'   OLS 最优 SSE = '+osse.toFixed(2)+'   （b₁='+ob1.toFixed(2)+', b₀='+ob0.toFixed(2)+'）';
}
el('b1').addEventListener('input',regRedraw);el('b0').addEventListener('input',regRedraw);regRedraw();
"""
    return _html_doc("线性回归拟合", body, js)


# ============================================================
# 模板 4：贝叶斯先验→后验
# ============================================================
def bayesian_update(query: str = "") -> str:
    body = (
        "<h3>贝叶斯更新 · 先验 → 后验</h3>"
        "<p class=\"desc\">先验 Beta(a,b)，观测 s 次成功 / f 次失败。"
        "后验 Beta(a+s, b+f) = 先验 × 似然。拖动滑块观察后验如何被数据「拉向」似然。</p>"
        "<div class=\"controls\">"
        "<div class=\"ctrl\">先验 a"
        "<input type=\"range\" id=\"a\" min=\"0.5\" max=\"15\" step=\"0.5\" value=\"2\">"
        "<b id=\"av\">2</b></div>"
        "<div class=\"ctrl\">先验 b"
        "<input type=\"range\" id=\"b\" min=\"0.5\" max=\"15\" step=\"0.5\" value=\"2\">"
        "<b id=\"bv\">2</b></div>"
        "<div class=\"ctrl\">成功 s"
        "<input type=\"range\" id=\"s\" min=\"0\" max=\"20\" step=\"1\" value=\"7\">"
        "<b id=\"sv\">7</b></div>"
        "<div class=\"ctrl\">失败 f"
        "<input type=\"range\" id=\"f\" min=\"0\" max=\"20\" step=\"1\" value=\"3\">"
        "<b id=\"fv\">3</b></div>"
        "</div>"
        "<svg id=\"plt\" viewBox=\"0 0 680 300\" preserveAspectRatio=\"xMidYMid meet\"></svg>"
        "<div class=\"legend\">"
        "<span><i class=\"swatch\" style=\"background:#8a8e85\"></i>先验</span>"
        "<span><i class=\"swatch\" style=\"background:#ba1a1a\"></i>似然</span>"
        "<span><i class=\"swatch\" style=\"background:#2d5a27\"></i>后验</span>"
        "</div>"
        "<div class=\"note\" id=\"nt\"></div>"
    )
    js = r"""
function bayesRedraw(){
  var a=val('a'),b=val('b'),s=val('s'),f=val('f');
  el('av').textContent=a;el('bv').textContent=b;el('sv').textContent=s;el('fv').textContent=f;
  var L=50,R=640,T=30,B=270,xmin=0,xmax=1;
  // find max for scaling
  var mx=0;for(var i=1;i<200;i++){var x=i/200;mx=Math.max(mx,betaPdf(x,a,b),betaPdf(x,s+1,f+1),betaPdf(x,a+s,b+f));}
  if(mx<=0)mx=1;var ymax=mx*1.15;
  function sx(x){return L+(x-xmin)/(xmax-xmin)*(R-L);}
  function sy(v){return B-(v)/ymax*(B-T);}
  function curve(fn,stroke,fill){
    var path='M'+sx(0).toFixed(1)+' '+sy(fn(1e-4)).toFixed(1);
    for(var i=1;i<=200;i++){var x=i/201;path+=' L'+sx(x).toFixed(1)+' '+sy(fn(x)).toFixed(1);}
    if(fill){path+=' L'+sx(1).toFixed(1)+' '+sy(0).toFixed(1)+' L'+sx(0).toFixed(1)+' '+sy(0).toFixed(1)+' Z';p.push('<path d="'+path+'" fill="'+fill+'" opacity="0.15"/>');}
    var path2='M'+sx(0.005).toFixed(1)+' '+sy(fn(0.005)).toFixed(1);
    for(var i=2;i<=200;i++){var x=i/201;path2+=' L'+sx(x).toFixed(1)+' '+sy(fn(x)).toFixed(1);}
    p.push('<path d="'+path2+'" fill="none" stroke="'+stroke+'" stroke-width="2"/>');
  }
  var p=[];
  p.push('<line x1="'+L+'" y1="'+B+'" x2="'+R+'" y2="'+B+'" stroke="#c2c9bb"/>');
  p.push('<line x1="'+L+'" y1="'+T+'" x2="'+L+'" y2="'+B+'" stroke="#c2c9bb"/>');
  for(var i=0;i<=5;i++){var xv=i/5,px=sx(xv);p.push('<text x="'+px+'" y="'+(B+16)+'" font-size="10" fill="#42493e" text-anchor="middle">'+xv.toFixed(1)+'</text>');}
  curve(function(x){return betaPdf(x,a,b);},'#8a8e85','#8a8e85');
  curve(function(x){return betaPdf(x,s+1,f+1);},'#ba1a1a','#ba1a1a');
  curve(function(x){return betaPdf(x,a+s,b+f);},'#2d5a27','#2d5a27');
  el('plt').innerHTML=p.join('');
  var pm=(a+s)/(a+b+s+f);
  var lm=(s+1)/(s+f+2);
  el('nt').textContent='后验 Beta('+(a+s).toFixed(1)+', '+(b+f).toFixed(1)+')   后验均值 = '+pm.toFixed(3)+'   似然均值 = '+lm.toFixed(3);
}
el('a').addEventListener('input',bayesRedraw);el('b').addEventListener('input',bayesRedraw);el('s').addEventListener('input',bayesRedraw);el('f').addEventListener('input',bayesRedraw);bayesRedraw();
"""
    return _html_doc("贝叶斯更新", body, js)


# ============================================================
# 模板 5：置信区间覆盖率
# ============================================================
def confidence_interval(query: str = "") -> str:
    body = (
        "<h3>置信区间 · 覆盖率演示</h3>"
        "<p class=\"desc\">真实均值 μ=50，σ=10。每次抽取 n 个样本构造 "
        "(1-α) 置信区间。绿色覆盖 μ，红色未覆盖。调整 n 与置信水平观察覆盖率变化。</p>"
        "<div class=\"controls\">"
        "<div class=\"ctrl\">样本量 n"
        "<input type=\"range\" id=\"n\" min=\"5\" max=\"50\" step=\"1\" value=\"15\">"
        "<b id=\"nv\">15</b></div>"
        "<div class=\"ctrl\">置信水平"
        "<input type=\"range\" id=\"conf\" min=\"0.5\" max=\"0.99\" step=\"0.01\" value=\"0.95\">"
        "<b id=\"cv\">0.95</b></div>"
        "<div class=\"ctrl\"><input type=\"button\" id=\"resample\" value=\"重新抽样\" onclick=\"ciRedraw()\"></div>"
        "</div>"
        "<svg id=\"plt\" viewBox=\"0 0 680 320\" preserveAspectRatio=\"xMidYMid meet\"></svg>"
        "<div class=\"note\" id=\"nt\"></div>"
    )
    js = r"""
var MU=50,SD=10,N_CI=20;
function ciRedraw(){
  var n=val('n'),conf=val('conf');
  el('nv').textContent=n;el('cv').textContent=conf.toFixed(2);
  var zc=normInv(1-(1-conf)/2);
  var L=60,R=640,T=20,B=300,xmin=35,xmax=65;
  function sx(x){return L+(x-xmin)/(xmax-xmin)*(R-L);}
  var p=[];
  p.push('<line x1="'+L+'" y1="'+T+'" x2="'+L+'" y2="'+B+'" stroke="#c2c9bb"/>');
  // mu line
  p.push('<line x1="'+sx(MU)+'" y1="'+T+'" x2="'+sx(MU)+'" y2="'+B+'" stroke="#2d5a27" stroke-width="1.5" stroke-dasharray="4 2"/>');
  p.push('<text x="'+sx(MU)+'" y="'+(T-4)+'" font-size="10" fill="#2d5a27" text-anchor="middle">μ=50</text>');
  // x ticks
  for(var v=40;v<=60;v+=5){p.push('<text x="'+sx(v)+'" y="'+(B+14)+'" font-size="10" fill="#42493e" text-anchor="middle">'+v+'</text>');}
  var rng=lcg(20260801);
  var cover=0;
  for(var k=0;k<N_CI;k++){
    var sum=0;for(var i=0;i<n;i++){sum+=MU+SD*randn(rng);}
    var mean=sum/n;
    var hw=zc*SD/Math.sqrt(n);
    var lo=mean-hw,hi=mean+hw;
    var ok=(lo<=MU&&MU<=hi);if(ok)cover++;
    var y=T+10+k*((B-T-10)/N_CI);
    var col=ok?'#2d5a27':'#ba1a1a';
    p.push('<line x1="'+sx(lo).toFixed(1)+'" y1="'+y+'" x2="'+sx(hi).toFixed(1)+'" y2="'+y+'" stroke="'+col+'" stroke-width="2.5"/>');
    p.push('<circle cx="'+sx(mean).toFixed(1)+'" cy="'+y+'" r="2.5" fill="'+col+'"/>');
  }
  el('plt').innerHTML=p.join('');
  el('nt').textContent='覆盖 '+cover+'/'+N_CI+' = '+(cover/N_CI*100).toFixed(0)+'%   （名义 '+conf.toFixed(2)+'，半宽 ±'+(zc*SD/Math.sqrt(n)).toFixed(2)+'）';
}
el('n').addEventListener('input',ciRedraw);el('conf').addEventListener('input',ciRedraw);ciRedraw();
"""
    return _html_doc("置信区间覆盖率", body, js)


# ============================================================
# 模板 6：抽样分布
# ============================================================
def sampling_distribution(query: str = "") -> str:
    body = (
        "<h3>抽样分布 · 样本直方图趋近总体</h3>"
        "<p class=\"desc\">曲线为总体分布，柱状为一次抽样的经验直方图。"
        "随样本量 n 增大，直方图逐渐逼近总体形状。</p>"
        "<div class=\"controls\">"
        "<div class=\"ctrl\">样本量 n"
        "<input type=\"range\" id=\"n\" min=\"5\" max=\"400\" step=\"5\" value=\"30\">"
        "<b id=\"nv\">30</b></div>"
        "<div class=\"ctrl\">总体"
        "<select id=\"dist\"><option value=\"normal\">正态 N(0,1)</option><option value=\"exp\">指数 Exp(1)</option></select>"
        "</div>"
        "<div class=\"ctrl\"><input type=\"button\" value=\"重新抽样\" onclick=\"sdRedraw()\"></div>"
        "</div>"
        "<svg id=\"plt\" viewBox=\"0 0 680 300\" preserveAspectRatio=\"xMidYMid meet\"></svg>"
        "<div class=\"legend\">"
        "<span><i class=\"swatch\" style=\"background:#2d5a27\"></i>总体 PDF</span>"
        "<span><i class=\"swatch\" style=\"background:#3f6833;opacity:0.5\"></i>样本直方图</span>"
        "</div>"
        "<div class=\"note\" id=\"nt\"></div>"
    )
    js = r"""
function sdRedraw(){
  var n=val('n'),dist=document.getElementById('dist').value;
  el('nv').textContent=n;
  var L=50,R=640,T=30,B=270;
  var xmin=dist==='exp'?0:-4,xmax=dist==='exp'?6:4;
  function sx(x){return L+(x-xmin)/(xmax-xmin)*(R-L);}
  // population pdf
  var pdf=dist==='exp'?function(x){return x<0?0:Math.exp(-x);}:function(x){return normPdf(x,0,1);};
  var pm=0;for(var i=0;i<=200;i++){var x=xmin+(xmax-xmin)*i/200;pm=Math.max(pm,pdf(x));}
  var ymax=pm*1.25;
  function sy(v){return B-(v)/ymax*(B-T);}
  var rng=lcg(424242);
  var samples=[];
  for(var i=0;i<n;i++){if(dist==='exp'){var u=rng();samples.push(-Math.log(u+1e-12));}else{samples.push(randn(rng));}}
  // histogram
  var nbins=24,binw=(xmax-xmin)/nbins,counts=new Array(nbins).fill(0);
  for(var i=0;i<n;i++){var idx=Math.floor((samples[i]-xmin)/binw);if(idx<0)idx=0;if(idx>=nbins)idx=nbins-1;counts[idx]++;}
  var cmax=0;for(var i=0;i<nbins;i++)cmax=Math.max(cmax,counts[i]);
  // scale histogram to density: count/n/binw
  var p=[];
  p.push('<line x1="'+L+'" y1="'+B+'" x2="'+R+'" y2="'+B+'" stroke="#c2c9bb"/>');
  p.push('<line x1="'+L+'" y1="'+T+'" x2="'+L+'" y2="'+B+'" stroke="#c2c9bb"/>');
  var hdensMax=cmax/n/binw;
  // use max(pdf, hist density) for y scale
  var ym=Math.max(pm,hdensMax)*1.2;
  function sy2(v){return B-(v)/ym*(B-T);}
  // bars
  for(var i=0;i<nbins;i++){var x0=xmin+i*binw,dens=counts[i]/n/binw;p.push('<rect x="'+sx(x0).toFixed(1)+'" y="'+sy2(dens).toFixed(1)+'" width="'+(sx(binw)-sx(0)-1).toFixed(1)+'" height="'+(B-sy2(dens)).toFixed(1)+'" fill="#3f6833" opacity="0.45"/>');}
  // curve
  var path='';for(var i=0;i<=200;i++){var x=xmin+(xmax-xmin)*i/200;path+=(i?'L':'M')+sx(x).toFixed(1)+' '+sy2(pdf(x)).toFixed(1)+' ';}
  p.push('<path d="'+path+'" fill="none" stroke="#2d5a27" stroke-width="2.2"/>');
  el('plt').innerHTML=p.join('');
  var mean=0;for(var i=0;i<n;i++)mean+=samples[i];mean/=n;
  el('nt').textContent='n='+n+'   样本均值 = '+mean.toFixed(3)+'   总体均值 = '+(dist==='exp'?'1.000':'0.000');
}
el('n').addEventListener('input',sdRedraw);el('dist').addEventListener('change',sdRedraw);sdRedraw();
"""
    return _html_doc("抽样分布", body, js)


# ============================================================
# 注册表 & 匹配
# ============================================================
TEMPLATES: dict[str, Callable[..., str]] = {
    "clt_demo": clt_demo,
    "hypothesis_test": hypothesis_test,
    "regression_line": regression_line,
    "bayesian_update": bayesian_update,
    "confidence_interval": confidence_interval,
    "sampling_distribution": sampling_distribution,
}

TEMPLATE_META: dict[str, tuple[str, str]] = {
    "clt_demo": ("中心极限定理演示", "拖动 n 观察样本均值分布趋近正态、方差缩小"),
    "hypothesis_test": ("假设检验拒绝域", "调整 α 与观测 z，可视化拒绝域、临界值与 p 值"),
    "regression_line": ("线性回归拟合", "拖动斜率/截距，对比 OLS 最优解与残差平方和"),
    "bayesian_update": ("贝叶斯更新", "先验 Beta × 似然 = 后验，三曲线叠加对比"),
    "confidence_interval": ("置信区间覆盖率", "多次抽样可视化区间是否覆盖真实均值"),
    "sampling_distribution": ("抽样分布", "样本直方图随 n 增大趋近总体分布"),
}


def match_template(query: str) -> str | None:
    """根据查询关键词匹配最相关的模板 key。无匹配返回 None。

    匹配优先级：中心极限 > 假设检验 > 贝叶斯 > 置信区间 > 回归 > 抽样分布。
    （「抽样分布」单独出现时归 sampling_distribution，但「中心极限」优先。）
    """
    q = (query or "").lower()
    if not q.strip():
        return None
    if any(k in q for k in ["中心极限", "极限定理", "clt", "central limit", "样本均值分布", "大数定律", "大数"]):
        return "clt_demo"
    if any(k in q for k in ["假设检验", "拒绝域", "p值", "p-value", "p value", "显著性水平", "hypothesis", "rejection", "t检验", "z检验", "检验统计", "原假设"]):
        return "hypothesis_test"
    if any(k in q for k in ["贝叶斯", "先验", "后验", "似然函数", "bayes", "prior", "posterior", "bayesian"]):
        return "bayesian_update"
    if any(k in q for k in ["置信区间", "区间估计", "confidence interval", "覆盖率", "置信水平"]):
        return "confidence_interval"
    if any(k in q for k in ["线性回归", "回归", "最小二乘", "regression", "least square", "拟合直线", "ols", "残差"]):
        return "regression_line"
    if any(k in q for k in ["抽样分布", "sampling distribution", "样本量", "样本分布", "直方图"]):
        return "sampling_distribution"
    return None


def get_template_html(key: str, query: str = "") -> str | None:
    """返回模板 HTML，key 无效返回 None。"""
    fn = TEMPLATES.get(key)
    if fn is None:
        return None
    return fn(query)


def template_meta(key: str) -> tuple[str, str] | None:
    """返回 (title, caption)，key 无效返回 None。"""
    return TEMPLATE_META.get(key)


__all__ = [
    "TEMPLATES",
    "TEMPLATE_META",
    "match_template",
    "get_template_html",
    "template_meta",
]
