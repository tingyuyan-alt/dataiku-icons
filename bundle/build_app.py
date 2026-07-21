import json, os, base64
HERE = os.path.dirname(os.path.abspath(__file__))
def _p(*parts): return os.path.join(HERE, *parts)
mat = json.load(open(_p("data","icons_final.json")))
brand = json.load(open(_p("data","brand_final.json")))
mat_json   = json.dumps(mat,   separators=(",",":"))
brand_json = json.dumps(brand, separators=(",",":"), ensure_ascii=False)
N_MAT   = f"{len(mat):,}"
N_BRAND = f"{len(brand):,}"
FAVICON = base64.b64encode(open(_p("logo.svg"),"rb").read()).decode()

HTML = r'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Dataiku Icons</title>
<link rel="icon" type="image/svg+xml" href="data:image/svg+xml;base64,__FAVICON__">
<link rel="apple-touch-icon" href="data:image/svg+xml;base64,__FAVICON__">
<style>
  :root{
    --dark-green:#06312E; --beige:#F8F4E4; --white:#FFFEF9; --black:#1A1A1A;
    --green:#3EDAB2; --light-green:#C7FFF1; --blue-grey:#42485B;
    --surface:#FFFEF9; --tile:#FFFFFF; --panel:#FFFFFF;
    --tile-bg:#FFFFFF; --tile-hover:#F8F4E4; --tile-label:#5F6B67;
    --line:rgba(26,26,26,.12); --line-strong:rgba(26,26,26,.22);
    --muted:#5F6B67; --text:#1A1A1A;
    --icon:#1A1A1A;
    --mono:ui-monospace,"Söhne Mono","SFMono-Regular",Menlo,Consolas,monospace;
    --body:Inter,-apple-system,"Segoe UI",Arial,sans-serif;
    --display:Georgia,"Signifier",serif;
  }
  *{box-sizing:border-box}
  html,body{margin:0}
  body{background:var(--surface);color:var(--text);font-family:var(--body);
       -webkit-font-smoothing:antialiased;line-height:1.4}
  ::selection{background:var(--green);color:var(--black)}

  header{padding:34px 28px 18px;max-width:1400px;margin:0 auto}
  h1{font-family:var(--display);font-weight:300;font-size:clamp(30px,4.4vw,46px);
     letter-spacing:.2px;margin:0;line-height:1.05;color:var(--black)}
  .tag{color:var(--muted);font-size:14px;max-width:60ch;margin:12px 0 18px}
  .spec{display:flex;gap:8px;flex-wrap:wrap}
  .chip{font-family:var(--mono);font-size:11px;letter-spacing:.06em;text-transform:uppercase;
        color:var(--muted);border:1px solid var(--line-strong);padding:5px 9px;
        background:rgba(62,218,178,.10)}
  .chip b{color:var(--dark-green);font-weight:600}
  .spec-brand{color:var(--muted);font-size:13px;font-family:var(--mono);letter-spacing:.04em}
  body:not(.tab-brand) .spec-brand{display:none}
  body.tab-brand .spec{display:none}
  body.tab-brand .swatches{display:none}
  body.tab-brand [data-act="jsx"]{display:none}

  /* ---- tabs ---- */
  .tabs{max-width:1400px;margin:0 auto;padding:0 28px;display:flex;
        border-bottom:1px solid var(--line)}
  .tab{background:none;border:0;border-bottom:2px solid transparent;margin-bottom:-1px;
       font-family:var(--body);font-size:14px;color:var(--muted);padding:13px 18px;
       cursor:pointer;display:flex;align-items:center;gap:8px}
  .tab:hover{color:var(--text)}
  .tab[aria-selected="true"]{color:var(--black);border-bottom-color:var(--green)}
  .tab span{font-family:var(--mono);font-size:11px;color:var(--muted);
       border:1px solid var(--line-strong);padding:1px 6px}
  .tab[aria-selected="true"] span{color:var(--dark-green)}
  .tab:focus-visible{outline:2px solid var(--green);outline-offset:2px}

  /* ---- controls ---- */
  .controls{position:sticky;top:0;z-index:20;background:rgba(255,254,249,.92);
            backdrop-filter:blur(8px);border-bottom:1px solid var(--line)}
  .controls-in{max-width:1400px;margin:0 auto;padding:14px 28px;
               display:flex;gap:14px;align-items:center;flex-wrap:wrap}
  .search{flex:1 1 300px;position:relative;min-width:240px}
  .search input{width:100%;background:var(--white);border:1px solid var(--line-strong);
    color:var(--text);font-family:var(--body);font-size:15px;padding:12px 14px 12px 40px}
  .search input:focus{outline:none;border-color:var(--green);box-shadow:0 0 0 1px var(--green)}
  .search svg{position:absolute;left:12px;top:50%;transform:translateY(-50%);
    width:18px;height:18px;color:var(--muted)}
  select{background:var(--white);color:var(--text);border:1px solid var(--line-strong);
    font-family:var(--body);font-size:14px;padding:11px 12px;cursor:pointer}
  select:focus{outline:none;border-color:var(--green)}
  .swatches{display:flex;gap:6px;align-items:center}
  .sw{width:26px;height:26px;border:1px solid var(--line-strong);cursor:pointer;padding:0}
  .sw[aria-pressed="true"]{box-shadow:0 0 0 2px var(--surface),0 0 0 3px var(--green)}
  .lbl{font-family:var(--mono);font-size:11px;color:var(--muted);text-transform:uppercase;letter-spacing:.06em}
  .count{margin-left:auto;font-family:var(--mono);font-size:12px;color:var(--muted);white-space:nowrap}
  .count b{color:var(--dark-green)}

  /* ---- grid ---- */
  main{max-width:1400px;margin:0 auto;padding:22px 24px 80px}
  .grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(104px,1fr));gap:1px;
        background:var(--line);border:1px solid var(--line)}
  .tile{background:var(--tile-bg);border:0;cursor:pointer;color:var(--icon);
        display:flex;flex-direction:column;align-items:center;gap:8px;
        padding:18px 8px 12px;transition:background .12s;
        content-visibility:auto;contain-intrinsic-size:118px}
  .tile:hover{background:var(--tile-hover)}
  .tile:focus-visible{outline:2px solid var(--green);outline-offset:-2px}
  .tile svg{width:34px;height:34px;display:block}
  .grid.mat .tile svg{fill:currentColor}
  .tile .nm{font-family:var(--mono);font-size:10px;color:var(--tile-label);
        max-width:100%;overflow:hidden;text-overflow:ellipsis;white-space:nowrap;letter-spacing:.02em}
  .empty{padding:60px 20px;text-align:center;color:var(--muted)}
  .empty b{color:var(--text);font-weight:500}

  /* ---- drawer ---- */
  .scrim{position:fixed;inset:0;background:rgba(26,26,26,.34);opacity:0;pointer-events:none;
    transition:opacity .18s;z-index:40}
  .scrim.on{opacity:1;pointer-events:auto}
  .drawer{position:fixed;top:0;right:0;height:100%;width:min(420px,92vw);
    background:var(--panel);border-left:1px solid var(--line-strong);z-index:50;
    transform:translateX(100%);transition:transform .2s cubic-bezier(.4,0,.2,1);
    display:flex;flex-direction:column;box-shadow:-16px 0 40px rgba(26,26,26,.10)}
  .drawer.on{transform:none}
  .d-head{display:flex;justify-content:space-between;align-items:center;
    padding:18px 20px;border-bottom:1px solid var(--line)}
  .d-head .cat{font-family:var(--mono);font-size:11px;letter-spacing:.08em;
    text-transform:uppercase;color:var(--dark-green)}
  .x{background:none;border:0;color:var(--muted);font-size:26px;line-height:1;cursor:pointer;padding:0 4px}
  .x:hover{color:var(--text)}
  .preview{padding:26px 20px;display:flex;flex-direction:column;align-items:center;gap:16px}
  .stage{width:172px;height:172px;display:flex;align-items:center;justify-content:center;
    border:1px solid var(--line);background:var(--white)}
  .stage svg{width:96px;height:96px}
  .drawer.mat .stage svg{fill:var(--icon)}
  .d-name{font-family:var(--mono);font-size:15px;color:var(--text);word-break:break-word;text-align:center}
  .actions{padding:4px 20px 24px;display:grid;grid-template-columns:1fr 1fr;gap:8px;overflow:auto}
  .btn{font-family:var(--body);font-size:13px;padding:11px 12px;cursor:pointer;
    border:1px solid var(--line-strong);background:var(--white);color:var(--text);
    text-align:center;transition:.12s}
  .btn:hover{border-color:var(--green);background:rgba(62,218,178,.12)}
  .btn.primary{background:var(--green);color:var(--black);border-color:var(--green);font-weight:600}
  .btn.primary:hover{background:var(--light-green);color:var(--black)}
  .btn.full{grid-column:1/-1}
  .btn.copied{background:var(--light-green);color:var(--black);border-color:var(--light-green)}

  .pager{display:flex;justify-content:center;align-items:center;gap:4px;flex-wrap:wrap;padding:28px 8px 0}
  .pager button{font-family:var(--mono);font-size:13px;min-width:38px;height:38px;padding:0 10px;
    border:1px solid var(--line-strong);background:var(--white);color:var(--text);cursor:pointer;transition:.12s}
  .pager button:hover:not(:disabled){border-color:var(--green);background:rgba(62,218,178,.12)}
  .pager button[aria-current="page"]{background:var(--green);border-color:var(--green);color:var(--black);font-weight:600}
  .pager button:disabled{color:var(--muted);cursor:not-allowed;opacity:.5}
  .pager .gap{min-width:22px;text-align:center;color:var(--muted);font-family:var(--mono)}
  .pager .nav{padding:0 14px}

  footer{max-width:1400px;margin:0 auto;padding:0 28px 40px;color:var(--muted);
    font-size:12px;font-family:var(--mono);border-top:1px solid var(--line);padding-top:20px}
  @media (prefers-reduced-motion:reduce){*{transition:none!important}}
</style>
</head>
<body>
<header>
  <h1>Dataiku Icons</h1>
  <p class="tag">Two icon sets in one place: the Material Symbols system locked to the brand spec, and Dataiku&rsquo;s product icons in their original colors. Search, recolor the Material set from the approved palette, and grab any icon as SVG, PNG, name, or JSX.</p>
  <div class="spec">
    <span class="chip">Style <b>Material Symbols &middot; Sharp</b></span>
    <span class="chip">Fill <b>1</b></span>
    <span class="chip">Weight <b>500</b></span>
    <span class="chip">Grade <b>200</b></span>
    <span class="chip">Optical size <b>24</b></span>
  </div>
  <div class="spec-brand">Dataiku product icons &middot; original colors preserved &middot; grouped by product area</div>
</header>

<div class="tabs" role="tablist" aria-label="Icon sets">
  <button class="tab" role="tab" data-tab="mat"   aria-selected="true">Material Symbols <span>__NMAT__</span></button>
  <button class="tab" role="tab" data-tab="brand" aria-selected="false">DKU Product Icons <span>__NBRAND__</span></button>
</div>

<div class="controls">
  <div class="controls-in">
    <div class="search">
      <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="11" cy="11" r="7"/><path d="M21 21l-4.3-4.3"/></svg>
      <input id="q" type="search" placeholder="Search icons&hellip;" autocomplete="off" spellcheck="false" aria-label="Search icons">
    </div>
    <select id="cat" aria-label="Filter by category"></select>
    <div class="swatches" role="group" aria-label="Icon color">
      <span class="lbl">Color</span>
      <button class="sw" title="Core Black"  data-c="#1A1A1A" style="background:#1A1A1A"></button>
      <button class="sw" title="Core White"  data-c="#FFFEF9" style="background:#FFFEF9"></button>
      <button class="sw" title="Green"        data-c="#3EDAB2" style="background:#3EDAB2"></button>
    </div>
    <div class="count" id="count"></div>
  </div>
</div>

<main>
  <div class="grid mat" id="grid"></div>
  <div class="empty" id="empty" hidden>No icons match <b id="emptyq"></b>. Try a shorter term or a different category.</div>
  <nav class="pager" id="pager" aria-label="Icon pages"></nav>
</main>

<footer id="foot"></footer>

<div class="scrim" id="scrim"></div>
<aside class="drawer mat" id="drawer" aria-hidden="true" aria-label="Icon detail">
  <div class="d-head"><span class="cat" id="dCat"></span><button class="x" id="close" aria-label="Close">&times;</button></div>
  <div class="preview">
    <div class="stage" id="stage"></div>
    <div class="swatches" role="group" aria-label="Icon color">
      <span class="lbl">Color</span>
      <button class="sw" title="Core Black" data-c="#1A1A1A" style="background:#1A1A1A"></button>
      <button class="sw" title="Core White" data-c="#FFFEF9" style="background:#FFFEF9"></button>
      <button class="sw" title="Green"      data-c="#3EDAB2" style="background:#3EDAB2"></button>
    </div>
    <div class="d-name" id="dName"></div>
  </div>
  <div class="actions">
    <button class="btn primary full" data-act="png">Copy PNG</button>
    <button class="btn primary full" data-act="svg">Copy SVG</button>
    <button class="btn" data-act="name">Copy name</button>
    <button class="btn" data-act="jsx">Copy JSX</button>
    <button class="btn" data-act="dlpng">Download PNG</button>
    <button class="btn" data-act="dlsvg">Download SVG</button>
  </div>
</aside>

<script id="data"  type="application/json">__MAT__</script>
<script id="brand" type="application/json">__BRAND__</script>
<script>
const MAT   = JSON.parse(document.getElementById('data').textContent);
const BRAND = JSON.parse(document.getElementById('brand').textContent);
const MAT_NAMES   = Object.keys(MAT);
const BRAND_NAMES = Object.keys(BRAND);
const MAT_IDX   = MAT_NAMES.map(n => (n.replace(/_/g,' ')+' '+MAT[n].c).toLowerCase());
const BRAND_IDX = BRAND_NAMES.map(n => (n+' '+BRAND[n].c).toLowerCase());
const MVB='0 0 960 960';
const XMLNS='xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink"';
const matInner = d => `<g transform="translate(0 960) scale(1 -1)"><path d="${d}"/></g>`;
const escA=s=>String(s).replace(/&/g,'&amp;').replace(/"/g,'&quot;');
const escH=s=>String(s).replace(/&/g,'&amp;').replace(/</g,'&lt;');

let TAB='mat';
const isMat = ()=> TAB==='mat';
const curNames = ()=> isMat()?MAT_NAMES:BRAND_NAMES;
const curIdx   = ()=> isMat()?MAT_IDX:BRAND_IDX;
const rec = n => isMat()?MAT[n]:BRAND[n];
function iconSVG(n){
  if(isMat()) return `<svg viewBox="${MVB}" aria-hidden="true">${matInner(MAT[n].p)}</svg>`;
  const r=BRAND[n]; return `<svg viewBox="${r.vb}" preserveAspectRatio="xMidYMid meet" aria-hidden="true">${r.s}</svg>`;
}

// ---- controls ----
const q=document.getElementById('q'), catSel=document.getElementById('cat');
const grid=document.getElementById('grid'), countEl=document.getElementById('count'), empty=document.getElementById('empty');
function populateCats(){
  const cats=[...new Set(curNames().map(n=>rec(n).c))].sort();
  catSel.innerHTML='<option value="">All categories</option>'+cats.map(c=>`<option>${escH(c)}</option>`).join('');
}
const PAGE_SIZE=600;
let filtered=[]; let page=1;
const pager=document.getElementById('pager');
function applyFilter(){
  const term=q.value.trim().toLowerCase(), cat=catSel.value, names=curNames(), idx=curIdx();
  filtered=names.filter((n,i)=>{
    if(cat && rec(n).c!==cat) return false;
    if(!term) return true;
    return idx[i].includes(term);
  });
  page=1;
  render();
}
function pageItems(total,cur){
  if(total<=7) return Array.from({length:total},(_,i)=>i+1);
  const keep=new Set([1,2,total-1,total,cur-1,cur,cur+1]);
  const arr=[...keep].filter(n=>n>=1&&n<=total).sort((a,b)=>a-b);
  const out=[]; let prev=0;
  for(const n of arr){ if(n-prev>1) out.push('gap'); out.push(n); prev=n; }
  return out;
}
function renderPager(total){
  if(total<=1){ pager.innerHTML=''; return; }
  let html=`<button class="nav" data-p="${page-1}"${page===1?' disabled':''} aria-label="Previous page">Prev</button>`;
  for(const it of pageItems(total,page)){
    html += it==='gap' ? `<span class="gap">\u2026</span>`
      : `<button data-p="${it}"${it===page?' aria-current="page"':''}>${it}</button>`;
  }
  html+=`<button class="nav" data-p="${page+1}"${page===total?' disabled':''} aria-label="Next page">Next</button>`;
  pager.innerHTML=html;
}
function render(){
  const total=Math.max(1,Math.ceil(filtered.length/PAGE_SIZE));
  if(page>total) page=total;
  const start=(page-1)*PAGE_SIZE;
  const shown=filtered.slice(start,start+PAGE_SIZE);
  empty.hidden=filtered.length>0;
  document.getElementById('emptyq').textContent=q.value||'(this category)';
  grid.style.display=filtered.length?'grid':'none';
  grid.innerHTML=shown.map(n=>
    `<button class="tile" data-n="${escA(n)}" title="${escA(n)}">${iconSVG(n)}<span class="nm">${escH(n)}</span></button>`
  ).join('');
  const pg = total>1 ? ` &middot; page ${page} of ${total}` : '';
  countEl.innerHTML=`<b>${filtered.length.toLocaleString()}</b> icon${filtered.length!==1?'s':''}${pg}`;
  renderPager(total);
}
pager.addEventListener('click',e=>{
  const b=e.target.closest('button'); if(!b||b.disabled) return;
  const p=parseInt(b.dataset.p,10); if(!p) return;
  page=p; render();
  const top=document.querySelector('main').offsetTop-70;
  window.scrollTo({top:top<0?0:top, behavior:'smooth'});
});

// ---- color (Material only) ----
const swatches=[...document.querySelectorAll('.sw')];
let ICON_COLOR='#1A1A1A';
const onDarkColor=c=> c==='#FFFEF9'||c==='#3EDAB2';   // White or Green
function syncStage(){
  const stg=document.getElementById('stage'); if(!stg) return;
  if(!isMat()){ stg.style.background='var(--white)'; return; }
  stg.style.background = onDarkColor(ICON_COLOR) ? 'var(--black)' : 'var(--white)';
}
function setColor(c){
  ICON_COLOR=c;
  const root=document.documentElement.style;
  root.setProperty('--icon',c);
  const dark=onDarkColor(c);
  root.setProperty('--tile-bg',    dark?'#1A1A1A':'#FFFFFF');
  root.setProperty('--tile-hover', dark?'#2E2E2E':'#F8F4E4');
  root.setProperty('--tile-label', dark?'#9DB8B0':'#5F6B67');
  syncStage();
  swatches.forEach(s=>s.setAttribute('aria-pressed', s.dataset.c===c?'true':'false'));
}
swatches.forEach(b=>b.addEventListener('click',()=>setColor(b.dataset.c)));
setColor('#1A1A1A');
function applyGround(){
  if(isMat()){ setColor(ICON_COLOR); }
  else{
    const root=document.documentElement.style;
    root.setProperty('--tile-bg','#FFFFFF');
    root.setProperty('--tile-hover','#F8F4E4');
    root.setProperty('--tile-label','#5F6B67');
    syncStage();
  }
}

// ---- tabs ----
function switchTab(t){
  if(t===TAB) return;
  TAB=t;
  document.querySelectorAll('.tab').forEach(x=>x.setAttribute('aria-selected', x.dataset.tab===t?'true':'false'));
  document.body.classList.toggle('tab-brand', t==='brand');
  grid.classList.toggle('mat', isMat());
  grid.classList.toggle('brand', !isMat());
  q.value='';
  q.placeholder = isMat() ? 'Search '+MAT_NAMES.length.toLocaleString()+' icons\u2026' : 'Search '+BRAND_NAMES.length+' product icons\u2026';
  populateCats();
  applyGround();
  closeDrawer();
  applyFilter();
}
document.querySelectorAll('.tab').forEach(b=>b.addEventListener('click',()=>switchTab(b.dataset.tab)));

// ---- drawer ----
const drawer=document.getElementById('drawer'), scrim=document.getElementById('scrim');
const stage=document.getElementById('stage'), dName=document.getElementById('dName'), dCat=document.getElementById('dCat');
let current=null;
function openIcon(n){
  current=n;
  drawer.classList.toggle('mat', isMat());
  drawer.classList.toggle('brand', !isMat());
  stage.innerHTML=iconSVG(n);
  dName.textContent=n; dCat.textContent=rec(n).c;
  syncStage();
  drawer.classList.add('on'); scrim.classList.add('on'); drawer.setAttribute('aria-hidden','false');
}
function closeDrawer(){drawer.classList.remove('on');scrim.classList.remove('on');drawer.setAttribute('aria-hidden','true');}
grid.addEventListener('click',e=>{const t=e.target.closest('.tile'); if(t) openIcon(t.dataset.n);});
document.getElementById('close').addEventListener('click',closeDrawer);
scrim.addEventListener('click',closeDrawer);
document.addEventListener('keydown',e=>{if(e.key==='Escape')closeDrawer();});

// ---- export ----
function dims(vb){const p=vb.trim().split(/\s+/);return [p[2]||'24', p[3]||'24'];}
function buildSVG(n){
  if(isMat()){
    return `<svg ${XMLNS} width="24" height="24" viewBox="${MVB}"><g transform="translate(0 960) scale(1 -1)"><path d="${MAT[n].p}" fill="${ICON_COLOR}"/></g></svg>`;
  }
  const r=BRAND[n]; const [w,h]=dims(r.vb);
  return `<svg ${XMLNS} width="${w}" height="${h}" viewBox="${r.vb}">${r.s}</svg>`;
}
function pngSVG(n,size){
  if(isMat()){
    return `<svg ${XMLNS} width="${size}" height="${size}" viewBox="${MVB}"><g transform="translate(0 960) scale(1 -1)"><path d="${MAT[n].p}" fill="${ICON_COLOR}"/></g></svg>`;
  }
  const r=BRAND[n];
  return `<svg ${XMLNS} width="${size}" height="${size}" viewBox="${r.vb}" preserveAspectRatio="xMidYMid meet">${r.s}</svg>`;
}
function toPascal(n){return 'Icon'+n.split('_').map(s=>s.charAt(0).toUpperCase()+s.slice(1)).join('');}
function buildJSX(n){
  return `const ${toPascal(n)} = (props) => (\n  <svg width="24" height="24" viewBox="${MVB}" fill="currentColor" {...props}>\n`
    + `    <g transform="translate(0 960) scale(1 -1)"><path d="${MAT[n].p}" /></g>\n  </svg>\n);`;
}
function flash(btn,label){if(!btn.dataset.label)btn.dataset.label=btn.textContent;
  btn.textContent=label;btn.classList.add('copied');clearTimeout(btn._t);
  btn._t=setTimeout(()=>{btn.textContent=btn.dataset.label;btn.classList.remove('copied');},1200);}
async function copy(txt){try{await navigator.clipboard.writeText(txt);return true;}catch{
  const ta=document.createElement('textarea');ta.value=txt;document.body.appendChild(ta);ta.select();
  try{document.execCommand('copy');}catch{} ta.remove();return true;}}
function download(name,blob){const u=URL.createObjectURL(blob);const a=document.createElement('a');
  a.href=u;a.download=name;a.click();setTimeout(()=>URL.revokeObjectURL(u),1000);}
function renderPNG(n,size){
  return new Promise((resolve,reject)=>{
    const svg=pngSVG(n,size);
    const img=new Image();
    img.onload=()=>{const c=document.createElement('canvas');c.width=c.height=size;
      const ctx=c.getContext('2d');ctx.imageSmoothingEnabled=true;ctx.imageSmoothingQuality='high';
      ctx.drawImage(img,0,0,size,size);
      c.toBlob(bl=>bl?resolve(bl):reject(new Error('encode')),'image/png');};
    img.onerror=()=>reject(new Error('load'));
    img.src='data:image/svg+xml;base64,'+btoa(unescape(encodeURIComponent(svg)));
  });
}
function safeFile(n){return n.replace(/[^\w.-]+/g,'_');}

document.querySelector('.actions').addEventListener('click',async e=>{
  const b=e.target.closest('.btn'); if(!b||!current) return;
  if(!b.dataset.label)b.dataset.label=b.textContent;
  const n=current, act=b.dataset.act;
  if(act==='svg'){await copy(buildSVG(n));flash(b,'Copied!');}
  else if(act==='name'){await copy(n);flash(b,'Copied!');}
  else if(act==='jsx'){await copy(buildJSX(n));flash(b,'Copied!');}
  else if(act==='png'){
    if(!(navigator.clipboard && window.ClipboardItem)){flash(b,'Not supported');return;}
    b.textContent='Copying\u2026';
    try{
      await navigator.clipboard.write([new ClipboardItem({'image/png':renderPNG(n,512)})]);
      flash(b,'Copied!');
    }catch(err){
      try{const blob=await renderPNG(n,512);
        await navigator.clipboard.write([new ClipboardItem({'image/png':blob})]);
        flash(b,'Copied!');
      }catch(e2){flash(b,'Blocked \u2014 use Download');}
    }
  }
  else if(act==='dlpng'){const blob=await renderPNG(n,512);download(safeFile(n)+'.png',blob);flash(b,'Saved!');}
  else if(act==='dlsvg'){download(safeFile(n)+'.svg',new Blob([buildSVG(n)],{type:'image/svg+xml'}));flash(b,'Saved!');}
});

// ---- init ----
q.addEventListener('input',applyFilter);
catSel.addEventListener('change',applyFilter);
q.placeholder='Search '+MAT_NAMES.length.toLocaleString()+' icons\u2026';
populateCats();
applyFilter();
document.getElementById('foot').innerHTML =
  `${MAT_NAMES.length.toLocaleString()} Material Symbols (Apache-2.0, Sharp / Fill 1 / wght 500 / Grade 200 / opsz 24) `
  + `&middot; ${BRAND_NAMES.length} DKU product icons &middot; internal design system`;
</script>
</body>
</html>'''

HTML = (HTML.replace("__MAT__", mat_json)
            .replace("__BRAND__", brand_json)
            .replace("__NMAT__", N_MAT)
            .replace("__NBRAND__", N_BRAND)
            .replace("__FAVICON__", FAVICON))
open(_p("index.html"),"w").write(HTML)
print("wrote index.html, size MB:", round(os.path.getsize(_p("index.html"))/1e6,2))
