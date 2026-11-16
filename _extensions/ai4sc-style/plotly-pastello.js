/** Precise SVG geometry with dry pastel pigment and exposed paper tooth. No raster images.
 * Adjust these parameters, then reload. Grain sizes are in displayed CSS pixels.
 */
export const PASTELLO = Object.freeze({
  // Keep grain below pixel-scale frequencies and soften the noise before contrast.
  // Only pigment is smoothed; SourceGraphic edges and typography stay sharp.
  grainFrequency: '0.34 0.46', octaves: 2, seed: 17,
  grainContrast: 2.25, grainMidpoint: 0.45, grainSoftness: 0.32,
  fillStrength: 0.50, lineStrength: 0.36, markerStrength: 0.32,
  fillOpacity: 1,
  // A pastel dragged across paper loads both edges, with a lighter, uneven middle.
  // Asymmetric pressure avoids a glossy, symmetric bevel or a misty noise field.
  pressureStops: [[0, 1], [0.09, 0.97], [0.28, 0.86], [0.49, 0.74], [0.7, 0.83], [0.91, 0.93], [1, 0.96]],
  pressureVariation: 0.20, pressurePatches: 4,
  edgeLoad: 0.43, edgeWidth: 1.6, edgeOffsetX: 0.6, edgeOffsetY: 1.5,
  edgeWear: 0.85,
  edgeDisplacement: 0, edgeFeather: 0,
  // Optional torn-paint look, opt-in per chart with layout.meta.ai4sc_pastello = {ragged: true}.
  // Two scales of seeded variation for the opt-in paint edge.
  raggedFrequency: '0.011 0.02', raggedScale: 5, raggedFine: '0.05', raggedFineScale: 1.2,
  washFrequency: '0.012 0.028', washContrast: 1.7, washMidpoint: 0.35, washStrength: 0.30,
  driftFrequency: '0.002 0.06', driftStrength: 0.14,
  raggedMaskMargin: 0.35,
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
  return {enabled, texture: value?.texture !== false, grid: value?.grid === true, ragged: value?.ragged === true};
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
function makeFilter(id, strength, opacity, ragged = false) {
  const filter = svgNode('filter', {id, filterUnits: 'userSpaceOnUse', primitiveUnits: 'userSpaceOnUse', 'color-interpolation-filters': 'sRGB'});
  const torn = ragged && id.endsWith('-fill');
  if (!torn || PASTELLO.edgeDisplacement > 0) {
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
  }
  let material = 'pigment';
  let shape = 'SourceGraphic', shapeAlpha = 'SourceAlpha';
  if (torn) {
    // Warp the original premultiplied paint without thresholding its opacity.
    filter.append(svgNode('feTurbulence', {type: 'fractalNoise', baseFrequency: PASTELLO.raggedFrequency,
      numOctaves: 2, seed: PASTELLO.seed + 5, result: 'tornWarp'}));
    filter.append(svgNode('feDisplacementMap', {in: 'SourceGraphic', in2: 'tornWarp', scale: PASTELLO.raggedScale,
      xChannelSelector: 'R', yChannelSelector: 'G', result: 'tornRough'}));
    filter.append(svgNode('feTurbulence', {type: 'fractalNoise', baseFrequency: PASTELLO.raggedFine,
      numOctaves: 1, seed: PASTELLO.seed + 9, result: 'tornFine'}));
    filter.append(svgNode('feDisplacementMap', {in: 'tornRough', in2: 'tornFine', scale: PASTELLO.raggedFineScale,
      xChannelSelector: 'G', yChannelSelector: 'R', result: 'tornShape'}));
    const coverage = svgNode('feComponentTransfer', {in: 'tornShape', result: 'tornAlpha'});
    coverage.append(svgNode('feFuncA', {type: 'gamma', amplitude: 1, exponent: 0.001, offset: 0}));
    filter.append(coverage);
    shape = 'tornShape'; shapeAlpha = 'tornAlpha';
    // Soft wash: low-frequency blotches and a faint horizontal drift replace the pixel grain.
    filter.append(svgNode('feTurbulence', {type: 'fractalNoise', baseFrequency: PASTELLO.washFrequency,
      numOctaves: 3, seed: PASTELLO.seed - 14, result: 'wash'}));
    filter.append(svgNode('feColorMatrix', {in: 'wash', type: 'matrix',
      values: `0 0 0 0 0  0 0 0 0 0  0 0 0 0 0  ${PASTELLO.washContrast} 0 0 0 ${-PASTELLO.washMidpoint}`, result: 'washRaw'}));
    const washAlpha = svgNode('feComponentTransfer', {in: 'washRaw', result: 'washAlpha'});
    washAlpha.append(svgNode('feFuncA', {type: 'linear', slope: PASTELLO.washStrength, intercept: 1 - PASTELLO.washStrength}));
    filter.append(washAlpha);
    filter.append(svgNode('feTurbulence', {type: 'fractalNoise', baseFrequency: PASTELLO.driftFrequency,
      numOctaves: 2, seed: PASTELLO.seed - 10, result: 'drift'}));
    filter.append(svgNode('feColorMatrix', {in: 'drift', type: 'matrix',
      values: '0 0 0 0 0  0 0 0 0 0  0 0 0 0 0  1.5 0 0 0 -0.12', result: 'driftRaw'}));
    const driftAlpha = svgNode('feComponentTransfer', {in: 'driftRaw', result: 'driftAlpha'});
    driftAlpha.append(svgNode('feFuncA', {type: 'linear', slope: PASTELLO.driftStrength, intercept: 1 - PASTELLO.driftStrength}));
    filter.append(driftAlpha);
    filter.append(svgNode('feComposite', {in: 'washAlpha', in2: 'driftAlpha', operator: 'in', result: 'washPigment'}));
    material = 'washPigment';
  }
  if (id.endsWith('-fill')) {
    // Pigment accumulates INSIDE the leading edge. No outline or geometry change.
    filter.append(svgNode('feOffset', {in: shapeAlpha, dx: PASTELLO.edgeOffsetX, dy: PASTELLO.edgeOffsetY, result: 'edgeOffset'}));
    filter.append(svgNode('feGaussianBlur', {in: 'edgeOffset', stdDeviation: PASTELLO.edgeWidth, result: 'edgeSoftness'}));
    filter.append(svgNode('feComposite', {in: shapeAlpha, in2: 'edgeSoftness', operator: 'out', result: 'edgePigment'}));
    filter.append(svgNode('feComposite', {in: material, in2: 'edgePigment', operator: 'arithmetic', k2: 1, k3: PASTELLO.edgeLoad, result: 'loadedPigment'}));
    // Torn shape already defines the edge: skip the grain-based edge wear there.
    if (torn) {
      material = 'loadedPigment';
    } else {
      // Sample the alpha edge with the same paper grain and keep the result
      // inside SourceGraphic. This wears the edge inward without moving the mark.
      const coverage = svgNode('feComponentTransfer', {in: shapeAlpha, result: 'coverage'});
      coverage.append(svgNode('feFuncA', {type: 'gamma', amplitude: 1, exponent: 0.001, offset: 0}));
      filter.append(coverage);
      filter.append(svgNode('feDisplacementMap', {in: 'coverage', in2: 'grain', scale: PASTELLO.edgeWear,
        xChannelSelector: 'R', yChannelSelector: 'G', result: 'wornEdge'}));
      filter.append(svgNode('feComposite', {in: 'loadedPigment', in2: 'wornEdge', operator: 'in', result: 'dryPigment'}));
      material = 'dryPigment';
    }
  }
  filter.append(svgNode('feComposite', {in: shape, in2: material, operator: 'in', result: 'paint'}));
  let source = 'paint';
  if (PASTELLO.edgeDisplacement > 0) {
    filter.append(svgNode('feDisplacementMap', {in: source, in2: 'grain', scale: Math.min(1, PASTELLO.edgeDisplacement), xChannelSelector: 'R', yChannelSelector: 'G', result: 'edge'}));
    source = 'edge';
  }
  if (PASTELLO.edgeFeather > 0) filter.append(svgNode('feGaussianBlur', {in: source, stdDeviation: Math.min(0.3, PASTELLO.edgeFeather)}));
  return filter;
}
export function createRaggedImageFilter(id) {
  const filter = makeFilter(id, PASTELLO.fillStrength, PASTELLO.fillOpacity, true);
  // CSS-filtered images each have their own size; pad relative to that image.
  filter.setAttribute('filterUnits', 'objectBoundingBox');
  for (const [attr, value] of Object.entries({x: '-10%', y: '-10%', width: '120%', height: '120%'})) {
    filter.setAttribute(attr, value);
  }
  return filter;
}

export function createRaggedShapeMaterial(prefix) {
  const defs = svgNode('defs', {'data-pastello': prefix});
  defs.append(createRaggedImageFilter(`${prefix}-fill`));
  addPressureMasks(defs, true);
  return defs;
}

function scaleMaterial(defs, svg) {
  const matrix = svg.getScreenCTM();
  const scale = Math.round(Math.max(0.15, Math.min(4, matrix ? Math.hypot(matrix.a, matrix.b) : 1)) * 1000) / 1000;
  if (defs.dataset.materialScale === String(scale)) return;
  defs.dataset.materialScale = String(scale);
  const frequency = value => String(value).split(/\s+/).map(n => Number(n) * scale).join(' ');
  for (const filter of defs.querySelectorAll('filter')) {
    filter.querySelector('[result="grain"]')?.setAttribute('baseFrequency', frequency(PASTELLO.grainFrequency));
    filter.querySelector('[result="edgeSoftness"]')?.setAttribute('stdDeviation', PASTELLO.edgeWidth / scale);
    const offset = filter.querySelector('[result="edgeOffset"]');
    offset?.setAttribute('dx', PASTELLO.edgeOffsetX / scale);
    offset?.setAttribute('dy', PASTELLO.edgeOffsetY / scale);
    filter.querySelector('[result="wornEdge"]')?.setAttribute('scale', Math.min(1, PASTELLO.edgeWear) / scale);
    filter.querySelector('[result="tornWarp"]')?.setAttribute('baseFrequency', frequency(PASTELLO.raggedFrequency));
    filter.querySelector('[result="tornFine"]')?.setAttribute('baseFrequency', frequency(PASTELLO.raggedFine));
    filter.querySelector('[result="tornRough"]')?.setAttribute('scale', PASTELLO.raggedScale / scale);
    filter.querySelector('[result="tornShape"]')?.setAttribute('scale', PASTELLO.raggedFineScale / scale);
    filter.querySelector('[result="wash"]')?.setAttribute('baseFrequency', frequency(PASTELLO.washFrequency));
    filter.querySelector('[result="drift"]')?.setAttribute('baseFrequency', frequency(PASTELLO.driftFrequency));
    filter.querySelector('[result="softGrain"]')?.setAttribute('stdDeviation', PASTELLO.grainSoftness / scale);
  }
}
function addPressureMasks(defs, ragged = false) {
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
      // The expanded white backing must not cancel pressure within the mark.
      const gray = Math.round(255 * opacity);
      gradient.append(svgNode('stop', {offset, 'stop-color': ragged ? `rgb(${gray},${gray},${gray})` : 'white',
        'stop-opacity': ragged ? 1 : opacity}));
    }
    const m = ragged ? PASTELLO.raggedMaskMargin : 0;
    const mask = svgNode('mask', {id, maskUnits: 'objectBoundingBox', maskContentUnits: 'objectBoundingBox', x: -m, y: -m, width: 1 + 2 * m, height: 1 + 2 * m, 'mask-type': 'luminance', 'color-interpolation': 'sRGB'});
    // Let the irregular paint edge extend just beyond the original bounding box.
    if (ragged) mask.append(svgNode('rect', {x: -m, y: -m, width: 1 + 2 * m, height: 1 + 2 * m, fill: 'white'}));
    mask.append(svgNode('rect', {x: 0, y: 0, width: 1, height: 1, fill: `url(#${id}-gradient)`}));
    // Soft, irregular pressure lifts along the stroke, not another noise layer.
    // Luminance dabs reduce pigment locally; the original mark is never displaced.
    for (let i = 0; i < PASTELLO.pressurePatches; i++) {
      const along = (i + 0.25 + random() * 0.5) / PASTELLO.pressurePatches;
      const across = 0.25 + random() * 0.5;
      const length = 0.09 + random() * 0.12;
      const breadth = 0.26 + random() * 0.21;
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
    if (!defs || defs.dataset.ragged !== String(opts.ragged)) {
      const previous = defs;
      defs = svgNode('defs', {'data-pastello': previous?.dataset.pastello || `ai4sc-pigment-${++serial}`,
        'data-ragged': opts.ragged});
      for (const kind of ['fill', 'line', 'marker']) defs.append(makeFilter(`${defs.dataset.pastello}-${kind}`, PASTELLO[kind + 'Strength'], kind === 'fill' ? PASTELLO.fillOpacity : 1, opts.ragged));
      addPressureMasks(defs, opts.ragged);
      if (previous) previous.replaceWith(defs);
      else svg.prepend(defs);
    }
    scaleMaterial(defs, svg);
    // Union in each target's LOCAL user space, including thin and negative paths.
    // This avoids objectBoundingBox failures on perfectly horizontal/vertical lines.
    // Hidden Reveal slides can report zero bounding boxes. Keep a chart-sized
    // minimum region so their marks remain visible when the slide is activated.
    const materialPad = opts.ragged ? Math.max(8, 8 / Number(defs.dataset.materialScale)) : 8;
    let x = -materialPad, y = -materialPad;
    let right = (el._fullLayout?.width || Number(svg.getAttribute('width')) || 1920) + materialPad;
    let bottom = (el._fullLayout?.height || Number(svg.getAttribute('height')) || 1080) + materialPad;
    for (const [node] of selected) {
      const b = node.getBBox();
      const pad = Math.max(materialPad, parseFloat(getComputedStyle(node).strokeWidth) || 0);
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
