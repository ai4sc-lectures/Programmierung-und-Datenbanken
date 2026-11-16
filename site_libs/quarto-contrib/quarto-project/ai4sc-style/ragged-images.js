// Quarto can relocate the entry script; resources stay at the project root.
const offset = document.querySelector('meta[name="quarto:offset"]')?.content || './';
const {createRaggedImageFilter, createRaggedShapeMaterial} = await import(
  new URL('_extensions/ai4sc-style/plotly-pastello.js', new URL(offset, document.baseURI)).href
);

const NS = 'http://www.w3.org/2000/svg';
const id = 'ai4sc-ragged-image-fill';
const images = 'img.ragged, figure.ragged img';
const sourceOf = img => img.getAttribute('data-src') || img.getAttribute('src');
const svgCopies = new Map();

if (!document.getElementById(id)) {
  const svg = document.createElementNS(NS, 'svg');
  svg.setAttribute('aria-hidden', 'true');
  svg.setAttribute('width', '0');
  svg.setAttribute('height', '0');
  svg.style.position = 'absolute';
  const defs = document.createElementNS(NS, 'defs');
  defs.append(createRaggedImageFilter(id));
  svg.append(defs);
  document.body.append(svg);

  const style = document.createElement('style');
  style.textContent = `img[data-ai4sc-ragged-raster] { filter: url("#${id}"); }`;
  document.head.append(style);
}

async function makeSvgCopy(url) {
  const response = await fetch(url);
  if (!response.ok) return null;
  const doc = new DOMParser().parseFromString(await response.text(), 'image/svg+xml');
  const svg = doc.documentElement;
  if (svg.localName !== 'svg' || svg.namespaceURI !== NS) return null;

  // Keep the SVG in an <img>'s isolated rendering context. Filter only painted
  // shapes; applying the filter to a parent group would also distort its labels.
  let prefix = 'ai4sc-ragged-image';
  while ([...doc.querySelectorAll('[id]')].some(node => node.id.startsWith(`${prefix}-`))) prefix += '-copy';
  const protectedElements = 'defs, symbol, marker, pattern, clipPath, mask, filter, text, foreignObject';
  const shapes = [...svg.querySelectorAll('path,rect,circle,ellipse,polygon')].filter(shape =>
    !shape.closest(protectedElements) && !shape.hasAttribute('filter') &&
    shape.closest('[fill]')?.getAttribute('fill') !== 'none' && shape.namespaceURI === NS
  );
  if (!shapes.length) return null;
  svg.prepend(doc.importNode(createRaggedShapeMaterial(prefix), true));
  for (const shape of shapes) {
    shape.setAttribute('filter', `url(#${prefix}-fill)`);
    if (!shape.hasAttribute('mask') && !shape.style.mask) {
      const tallRect = shape.localName === 'rect' &&
        shape.height.baseVal.value > shape.width.baseVal.value;
      shape.setAttribute('mask', `url(#${prefix}-pressure-${tallRect ? 'x' : 'y'})`);
    }
  }
  return URL.createObjectURL(new Blob([new XMLSerializer().serializeToString(svg)], {type: 'image/svg+xml'}));
}

for (const image of document.querySelectorAll(images)) {
  const source = sourceOf(image);
  if (!source) continue;
  const url = new URL(source, document.baseURI);
  if (!/\.svgz?$/i.test(url.pathname) && !/^data:image\/svg\+xml[;,]/i.test(source)) {
    image.setAttribute('data-ai4sc-ragged-raster', '');
    continue;
  }
  // If we cannot read an SVG, keep the original rather than filtering its text.
  if (image.hasAttribute('srcset') || image.hasAttribute('data-srcset') || image.closest('picture')) continue;
  if (!svgCopies.has(url.href)) svgCopies.set(url.href, makeSvgCopy(url.href).catch(() => null));
  svgCopies.get(url.href).then(copy => {
    if (!copy || sourceOf(image) !== source) return;
    if (image.hasAttribute('data-src')) image.setAttribute('data-src', copy);
    if (image.getAttribute('src') === source || !image.hasAttribute('data-src')) image.src = copy;
  });
}
