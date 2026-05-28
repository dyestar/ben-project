# -*- coding: utf-8 -*-
A = '&'

fonts = ('https://fonts.googleapis.com/css2?'
    + 'family=Playfair+Display:ital,wght@0,400;0,500;0,600;0,700;0,800;0,900;1,400;1,700'
    + A + 'family=Source+Serif+4:ital,opsz,wght@0,8..60,300;0,8..60,400;0,8..60,500;0,8..60,600;1,8..60,400'
    + A + 'family=IBM+Plex+Mono:wght@300;400;500;600'
    + A + 'family=Noto+Serif+SC:wght@300;400;500;600;700;900'
    + A + 'family=Noto+Sans+SC:wght@300;400;500;700;900'
    + A + 'display=swap')

slides_path = r'C:\Users\Ben\Documents\Codex\2026-05-25\new-chat-4\_slides.txt'
out_path = r'C:\Users\Ben\Documents\Codex\2026-05-25\new-chat-4\商务礼仪培训.html'

with open(slides_path, 'r', encoding='utf-8') as sf:
    slides_content = sf.read()

CSS = r'''
:root{
    --ink:#0a0a0b;--ink-rgb:10,10,11;--paper:#f1efea;--paper-rgb:241,239,234;
    --paper-tint:#e8e5de;--ink-tint:#18181a;
    --mono:"IBM Plex Mono",ui-monospace,monospace;
    --serif-en:"Playfair Display","Source Serif 4",Georgia,serif;
    --serif-body-en:"Source Serif 4",Georgia,serif;
    --serif-zh:"Noto Serif SC",source-han-serif-sc,serif;
    --sans-zh:"Noto Sans SC",source-han-sans-sc,sans-serif;
}
*{box-sizing:border-box;margin:0;padding:0}
html,body{width:100%;height:100%;overflow:hidden;background:var(--ink);color:var(--paper);font-family:var(--sans-zh);-webkit-font-smoothing:antialiased;text-rendering:optimizeLegibility}
canvas.bg{position:fixed;inset:0;width:100vw;height:100vh;z-index:0;display:block;transition:opacity 1.2s ease}
canvas#bg-light{opacity:0}canvas#bg-dark{opacity:1}
body.light-bg canvas#bg-light{opacity:1}
body.light-bg canvas#bg-dark{opacity:0}
body.low-power canvas.bg{display:none!important}
#deck{position:fixed;inset:0;width:1500vw;height:100vh;display:flex;flex-wrap:nowrap;transition:transform .9s cubic-bezier(.77,0,.175,1);z-index:10;will-change:transform}
.slide{width:100vw;height:100vh;flex:0 0 100vw;position:relative;padding:6vh 6vw 10vh 6vw;display:flex;flex-direction:column;overflow:hidden}
.slide.light{color:var(--ink);background:var(--paper)}
.slide.dark{color:var(--paper);background:var(--ink)}
.slide::before{content:"";position:absolute;inset:0;z-index:-1;pointer-events:none;transition:background .7s ease}
.slide.light::before{background:rgba(var(--paper-rgb),.78);backdrop-filter:blur(3px)}
.slide.dark::before{background:rgba(var(--ink-rgb),.78);backdrop-filter:blur(3px)}
.slide.hero.light::before{background:rgba(var(--paper-rgb),.16);backdrop-filter:none}
.slide.hero.dark::before{background:rgba(var(--ink-rgb),.12);backdrop-filter:none}
.slide.hero::after{content:"";position:absolute;inset:0;z-index:-1;pointer-events:none}
.slide.hero.light::after{background:linear-gradient(180deg,rgba(var(--paper-rgb),.28) 0%,rgba(var(--paper-rgb),0) 14%,rgba(var(--paper-rgb),0) 86%,rgba(var(--paper-rgb),.28) 100%)}
.slide.hero.dark::after{background:linear-gradient(180deg,rgba(var(--ink-rgb),.32) 0%,rgba(var(--ink-rgb),0) 14%,rgba(var(--ink-rgb),0) 86%,rgba(var(--ink-rgb),.32) 100%)}
.chrome{display:flex;justify-content:space-between;align-items:flex-start;font-family:var(--mono);font-size:12px;letter-spacing:.18em;text-transform:uppercase;opacity:.7}
.chrome .left,.chrome .right{display:flex;gap:2.4em;align-items:center}
.chrome .sep{width:40px;height:1px;background:currentColor;opacity:.4}
.foot{margin-top:auto;display:flex;justify-content:space-between;align-items:flex-end;font-family:var(--mono);font-size:12px;letter-spacing:.14em;text-transform:uppercase;opacity:.55}
.foot .title{font-family:var(--serif-zh);font-weight:400;letter-spacing:.05em;text-transform:none;opacity:.75;font-size:13px}
.tag{display:inline-block;font-family:var(--mono);font-size:11px;letter-spacing:.24em;text-transform:uppercase;padding:6px 14px;border:1px solid currentColor;opacity:.85}
.rule{width:100%;height:1px;background:currentColor;opacity:.25;margin:3vh 0}
.h-hero{font-family:var(--serif-zh);font-weight:700;font-size:max(48px,5.8vw);line-height:1.08;letter-spacing:-.01em}
.h-xl{font-family:var(--serif-zh);font-weight:600;font-size:max(32px,3.6vw);line-height:1.15;letter-spacing:-.005em}
.h-sub{font-family:var(--serif-en);font-weight:400;font-style:italic;font-size:max(16px,1.4vw);line-height:1.4;opacity:.78}
.lead{font-family:var(--serif-body-en);font-size:max(16px,1.25vw);line-height:1.65;opacity:.82}
.kicker{font-family:var(--mono);font-size:11px;letter-spacing:.22em;text-transform:uppercase;opacity:.65}
.meta-row{display:flex;gap:3vw;align-items:center;font-family:var(--mono);font-size:12px;opacity:.6}
.grid-2{display:grid;grid-template-columns:1fr 1fr;gap:3vw 4vh;align-items:start}
.grid-3{display:grid;grid-template-columns:1fr 1fr 1fr;gap:3vw 4vh;align-items:start}
.grid-4{display:grid;grid-template-columns:1fr 1fr 1fr 1fr;gap:2.5vw 4vh;align-items:start}
.icon-card{display:flex;flex-direction:column;gap:1.8vh}
.icon-card i{opacity:.55;margin-bottom:.5vh}
.icon-card .card-title{font-family:var(--serif-zh);font-weight:600;font-size:max(16px,1.3vw);line-height:1.3}
.icon-card .card-desc{font-family:var(--sans-zh);font-size:max(13px,1.05vw);line-height:1.65;opacity:.72}
.char-card{border-left:3px solid currentColor;padding:2vh 2vw;display:flex;flex-direction:column;gap:.8vh}
.char-card .char-name{font-family:var(--serif-zh);font-weight:600;font-size:max(18px,1.5vw)}
.char-card .char-role{font-family:var(--mono);font-size:11px;letter-spacing:.18em;opacity:.6}
.char-card .char-desc{font-family:var(--sans-zh);font-size:max(13px,1vw);line-height:1.55;opacity:.7;margin-top:.5vh}
.etiquette-table{width:100%;border-collapse:collapse;font-family:var(--sans-zh);font-size:max(13px,1vw)}
.etiquette-table th{text-align:left;font-family:var(--mono);font-size:11px;letter-spacing:.16em;text-transform:uppercase;opacity:.55;padding:1.5vh 1vw;border-bottom:1px solid currentColor}
.etiquette-table td{padding:1.2vh 1vw;border-bottom:1px solid rgba(var(--ink-rgb),.12);line-height:1.5;opacity:.8}
.act-num{font-family:var(--serif-en);font-size:max(80px,9vw);line-height:1;opacity:.15;position:absolute;top:5vh;right:5vw}
blockquote.scene-quote{font-family:var(--serif-zh);font-size:max(18px,1.5vw);line-height:1.7;opacity:.78;border-left:2px solid currentColor;padding-left:2.5vw;margin-top:3vh;max-width:75%}
#nav{position:fixed;bottom:3.5vh;right:3vw;z-index:100;display:flex;gap:10px;align-items:center}
#nav button{width:32px;height:32px;border-radius:50%;border:1.5px solid rgba(var(--ink-rgb),.25);background:rgba(var(--paper-rgb),.7);cursor:pointer;display:flex;align-items:center;justify-content:center;transition:all .25s;color:var(--ink)}
#nav button:hover{background:var(--paper);border-color:rgba(var(--ink-rgb),.5)}
body.dark-bg #nav button{background:rgba(var(--ink-rgb),.7);color:var(--paper);border-color:rgba(var(--paper-rgb),.25)}
body.dark-bg #nav button:hover{background:var(--ink-tint);border-color:rgba(var(--paper-rgb),.5)}
#nav .dots{display:flex;gap:8px}
#nav .dots span{width:8px;height:8px;border-radius:50%;background:rgba(var(--ink-rgb),.2);transition:all .3s;cursor:pointer}
#nav .dots span.active{background:var(--ink);transform:scale(1.4)}
body.dark-bg #nav .dots span{background:rgba(var(--paper-rgb),.2)}
body.dark-bg #nav .dots span.active{background:var(--paper)}
.table-wrap{overflow:auto;max-height:55vh;margin-top:4vh}
.nb{font-family:var(--serif-en);font-weight:700;font-size:max(52px,5.5vw);line-height:1;letter-spacing:-.02em}
.nb-label{font-family:var(--mono);font-size:11px;letter-spacing:.16em;text-transform:uppercase;opacity:.6;margin-top:.8vh}
'''

# WebGL shader JS (inlined, no & in it)
WEBGL_JS = r'''<script>
const bgFrag=
precision highp float;
uniform vec2 u_resolution;
uniform float u_time;
uniform vec3 u_ink;
uniform vec3 u_paper;
void main(){
  vec2 uv=gl_FragCoord.xy/u_resolution.xy;
  float t=u_time*.15;
  float n=sin(uv.x*2.8+t)*cos(uv.y*2.3-t*.7)*.5+.5;
  n+=sin(uv.x*5.5-t*.4)*cos(uv.y*4.8+t*.3)*.3;
  n+=sin((uv.x+uv.y)*3.2+t*.6)*.2;
  n=n*.5+.25;
  vec3 col=mix(u_ink,u_paper,n*.35);
  col+=vec3(.02,.01,.03)*sin(uv.y*40.+t);
  gl_FragColor=vec4(col,1.);
};
function createBG(id,ink,paper){
  const c=document.getElementById(id);
  if(!c)return;
  const gl=c.getContext('webgl')||c.getContext('experimental-webgl');
  if(!gl)return;
  const vs=gl.createShader(gl.VERTEX_SHADER);
  gl.shaderSource(vs,'attribute vec2 p;void main(){gl_Position=vec4(p,0,1);}');
  gl.compileShader(vs);
  const fs=gl.createShader(gl.FRAGMENT_SHADER);
  gl.shaderSource(fs,bgFrag);
  gl.compileShader(fs);
  const prog=gl.createProgram();
  gl.attachShader(prog,vs);gl.attachShader(prog,fs);
  gl.linkProgram(prog);gl.useProgram(prog);
  const buf=gl.createBuffer();
  gl.bindBuffer(gl.ARRAY_BUFFER,buf);
  gl.bufferData(gl.ARRAY_BUFFER,new Float32Array([-1,-1,1,-1,-1,1,1,1]),gl.STATIC_DRAW);
  const pLoc=gl.getAttribLocation(prog,'p');
  gl.enableVertexAttribArray(pLoc);
  gl.vertexAttribPointer(pLoc,2,gl.FLOAT,false,0,0);
  const uRes=gl.getUniformLocation(prog,'u_resolution');
  const uTime=gl.getUniformLocation(prog,'u_time');
  const uInk=gl.getUniformLocation(prog,'u_ink');
  const uPaper=gl.getUniformLocation(prog,'u_paper');
  function render(t){
    gl.uniform2f(uRes,c.width,c.height);
    gl.uniform1f(uTime,t*.001);
    gl.uniform3f(uInk,ink[0],ink[1],ink[2]);
    gl.uniform3f(uPaper,paper[0],paper[1],paper[2]);
    gl.drawArrays(gl.TRIANGLE_STRIP,0,4);
    requestAnimationFrame(render);
  }
  requestAnimationFrame(render);
}
createBG('bg-dark',[.039,.039,.043],[.945,.937,.918]);
createBG('bg-light',[.039,.039,.043],[.945,.937,.918]);
</script>'''

# Navigation JS
NAV_JS = r'''<script>
const slides=[...document.querySelectorAll('.slide')];
const totalSlides=slides.length;
const deck=document.getElementById('deck');
let idx=0;
const dotsEl=document.getElementById('nav-dots');
for(let i=0;i<totalSlides;i++){
  const d=document.createElement('span');
  if(i===0)d.className='active';
  d.addEventListener('click',()=>go(i));
  dotsEl.appendChild(d);
}
function go(i){
  if(i<0||i>=totalSlides)return;
  idx=i;
  deck.style.transform='translateX(-'+idx*100+'vw)';
  const isDark=slides[idx].classList.contains('dark');
  document.body.classList.toggle('dark-bg',isDark);
  document.body.classList.toggle('light-bg',!isDark);
  dotsEl.querySelectorAll('span').forEach((d,j)=>d.classList.toggle('active',j===idx));
  if(window.__playSlide)window.__playSlide(idx);
}
document.getElementById('nav-prev').addEventListener('click',()=>go(idx-1));
document.getElementById('nav-next').addEventListener('click',()=>go(idx+1));
document.addEventListener('keydown',e=>{
  if(e.key==='ArrowRight'||e.key==='ArrowDown'){e.preventDefault();if(window.__pipeAdvance&&window.__pipeAdvance())return;go(idx+1)}
  if(e.key==='ArrowLeft'||e.key==='ArrowUp'){e.preventDefault();go(idx-1)}
  if(e.key==='Home'){e.preventDefault();go(0)}
  if(e.key==='End'){e.preventDefault();go(totalSlides-1)}
});
document.addEventListener('wheel',e=>{
  if(Math.abs(e.deltaX)>Math.abs(e.deltaY))return;
  if(e.deltaY>30){if(window.__pipeAdvance&&window.__pipeAdvance())return;go(idx+1)}
  if(e.deltaY<-30)go(idx-1);
},{passive:true});
let tx=0;
document.addEventListener('touchstart',e=>{tx=e.changedTouches[0].clientX});
document.addEventListener('touchend',e=>{
  const dx=e.changedTouches[0].clientX-tx;
  if(Math.abs(dx)>50){if(dx<0){if(window.__pipeAdvance&&window.__pipeAdvance())return;go(idx+1)}else go(idx-1)}
},{passive:true});
go(0);
</script>'''

# Motion One animation JS
MOTION_JS = r'''<script type="module">
let motion;
try {
  motion = await import('https://cdn.jsdelivr.net/npm/motion@11.11.17/+esm');
} catch(e2) {
  console.warn('[motion] CDN failed, disabling animations');
  document.querySelectorAll('[data-anim]').forEach(el=>{el.style.opacity='1';el.style.transform='none'});
}
if(motion){
  const { animate, stagger } = motion;
  document.body.classList.add('motion-ready');
  const EASE = [.22, 1, .36, 1];
  const slidesAll = [...document.querySelectorAll('.slide')];
  let pipeStep = -1;
  let lastIdx = -1;

  function resetAnims(slide){
    slide.querySelectorAll('[data-anim]').forEach(el=>{
      el.style.opacity='';
      el.style.transform='';
    });
  }

  function revealStatic(slide){
    resetAnims(slide);
    document.getAnimations?.().forEach(a=>a.cancel());
    slide.querySelectorAll('[data-anim]').forEach(el=>{
      el.style.opacity='1';
      el.style.transform='none';
    });
  }

  function playSlide(i){
    const slide = slidesAll[i];
    if(!slide) return;
    lastIdx = i;
    const recipe = slide.dataset.animate || (slide.classList.contains('hero') ? 'hero' : 'cascade');

    if(window.__lowPowerMode){
      revealStatic(slide);
      return;
    }

    resetAnims(slide);
    const all = [...slide.querySelectorAll('[data-anim]')];
    if(!all.length) return;

    if(recipe === 'quote'){
      const lines = all.filter(el=>el.dataset.anim==='line');
      const others = all.filter(el=>el.dataset.anim!=='line');
      if(others.length) animate(others, {opacity:[0,1], y:[8,0]}, {duration:.6, delay:stagger(.12, {start:.2}), easing:EASE});
      if(lines.length)  animate(lines,  {opacity:[.35,1], y:[10,0]}, {duration:.8, delay:stagger(.55, {start:.5}), easing:EASE});
      return;
    }

    if(recipe === 'hero'){
      animate(all, {opacity:[0,1], y:[14,0]}, {duration:.9, delay:stagger(.16, {start:.2}), easing:EASE});
      return;
    }

    animate(all, {opacity:[0,1], y:[16,0]}, {duration:.75, delay:stagger(.1, {start:.15}), easing:EASE});
  }

  function pipeAdvance(){
    if(window.__lowPowerMode) return false;
    const slide = slidesAll[lastIdx];
    if(!slide || slide.dataset.animate !== 'pipeline') return false;
    const steps  = [...slide.querySelectorAll('[data-anim="step"]')];
    const arrows = [...slide.querySelectorAll('[data-anim="arrow"]')];
    if(pipeStep >= steps.length - 1) return false;
    pipeStep++;
    animate(steps[pipeStep], {opacity:[0.15,1], y:[8,0]}, {duration:.5, easing:EASE});
    if(pipeStep > 0 && arrows[pipeStep-1]){
      animate(arrows[pipeStep-1], {opacity:[0.15,.7]}, {duration:.3, delay:.15});
    }
    return true;
  }

  window.__playSlide = playSlide;
  window.__pipeAdvance = pipeAdvance;
  playSlide(0);
}
</script>'''

with open(out_path, 'w', encoding='utf-8') as f:
    f.write(f'''<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>商务礼仪 · 跨境电商客户接待模拟</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="{fonts}" rel="stylesheet">
<style>
{CSS}
</style>
</head>
<body>
<canvas class="bg" id="bg-dark"></canvas>
<canvas class="bg" id="bg-light"></canvas>

<div id="deck">
{slides_content}
</div>

<div id="nav">
  <button id="nav-prev" aria-label="Previous"><i data-lucide="chevron-left" style="width:18px;height:18px"></i></button>
  <div class="dots" id="nav-dots"></div>
  <button id="nav-next" aria-label="Next"><i data-lucide="chevron-right" style="width:18px;height:18px"></i></button>
</div>

{WEBGL_JS}
{NAV_JS}
<script src="https://unpkg.com/lucide@latest/dist/umd/lucide.min.js"></script>
<script>lucide.createIcons();</script>
{MOTION_JS}
</body>
</html>''')

import os
size = os.path.getsize(out_path)
print(f'HTML generated: {size} bytes - {out_path}')
