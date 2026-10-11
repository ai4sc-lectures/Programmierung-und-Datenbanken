// animations.js — GSAP on inline SVG elements
// SVG default state = end state (for Typst/PDF).
// GSAP resets to start state on DOMContentLoaded.

const BA = {
  step: -1,
  msgs: [
    'Bit 0: 1+1 = 10₂ → Summe 0, Übertrag 1',
    'Bit 1: 0+1+1 = 10₂ → Summe 0, Übertrag 1',
    'Bit 2: 1+1+1 = 11₂ → Summe 1, Übertrag 1',
    'Bit 3: 1+0+1 = 10₂ → Summe 0, Übertrag 1',
    'Bit 4: 0+0+1 = 01₂ → Summe 1, kein Übertrag',
    '13 + 7 = 20 ✓',
  ],
  data: [
    { hi:'ba-hi0', carry:'ba-c1', result:'ba-r0' },
    { hi:'ba-hi1', carry:'ba-c2', result:'ba-r1' },
    { hi:'ba-hi2', carry:'ba-c3', result:'ba-r2' },
    { hi:'ba-hi3', carry:'ba-c4', result:'ba-r3' },
    { hi:'ba-hi4', carry:null,    result:'ba-r4' },
  ],
  animated: ['ba-hi0','ba-hi1','ba-hi2','ba-hi3','ba-hi4',
             'ba-c1','ba-c2','ba-c3','ba-c4',
             'ba-r0','ba-r1','ba-r2','ba-r3','ba-r4','ba-r5'],

  g(id) { return document.getElementById(id); },

  reset() {
    this.step = -1;
    const s = this.g('ba-status');
    if (s) s.textContent = 'Klick zum Starten';
    // reset all animated elements to hidden
    this.animated.forEach(id => gsap.set(this.g(id), { opacity: 0 }));
  },

  next() {
    this.step++;
    if (this.step > 5) { this.reset(); return; }

    const s = this.g('ba-status');
    if (s) s.textContent = this.msgs[this.step];

    if (this.step < 5) {
      const { hi, carry, result } = this.data[this.step];
      if (this.step > 0) gsap.to(this.g(this.data[this.step-1].hi), { opacity:0, duration:0.2 });
      gsap.fromTo(this.g(hi),     { opacity:0 },        { opacity:1, duration:0.25 });
      gsap.fromTo(this.g(result), { opacity:0, y:-4 },  { opacity:1, y:0, duration:0.3, delay:0.35 });
      if (carry) gsap.fromTo(this.g(carry), { opacity:0, y:6 }, { opacity:1, y:0, duration:0.3, delay:0.55 });
    } else {
      gsap.to(this.g(this.data[4].hi), { opacity:0, duration:0.2 });
      gsap.fromTo(this.g('ba-r5'), { opacity:0, y:-4 }, { opacity:1, y:0, duration:0.35, delay:0.2 });
    }
  },
};

window.baNext = () => BA.next();

// reset to start state on load (SVG default is end state for Typst)
document.addEventListener('DOMContentLoaded', () => {
  if (document.getElementById('ba-r0')) BA.reset();
});

if (typeof Reveal !== 'undefined') {
  Reveal.on('slidechanged', e => {
    if (e.currentSlide?.querySelector('#ba-r0')) BA.reset();
  });
}

// ─── Shift-and-Add Multiplication ──────────────────────

const BM = {
  step: -1,
  msgs: [
    'B[0]=1 → A<<0 addieren (×1)',
    'B[1]=0 → A<<1 überspringen (×2)',
    'B[2]=1 → A<<2 addieren (×4)',
    '3 × 5 = 01111 = 15 ✓',
  ],
  animated: ['bm-p0','bm-p1','bm-p2','bm-result',
             'bm-bhi0','bm-bhi1','bm-bhi2'],

  g(id) { return document.getElementById(id); },

  reset() {
    this.step = -1;
    const s = this.g('bm-status');
    if (s) s.textContent = 'Klick zum Starten';
    this.animated.forEach(id => gsap.set(this.g(id), { opacity: 0 }));
  },

  next() {
    this.step++;
    if (this.step > 3) { this.reset(); return; }

    const s = this.g('bm-status');
    if (s) s.textContent = this.msgs[this.step];

    if (this.step < 3) {
      // fade out previous B highlight
      if (this.step > 0) gsap.to(this.g('bm-bhi'+(this.step-1)), { opacity:0, duration:0.2 });
      // show B highlight
      gsap.fromTo(this.g('bm-bhi'+this.step), { opacity:0 }, { opacity:1, duration:0.25 });
      // show shift row
      gsap.fromTo(this.g('bm-p'+this.step), { opacity:0, y:-4 }, { opacity:1, y:0, duration:0.3, delay:0.3 });
    } else {
      gsap.to(this.g('bm-bhi2'), { opacity:0, duration:0.2 });
      gsap.fromTo(this.g('bm-result'), { opacity:0, y:-4 }, { opacity:1, y:0, duration:0.35, delay:0.2 });
    }
  },
};

window.bmNext = () => BM.next();

document.addEventListener('DOMContentLoaded', () => {
  if (document.getElementById('bm-result')) BM.reset();
});

if (typeof Reveal !== 'undefined') {
  Reveal.on('slidechanged', e => {
    if (e.currentSlide?.querySelector('#bm-result')) BM.reset();
  });
}
