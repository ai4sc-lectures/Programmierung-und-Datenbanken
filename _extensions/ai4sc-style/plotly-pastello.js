/** Precise SVG geometry with dry pastel pigment and exposed paper tooth. No raster images.
 * Adjust these parameters, then reload. Grain sizes are in displayed CSS pixels.
 */
export const PASTELLO = Object.freeze({
  // Keep grain below pixel-scale frequencies and soften the noise before contrast.
  // Only pigment is smoothed; SourceGraphic edges and typography stay sharp.
  grainFrequency: '0.34 0.46', octaves: 2, seed: 17,
  grainContrast: 1.8, grainMidpoint: 0.45, grainSoftness: 0.38,
  fillStrength: 0.46, lineStrength: 0.36, markerStrength: 0.32,
  fillOpacity: 0.97,
  // A pastel dragged across paper loads both edges, with a lighter, uneven middle.
  // Asymmetric pressure avoids a glossy, symmetric bevel or a misty noise field.
  pressureStops: [[0, 0.98], [0.12, 0.91], [0.35, 0.72], [0.64, 0.75], [0.88, 0.88], [1, 0.93]],
  pressureVariation: 0.16, pressurePatches: 7,
  edgeLoad: 0.40, edgeWidth: 1.2, edgeOffsetX: 0.6, edgeOffsetY: 1.3,
  edgeDisplacement: 0, edgeFeather: 0,
  gridOpacity: 0.04, gridSize: 24,
});
const NS = 'http://www.w3.org/2000/svg';
const paletteNames = ['sage', 'violet', 'blue', 'amber', 'rose', 'gray'];
const fallback = ['#8B9E87', '#A398BC', '#91B5CB', '#D6B65E', '#C58E89', '#99958C'];
const bindings = new WeakMap();
let serial = 0;
const props = () => getComputedStyle(document.querySelector('.reveal') || document.documentElement);
export function pastelloOptions(layout = {}) {
  const value = layout.meta?.ai4sc_pastello;
  if (value === false || value?.enabled === false) return {enabled: false};
  const enabled = value === true || value?.enabled === true || props().getPropertyValue('--ai4sc-pastello').trim() === '1';
  return {enabled, texture: value?.texture !== false, grid: value?.grid === true};
}
export function pastelloDefaults() {
  const css = props();
  const token = (name, defaultValue) => css.getPropertyValue(name).trim() || defaultValue;
  const axis = {showgrid: false, zeroline: false, showline: false, tickfont: {color: token('--carbon', '#68665E')}};
  return {
    paper_bgcolor: 'rgba(0,0,0,0)', plot_bgcolor: 'rgba(0,0,0,0)',
    colorway: paletteNames.map((name, i) => token('--pastello-' + name, fallback[i])),
    font: {color: token('--ink', '#302F2B'), family: 'DINPro, Inter, ui-sans-serif, system-ui, sans-serif', size: 16},
    title: { font: { size: 24 } },
    xaxis: axis, yaxis: axis, legend: {bgcolor: 'rgba(0,0,0,0)', borderwidth: 0},
  };
}
export function pastelloLayout(layout = {}) {
  if (!pastelloOptions(layout).enabled) return layout;
  const defaults = pastelloDefaults();
  const old = layout.template || {};
  const base = {...old.layout, ...defaults};
  for (const key of Object.keys({...old.layout, ...layout})) {
    if (/^[xy]axis\d*$/.test(key)) base[key] = {...old.layout?.[key], ...defaults.xaxis};
  }
  // Layout-level user settings continue to take precedence over template defaults.
  return {...layout, template: {...old, layout: base}};
}
function svgNode(tag, attrs = {}) {
  const el = document.createElementNS(NS, tag);
  Object.entries(attrs).forEach(([k, v]) => el.setAttribute(k, String(v)));
  return el;
}
function makeFilter(id, strength, opacity) {
  const filter = svgNode('filter', {id, filterUnits: 'userSpaceOnUse', primitiveUnits: 'userSpaceOnUse', 'color-interpolation-filters': 'sRGB'});
  filter.append(svgNode('feTurbulence', {type: 'fractalNoise', baseFrequency: PASTELLO.grainFrequency,
    numOctaves: PASTELLO.octaves, seed: PASTELLO.seed, result: 'grain'}));
  filter.append(svgNode('feGaussianBlur', {in: 'grain', stdDeviation: PASTELLO.grainSoftness, result: 'softGrain'}));
  // Expand the narrow fractal-noise range BEFORE setting a pigment floor.
  // The previous tiny linear modulation survived mostly as a uniform opacity change.
  filter.append(svgNode('feColorMatrix', {in: 'softGrain', type: 'matrix',
    values: `0 0 0 0 0  0 0 0 0 0  0 0 0 0 0  ${PASTELLO.grainContrast} 0 0 0 ${0.5 - PASTELLO.grainMidpoint * PASTELLO.grainContrast}`, result: 'tooth'}));
  const transfer = svgNode('feComponentTransfer', {in: 'tooth', result: 'pigment'});
  transfer.append(svgNode('feFuncA', {type: 'linear', slope: strength * opacity, intercept: (1 - strength) * opacity}));
  filter.append(transfer);
  let material = 'pigment';
  if (id.endsWith('-fill')) {
    // Pigment accumulates INSIDE the leading edge. No outline or geometry change.
    filter.append(svgNode('feOffset', {in: 'SourceAlpha', dx: PASTELLO.edgeOffsetX, dy: PASTELLO.edgeOffsetY, result: 'edgeOffset'}));
    filter.append(svgNode('feGaussianBlur', {in: 'edgeOffset', stdDeviation: PASTELLO.edgeWidth, result: 'edgeSoftness'}));
    filter.append(svgNode('feComposite', {in: 'SourceAlpha', in2: 'edgeSoftness', operator: 'out', result: 'edgePigment'}));
    filter.append(svgNode('feComposite', {in: 'pigment', in2: 'edgePigment', operator: 'arithmetic', k2: 1, k3: PASTELLO.edgeLoad, result: 'loadedPigment'}));
    material = 'loadedPigment';
  }
  filter.append(svgNode('feComposite', {in: 'SourceGraphic', in2: material, operator: 'in', result: 'paint'}));
  let source = 'paint';
  if (PASTELLO.edgeDisplacement > 0) {
    filter.append(svgNode('feDisplacementMap', {in: source, in2: 'grain', scale: Math.min(1, PASTELLO.edgeDisplacement), xChannelSelector: 'R', yChannelSelector: 'G', result: 'edge'}));
    source = 'edge';
  }
  if (PASTELLO.edgeFeather > 0) filter.append(svgNode('feGaussianBlur', {in: source, stdDeviation: Math.min(0.3, PASTELLO.edgeFeather)}));
  return filter;
}
function scaleMaterial(defs, svg) {
  const matrix = svg.getScreenCTM();
  const scale = Math.round(Math.max(0.15, Math.min(4, matrix ? Math.hypot(matrix.a, matrix.b) : 1)) * 1000) / 1000;
  if (defs.dataset.materialScale === String(scale)) return;
  defs.dataset.materialScale = String(scale);
  const frequency = value => String(value).split(/\s+/).map(n => Number(n) * scale).join(' ');
  for (const filter of defs.querySelectorAll('filter')) {
    filter.querySelector('[result="grain"]').setAttribute('baseFrequency', frequency(PASTELLO.grainFrequency));
    filter.querySelector('[result="edgeSoftness"]')?.setAttribute('stdDeviation', PASTELLO.edgeWidth / scale);
    const offset = filter.querySelector('[result="edgeOffset"]');
    offset?.setAttribute('dx', PASTELLO.edgeOffsetX / scale);
    offset?.setAttribute('dy', PASTELLO.edgeOffsetY / scale);
    filter.querySelector('[result="softGrain"]').setAttribute('stdDeviation', PASTELLO.grainSoftness / scale);
  }
}
function addPressureMasks(defs) {
  // Shared object-bounding-box masks adapt to every bar/polygon, without per-mark filters.
  const patchId = `${defs.dataset.pastello}-pressure-patch`;
  const patch = svgNode('radialGradient', {id: patchId});
  patch.append(svgNode('stop', {offset: 0, 'stop-color': 'black', 'stop-opacity': PASTELLO.pressureVariation}),
    svgNode('stop', {offset: 0.4, 'stop-color': 'black', 'stop-opacity': PASTELLO.pressureVariation * 0.65}),
    svgNode('stop', {offset: 1, 'stop-color': 'black', 'stop-opacity': 0}));
  defs.append(patch);
  for (const axis of ['x', 'y']) {
    // Fixed seeds make pressure irregular without changing it on redraw or toggle.
    let seed = PASTELLO.seed + (axis === 'x' ? 101 : 211);
    const random = () => {
      seed = (Math.imul(seed, 1664525) + 1013904223) >>> 0;
      return seed / 4294967296;
    };
    const id = `${defs.dataset.pastello}-pressure-${axis}`;
    const gradient = svgNode('linearGradient', {id: `${id}-gradient`, x1: 0, y1: 0, x2: axis === 'x' ? 1 : 0, y2: axis === 'y' ? 1 : 0});
    for (const [offset, opacity] of PASTELLO.pressureStops) {
      gradient.append(svgNode('stop', {offset, 'stop-color': 'white', 'stop-opacity': opacity}));
    }
    const mask = svgNode('mask', {id, maskUnits: 'objectBoundingBox', maskContentUnits: 'objectBoundingBox', x: 0, y: 0, width: 1, height: 1, 'mask-type': 'luminance', 'color-interpolation': 'sRGB'});
    mask.append(svgNode('rect', {x: 0, y: 0, width: 1, height: 1, fill: `url(#${id}-gradient)`}));
    // Soft, irregular pressure lifts along the stroke, not another noise layer.
    // Luminance dabs reduce pigment locally; the original mark is never displaced.
    for (let i = 0; i < PASTELLO.pressurePatches; i++) {
      const along = (i + 0.25 + random() * 0.5) / PASTELLO.pressurePatches;
      const across = 0.25 + random() * 0.5;
      const length = 0.07 + random() * 0.10;
      const breadth = 0.20 + random() * 0.18;
      mask.append(svgNode('ellipse', {cx: axis === 'y' ? along : across, cy: axis === 'y' ? across : along,
        rx: axis === 'y' ? length : breadth, ry: axis === 'y' ? breadth : length,
        fill: `url(#${patchId})`}));
    }
    defs.append(gradient, mask);
  }
}
export function refreshPastello(el) {
  bindings.get(el)?.refresh();
}
function targets(svg) {
  const found = [];
  const add = (selector, kind) => svg.querySelectorAll(selector).forEach(el => found.push([el, kind]));
  add('.barlayer .trace.bars .point > path, .scatterlayer .trace .js-fill', 'fill');
  add('.scatterlayer .trace .js-line', 'line');
  add('.scatterlayer .trace .points path.point', 'marker');
  svg.querySelectorAll('.shapelayer path[data-index]').forEach(el => {
    const s = getComputedStyle(el);
    found.push([el, s.fill !== 'none' && s.fill !== 'rgba(0, 0, 0, 0)' && Number(s.fillOpacity) !== 0 ? 'fill' : 'line']);
  });
  return found;
}
function decorate(el) {
  const opts = pastelloOptions(el.layout);
  const state = bindings.get(el);
  if (!state) return;
  const css = props();
  const gridOpacity = css.getPropertyValue('--pastello-grid-opacity').trim() || PASTELLO.gridOpacity;
  const gridSize = css.getPropertyValue('--pastello-grid-size').trim() || `${PASTELLO.gridSize}px`;
  el.style.backgroundImage = opts.enabled && opts.grid ? `linear-gradient(rgba(82,102,77,${gridOpacity}) 1px, transparent 1px), linear-gradient(90deg, rgba(82,102,77,${gridOpacity}) 1px, transparent 1px)` : state.backgroundImage;
  el.style.backgroundSize = opts.enabled && opts.grid ? `${gridSize} ${gridSize}` : state.backgroundSize;
  for (const svg of el.querySelectorAll('svg.main-svg')) {
    const selected = targets(svg);
    let defs = svg.querySelector('defs[data-pastello]');
    if (!opts.enabled || !opts.texture) {
      svg.querySelectorAll('[data-pastello-filter]').forEach(node => {
        const old = node.getAttribute('data-pastello-filter');
        if (old) node.setAttribute('filter', old); else node.removeAttribute('filter');
        node.removeAttribute('data-pastello-filter');
        if (node.hasAttribute('data-pastello-mask')) {
          const mask = node.getAttribute('data-pastello-mask');
          if (mask) node.setAttribute('mask', mask); else node.removeAttribute('mask');
          node.removeAttribute('data-pastello-mask');
        }
      });
      defs?.remove();
      continue;
    }
    if (!selected.length) continue;
    if (!defs) {
      defs = svgNode('defs', {'data-pastello': `ai4sc-pigment-${++serial}`});
      for (const kind of ['fill', 'line', 'marker']) defs.append(makeFilter(`${defs.dataset.pastello}-${kind}`, PASTELLO[kind + 'Strength'], kind === 'fill' ? PASTELLO.fillOpacity : 1));
      addPressureMasks(defs);
      svg.prepend(defs);
    }
    scaleMaterial(defs, svg);
    // Union in each target's LOCAL user space, including thin and negative paths.
    // This avoids objectBoundingBox failures on perfectly horizontal/vertical lines.
    // Hidden Reveal slides can report zero bounding boxes. Keep a chart-sized
    // minimum region so their marks remain visible when the slide is activated.
    let x = -8, y = -8;
    let right = (el._fullLayout?.width || Number(svg.getAttribute('width')) || 1920) + 8;
    let bottom = (el._fullLayout?.height || Number(svg.getAttribute('height')) || 1080) + 8;
    for (const [node] of selected) {
      const b = node.getBBox();
      const pad = Math.max(8, parseFloat(getComputedStyle(node).strokeWidth) || 0);
      x = Math.min(x, b.x - pad); y = Math.min(y, b.y - pad);
      right = Math.max(right, b.x + b.width + pad); bottom = Math.max(bottom, b.y + b.height + pad);
    }
    for (const filter of defs.querySelectorAll('filter')) {
      for (const [name, value] of Object.entries({x, y, width: right - x, height: bottom - y})) {
        if (filter.getAttribute(name) !== String(value)) filter.setAttribute(name, value);
      }
    }
    for (const [node, kind] of selected) {
      if (!node.hasAttribute('data-pastello-filter')) node.setAttribute('data-pastello-filter', node.getAttribute('filter') || '');
      node.setAttribute('filter', `url(#${defs.dataset.pastello}-${kind})`);
      if (kind === 'fill' && (!node.hasAttribute('mask') || node.hasAttribute('data-pastello-mask'))) {
        const box = node.getBBox();
        if (box.width > 0 && box.height > 0) {
          if (!node.hasAttribute('data-pastello-mask')) node.setAttribute('data-pastello-mask', node.getAttribute('mask') || '');
          const axis = node.closest('.barlayer') && box.height > box.width ? 'x' : 'y';
          node.setAttribute('mask', `url(#${defs.dataset.pastello}-pressure-${axis})`);
        }
      }
    }
  }
}
export function attachPastello(el) {
  if (!el?.on) return;
  if (!bindings.has(el)) {
    const state = {pending: false, backgroundImage: el.style.backgroundImage, backgroundSize: el.style.backgroundSize};
    state.refresh = () => {
      if (state.pending) return;
      state.pending = true;
      requestAnimationFrame(() => { state.pending = false; if (el.isConnected) decorate(el); });
    };
    bindings.set(el, state);
  }
  const state = bindings.get(el);
  // newPlot/purge may reset Plotly's emitter; remove only our own listeners.
  for (const event of ['plotly_afterplot', 'plotly_animated']) {
    el.removeListener?.(event, state.refresh);
    el.on(event, state.refresh);
  }
  if (pastelloOptions(el.layout).enabled) decorate(el);
  else state.refresh();
}
