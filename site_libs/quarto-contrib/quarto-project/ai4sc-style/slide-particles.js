const DEFAULT_PARTICLE_CONFIG = {
  analysisIntervalMs: 5000,
  readyDelayMs: 180,
  slideChangeDelayMs: 220,
  fragmentDelayMs: 120,
  resizeDelayMs: 180,
  downsampleFactor: 2.5,
  minAnalysisWidth: 420,
  minAnalysisHeight: 280,
  maxAnalysisWidth: 640,
  maxAnalysisHeight: 420,
  particleCount: 500,
  particleTheme: "binary-mesh",
  particleRenderMode: "circle",
  particleGridCellWidth: 20,
  particleGridCellHeight: 20,
  particleCheckerMaskThreshold: 0.16,
  particleCheckerSwapInterval: 0.38,
  particleGlyphSet: "01",
  particleGlyphFontFamily: "'DINPro', 'Inter', ui-sans-serif, system-ui, sans-serif;",
  particlePixelSize: 1.9,
  particleGlyphScale: 1.9,
  particleGlyphSizeFactor: 3.1,
  particleConnectionMode: "none",
  particleConnectionK: 2,
  particleConnectionMaxDistance: 120,
  particleConnectionOpacity: 0.12,
  particleConnectionWidth: 1,
  particleContourLevels: 12,
  particleContourMinValue: 0.06,
  particleContourMaxValue: 0.78,
  particleContourMinDistance: 16,
  particleContourOuterSmoothing: 2,
  particleContourLevelBias: 2.2,
  particleHeightMapMidRadius: 3,
  particleHeightMapFarRadius: 11,
  particleHeightMapBlendStrength: 1.35,
  particleFieldLineCount: 56,
  particleFieldLineSteps: 60,
  particleFieldLineStepSize: 9,
  particleFieldLineMinLength: 120,
  particleFieldLineEdgeInset: 12,
  particleFieldLinePull: 1.2,
  particleFieldLineSwirl: 0.42,
  particleFieldLineFlowStrength: 1,
  particleFieldLineBaselinePull: 0.035,
  particleFieldLineWaveAmplitude: 0,
  particleFieldLineWaveSpeed: 0.12,
  particleFieldLineWaveFrequency: 0.18,
  particleLifeMin: 12,
  particleLifeMax: 22,
  particleBurstDuration: 0.42,
  particleBurstVelocity: 11,
  particleBirthDuration: 0.36,
  particleBirthVelocity: 10,
  particleRespawnMinDistance: 0.8,
  particleRespawnMaxDistance: 3.2,
  particleRandomRespawnRatio: 0.14,
  anchorTargetCount: 220,
  anchorPull: 1.35,
  particleMinSpeed: 5,
  particleMaxSpeed: 18,
  orbitTarget: 6.5,
  orbitWidth: 3.5,
  orbitPull: 0.42,
  seekForce: 0.95,
  tangentForce: 11,
  driftForce: 0.22,
  damping: 0.978,
  maxVelocity: 26,
  noiseForce: 1.25,
  auraBlurPasses: 0,
  textSupportMaxFontPx: 999,
  textSupportIncludeHeadings: true,
  opacity: 0.48,
  glowOpacity: 0.18,
  excludeSelector: [
    ".footer",
    ".slide-logo",
    ".slide-number",
    ".verticator",
    ".slide-menu-button",
    ".slide-chalkboard-buttons",
    ".speaker-notes",
    "[data-particles='off']",
  ].join(", "),
};

const PARTICLE_THEME_PRESETS = {
  circles: {},
  "pastel-cells": {
    particleRenderMode: "pastel-cells",
    particleCount: 100,
    particleLifeMin: 9,
    particleLifeMax: 16,
    opacity: 0.38,
    glowOpacity: 0,
    particleConnectionMode: "none",
    pastelCellDensity: 0.32,
    pastelCellAttentionRadius: 72,
  },
  "pastel-dust": {
    particleRenderMode: "pigment",
    particleCount: 100,
    particleMinSpeed: 2.0,
    particleMaxSpeed: 5.0,
    particleLifeMin: 24,
    particleLifeMax: 40,
    opacity: 0.62,
    glowOpacity: 0,
    particleConnectionMode: "none",
  },
  binary: {
    particleRenderMode: "matrix",
    particleGlyphSet: "01",
    particleGlyphScale: 1.75,
    particleGlyphSizeFactor: 2.9,
    opacity: 0.44,
    glowOpacity: 0.12,
    tangentForce: 10.4,
  },
  "binary-minimal": {
    particleRenderMode: "matrix",
    particleGlyphSet: "01",
    particleGlyphScale: 1.45,
    particleGlyphSizeFactor: 2.35,
    opacity: 0.4,
    glowOpacity: 0.08,
    tangentForce: 8.8,
    noiseForce: 0.52,
    particleMinSpeed: 4.2,
    particleMaxSpeed: 13.5,
  },
  "binary-mesh": {
    particleRenderMode: "matrix",
    particleGlyphSet: "01",
    particleGlyphScale: 1.75,
    particleGlyphSizeFactor: 2.85,
    particleConnectionMode: "k-nearest",
    particleConnectionK: 2,
    particleConnectionMaxDistance: 92,
    particleConnectionOpacity: 0.11,
    particleConnectionWidth: 0.85,
    particleRandomRespawnRatio: 0.2,
    opacity: 0.4,
    glowOpacity: 0.08,
    tangentForce: 10.1,
    noiseForce: 0.88,
  },
  "ai-minimal": {
    particleRenderMode: "matrix",
    particleGlyphSet: "AI",
    particleGlyphScale: 1.45,
    particleGlyphSizeFactor: 2.35,
    opacity: 0.4,
    glowOpacity: 0.08,
    tangentForce: 8.8,
    noiseForce: 0.52,
    particleMinSpeed: 4.2,
    particleMaxSpeed: 13.5,
  },
  "ai4sc-minimal": {
    particleRenderMode: "matrix",
    particleGlyphSet: "AI4SC",
    particleGlyphScale: 1.45,
    particleGlyphSizeFactor: 2.35,
    opacity: 0.4,
    glowOpacity: 0.08,
    tangentForce: 8.8,
    noiseForce: 0.52,
    particleMinSpeed: 4.2,
    particleMaxSpeed: 13.5,
  },
  "ml-minimal": {
    particleRenderMode: "matrix",
    particleGlyphSet: "ML",
    particleGlyphScale: 1.45,
    particleGlyphSizeFactor: 2.35,
    opacity: 0.4,
    glowOpacity: 0.08,
    tangentForce: 8.8,
    noiseForce: 0.52,
    particleMinSpeed: 4.2,
    particleMaxSpeed: 13.5,
  },
  matrix: {
    particleRenderMode: "matrix",
    particleGlyphSet: "01アイウエオカキクケコABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789",
    particleGlyphScale: 1.75,
    particleGlyphSizeFactor: 2.95,
    opacity: 0.46,
    glowOpacity: 0.13,
    tangentForce: 10.6,
  },
  "subtle-pixels": {
    particleRenderMode: "pixel",
    particlePixelSize: 1.6,
    opacity: 0.42,
    glowOpacity: 0.14,
  },
  "token-stream": {
    particleRenderMode: "matrix",
    particleGlyphSet: "<>[]{}()/=+-_:;AIMLRGTV0123456789",
    particleGlyphScale: 1.75,
    particleGlyphSizeFactor: 2.85,
    opacity: 0.46,
    glowOpacity: 0.13,
    tangentForce: 10.6,
  },
  "latent-grid": {
    particleRenderMode: "pixel",
    particlePixelSize: 2.2,
    opacity: 0.4,
    glowOpacity: 0.11,
    noiseForce: 0.9,
    tangentForce: 9.8,
  },
  reasoning: {
    particleRenderMode: "matrix",
    particleGlyphSet: ".:·+=<>/?-",
    particleGlyphScale: 1.65,
    particleGlyphSizeFactor: 2.75,
    opacity: 0.42,
    glowOpacity: 0.1,
    noiseForce: 0.85,
  },
  "neural-mesh": {
    particleRenderMode: "pixel",
    particlePixelSize: 1.7,
    particleConnectionMode: "k-nearest",
    particleConnectionK: 2,
    particleConnectionMaxDistance: 96,
    particleConnectionOpacity: 0.12,
    particleConnectionWidth: 0.9,
    particleRandomRespawnRatio: 0.24,
    opacity: 0.38,
    glowOpacity: 0.08,
    noiseForce: 0.9,
  },
  "knowledge-graph": {
    particleRenderMode: "circle",
    particleConnectionMode: "k-nearest",
    particleConnectionK: 1,
    particleConnectionMaxDistance: 156,
    particleConnectionOpacity: 0.16,
    particleConnectionWidth: 1.35,
    particleRandomRespawnRatio: 0.18,
    particleMinSpeed: 4.2,
    particleMaxSpeed: 14,
    tangentForce: 8.2,
    noiseForce: 0.62,
    opacity: 0.44,
    glowOpacity: 0.09,
  },
  "gravitational-circles": {
    particleRenderMode: "circle",
    particleConnectionMode: "k-nearest",
    particleConnectionK: 1,
    particleConnectionMaxDistance: 172,
    particleConnectionOpacity: 0.1,
    particleConnectionWidth: 0.7,
    particleRandomRespawnRatio: 0.12,
    particleMinSpeed: 3.8,
    particleMaxSpeed: 11.5,
    anchorPull: 1.1,
    orbitPull: 0.34,
    tangentForce: 9.9,
    noiseForce: 0.34,
    opacity: 0.34,
    glowOpacity: 0.05,
  },
  "gravitational-lines": {
    particleRenderMode: "circle",
    particleConnectionMode: "contour-lines",
    particleConnectionOpacity: 0.28,
    particleConnectionWidth: 1.15,
    particleContourLevels: 14,
    particleContourMinValue: 0.04,
    particleContourMaxValue: 0.76,
    particleContourMinDistance: 14,
    particleContourOuterSmoothing: 3,
    particleContourLevelBias: 2.1,
    particleHeightMapMidRadius: 12,
    particleHeightMapFarRadius: 48,
    particleHeightMapBlendStrength: 1.95,
    particleCount: 0,
    opacity: 0,
    glowOpacity: 0,
  },
  checker: {
    // Checker mode uses slow births and one-cell swaps so mask changes feel transported,
    // rather than re-seeded or flickery.
    particleRenderMode: "checker",
    particleConnectionMode: "none",
    glowOpacity: 0,
    opacity: 0.44,
    particleCheckerBirthDelayMin: 1.4,
    particleCheckerBirthDelayMax: 3,
    particleCheckerDeathDelayMin: 0.45,
    particleCheckerDeathDelayMax: 1,
    particleCheckerMoveLerp: 12,
  },
};

const USER_PARTICLE_CONFIG = {...window.slideParticlesConfig, ...window.slideParticlesOverrides};
const PARTICLE_THEME_KEY = String(
  USER_PARTICLE_CONFIG.particleTheme || DEFAULT_PARTICLE_CONFIG.particleTheme || "circles",
).toLowerCase();
const PARTICLE_THEME_CONFIG = PARTICLE_THEME_PRESETS[PARTICLE_THEME_KEY] || {};

const PARTICLE_CONFIG = {
  ...DEFAULT_PARTICLE_CONFIG,
  ...PARTICLE_THEME_CONFIG,
  ...USER_PARTICLE_CONFIG,
};
if (PARTICLE_CONFIG.particleRenderMode === "binary") {
  PARTICLE_CONFIG.particleRenderMode = "matrix";
  if (!PARTICLE_CONFIG.particleGlyphSet) {
    PARTICLE_CONFIG.particleGlyphSet = "01";
  }
}

const PARTICLE_DEBUG =
  new URLSearchParams(window.location.search).get("particle-debug") === "1";
const DEBUG_VIEW_SEQUENCE = ["original", "blurred", "mask"];

const DEBUG_MULTIPLIERS = PARTICLE_DEBUG
  ? { opacity: 2.35, glowOpacity: 3.2, radius: 1.85, glowRadius: 2.15 }
  : { opacity: 1, glowOpacity: 1, radius: 1, glowRadius: 1 };

function clamp(value, min, max) {
  return Math.min(max, Math.max(min, value));
}

function parseCssColor(value) {
  if (!value || value === "transparent") return null;
  const normalized = value.trim().toLowerCase();
  if (normalized.startsWith("#")) {
    const hex = normalized.slice(1);
    if (hex.length === 3 || hex.length === 4) {
      const channels = hex.split("").map((channel) => channel + channel);
      return {
        r: Number.parseInt(channels[0], 16),
        g: Number.parseInt(channels[1], 16),
        b: Number.parseInt(channels[2], 16),
        a: channels[3] ? Number.parseInt(channels[3], 16) / 255 : 1,
      };
    }
    if (hex.length === 6 || hex.length === 8) {
      return {
        r: Number.parseInt(hex.slice(0, 2), 16),
        g: Number.parseInt(hex.slice(2, 4), 16),
        b: Number.parseInt(hex.slice(4, 6), 16),
        a: hex.length === 8 ? Number.parseInt(hex.slice(6, 8), 16) / 255 : 1,
      };
    }
  }

  const match = normalized.match(/rgba?\(([^)]+)\)/);
  if (!match) return null;
  const parts = match[1]
    .split(",")
    .map((part) => part.trim())
    .filter(Boolean);
  if (parts.length < 3) return null;
  return {
    r: Number.parseFloat(parts[0]),
    g: Number.parseFloat(parts[1]),
    b: Number.parseFloat(parts[2]),
    a: parts[3] == null ? 1 : Number.parseFloat(parts[3]),
  };
}

function relativeLuminance({ r, g, b }) {
  const normalize = (channel) => {
    const value = clamp(channel / 255, 0, 1);
    return value <= 0.03928 ? value / 12.92 : ((value + 0.055) / 1.055) ** 2.4;
  };
  const lr = normalize(r);
  const lg = normalize(g);
  const lb = normalize(b);
  return 0.2126 * lr + 0.7152 * lg + 0.0722 * lb;
}

function resolveBackgroundLuminance(element) {
  let current = element;
  while (current && current instanceof HTMLElement) {
    const color = parseCssColor(getComputedStyle(current).backgroundColor);
    if (color && color.a > 0.04) {
      return relativeLuminance(color);
    }
    current = current.parentElement;
  }

  const bodyColor = parseCssColor(getComputedStyle(document.body).backgroundColor);
  if (bodyColor && bodyColor.a > 0.04) {
    return relativeLuminance(bodyColor);
  }
  return 0;
}

function computeGradient(field, width, height, x, y) {
  const x0 = clamp(Math.floor(x), 0, width - 1);
  const x1 = clamp(x0 + 1, 0, width - 1);
  const y0 = clamp(Math.floor(y), 0, height - 1);
  const y1 = clamp(y0 + 1, 0, height - 1);
  const get = (sx, sy) => field[sy * width + sx];
  return {
    dx: get(x1, y0) - get(x0, y0),
    dy: get(x0, y1) - get(x0, y0),
  };
}

function blurMask(mask, width, height) {
  const temp = new Float32Array(mask.length);
  const output = new Float32Array(mask.length);

  for (let y = 0; y < height; y += 1) {
    for (let x = 0; x < width; x += 1) {
      let sum = 0;
      let count = 0;
      for (let ox = -1; ox <= 1; ox += 1) {
        const sx = x + ox;
        if (sx < 0 || sx >= width) continue;
        sum += mask[y * width + sx];
        count += 1;
      }
      temp[y * width + x] = sum / count;
    }
  }

  for (let y = 0; y < height; y += 1) {
    for (let x = 0; x < width; x += 1) {
      let sum = 0;
      let count = 0;
      for (let oy = -1; oy <= 1; oy += 1) {
        const sy = y + oy;
        if (sy < 0 || sy >= height) continue;
        sum += temp[sy * width + x];
        count += 1;
      }
      output[y * width + x] = sum / count;
    }
  }

  return output;
}

function gaussianKernel1d(radius) {
  const safeRadius = Math.max(1, Math.floor(radius));
  const sigma = Math.max(0.6, safeRadius / 2.2);
  const size = safeRadius * 2 + 1;
  const kernel = new Float32Array(size);
  let sum = 0;

  for (let i = 0; i < size; i += 1) {
    const offset = i - safeRadius;
    const value = Math.exp(-(offset * offset) / (2 * sigma * sigma));
    kernel[i] = value;
    sum += value;
  }

  for (let i = 0; i < size; i += 1) {
    kernel[i] /= sum || 1;
  }

  return { kernel, radius: safeRadius };
}

function gaussianBlurMask(mask, width, height, radius) {
  if (radius <= 1) {
    return blurMask(mask, width, height);
  }

  const { kernel, radius: safeRadius } = gaussianKernel1d(radius);
  const temp = new Float32Array(mask.length);
  const output = new Float32Array(mask.length);

  for (let y = 0; y < height; y += 1) {
    for (let x = 0; x < width; x += 1) {
      let sum = 0;
      for (let offset = -safeRadius; offset <= safeRadius; offset += 1) {
        const sx = clamp(x + offset, 0, width - 1);
        sum += mask[y * width + sx] * kernel[offset + safeRadius];
      }
      temp[y * width + x] = sum;
    }
  }

  for (let y = 0; y < height; y += 1) {
    for (let x = 0; x < width; x += 1) {
      let sum = 0;
      for (let offset = -safeRadius; offset <= safeRadius; offset += 1) {
        const sy = clamp(y + offset, 0, height - 1);
        sum += temp[sy * width + x] * kernel[offset + safeRadius];
      }
      output[y * width + x] = sum;
    }
  }

  return output;
}

function normalizeMask(mask) {
  let peak = 0;
  for (let i = 0; i < mask.length; i += 1) {
    peak = Math.max(peak, mask[i]);
  }
  if (peak <= 0.0001) {
    return mask.slice();
  }

  const normalized = new Float32Array(mask.length);
  for (let i = 0; i < mask.length; i += 1) {
    normalized[i] = clamp(mask[i] / peak, 0, 1);
  }
  return normalized;
}

function mergeContourHeightMaps(baseMask, midMask, farMask, blendStrength) {
  const merged = new Float32Array(baseMask.length);
  const strength = Math.max(0.25, Number(blendStrength || 1.35));

  for (let i = 0; i < baseMask.length; i += 1) {
    const base = clamp(baseMask[i], 0, 1);
    const mid = clamp(midMask[i], 0, 1);
    const far = clamp(farMask[i], 0, 1);
    const shapedBase = Math.pow(base, 1.14);
    const shapedMid = Math.pow(mid, 0.98);
    const shapedFar = Math.pow(far, 0.84);
    const diffusion = clamp(shapedMid * 0.52 + shapedFar * 1.2, 0, 1);
    const burn = 1 - (1 - diffusion) * Math.pow(1 - shapedBase * 0.58, strength * 0.5);
    const contourAnchor = Math.max(base * 0.26, shapedBase * 0.22);
    merged[i] = clamp(burn * 0.93 + contourAnchor * 0.07, 0, 1);
  }

  return merged;
}

function downsampleMask(source, sourceWidth, sourceHeight, targetWidth, targetHeight) {
  const reduced = new Float32Array(targetWidth * targetHeight);
  const scaleX = sourceWidth / targetWidth;
  const scaleY = sourceHeight / targetHeight;

  for (let ty = 0; ty < targetHeight; ty += 1) {
    const startY = ty * scaleY;
    const endY = Math.min(sourceHeight, (ty + 1) * scaleY);
    const y0 = Math.floor(startY);
    const y1 = Math.max(y0 + 1, Math.ceil(endY));

    for (let tx = 0; tx < targetWidth; tx += 1) {
      const startX = tx * scaleX;
      const endX = Math.min(sourceWidth, (tx + 1) * scaleX);
      const x0 = Math.floor(startX);
      const x1 = Math.max(x0 + 1, Math.ceil(endX));

      let sum = 0;
      let peak = 0;
      let count = 0;
      for (let sy = y0; sy < y1; sy += 1) {
        for (let sx = x0; sx < x1; sx += 1) {
          const value = source[sy * sourceWidth + sx];
          sum += value;
          peak = Math.max(peak, value);
          count += 1;
        }
      }

      const average = count > 0 ? sum / count : 0;
      reduced[ty * targetWidth + tx] = clamp(peak * 0.7 + average * 0.3, 0, 1);
    }
  }

  return reduced;
}

function paintRoundedRect(context, x, y, width, height, radius) {
  const r = Math.min(radius, width / 2, height / 2);
  context.beginPath();
  context.moveTo(x + r, y);
  context.arcTo(x + width, y, x + width, y + height, r);
  context.arcTo(x + width, y + height, x, y + height, r);
  context.arcTo(x, y + height, x, y, r);
  context.arcTo(x, y, x + width, y, r);
  context.closePath();
  context.fill();
}

function buildDistanceField(mask, width, height) {
  const distance = new Float32Array(width * height);
  const queue = new Uint32Array(width * height);
  let head = 0;
  let tail = 0;

  for (let i = 0; i < mask.length; i += 1) {
    if (mask[i] > 0.28) {
      distance[i] = 0;
      queue[tail] = i;
      tail += 1;
    } else {
      distance[i] = Number.POSITIVE_INFINITY;
    }
  }

  const neighbors = [
    [-1, 0, 1],
    [1, 0, 1],
    [0, -1, 1],
    [0, 1, 1],
    [-1, -1, Math.SQRT2],
    [1, -1, Math.SQRT2],
    [-1, 1, Math.SQRT2],
    [1, 1, Math.SQRT2],
  ];

  while (head < tail) {
    const index = queue[head];
    head += 1;
    const x = index % width;
    const y = Math.floor(index / width);
    const base = distance[index];

    for (const [ox, oy, step] of neighbors) {
      const nx = x + ox;
      const ny = y + oy;
      if (nx < 0 || nx >= width || ny < 0 || ny >= height) continue;
      const nIndex = ny * width + nx;
      const next = base + step;
      if (next < distance[nIndex]) {
        distance[nIndex] = next;
        queue[tail] = nIndex;
        tail += 1;
      }
    }
  }

  return distance;
}

function pickParticleGlyph(particle, glyphSet) {
  const symbols = (glyphSet || "").trim();
  if (!symbols) return "0";
  const indexSeed = Math.abs(
    Math.floor((particle.phase * 1000 + particle.radius * 37 + particle.life * 17) % symbols.length),
  );
  return symbols[indexSeed % symbols.length];
}

function computeMaskCoverage(mask) {
  if (!mask?.length) return 0;
  let active = 0;
  for (let i = 0; i < mask.length; i += 1) {
    if (mask[i] > 0.16) active += 1;
  }
  return active / mask.length;
}

function checkerCellCenter(index, columns, rows, width, height) {
  const cellWidth = width / columns;
  const cellHeight = height / rows;
  const column = index % columns;
  const row = Math.floor(index / columns);
  return {
    x: (column + 0.5) * cellWidth,
    y: (row + 0.5) * cellHeight,
  };
}

function checkerTransitionFactor(dt, speed) {
  return 1 - Math.exp(-Math.max(0, speed) * dt);
}

function installDebugMarker() {
  if (!PARTICLE_DEBUG) return;

  const apply = () => {
    if (document.getElementById("particle-debug-badge")) return;

    const container = document.createElement("div");
    container.id = "particle-debug-container";
    Object.assign(container.style, {
      position: "fixed",
      top: "12px",
      left: "12px",
      zIndex: "99999",
      pointerEvents: "auto",
      fontFamily: "monospace",
    });

    const badge = document.createElement("div");
    badge.id = "particle-debug-badge";
    Object.assign(badge.style, {
      padding: "8px 12px",
      borderRadius: "999px",
      background: "rgba(255, 0, 170, 0.92)",
      color: "#fff",
      fontSize: "16px",
      letterSpacing: "0.04em",
      boxShadow: "0 0 0 3px rgba(128, 0, 255, 0.5)",
      cursor: "pointer",
      userSelect: "none",
    });

    const meta = document.createElement("div");
    meta.id = "particle-debug-meta";
    meta.textContent = "waiting for mask";
    Object.assign(meta.style, {
      fontSize: "12px",
      color: "rgba(255,255,255,0.75)",
      marginTop: "8px",
      maxWidth: "360px",
    });

    const overlay = document.createElement("canvas");
    overlay.id = "particle-debug-mask-overlay";
    Object.assign(overlay.style, {
      position: "fixed",
      inset: "0",
      width: "100vw",
      height: "100vh",
      pointerEvents: "none",
      zIndex: "99990",
      opacity: "1",
      mixBlendMode: "normal",
    });

    container.appendChild(badge);
    container.appendChild(meta);
    document.body.appendChild(container);
    document.body.appendChild(overlay);
    document.body.style.outline = "4px solid rgba(128, 0, 255, 0.85)";
  };

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", apply, { once: true });
  } else {
    apply();
  }
}

class SlideParticles {
  constructor() {
    this.reveal = null;
    this.revealElement = null;
    this.canvas = null;
    this.context = null;
    this.maskCanvas = document.createElement("canvas");
    this.maskContext = this.maskCanvas.getContext("2d", {
      willReadFrequently: true,
    });
    this.analysisCanvas = document.createElement("canvas");
    this.analysisContext = this.analysisCanvas.getContext("2d", {
      willReadFrequently: true,
    });
    this.debugCanvas = null;
    this.debugContext = null;
    this.debugMeta = null;
    this.debugBadge = null;
    this.debugView = "original";
    this.metrics = { width: 1, height: 1, scaledWidth: 1, scaledHeight: 1 };
    this.fieldMetrics = { width: 1, height: 1 };
    this.mask = null;
    this.field = null;
    this.blurredMask = null;
    this.lastMaskMode = "waiting";
    this.lastMaskCoverage = 0;
    this.particleRgb = [111, 232, 255];
    this.glowRgb = [0, 212, 170];
    this.blendMode = "screen";
    this.orbitAnchors = [];
    this.fieldLineCurves = [];
    this.particles = [];
    this.pigmentSprites = null;
    this.pastelCellSprites = null;
    this.pastelCells = [];
    this.pastelCellsSlide = null;
    this.motionPreference = window.matchMedia("(prefers-reduced-motion: reduce)");
    this.checkerCellMask = null;
    this.checkerParticleMap = [];
    this.refreshHandle = 0;
    this.frameHandle = 0;
    this.lastFrameTime = performance.now();
    this.svgSourceInfoCache = new Map();
    this.supported = Boolean(this.maskContext && this.analysisContext);
  }

  resolveParticleTheme() {
    const el = this.getActiveSlide() || document.body;
    const lum = resolveBackgroundLuminance(el);
    if (lum > 0.5) {
      this.particleRgb = [20, 80, 180];
      this.glowRgb = [0, 120, 110];
      this.blendMode = "multiply";
    } else {
      this.particleRgb = [111, 232, 255];
      this.glowRgb = [0, 212, 170];
      this.blendMode = "screen";
    }
    if (PARTICLE_CONFIG.particleRenderMode === "pigment" || this.isPastelCellsMode()) this.blendMode = "normal";
    if (this.canvas) {
      this.canvas.style.mixBlendMode = this.blendMode;
      if (this.isPastelCellsMode()) this.canvas.style.setProperty("z-index", "3", "important");
      else if (PARTICLE_CONFIG.particleRenderMode !== "pigment") this.canvas.style.removeProperty("z-index");
    }
  }

  init(reveal) {
    if (!this.supported) return;
    this.reveal = reveal;
    this.revealElement = reveal.getRevealElement();
    if (!this.revealElement) return;

    this.resolveParticleTheme();
    this.ensureCanvas();
    this.hydrateDebugElements();
    this.resize();
    this.seedParticles();
    this.bindEvents();
    this.scheduleAnalysis(0);
    this.animate();
  }

  ensureCanvas() {
    if (this.canvas) return;
    this.revealElement.querySelectorAll(".slide-particles-layer").forEach((layer) => layer.remove());

    this.canvas = document.createElement("canvas");
    this.canvas.className = "slide-particles-layer";
    this.canvas.setAttribute("aria-hidden", "true");
    Object.assign(this.canvas.style, {
      position: "absolute",
      inset: "0",
      display: "block",
      width: "100%",
      height: "100%",
      margin: "0",
      padding: "0",
      border: "0",
      pointerEvents: "none",
      zIndex: "1",
      opacity: "0.9",
      mixBlendMode: this.blendMode,
      background: PARTICLE_DEBUG ? "rgba(128, 0, 255, 0.18)" : "transparent",
    });
    if (["pigment", "pastel-cells"].includes(PARTICLE_CONFIG.particleRenderMode)) {
      // reveal-fixes.css resets layer stacking with !important. This opt-in,
      // pointer-transparent layer must remain above opaque slide surfaces.
      this.canvas.style.setProperty("z-index", "3", "important");
    }
    this.context = this.canvas.getContext("2d");
    this.revealElement.insertBefore(this.canvas, this.revealElement.firstChild);
  }

  hydrateDebugElements() {
    if (!PARTICLE_DEBUG) return;
    this.debugCanvas = document.getElementById("particle-debug-mask-overlay");
    this.debugContext = this.debugCanvas?.getContext("2d") || null;
    this.debugMeta = document.getElementById("particle-debug-meta");
    this.debugBadge = document.getElementById("particle-debug-badge");
    if (this.debugBadge && !this.debugBadge.dataset.particleDebugBound) {
      this.debugBadge.dataset.particleDebugBound = "true";
      this.debugBadge.addEventListener("click", () => {
        const currentIndex = DEBUG_VIEW_SEQUENCE.indexOf(this.debugView);
        this.debugView =
          DEBUG_VIEW_SEQUENCE[(currentIndex + 1) % DEBUG_VIEW_SEQUENCE.length];
        this.updateDebugBadge();
        this.updateDebugPreview();
      });
    }
    this.updateDebugBadge();
  }

  updateDebugBadge() {
    if (!this.debugBadge) return;
    this.debugBadge.textContent = `particle-debug active · ${this.debugView}`;
  }

  resize() {
    if (!this.canvas || !this.context) return;
    const rect = this.revealElement.getBoundingClientRect();
    const ratio = window.devicePixelRatio || 1;
    this.metrics.width = Math.max(1, Math.round(rect.width));
    this.metrics.height = Math.max(1, Math.round(rect.height));
    this.canvas.width = Math.max(1, Math.round(rect.width * ratio));
    this.canvas.height = Math.max(1, Math.round(rect.height * ratio));
    this.canvas.style.width = `${rect.width}px`;
    this.canvas.style.height = `${rect.height}px`;
    this.context.setTransform(ratio, 0, 0, ratio, 0, 0);

    const rawScaledWidth = Math.round(this.metrics.width / PARTICLE_CONFIG.downsampleFactor);
    const rawScaledHeight = Math.round(this.metrics.height / PARTICLE_CONFIG.downsampleFactor);
    this.metrics.scaledWidth = clamp(
      rawScaledWidth,
      PARTICLE_CONFIG.minAnalysisWidth,
      PARTICLE_CONFIG.maxAnalysisWidth,
    );
    this.metrics.scaledHeight = clamp(
      rawScaledHeight,
      PARTICLE_CONFIG.minAnalysisHeight,
      PARTICLE_CONFIG.maxAnalysisHeight,
    );

    this.maskCanvas.width = this.metrics.width;
    this.maskCanvas.height = this.metrics.height;
    this.analysisCanvas.width = this.metrics.scaledWidth;
    this.analysisCanvas.height = this.metrics.scaledHeight;

    if (PARTICLE_DEBUG && this.debugCanvas) {
      this.debugCanvas.width = Math.max(1, Math.round(window.innerWidth * ratio));
      this.debugCanvas.height = Math.max(1, Math.round(window.innerHeight * ratio));
      this.debugCanvas.style.width = `${window.innerWidth}px`;
      this.debugCanvas.style.height = `${window.innerHeight}px`;
      this.debugContext?.setTransform(ratio, 0, 0, ratio, 0, 0);
    }
  }

  bindEvents() {
    this.reveal.on("ready", () => this.scheduleAnalysis(PARTICLE_CONFIG.readyDelayMs));
    this.reveal.on("slidechanged", () => this.scheduleAnalysis(PARTICLE_CONFIG.slideChangeDelayMs));
    this.reveal.on("slidetransitionend", () => this.scheduleAnalysis(50));
    this.reveal.on("fragmentshown", () => this.scheduleAnalysis(PARTICLE_CONFIG.fragmentDelayMs));
    this.reveal.on("fragmenthidden", () => this.scheduleAnalysis(PARTICLE_CONFIG.fragmentDelayMs));
    window.addEventListener("resize", () => {
      this.resize();
      this.scheduleAnalysis(PARTICLE_CONFIG.resizeDelayMs);
    });
  }

  getActiveSlide() {
    const slide = this.reveal?.getCurrentSlide();
    if (PARTICLE_CONFIG.particleRenderMode === "pigment" && !this.isPastelCellsMode()) {
      return slide?.matches("[data-particles='on']") ? slide : null;
    }
    if (this.isPastelCellsMode() && slide?.matches("[data-particles='on']")) return slide;
    if (!slide || slide.id === "title-slide") return null;
    if (slide.matches("[data-particles='off']")) return null;
    return slide;
  }

  getRefreshDelay(slide = this.getActiveSlide()) {
    if (!slide) return null;
    if (slide.querySelector("video, canvas, iframe, [data-particles-refresh='interval']")) {
      return PARTICLE_CONFIG.analysisIntervalMs;
    }
    return null;
  }

  isPastelCellsMode() {
    return PARTICLE_CONFIG.particleRenderMode === "pastel-cells" ||
      this.reveal?.getCurrentSlide()?.dataset.particleTheme === "pastel-cells";
  }

  isCheckerMode() {
    return String(PARTICLE_CONFIG.particleRenderMode || "circle").toLowerCase() === "checker";
  }

  isContourMode() {
    return String(PARTICLE_CONFIG.particleConnectionMode || "none").toLowerCase() === "contour-lines";
  }

  isGravitationalContourTheme() {
    return PARTICLE_THEME_KEY === "gravitational-lines" && this.isContourMode();
  }

  getGridDimensions() {
    const cellWidth = Math.max(1, Number(PARTICLE_CONFIG.particleGridCellWidth || 20));
    const cellHeight = Math.max(1, Number(PARTICLE_CONFIG.particleGridCellHeight || 20));
    return {
      columns: Math.max(1, Math.round(this.metrics.width / cellWidth)),
      rows: Math.max(1, Math.round(this.metrics.height / cellHeight)),
    };
  }

  scheduleAnalysis(delayMs) {
    // Free drifting pigment needs no content masks or periodic slide analysis.
    if (PARTICLE_CONFIG.particleRenderMode === "pigment" && !this.isPastelCellsMode()) return;
    if (delayMs == null) return;
    window.clearTimeout(this.refreshHandle);
    this.refreshHandle = window.setTimeout(async () => {
      const slide = this.getActiveSlide();
      if (slide && this.isPastelCellsMode()) {
        // Reveal translates sections during transitions. Analyse after they settle
        // so cached cells line up with the final CSS grid, not an intermediate frame.
        const animations = [...(slide.getAnimations?.() || []),
          ...(slide.parentElement?.getAnimations?.() || [])].filter(a => a.playState === "running");
        if (animations.length) await Promise.allSettled(animations.map(a => a.finished));
        if (slide !== this.getActiveSlide()) return;
      }
      this.recomputeField();
    }, delayMs);
  }

  isSvgImageElement(element) {
    return (
      element instanceof HTMLImageElement &&
      typeof element.currentSrc === "string" &&
      /\.svg(?:[?#].*)?$/i.test(element.currentSrc || element.src || "")
    );
  }

  getSvgSourceInfo(element) {
    if (!this.isSvgImageElement(element)) return null;
    const sourceUrl = new URL(element.currentSrc || element.src, document.baseURI).href;
    const cached = this.svgSourceInfoCache.get(sourceUrl);
    if (cached) {
      return cached.status === "ready" ? cached.value : null;
    }

    const pending = { status: "pending", value: null };
    this.svgSourceInfoCache.set(sourceUrl, pending);
    fetch(sourceUrl)
      .then((response) => (response.ok ? response.text() : Promise.reject(new Error("svg-fetch"))))
      .then((svgText) => {
        const measured = this.measureSvgSourceInfo(svgText);
        this.svgSourceInfoCache.set(sourceUrl, {
          status: "ready",
          value: measured,
        });
        this.scheduleAnalysis(0);
      })
      .catch(() => {
        this.svgSourceInfoCache.set(sourceUrl, {
          status: "ready",
          value: null,
        });
      });
    return null;
  }

  measureSvgSourceInfo(svgText) {
    if (!svgText) return null;
    const parser = new DOMParser();
    const parsed = parser.parseFromString(svgText, "image/svg+xml");
    const svg = parsed.documentElement;
    if (!(svg instanceof SVGSVGElement)) return null;

    const parseLength = (value, fallback = 0) => {
      if (value == null || value === "") return fallback;
      const numeric = Number.parseFloat(String(value));
      return Number.isFinite(numeric) ? numeric : fallback;
    };

    const viewBox = svg.viewBox?.baseVal;
    const sourceBox = viewBox && viewBox.width > 0 && viewBox.height > 0
      ? {
          x: viewBox.x,
          y: viewBox.y,
          width: viewBox.width,
          height: viewBox.height,
        }
      : {
          x: 0,
          y: 0,
          width: parseLength(svg.getAttribute("width"), 1),
          height: parseLength(svg.getAttribute("height"), 1),
        };
    if (sourceBox.width <= 0 || sourceBox.height <= 0) return null;

    const mount = document.createElement("div");
    Object.assign(mount.style, {
      position: "absolute",
      left: "-99999px",
      top: "-99999px",
      width: "0",
      height: "0",
      overflow: "hidden",
      pointerEvents: "none",
      visibility: "hidden",
    });
    const measuredSvg = document.createElementNS("http://www.w3.org/2000/svg", "svg");
    mount.appendChild(measuredSvg);
    mount.innerHTML = svg.outerHTML;
    document.body.appendChild(mount);

    const liveSvg = mount.querySelector("svg");
    if (!(liveSvg instanceof SVGSVGElement)) {
      mount.remove();
      return null;
    }

    const graphics = Array.from(
      liveSvg.querySelectorAll("path, rect, circle, ellipse, line, polyline, polygon, text, image, use"),
    ).filter((node) => node instanceof SVGGraphicsElement);

    let minX = Number.POSITIVE_INFINITY;
    let minY = Number.POSITIVE_INFINITY;
    let maxX = Number.NEGATIVE_INFINITY;
    let maxY = Number.NEGATIVE_INFINITY;

    graphics.forEach((node) => {
      if (!(node instanceof SVGGraphicsElement)) return;
      if (node.closest("defs, clipPath, mask, pattern, marker, symbol")) return;
      const style = getComputedStyle(node);
      if (
        style.display === "none" ||
        style.visibility === "hidden" ||
        Number.parseFloat(style.opacity || "1") <= 0.03
      ) {
        return;
      }

      let box;
      try {
        box = node.getBBox();
      } catch (_error) {
        return;
      }
      if (!box || box.width <= 0.5 || box.height <= 0.5) return;

      const widthRatio = box.width / sourceBox.width;
      const heightRatio = box.height / sourceBox.height;
      const fillColor = parseCssColor(style.fill);
      const strokeColor = parseCssColor(style.stroke);
      const fillLum = fillColor ? relativeLuminance(fillColor) : null;
      const strokeLum = strokeColor ? relativeLuminance(strokeColor) : null;
      const fillOpacity = Number.parseFloat(style.fillOpacity || "1");
      const strokeOpacity = Number.parseFloat(style.strokeOpacity || "1");
      const hasFill = style.fill !== "none" && fillOpacity > 0.03;
      const hasStroke =
        style.stroke !== "none" &&
        Number.parseFloat(style.strokeWidth || "0") > 0 &&
        strokeOpacity > 0.03;
      const isLargeBackdrop =
        widthRatio > 0.9 &&
        heightRatio > 0.9 &&
        (
          (hasFill && fillLum != null && fillLum > 0.72) ||
          (hasFill && fillOpacity < 0.14) ||
          (!hasFill && hasStroke && strokeLum != null && strokeLum > 0.72)
        );
      if (isLargeBackdrop) return;

      if (box.x < minX) minX = box.x;
      if (box.y < minY) minY = box.y;
      if (box.x + box.width > maxX) maxX = box.x + box.width;
      if (box.y + box.height > maxY) maxY = box.y + box.height;
    });

    mount.remove();
    if (!Number.isFinite(minX) || !Number.isFinite(minY) || !Number.isFinite(maxX) || !Number.isFinite(maxY)) {
      return null;
    }

    return {
      viewBox: sourceBox,
      bounds: {
        minX,
        minY,
        maxX,
        maxY,
      },
    };
  }

  recomputeField() {
    const slide = this.getActiveSlide();
    if (!slide) {
      this.mask = null;
    this.field = null;
    this.blurredMask = null;
    this.fieldLineCurves = [];
    this.updateDebugPreview();
    return;
    }
    this.resolveParticleTheme();
    this.deriveFieldFromGeometry(slide);
    if (this.isPastelCellsMode()) this.rebuildPastelCells(slide);
    this.scheduleAnalysis(this.getRefreshDelay(slide));
  }

  paintTextGeometryMask(slide, ctx, width, height, scaleX, scaleY) {
    const revealRect = this.revealElement.getBoundingClientRect();
    const metricsCanvas = document.createElement("canvas");
    const metricsContext = metricsCanvas.getContext("2d");
    const isVisible = (element) => {
      const style = getComputedStyle(element);
      return (
        style.display !== "none" &&
        style.visibility !== "hidden" &&
        Number.parseFloat(style.opacity || "1") > 0.02
      );
    };

    const measureLargeTextRect = (textNode, rect, style) => {
      if (!metricsContext || !style) return null;
      const text = textNode.textContent?.trim();
      if (!text) return null;

      const fontStyle = style.fontStyle || "normal";
      const fontVariant = style.fontVariant || "normal";
      const fontWeight = style.fontWeight || "400";
      const fontSize = style.fontSize || "16px";
      const fontFamily = style.fontFamily || "sans-serif";
      metricsContext.font = `${fontStyle} ${fontVariant} ${fontWeight} ${fontSize} ${fontFamily}`;

      const metrics = metricsContext.measureText(text);
      if (
        !Number.isFinite(metrics.actualBoundingBoxAscent) ||
        !Number.isFinite(metrics.actualBoundingBoxDescent) ||
        metrics.actualBoundingBoxAscent <= 0
      ) {
        return null;
      }

      const ascent = metrics.actualBoundingBoxAscent;
      const descent = Math.max(0, metrics.actualBoundingBoxDescent);
      const inkHeight = ascent + descent;
      const lineHeight =
        Number.parseFloat(style.lineHeight || "0") || rect.height;
      const verticalSlack = Math.max(0, lineHeight - inkHeight);
      const topBias = Math.min(verticalSlack * 0.72, ascent * 0.08);
      const fontVariantCaps = (style.fontVariantCaps || "").toLowerCase();
      const textTransform = (style.textTransform || "").toLowerCase();
      const styleSuggestsCaps =
        fontVariantCaps.includes("small-caps") ||
        fontVariantCaps.includes("all-small-caps") ||
        fontVariantCaps.includes("all-petite-caps") ||
        fontVariantCaps.includes("petite-caps") ||
        textTransform === "uppercase";
      const contentLooksUpper =
        text === text.toUpperCase() &&
        /[A-ZÄÖÜ0-9%]/.test(text) &&
        !/[gjpqyß]/.test(text);
      const isUpperLike = styleSuggestsCaps || contentLooksUpper;
      const effectiveDescent = isUpperLike ? Math.min(descent, 1) : descent;

      return {
        left: rect.left,
        top: rect.top + topBias,
        width: rect.width,
        height: Math.max(
          1,
          ascent + effectiveDescent - Math.min(effectiveDescent * 0.2, 1),
        ),
      };
    };
    const excluded = (element) => element.closest(PARTICLE_CONFIG.excludeSelector);

    const paintRect = (rect, options = {}) => {
      const {
        padding = 0.1,
        roundness = 0.3,
        minWidth = 0.8,
        minHeight = 1,
        weight = 1,
      } = options;
      const localX = (rect.left - revealRect.left) * scaleX;
      const localY = (rect.top - revealRect.top) * scaleY;
      const localW = Math.max(minWidth, rect.width * scaleX);
      const localH = Math.max(minHeight, rect.height * scaleY);
      if (localW <= 0.4 || localH <= 0.4) return;
      ctx.fillStyle = `rgba(255, 255, 255, ${clamp(weight, 0, 1)})`;
      paintRoundedRect(
        ctx,
        localX - padding,
        localY - padding,
        localW + padding * 2,
        localH + padding * 2,
        roundness,
      );
    };

    const walker = document.createTreeWalker(slide, NodeFilter.SHOW_TEXT, {
      acceptNode: (node) => {
        if (!node.textContent || !node.textContent.trim()) {
          return NodeFilter.FILTER_REJECT;
        }
        const parent = node.parentElement;
        if (!parent || excluded(parent) || !isVisible(parent)) {
          return NodeFilter.FILTER_REJECT;
        }
        return NodeFilter.FILTER_ACCEPT;
      },
    });

    let textNode = walker.nextNode();
    while (textNode) {
      const range = document.createRange();
      range.selectNodeContents(textNode);
      Array.from(range.getClientRects()).forEach((rect) => {
        const parent = textNode.parentElement;
        const style = parent ? getComputedStyle(parent) : null;
        const fontSizePx = style ? Number.parseFloat(style.fontSize || "16") : 16;
        if (fontSizePx > PARTICLE_CONFIG.textSupportMaxFontPx) return;
        const fontWeight = style ? Number.parseInt(style.fontWeight || "400", 10) : 400;
        const scaledFont = Math.max(1.4, fontSizePx * scaleY);
        const isHeading = parent ? /^H[1-6]$/.test(parent.tagName) : false;
        const isLargeText = fontSizePx >= 42 || rect.height * scaleY >= 28;
        if (isHeading && !PARTICLE_CONFIG.textSupportIncludeHeadings) return;
        const metricRect = isLargeText
          ? measureLargeTextRect(textNode, rect, style)
          : null;
        paintRect(metricRect || rect, {
          padding: isLargeText
            ? Math.max(0.04, scaledFont * 0.006)
            : isHeading
              ? Math.max(0.12, scaledFont * 0.014)
              : Math.max(0.08, scaledFont * 0.012),
          roundness: Math.max(0.3, scaledFont * 0.03),
          minWidth: Math.max(0.8, Math.min(6, rect.width * scaleX * 0.04)),
          minHeight: isLargeText
            ? Math.max(0.46, scaledFont * 0.34)
            : isHeading
              ? Math.max(0.95, scaledFont * 0.68)
              : Math.max(0.82, scaledFont * (fontWeight >= 600 ? 0.58 : 0.54)),
          weight: isHeading ? 1 : fontWeight >= 600 ? 0.96 : 0.9,
        });
      });
      textNode = walker.nextNode();
    }
  }

  paintVisualGeometryMask(slide, ctx, width, height, scaleX, scaleY) {
    const revealRect = this.revealElement.getBoundingClientRect();
    const slideBackgroundLuminance = resolveBackgroundLuminance(slide);
    const isVisible = (element) => {
      const style = getComputedStyle(element);
      return (
        style.display !== "none" &&
        style.visibility !== "hidden" &&
        Number.parseFloat(style.opacity || "1") > 0.02
      );
    };
    const excluded = (element) => element.closest(PARTICLE_CONFIG.excludeSelector);
    const wrapperMostlyContainsSingleVisual = (element) => {
      if (!(element instanceof HTMLElement)) return false;
      if (!element.matches(".quarto-figure, figure, .cell-output-display")) {
        return false;
      }
      const mediaCandidates = Array.from(
        element.querySelectorAll("img, svg, canvas, video"),
      ).filter((node) => node instanceof Element);
      if (mediaCandidates.length !== 1) return false;
      const media = mediaCandidates[0];
      if (!(media instanceof Element)) return false;
      const textContent = Array.from(element.childNodes)
        .filter((node) => node.nodeType === Node.TEXT_NODE)
        .map((node) => node.textContent || "")
        .join("")
        .trim();
      if (textContent.length > 0) return false;
      const wrapperRect = element.getBoundingClientRect();
      const mediaRect = media.getBoundingClientRect();
      if (wrapperRect.width < 2 || wrapperRect.height < 2) return false;
      const wrapperArea = wrapperRect.width * wrapperRect.height;
      const mediaArea = mediaRect.width * mediaRect.height;
      if (wrapperArea <= 1 || mediaArea <= 1) return false;
      const widthRatio = mediaRect.width / wrapperRect.width;
      const heightRatio = mediaRect.height / wrapperRect.height;
      const areaRatio = mediaArea / wrapperArea;
      return (
        (widthRatio > 0.58 && heightRatio > 0.58 && areaRatio > 0.42) ||
        areaRatio > 0.55
      );
    };

    const paintRect = (rect, options = {}) => {
      const {
        padding = 1.2,
        roundness = 1.6,
        minWidth = 1.6,
        minHeight = 1.8,
        weight = 0.22,
      } = options;
      const localX = (rect.left - revealRect.left) * scaleX;
      const localY = (rect.top - revealRect.top) * scaleY;
      const localW = Math.max(minWidth, rect.width * scaleX);
      const localH = Math.max(minHeight, rect.height * scaleY);
      if (localW <= 0.4 || localH <= 0.4) return;
      ctx.fillStyle = `rgba(255, 255, 255, ${clamp(weight, 0, 1)})`;
      paintRoundedRect(
        ctx,
        localX - padding,
        localY - padding,
        localW + padding * 2,
        localH + padding * 2,
        roundness,
      );
    };

    const paintImageAlphaMask = (element, options = {}) => {
      if (
        !(
          element instanceof HTMLImageElement ||
          element instanceof HTMLCanvasElement ||
          element instanceof HTMLVideoElement
        )
      ) {
        return false;
      }
      if (element instanceof HTMLImageElement && !element.complete) return false;
      if (element instanceof HTMLVideoElement && element.readyState < 2) return false;

      const rect = element.getBoundingClientRect();
      if (rect.width < 2 || rect.height < 2) return false;

      const localX = (rect.left - revealRect.left) * scaleX;
      const localY = (rect.top - revealRect.top) * scaleY;
      const localW = Math.max(1, Math.round(rect.width * scaleX));
      const localH = Math.max(1, Math.round(rect.height * scaleY));
      if (localW <= 1 || localH <= 1) return false;

      const maskCanvas = document.createElement("canvas");
      maskCanvas.width = localW;
      maskCanvas.height = localH;
      const maskContext = maskCanvas.getContext("2d", {
        willReadFrequently: true,
      });
      if (!maskContext) return false;

      const isSvgImage = this.isSvgImageElement(element);
      const svgSourceInfo = isSvgImage ? this.getSvgSourceInfo(element) : null;

      try {
        maskContext.clearRect(0, 0, localW, localH);
        maskContext.drawImage(element, 0, 0, localW, localH);
        const imageData = maskContext.getImageData(0, 0, localW, localH);
        const { data } = imageData;
        let occupiedPixels = 0;
        let minX = localW;
        let minY = localH;
        let maxX = -1;
        let maxY = -1;
        let strongMinX = localW;
        let strongMinY = localH;
        let strongMaxX = -1;
        let strongMaxY = -1;
        let strongOccupiedPixels = 0;
        const cropValueThreshold = isSvgImage ? 52 : 18;

        for (let offset = 0; offset < data.length; offset += 4) {
          const alpha = data[offset + 3] / 255;
          if (alpha < 0.02) {
            data[offset] = 0;
            data[offset + 1] = 0;
            data[offset + 2] = 0;
            data[offset + 3] = 0;
            continue;
          }

          const luminance = relativeLuminance({
            r: data[offset],
            g: data[offset + 1],
            b: data[offset + 2],
          });
          const contrast = Math.abs(luminance - slideBackgroundLuminance);
          const energy = clamp(alpha * (0.28 + contrast * 1.15), 0, 1);
          const value = Math.round(energy * 255);
          if (value > 10) {
            occupiedPixels += 1;
            const pixelIndex = offset / 4;
            const x = pixelIndex % localW;
            const y = Math.floor(pixelIndex / localW);
            if (x < minX) minX = x;
            if (y < minY) minY = y;
            if (x > maxX) maxX = x;
            if (y > maxY) maxY = y;
          }
          if (value >= cropValueThreshold) {
            strongOccupiedPixels += 1;
            const pixelIndex = offset / 4;
            const x = pixelIndex % localW;
            const y = Math.floor(pixelIndex / localW);
            if (x < strongMinX) strongMinX = x;
            if (y < strongMinY) strongMinY = y;
            if (x > strongMaxX) strongMaxX = x;
            if (y > strongMaxY) strongMaxY = y;
          }
          data[offset] = value;
          data[offset + 1] = value;
          data[offset + 2] = value;
          data[offset + 3] = value;
        }

        if (occupiedPixels === 0) return false;
        maskContext.putImageData(imageData, 0, 0);
        if (strongOccupiedPixels > 0) {
          minX = strongMinX;
          minY = strongMinY;
          maxX = strongMaxX;
          maxY = strongMaxY;
        }
        if (
          svgSourceInfo?.bounds &&
          svgSourceInfo.viewBox.width > 0 &&
          svgSourceInfo.viewBox.height > 0
        ) {
          const normalizedMinX =
            (svgSourceInfo.bounds.minX - svgSourceInfo.viewBox.x) / svgSourceInfo.viewBox.width;
          const normalizedMinY =
            (svgSourceInfo.bounds.minY - svgSourceInfo.viewBox.y) / svgSourceInfo.viewBox.height;
          const normalizedMaxX =
            (svgSourceInfo.bounds.maxX - svgSourceInfo.viewBox.x) / svgSourceInfo.viewBox.width;
          const normalizedMaxY =
            (svgSourceInfo.bounds.maxY - svgSourceInfo.viewBox.y) / svgSourceInfo.viewBox.height;
          minX = clamp(Math.floor(normalizedMinX * localW), 0, localW - 1);
          minY = clamp(Math.floor(normalizedMinY * localH), 0, localH - 1);
          maxX = clamp(Math.ceil(normalizedMaxX * localW), 0, localW - 1);
          maxY = clamp(Math.ceil(normalizedMaxY * localH), 0, localH - 1);
        }
        const cropPadding = 1;
        const cropX = clamp(minX - cropPadding, 0, localW - 1);
        const cropY = clamp(minY - cropPadding, 0, localH - 1);
        const cropRight = clamp(maxX + cropPadding + 1, 1, localW);
        const cropBottom = clamp(maxY + cropPadding + 1, 1, localH);
        const cropW = Math.max(1, cropRight - cropX);
        const cropH = Math.max(1, cropBottom - cropY);
        const destX = localX + (cropX / localW) * (rect.width * scaleX);
        const destY = localY + (cropY / localH) * (rect.height * scaleY);
        const destW = (cropW / localW) * (rect.width * scaleX);
        const destH = (cropH / localH) * (rect.height * scaleY);
        ctx.drawImage(
          maskCanvas,
          cropX,
          cropY,
          cropW,
          cropH,
          destX,
          destY,
          destW,
          destH,
        );
        return true;
      } catch (_error) {
        return false;
      }
    };

    const paintSvgGeometryMask = (element) => {
      if (!(element instanceof SVGSVGElement)) return false;

      const leafSelector = [
        "path",
        "rect",
        "circle",
        "ellipse",
        "line",
        "polyline",
        "polygon",
        "text",
        "image",
        "use",
      ].join(", ");
      const leaves = Array.from(element.querySelectorAll(leafSelector)).filter(
        (node) => node instanceof SVGGraphicsElement,
      );
      if (!leaves.length) return false;

      let painted = false;
      leaves.forEach((node) => {
        if (!(node instanceof SVGGraphicsElement)) return;
        const style = getComputedStyle(node);
        if (
          style.display === "none" ||
          style.visibility === "hidden" ||
          Number.parseFloat(style.opacity || "1") <= 0.02
        ) {
          return;
        }
        const fillOpacity = Number.parseFloat(style.fillOpacity || "1");
        const strokeOpacity = Number.parseFloat(style.strokeOpacity || "1");
        const hasFill = style.fill !== "none" && fillOpacity > 0.02;
        const hasStroke =
          style.stroke !== "none" &&
          Number.parseFloat(style.strokeWidth || "0") > 0 &&
          strokeOpacity > 0.02;
        if (!hasFill && !hasStroke) return;

        const rect = node.getBoundingClientRect();
        if (rect.width < 1 || rect.height < 1) return;

        const luminance =
          style.fill !== "none"
            ? relativeLuminance(parseCssColor(style.fill))
            : style.stroke !== "none"
              ? relativeLuminance(parseCssColor(style.stroke))
              : slideBackgroundLuminance;
        const contrast = Math.abs(luminance - slideBackgroundLuminance);
        const weight = clamp(
          0.2 +
            contrast * 0.52 +
            (hasStroke && !hasFill ? 0.1 : 0) +
            (hasFill ? fillOpacity * 0.12 : 0),
          0.18,
          0.84,
        );

        paintRect(rect, {
          padding: hasStroke && !hasFill ? 0.4 : 0.75,
          roundness: 1.1,
          minWidth: hasStroke ? 0.9 : 1.2,
          minHeight: hasStroke ? 0.9 : 1.2,
          weight,
        });
        painted = true;
      });
      return painted;
    };

    const sampleImageSignal = (element) => {
      if (
        !(
          element instanceof HTMLImageElement ||
          element instanceof HTMLCanvasElement ||
          element instanceof HTMLVideoElement
        )
      ) {
        return null;
      }
      if (element instanceof HTMLImageElement && !element.complete) return null;
      if (element instanceof HTMLVideoElement && element.readyState < 2) return null;

      const rect = element.getBoundingClientRect();
      if (rect.width < 2 || rect.height < 2) return null;

      const sampleWidth = 24;
      const sampleHeight = Math.max(
        12,
        Math.round(sampleWidth * (rect.height / Math.max(rect.width, 1))),
      );
      const sampleCanvas = document.createElement("canvas");
      sampleCanvas.width = sampleWidth;
      sampleCanvas.height = sampleHeight;
      const sampleContext = sampleCanvas.getContext("2d", {
        willReadFrequently: true,
      });
      if (!sampleContext) return null;

      try {
        sampleContext.clearRect(0, 0, sampleWidth, sampleHeight);
        sampleContext.drawImage(element, 0, 0, sampleWidth, sampleHeight);
        const { data } = sampleContext.getImageData(0, 0, sampleWidth, sampleHeight);
        let visibleEnergy = 0;
        let occupiedPixels = 0;
        for (let offset = 0; offset < data.length; offset += 4) {
          const alpha = data[offset + 3] / 255;
          if (alpha < 0.03) continue;
          const luminance = relativeLuminance({
            r: data[offset],
            g: data[offset + 1],
            b: data[offset + 2],
          });
          const contrast = Math.abs(luminance - slideBackgroundLuminance);
          const pixelEnergy = alpha * contrast;
          visibleEnergy += pixelEnergy;
          if (pixelEnergy > 0.045) occupiedPixels += 1;
        }

        const totalPixels = data.length / 4;
        if (!totalPixels) return null;
        const meanEnergy = visibleEnergy / totalPixels;
        const occupiedRatio = occupiedPixels / totalPixels;
        return { meanEnergy, occupiedRatio };
      } catch (_error) {
        return null;
      }
    };

    const imageMaskOptions = (element) => {
      const signal = sampleImageSignal(element);
      if (!signal) {
        return {
          padding: 0.7,
          roundness: 1.1,
          weight: 0.42,
        };
      }

      const density = clamp(signal.occupiedRatio, 0, 1);
      const visibility = clamp(signal.meanEnergy * 5.5, 0, 1);
      const strength = clamp(visibility * 0.68 + density * 0.55, 0.14, 0.96);
      return {
        padding: clamp(1.05 - strength * 0.55, 0.35, 0.95),
        roundness: clamp(0.9 + (1 - density) * 0.5, 0.85, 1.45),
        weight: clamp(0.24 + strength * 0.62, 0.24, 0.88),
      };
    };

    const visualSelectors = [
      "img",
      "svg",
      "canvas",
      "video",
      "iframe",
      "table",
      ".callout",
      ".cell-output-display",
      ".quarto-figure",
    ];
    visualSelectors.forEach((selector) => {
      slide.querySelectorAll(selector).forEach((element) => {
        if (!(element instanceof Element)) return;
        if (excluded(element) || !isVisible(element)) return;
        if (wrapperMostlyContainsSingleVisual(element)) return;
        const isCallout = element.matches(".callout");
        const isImageLike =
          element.matches("img") ||
          element.matches("canvas") ||
          element.matches("video");
        const isSvg = element instanceof SVGSVGElement;
        const imageOptions = isImageLike ? imageMaskOptions(element) : null;
        if (isImageLike && paintImageAlphaMask(element, imageOptions)) return;
        if (isSvg) {
          if (paintSvgGeometryMask(element)) return;
          paintRect(element.getBoundingClientRect(), {
            padding: 0.8,
            roundness: 1.2,
            weight: 0.32,
          });
          return;
        }
        paintRect(element.getBoundingClientRect(), {
          padding: isImageLike
            ? imageOptions.padding
            : isCallout
              ? 1.8
              : 1.2,
          roundness: isImageLike
            ? imageOptions.roundness
            : isCallout
              ? 2.4
              : 1.6,
          weight: isImageLike ? imageOptions.weight : isCallout ? 0.28 : 0.22,
        });
      });
    });
  }

  paintPlotlyGeometryMask(slide, ctx, width, height, scaleX, scaleY) {
    const revealRect = this.revealElement.getBoundingClientRect();

    const isVisible = (element) => {
      const style = getComputedStyle(element);
      return (
        style.display !== "none" &&
        style.visibility !== "hidden" &&
        Number.parseFloat(style.opacity || "1") > 0.02
      );
    };

    const isVisiblePlotlyNode = (node) => {
      if (!(node instanceof SVGGraphicsElement)) return false;
      if (!isVisible(node)) return false;
      if (
        node.closest(".draglayer, .hoverlayer, .zoomlayer, .menulayer, .modebar-container")
      ) {
        return false;
      }
      const style = getComputedStyle(node);
      const fill = style.fill;
      const stroke = style.stroke;
      const opacity = Number.parseFloat(style.opacity || "1");
      const fillOpacity = Number.parseFloat(style.fillOpacity || "1");
      const strokeOpacity = Number.parseFloat(style.strokeOpacity || "1");
      const hasFill =
        fill &&
        fill !== "none" &&
        fill !== "transparent" &&
        fillOpacity > 0.03;
      const hasStroke =
        stroke &&
        stroke !== "none" &&
        stroke !== "transparent" &&
        strokeOpacity > 0.03;
      return opacity > 0.03 && (hasFill || hasStroke);
    };

    const paintRect = (rect, options = {}) => {
      const {
        padding = 0.35,
        roundness = 0.9,
        minWidth = 0.9,
        minHeight = 0.9,
        weight = 0.42,
      } = options;
      const localX = (rect.left - revealRect.left) * scaleX;
      const localY = (rect.top - revealRect.top) * scaleY;
      const localW = Math.max(minWidth, rect.width * scaleX);
      const localH = Math.max(minHeight, rect.height * scaleY);
      if (localW <= 0.3 || localH <= 0.3) return;
      ctx.fillStyle = `rgba(255, 255, 255, ${clamp(weight, 0, 1)})`;
      paintRoundedRect(
        ctx,
        localX - padding,
        localY - padding,
        localW + padding * 2,
        localH + padding * 2,
        roundness,
      );
    };

    const hasMeaningfulPlotlyTrace = (root) => {
      if (!(root instanceof Element)) return false;
      const contentNodes = root.querySelectorAll(
        [
          ".barlayer .point path",
          ".scatterlayer path",
          ".scatterlayer circle",
          ".scatterlayer rect",
          ".boxlayer path",
          ".boxlayer rect",
          ".violinlayer path",
          ".ohlclayer path",
          ".candlesticklayer path",
          ".histogramlayer path",
          ".contourlayer path",
          ".heatmaplayer image",
          ".imagelayer image",
          ".pielayer path",
          ".funnellayer path",
          ".waterfalllayer path",
        ].join(", "),
      );
      return Array.from(contentNodes).some((node) => isVisiblePlotlyNode(node));
    };

    slide.querySelectorAll(".js-plotly-plot, .plotly").forEach((element) => {
      if (!(element instanceof HTMLElement)) return;
      if (!isVisible(element)) return;
      const mainSvg = element.querySelector("svg.main-svg");
      if (mainSvg instanceof SVGSVGElement && hasMeaningfulPlotlyTrace(mainSvg)) {
        const plotAreaRect =
          mainSvg.querySelector(".bglayer .bg") ||
          mainSvg.querySelector(".clips .plotclip rect");
        if (plotAreaRect instanceof SVGGraphicsElement) {
          const plotRect = plotAreaRect.getBoundingClientRect();
          if (plotRect.width > 4 && plotRect.height > 4) {
            paintRect(plotRect, {
              padding: 0.6,
              roundness: 1.3,
              minWidth: 2,
              minHeight: 2,
              weight: 0.18,
            });
          }
        }
      }
      const visualChildren = element.querySelectorAll(
        [
          ".main-svg .bar",
          ".main-svg .point",
          ".main-svg .scatterlayer path",
          ".main-svg .scatterlayer circle",
          ".main-svg .scatterlayer rect",
          ".main-svg .gridlayer path",
          ".main-svg .zerolinelayer path",
          ".main-svg .xaxislayer-above text",
          ".main-svg .yaxislayer-above text",
          ".main-svg .gtitle",
          ".main-svg .xtick text",
          ".main-svg .ytick text",
          ".main-svg .legend text",
          ".main-svg .legend path",
          ".main-svg .legend rect",
          ".main-svg .shapelayer path",
          ".main-svg .shapelayer rect",
          ".main-svg .shapelayer line",
          ".main-svg .imagelayer image",
          ".main-svg .heatmaplayer image",
          ".main-svg .contourlayer path",
          ".main-svg .boxlayer path",
          ".main-svg .boxlayer rect",
          ".main-svg .pielayer path",
          ".main-svg .violinlayer path",
          ".main-svg .ohlclayer path",
          ".main-svg .candlesticklayer path",
          ".main-svg .histogramlayer path",
          ".main-svg .funnellayer path",
          ".main-svg .waterfalllayer path",
        ].join(", "),
      );
      visualChildren.forEach((node) => {
        if (!isVisiblePlotlyNode(node)) return;
        const childRect = node.getBoundingClientRect();
        if (childRect.width <= 0.8 || childRect.height <= 0.8) return;
        paintRect(childRect);
      });
    });
  }

  deriveFieldFromGeometry(slide) {
    const { width, height, scaledWidth, scaledHeight } = this.metrics;
    const previousMask = this.mask ? Array.from(this.mask) : null;
    const revealRect = this.revealElement.getBoundingClientRect();
    const scaleX = width / Math.max(1, revealRect.width);
    const scaleY = height / Math.max(1, revealRect.height);
    const ctx = this.maskContext;

    ctx.clearRect(0, 0, width, height);
    ctx.fillStyle = "#000";
    ctx.fillRect(0, 0, width, height);

    this.paintTextGeometryMask(slide, ctx, width, height, scaleX, scaleY);
    this.paintVisualGeometryMask(slide, ctx, width, height, scaleX, scaleY);
    this.paintPlotlyGeometryMask(slide, ctx, width, height, scaleX, scaleY);

    const imageData = ctx.getImageData(0, 0, width, height);
    const rawMask = new Float32Array(width * height);
    const { data } = imageData;
    for (let i = 0; i < rawMask.length; i += 1) {
      rawMask[i] = clamp(data[i * 4] / 255, 0, 1);
    }

    let blurred = rawMask;
    let reduced;
    if (this.isGravitationalContourTheme()) {
      const midBlur = gaussianBlurMask(
        rawMask,
        width,
        height,
        Number(PARTICLE_CONFIG.particleHeightMapMidRadius || 3),
      );
      const farBlur = gaussianBlurMask(
        rawMask,
        width,
        height,
        Number(PARTICLE_CONFIG.particleHeightMapFarRadius || 11),
      );
      const baseReduced = downsampleMask(rawMask, width, height, scaledWidth, scaledHeight);
      const midReduced = downsampleMask(midBlur, width, height, scaledWidth, scaledHeight);
      const farReduced = downsampleMask(farBlur, width, height, scaledWidth, scaledHeight);
      const normalizedBase = normalizeMask(baseReduced);
      const normalizedMid = normalizeMask(midReduced);
      const normalizedFar = normalizeMask(farReduced);
      reduced = mergeContourHeightMaps(
        normalizedBase,
        normalizedMid,
        normalizedFar,
        Number(PARTICLE_CONFIG.particleHeightMapBlendStrength || 1.35),
      );
      this.blurredMask = { width: scaledWidth, height: scaledHeight, data: reduced.slice() };
      blurred = farBlur;
    } else {
      for (let i = 0; i < 1; i += 1) {
        blurred = blurMask(blurred, width, height);
      }
      this.blurredMask = { width, height, data: blurred.slice() };
      reduced = downsampleMask(blurred, width, height, scaledWidth, scaledHeight);
      for (let i = 0; i < PARTICLE_CONFIG.auraBlurPasses; i += 1) {
        reduced = blurMask(reduced, scaledWidth, scaledHeight);
      }
    }

    let fieldWidth = scaledWidth;
    let fieldHeight = scaledHeight;
    if (this.isCheckerMode()) {
      const { columns, rows } = this.getGridDimensions();
      reduced = downsampleMask(reduced, scaledWidth, scaledHeight, columns, rows);
      fieldWidth = columns;
      fieldHeight = rows;
      this.checkerCellMask = reduced.slice();
    } else {
      this.checkerCellMask = null;
    }

    this.fieldMetrics = { width: fieldWidth, height: fieldHeight };
    this.mask = reduced;
    this.field = buildDistanceField(reduced, fieldWidth, fieldHeight);
    if (this.isCheckerMode()) {
      this.syncCheckerTimersToMask(previousMask, reduced);
    }
    this.rebuildOrbitAnchors();
    if (this.isContourMode()) {
      this.rebuildContourLines();
    } else {
      this.rebuildFieldLines();
    }
    if (!this.isCheckerMode()) {
      this.particles.forEach((particle) => this.assignAnchorIndex(particle));
    }
    this.lastMaskMode = slide.querySelector(".js-plotly-plot, .plotly")
      ? "plotly geometry"
      : "geometry mask";
    this.lastMaskCoverage = computeMaskCoverage(reduced);
    this.updateDebugPreview();
  }

  rebuildOrbitAnchors() {
    this.orbitAnchors = [];
    if (!this.mask || !this.field) return;
    const candidates = [];
    for (let i = 0; i < this.mask.length; i += 1) {
      const maskValue = this.mask[i];
      const distance = this.field[i];
      if (maskValue < 0.1) continue;
      if (
        distance < PARTICLE_CONFIG.particleRespawnMinDistance ||
        distance > PARTICLE_CONFIG.orbitTarget + 1.8
      ) {
        continue;
      }
      candidates.push(i);
    }
    if (!candidates.length) return;
    const targetCount = Math.min(PARTICLE_CONFIG.anchorTargetCount, candidates.length);
    const step = Math.max(1, Math.floor(candidates.length / targetCount));
    for (let i = 0; i < candidates.length && this.orbitAnchors.length < targetCount; i += step) {
      const sampleIndex = candidates[i];
      const sx = sampleIndex % this.fieldMetrics.width;
      const sy = Math.floor(sampleIndex / this.fieldMetrics.width);
      this.orbitAnchors.push({
        x: ((sx + 0.5) / this.fieldMetrics.width) * this.metrics.width,
        y: ((sy + 0.5) / this.fieldMetrics.height) * this.metrics.height,
      });
    }
  }

  assignAnchorIndex(particle) {
    if (!this.orbitAnchors.length) {
      particle.anchorIndex = -1;
      return;
    }
    let bestIndex = 0;
    let bestDistance = Number.POSITIVE_INFINITY;
    for (let i = 0; i < this.orbitAnchors.length; i += 1) {
      const anchor = this.orbitAnchors[i];
      const distance = Math.hypot(anchor.x - particle.x, anchor.y - particle.y);
      if (distance < bestDistance) {
        bestDistance = distance;
        bestIndex = i;
      }
    }
    particle.anchorIndex = bestIndex;
  }

  generateFieldLineSeeds(targetCount) {
    const inset = clamp(
      Number(PARTICLE_CONFIG.particleFieldLineEdgeInset || 12),
      0,
      Math.min(this.metrics.width, this.metrics.height) * 0.25,
    );
    const seeds = [];
    const rows = Math.max(4, targetCount);

    for (let i = 0; i < rows; i += 1) {
      const t = rows === 1 ? 0.5 : i / (rows - 1);
      const y = inset + (this.metrics.height - inset * 2) * t;
      seeds.push({ x: inset, y, baselineY: y, direction: 1 });
    }

    return seeds;
  }

  getFieldVectorAt(x, y, direction = 1, baselineY = y) {
    const flowStrength = Number(PARTICLE_CONFIG.particleFieldLineFlowStrength || 1);
    const baselinePull = Number(PARTICLE_CONFIG.particleFieldLineBaselinePull || 0.035);
    const fallbackVector = () => {
      let vx = direction * flowStrength;
      let vy = (baselineY - y) * baselinePull;
      const magnitude = Math.hypot(vx, vy) || 1;
      vx /= magnitude;
      vy /= magnitude;
      return {
        vx,
        vy,
        distance: Number.POSITIVE_INFINITY,
        mask: 0,
        anchorDistance: Number.POSITIVE_INFINITY,
      };
    };

    if (!this.field || !this.mask) return fallbackVector();
    const scaleX = this.fieldMetrics.width / this.metrics.width;
    const scaleY = this.fieldMetrics.height / this.metrics.height;
    const fx = x * scaleX;
    const fy = y * scaleY;
    if (
      fx < 1 ||
      fy < 1 ||
      fx >= this.fieldMetrics.width - 1 ||
      fy >= this.fieldMetrics.height - 1
    ) {
      return fallbackVector();
    }

    const gradient = computeGradient(
      this.field,
      this.fieldMetrics.width,
      this.fieldMetrics.height,
      fx,
      fy,
    );
    const gradLength = Math.hypot(gradient.dx, gradient.dy) || 1;
    const nx = gradient.dx / gradLength;
    const ny = gradient.dy / gradLength;
    const tangentX = -ny * direction;
    const tangentY = nx * direction;
    const index =
      clamp(Math.round(fy), 0, this.fieldMetrics.height - 1) * this.fieldMetrics.width +
      clamp(Math.round(fx), 0, this.fieldMetrics.width - 1);
    const distance = this.field[index];
    const localMask = this.mask[index];
    const orbitDelta = distance - PARTICLE_CONFIG.orbitTarget;
    const radialForce = -clamp(
      orbitDelta,
      -PARTICLE_CONFIG.orbitWidth * 1.25,
      PARTICLE_CONFIG.orbitWidth * 1.8,
    ) * PARTICLE_CONFIG.orbitPull;

    let anchorForceX = 0;
    let anchorForceY = 0;
    let bestDistance = Number.POSITIVE_INFINITY;
    let bestAnchor = null;
    for (const anchor of this.orbitAnchors) {
      const dx = anchor.x - x;
      const dy = anchor.y - y;
      const anchorDistance = Math.hypot(dx, dy);
      if (anchorDistance < bestDistance) {
        bestDistance = anchorDistance;
        bestAnchor = anchor;
      }
    }
    if (bestAnchor && bestDistance > 1) {
      const dx = bestAnchor.x - x;
      const dy = bestAnchor.y - y;
      const pullScale = Number(PARTICLE_CONFIG.particleFieldLinePull || 1.2);
      const capture = clamp(1 - bestDistance / Math.max(this.metrics.width * 0.7, 1), 0, 1);
      const anchorScale = pullScale * capture;
      anchorForceX = (dx / bestDistance) * anchorScale;
      anchorForceY = (dy / bestDistance) * anchorScale;
    }

    const orbitBand = clamp(
      1 - Math.abs(distance - PARTICLE_CONFIG.orbitTarget) / Math.max(1, PARTICLE_CONFIG.orbitWidth * 3.2),
      0,
      1,
    );
    const baselineForceY = (baselineY - y) * baselinePull;
    const swirlStrength =
      Number(PARTICLE_CONFIG.particleFieldLineSwirl || 0.42) *
      (orbitBand * 0.95 + clamp(1 - bestDistance / 180, 0, 1) * 0.35);

    let vx =
      direction * flowStrength +
      tangentX * (PARTICLE_CONFIG.tangentForce * swirlStrength) +
      nx * radialForce * orbitBand * 0.95 +
      anchorForceX * 0.45;
    let vy =
      tangentY * (PARTICLE_CONFIG.tangentForce * swirlStrength) +
      ny * radialForce * orbitBand * 0.95 +
      anchorForceY +
      baselineForceY;

    const magnitude = Math.hypot(vx, vy);
    if (!Number.isFinite(magnitude) || magnitude < 0.0001) return fallbackVector();
    vx /= magnitude;
    vy /= magnitude;

    return { vx, vy, distance, mask: localMask, anchorDistance: bestDistance };
  }

  traceFieldLine(x, y, direction, baselineY = y) {
    const stepSize = Math.max(2, Number(PARTICLE_CONFIG.particleFieldLineStepSize || 9));
    const maxSteps = Math.max(8, Math.floor(PARTICLE_CONFIG.particleFieldLineSteps || 60));
    const inset = clamp(
      Number(PARTICLE_CONFIG.particleFieldLineEdgeInset || 12),
      0,
      Math.min(this.metrics.width, this.metrics.height) * 0.25,
    );
    const points = [];
    let cx = x;
    let cy = y;

    for (let step = 0; step < maxSteps; step += 1) {
      const vector = this.getFieldVectorAt(cx, cy, direction, baselineY);
      points.push({ x: cx, y: cy });
      cx += vector.vx * stepSize;
      cy += vector.vy * stepSize;
      if (
        cx < inset ||
        cy < 0 ||
        cx > this.metrics.width - inset ||
        cy > this.metrics.height
      ) {
        break;
      }
      if (cx >= this.metrics.width - inset * 0.9) {
        points.push({ x: this.metrics.width - inset, y: cy });
        break;
      }
    }

    const lastPoint = points[points.length - 1];
    if (lastPoint && lastPoint.x < this.metrics.width - inset * 0.9) {
      points.push({
        x: this.metrics.width - inset,
        y: lastPoint.y + (baselineY - lastPoint.y) * 0.35,
      });
    }

    return points;
  }

  rebuildFieldLines() {
    this.fieldLineCurves = [];
    if (!this.field || !this.mask || !this.orbitAnchors.length || this.isCheckerMode()) return;

    const targetCount = Math.max(8, Math.floor(PARTICLE_CONFIG.particleFieldLineCount || 56));
    const minLength = Math.max(24, Number(PARTICLE_CONFIG.particleFieldLineMinLength || 120));
    const seeds = this.generateFieldLineSeeds(targetCount);

    for (const seed of seeds) {
      const curve = this.traceFieldLine(seed.x, seed.y, seed.direction, seed.baselineY);
      if (curve.length < 6) continue;

      let length = 0;
      for (let j = 1; j < curve.length; j += 1) {
        length += Math.hypot(curve[j].x - curve[j - 1].x, curve[j].y - curve[j - 1].y);
      }
      if (length < minLength) continue;

      this.fieldLineCurves.push(curve);
      if (this.fieldLineCurves.length >= targetCount) break;
    }
  }

  rebuildContourLines() {
    this.fieldLineCurves = [];
    if (!this.mask || this.isCheckerMode()) return;

    const width = this.fieldMetrics.width;
    const height = this.fieldMetrics.height;
    const levelCount = Math.max(2, Math.floor(PARTICLE_CONFIG.particleContourLevels || 12));
    const minValue = clamp(Number(PARTICLE_CONFIG.particleContourMinValue || 0.06), 0, 1);
    const maxValue = clamp(
      Number(PARTICLE_CONFIG.particleContourMaxValue || 0.78),
      minValue + 0.01,
      1,
    );
    const minDistancePx = Math.max(0, Number(PARTICLE_CONFIG.particleContourMinDistance || 16));
    const levelBias = Math.max(1, Number(PARTICLE_CONFIG.particleContourLevelBias || 2.2));
    const levels = Array.from({ length: levelCount }, (_value, index) => {
      const t = levelCount === 1 ? 0.5 : index / (levelCount - 1);
      const biasedT = 1 - Math.pow(1 - t, levelBias);
      return minValue + (maxValue - minValue) * biasedT;
    });
    const joinThreshold = Math.max(
      2,
      ((this.metrics.width / Math.max(1, width)) + (this.metrics.height / Math.max(1, height))) * 0.75,
    );
    const segmentLookup = {
      1: [[3, 0]],
      2: [[0, 1]],
      3: [[3, 1]],
      4: [[1, 2]],
      5: [[3, 2], [0, 1]],
      6: [[0, 2]],
      7: [[3, 2]],
      8: [[2, 3]],
      9: [[0, 2]],
      10: [[0, 3], [1, 2]],
      11: [[1, 2]],
      12: [[3, 1]],
      13: [[0, 1]],
      14: [[3, 0]],
    };

    const interpolatePoint = (x, y, edge, level, a, b, c, d) => {
      const valueForEdge = {
        0: [a, b],
        1: [b, c],
        2: [d, c],
        3: [a, d],
      };
      const [v0, v1] = valueForEdge[edge];
      const ratio =
        Math.abs(v1 - v0) < 0.0001 ? 0.5 : clamp((level - v0) / (v1 - v0), 0, 1);
      if (edge === 0) return { x: x + ratio, y };
      if (edge === 1) return { x: x + 1, y: y + ratio };
      if (edge === 2) return { x: x + ratio, y: y + 1 };
      return { x, y: y + ratio };
    };
    const pointsClose = (left, right) =>
      Math.hypot(left.x - right.x, left.y - right.y) <= joinThreshold;
    const polylineSamplePoints = (points) => {
      if (!Array.isArray(points) || !points.length) return [];
      const sampled = [];
      const step = Math.max(1, Math.floor(points.length / 12));
      for (let i = 0; i < points.length; i += step) {
        sampled.push(points[i]);
      }
      const lastPoint = points[points.length - 1];
      if (sampled[sampled.length - 1] !== lastPoint) {
        sampled.push(lastPoint);
      }
      return sampled;
    };
    const polylinesTooClose = (left, right) => {
      const leftSamples = polylineSamplePoints(left);
      const rightSamples = polylineSamplePoints(right);
      for (const a of leftSamples) {
        for (const b of rightSamples) {
          if (Math.hypot(a.x - b.x, a.y - b.y) < minDistancePx) {
            return true;
          }
        }
      }
      return false;
    };
    const stitchSegments = (segments) => {
      const polylines = [];

      for (const segment of segments) {
        let placed = false;
        for (let i = 0; i < polylines.length; i += 1) {
          const line = polylines[i];
          const lineStart = line[0];
          const lineEnd = line[line.length - 1];
          const segStart = segment[0];
          const segEnd = segment[1];

          if (pointsClose(lineEnd, segStart)) {
            line.push(segEnd);
            placed = true;
            break;
          }
          if (pointsClose(lineEnd, segEnd)) {
            line.push(segStart);
            placed = true;
            break;
          }
          if (pointsClose(lineStart, segEnd)) {
            line.unshift(segStart);
            placed = true;
            break;
          }
          if (pointsClose(lineStart, segStart)) {
            line.unshift(segEnd);
            placed = true;
            break;
          }
        }

        if (!placed) {
          polylines.push([segment[0], segment[1]]);
        }
      }

      let merged = true;
      while (merged) {
        merged = false;
        for (let i = 0; i < polylines.length && !merged; i += 1) {
          for (let j = i + 1; j < polylines.length && !merged; j += 1) {
            const a = polylines[i];
            const b = polylines[j];
            const aStart = a[0];
            const aEnd = a[a.length - 1];
            const bStart = b[0];
            const bEnd = b[b.length - 1];

            if (pointsClose(aEnd, bStart)) {
              polylines[i] = [...a, ...b.slice(1)];
            } else if (pointsClose(aEnd, bEnd)) {
              polylines[i] = [...a, ...b.slice(0, -1).reverse()];
            } else if (pointsClose(aStart, bEnd)) {
              polylines[i] = [...b, ...a.slice(1)];
            } else if (pointsClose(aStart, bStart)) {
              polylines[i] = [...b.reverse(), ...a.slice(1)];
            } else {
              continue;
            }

            polylines.splice(j, 1);
            merged = true;
          }
        }
      }

      return polylines;
    };

    for (const level of levels) {
      const acceptedPolylines = [];
      const levelSegments = [];
      for (let y = 0; y < height - 1; y += 1) {
        for (let x = 0; x < width - 1; x += 1) {
          const a = this.mask[y * width + x];
          const b = this.mask[y * width + x + 1];
          const c = this.mask[(y + 1) * width + x + 1];
          const d = this.mask[(y + 1) * width + x];
          const caseIndex =
            (a >= level ? 1 : 0) |
            (b >= level ? 2 : 0) |
            (c >= level ? 4 : 0) |
            (d >= level ? 8 : 0);
          const segments = segmentLookup[caseIndex];
          if (!segments) continue;

          for (const [edgeA, edgeB] of segments) {
            const start = interpolatePoint(x, y, edgeA, level, a, b, c, d);
            const end = interpolatePoint(x, y, edgeB, level, a, b, c, d);
            const scaledStart = {
              x: (start.x / Math.max(1, width - 1)) * this.metrics.width,
              y: (start.y / Math.max(1, height - 1)) * this.metrics.height,
            };
            const scaledEnd = {
              x: (end.x / Math.max(1, width - 1)) * this.metrics.width,
              y: (end.y / Math.max(1, height - 1)) * this.metrics.height,
            };
            levelSegments.push([scaledStart, scaledEnd]);
          }
        }
      }

      const levelNorm =
        Math.abs(maxValue - minValue) < 0.0001
          ? 1
          : clamp((level - minValue) / (maxValue - minValue), 0, 1);
      const polylines = stitchSegments(levelSegments).filter((line) => line.length >= 3);

      for (const points of polylines) {
        const tooClose = acceptedPolylines.some((line) => polylinesTooClose(line, points));
        if (tooClose) continue;
        acceptedPolylines.push(points);
        this.fieldLineCurves.push({ points, levelNorm });
      }
    }
  }

  seedParticles() {
    if (this.isCheckerMode()) {
      const { columns, rows } = this.getGridDimensions();
      const totalCells = columns * rows;
      this.particles = Array.from({ length: totalCells }, (_value, index) => {
        const { x, y } = checkerCellCenter(
          index,
          columns,
          rows,
          this.metrics.width,
          this.metrics.height,
        );
        return {
          gridIndex: index,
          occupied: false,
          respawnTimer: this.randomCheckerBirthDelay(),
          decayTimer: this.randomCheckerDeathDelay(),
          moveCooldown: Math.random() * PARTICLE_CONFIG.particleCheckerSwapInterval,
          radius: 1,
          alpha: 0.18 + Math.random() * 0.36,
          phase: Math.random() * Math.PI * 2,
          age: Math.random() * (PARTICLE_CONFIG.particleLifeMax * 0.6),
          life:
            PARTICLE_CONFIG.particleLifeMin +
            Math.random() *
              (PARTICLE_CONFIG.particleLifeMax - PARTICLE_CONFIG.particleLifeMin),
          renderX: x,
          renderY: y,
          state: "alive",
          burstAge: 0,
          burstDuration: 0,
          burstStrength: 0,
          birthAge: 0,
          birthDuration: 0,
          birthStrength: 0,
          anchorIndex: -1,
          anchorDelay: 0,
        };
      });
      this.rebuildCheckerParticleMap();
      return;
    }

    this.particles = Array.from({ length: PARTICLE_CONFIG.particleCount }, () => ({
      x: Math.random() * this.metrics.width,
      y: Math.random() * this.metrics.height,
      vx: (Math.random() - 0.5) * 12,
      vy: (Math.random() - 0.5) * 12,
      radius: 0.9 + Math.random() * 1.8,
      alpha: 0.14 + Math.random() * 0.4,
      phase: Math.random() * Math.PI * 2,
      age: Math.random() * (PARTICLE_CONFIG.particleLifeMax * 0.7),
      life:
        PARTICLE_CONFIG.particleLifeMin +
        Math.random() *
          (PARTICLE_CONFIG.particleLifeMax - PARTICLE_CONFIG.particleLifeMin),
      state: "alive",
      burstAge: 0,
      burstDuration:
        PARTICLE_CONFIG.particleBurstDuration * (0.8 + Math.random() * 0.5),
      burstStrength: 0.45 + Math.random() * 0.4,
      birthAge: 0,
      birthDuration:
        PARTICLE_CONFIG.particleBirthDuration * (0.8 + Math.random() * 0.5),
      birthStrength: 0.5 + Math.random() * 0.36,
      anchorIndex: -1,
      anchorDelay: 0,
    }));
  }

  rebuildCheckerParticleMap() {
    if (!this.isCheckerMode()) return;
    const { columns, rows } = this.getGridDimensions();
    const totalCells = Math.max(
      columns * rows,
      this.fieldMetrics.width * this.fieldMetrics.height,
    );
    this.checkerParticleMap = new Array(totalCells);
    for (const particle of this.particles) {
      this.checkerParticleMap[particle.gridIndex] = particle;
    }
  }

  randomCheckerBirthDelay() {
    const min = Math.max(0.05, Number(PARTICLE_CONFIG.particleCheckerBirthDelayMin || 1.4));
    const max = Math.max(min, Number(PARTICLE_CONFIG.particleCheckerBirthDelayMax || 3));
    return min + Math.random() * (max - min);
  }

  randomCheckerDeathDelay() {
    const min = Math.max(0.05, Number(PARTICLE_CONFIG.particleCheckerDeathDelayMin || 0.45));
    const max = Math.max(min, Number(PARTICLE_CONFIG.particleCheckerDeathDelayMax || 1));
    return min + Math.random() * (max - min);
  }

  checkerMaskValueFor(mask, index) {
    return mask?.[index] || 0;
  }

  isCheckerTargetInMask(mask, index) {
    const threshold = clamp(PARTICLE_CONFIG.particleCheckerMaskThreshold || 0.16, 0, 1);
    return this.checkerMaskValueFor(mask, index) > threshold;
  }

  syncCheckerTimersToMask(previousMask, nextMask) {
    if (!this.isCheckerMode() || !this.particles.length) return;

    for (const particle of this.particles) {
      const wasTarget = this.isCheckerTargetInMask(previousMask, particle.gridIndex);
      const isTarget = this.isCheckerTargetInMask(nextMask, particle.gridIndex);

      if (!wasTarget && isTarget) {
        particle.respawnTimer = this.randomCheckerBirthDelay();
      } else if (wasTarget && !isTarget) {
        particle.decayTimer = this.randomCheckerDeathDelay();
      } else if (isTarget) {
        particle.decayTimer = this.randomCheckerDeathDelay();
      }
    }
  }

  isCheckerTargetIndex(index) {
    const threshold = clamp(PARTICLE_CONFIG.particleCheckerMaskThreshold || 0.16, 0, 1);
    return (this.mask?.[index] || 0) > threshold;
  }

  getCheckerMaskValue(index) {
    return this.mask?.[index] || 0;
  }

  getCheckerNeighborIndices(index) {
    const { width, height } = this.fieldMetrics;
    const column = index % width;
    const row = Math.floor(index / width);
    const neighbors = [];
    if (column > 0) neighbors.push(index - 1);
    if (column < width - 1) neighbors.push(index + 1);
    if (row > 0) neighbors.push(index - width);
    if (row < height - 1) neighbors.push(index + width);
    return neighbors;
  }

  swapCheckerParticles(source, target) {
    const sourceIndex = source.gridIndex;
    source.gridIndex = target.gridIndex;
    target.gridIndex = sourceIndex;
    this.checkerParticleMap[source.gridIndex] = source;
    this.checkerParticleMap[target.gridIndex] = target;
  }

  tryCheckerSwap(particle) {
    const neighbors = this.getCheckerNeighborIndices(particle.gridIndex);
    if (!neighbors.length) return;
    const currentMask = this.getCheckerMaskValue(particle.gridIndex);
    const currentTarget = this.isCheckerTargetIndex(particle.gridIndex);
    const candidates = [];

    for (const neighborIndex of neighbors) {
      const neighbor = this.checkerParticleMap[neighborIndex];
      if (!neighbor || neighbor.occupied === particle.occupied) continue;
      const neighborMask = this.getCheckerMaskValue(neighborIndex);
      const neighborTarget = this.isCheckerTargetIndex(neighborIndex);
      let score = -Infinity;

      if (particle.occupied) {
        if (!currentTarget && neighborTarget) {
          score = 100 + neighborMask;
        } else if (!currentTarget && !neighborTarget && neighborMask > currentMask) {
          score = 30 + neighborMask;
        } else if (currentTarget && neighborTarget && neighborMask > currentMask + 0.04) {
          score = 8 + neighborMask;
        }
      } else if (currentTarget && neighbor.occupied) {
        const neighborWrong = !neighborTarget;
        score = (neighborWrong ? 100 : 20) + (currentMask - neighborMask);
      }

      if (Number.isFinite(score)) {
        candidates.push({ neighbor, score: score + Math.random() * 0.2 });
      }
    }

    if (!candidates.length) return false;
    candidates.sort((left, right) => right.score - left.score);
    this.swapCheckerParticles(particle, candidates[0].neighbor);
    return true;
  }

  respawnParticle(particle) {
    particle.state = "birthing";
    particle.age = 0;
    particle.life =
      PARTICLE_CONFIG.particleLifeMin +
      Math.random() *
        (PARTICLE_CONFIG.particleLifeMax - PARTICLE_CONFIG.particleLifeMin);
    particle.burstAge = 0;
    particle.burstDuration =
      PARTICLE_CONFIG.particleBurstDuration * (0.8 + Math.random() * 0.5);
    particle.burstStrength = 0.45 + Math.random() * 0.4;
    particle.birthAge = 0;
    particle.birthDuration =
      PARTICLE_CONFIG.particleBirthDuration * (0.8 + Math.random() * 0.5);
    particle.birthStrength = 0.5 + Math.random() * 0.36;
    particle.phase = Math.random() * Math.PI * 2;

    const useRandomRespawn =
      Math.random() < clamp(PARTICLE_CONFIG.particleRandomRespawnRatio || 0, 0, 1);

    if (this.mask && this.field && !useRandomRespawn) {
      const candidates = [];
      for (let i = 0; i < this.mask.length; i += 1) {
        const maskValue = this.mask[i];
        const distance = this.field[i];
        if (maskValue < 0.12) continue;
        if (
          distance < PARTICLE_CONFIG.particleRespawnMinDistance ||
          distance > PARTICLE_CONFIG.particleRespawnMaxDistance
        ) {
          continue;
        }
        candidates.push(i);
      }
      if (candidates.length) {
        const sampleIndex = candidates[Math.floor(Math.random() * candidates.length)];
        const sx = sampleIndex % this.fieldMetrics.width;
        const sy = Math.floor(sampleIndex / this.fieldMetrics.width);
        particle.x =
          ((sx + Math.random() * 1.2 - 0.6) / this.fieldMetrics.width) *
          this.metrics.width;
        particle.y =
          ((sy + Math.random() * 1.2 - 0.6) / this.fieldMetrics.height) *
          this.metrics.height;
      } else {
        particle.x = Math.random() * this.metrics.width;
        particle.y = Math.random() * this.metrics.height;
      }
      this.assignAnchorIndex(particle);
      particle.anchorDelay = 0;
    } else {
      particle.x = Math.random() * this.metrics.width;
      particle.y = Math.random() * this.metrics.height;
      particle.anchorIndex = -1;
      particle.anchorDelay = 0.9;
    }

    const birthAngle = particle.phase + Math.random() * Math.PI * 2;
    const birthVelocity =
      PARTICLE_CONFIG.particleBirthVelocity *
      (useRandomRespawn ? 0.42 + particle.birthStrength * 0.12 : 0.86 + particle.birthStrength * 0.24);
    particle.vx = -Math.cos(birthAngle) * birthVelocity;
    particle.vy = -Math.sin(birthAngle) * birthVelocity;
  }

  triggerParticleBurst(particle, time) {
    particle.state = "bursting";
    particle.burstAge = 0;
    particle.burstDuration =
      PARTICLE_CONFIG.particleBurstDuration * (0.8 + Math.random() * 0.5);
    particle.burstStrength = 0.45 + Math.random() * 0.4;
    const angle = time * 0.7 + particle.phase + Math.random() * Math.PI * 2;
    const burstVelocity =
      PARTICLE_CONFIG.particleBurstVelocity * (0.78 + particle.burstStrength * 0.22);
    particle.vx = Math.cos(angle) * burstVelocity;
    particle.vy = Math.sin(angle) * burstVelocity;
  }

  updateDebugPreview() {
    if (!PARTICLE_DEBUG || !this.debugCanvas || !this.debugContext) return;
    const revealRect = this.revealElement.getBoundingClientRect();
    this.debugContext.clearRect(0, 0, window.innerWidth, window.innerHeight);

    const renderMaskImage = (maskData, width, height) => {
      const preview = this.debugContext.createImageData(width, height);
      for (let i = 0; i < maskData.length; i += 1) {
        const value = Math.round(clamp(maskData[i], 0, 1) * 255);
        const offset = i * 4;
        preview.data[offset] = value;
        preview.data[offset + 1] = Math.round(value * 0.45);
        preview.data[offset + 2] = 255;
        preview.data[offset + 3] = 255;
      }
      const tempCanvas = document.createElement("canvas");
      tempCanvas.width = width;
      tempCanvas.height = height;
      const tempContext = tempCanvas.getContext("2d");
      tempContext.putImageData(preview, 0, 0);
      this.debugContext.imageSmoothingEnabled = false;
      this.debugContext.drawImage(
        tempCanvas,
        0,
        0,
        width,
        height,
        revealRect.left,
        revealRect.top,
        revealRect.width,
        revealRect.height,
      );
    };

    const drawOverlayNote = (text) => {
      this.debugContext.save();
      this.debugContext.fillStyle = "rgba(17, 24, 39, 0.78)";
      this.debugContext.fillRect(revealRect.left + 18, revealRect.top + 18, 260, 34);
      this.debugContext.fillStyle = "rgba(255,255,255,0.95)";
      this.debugContext.font = "14px monospace";
      this.debugContext.textBaseline = "middle";
      this.debugContext.fillText(text, revealRect.left + 30, revealRect.top + 35);
      this.debugContext.restore();
    };

    if (this.debugView !== "original") {
      this.debugContext.fillStyle = "rgba(0, 0, 0, 0.96)";
      this.debugContext.fillRect(
        revealRect.left,
        revealRect.top,
        revealRect.width,
        revealRect.height,
      );
    }

    if (this.debugView === "blurred" && this.blurredMask) {
      renderMaskImage(this.blurredMask.data, this.blurredMask.width, this.blurredMask.height);
      drawOverlayNote("blurred mask");
    } else if (this.debugView === "mask" && this.mask) {
      renderMaskImage(this.mask, this.fieldMetrics.width, this.fieldMetrics.height);
      drawOverlayNote("final mask");
    } else if (this.debugView === "original") {
      drawOverlayNote("original slide");
    }

    if (this.debugMeta) {
      this.debugMeta.textContent =
        `${this.lastMaskMode} · ${this.debugView} · coverage ${(this.lastMaskCoverage * 100).toFixed(2)}% · raster ${this.fieldMetrics.width}x${this.fieldMetrics.height} · viewport ${this.metrics.width}x${this.metrics.height} · ${this.particles.length} particles`;
    }
  }

  animate() {
    if (!this.context || !this.canvas) return;
    const frame = (timestamp) => {
      const dt = clamp((timestamp - this.lastFrameTime) / 1000, 0.001, 0.033);
      this.lastFrameTime = timestamp;
      this.draw(dt, timestamp / 1000);
      this.frameHandle = window.requestAnimationFrame(frame);
    };
    this.frameHandle = window.requestAnimationFrame(frame);
  }

  draw(dt, time) {
    const ctx = this.context;
    const width = this.metrics.width;
    const height = this.metrics.height;
    ctx.clearRect(0, 0, width, height);

    if (this.isPastelCellsMode()) {
      if (this.getActiveSlide() && !this.motionPreference.matches) this.drawPastelCells(time);
      return;
    }
    if (PARTICLE_CONFIG.particleRenderMode === "pigment") {
      if (this.getActiveSlide() && !this.motionPreference.matches) this.drawPigment(dt, time);
      return;
    }
    if (this.isCheckerMode()) {
      this.drawChecker(dt, time);
      return;
    }

    const hasField = Boolean(this.field && this.mask);
    const scaleX = this.fieldMetrics.width / width;
    const scaleY = this.fieldMetrics.height / height;
    const effectiveDownsample =
      ((width / Math.max(1, this.fieldMetrics.width)) +
        (height / Math.max(1, this.fieldMetrics.height))) /
      2;
    const glowRadius = PARTICLE_CONFIG.orbitTarget * effectiveDownsample * 1.2;
    const renderMode = String(PARTICLE_CONFIG.particleRenderMode || "circle").toLowerCase();
    const connectionMode = String(
      PARTICLE_CONFIG.particleConnectionMode || "none",
    ).toLowerCase();
    const useFieldLines = connectionMode === "field-lines";
    const useContourLines = connectionMode === "contour-lines";
    const renderables = [];

    for (const particle of this.particles) {
      if (particle.state === "bursting") {
        particle.burstAge += dt;
        particle.vx *= 0.94;
        particle.vy *= 0.94;
        particle.x += particle.vx * dt;
        particle.y += particle.vy * dt;
        if (particle.burstAge >= particle.burstDuration) {
          this.respawnParticle(particle);
        }
      } else if (particle.state === "birthing") {
        particle.birthAge += dt;
        particle.vx *= 0.9;
        particle.vy *= 0.9;
        particle.x += particle.vx * dt;
        particle.y += particle.vy * dt;
        if (particle.birthAge >= particle.birthDuration) {
          particle.state = "alive";
          particle.vx *= 0.35;
          particle.vy *= 0.35;
        }
      } else if (hasField) {
        particle.age += dt;
        if (particle.age >= particle.life) {
          this.triggerParticleBurst(particle, time);
          continue;
        }

        if (particle.anchorDelay > 0) {
          particle.anchorDelay = Math.max(0, particle.anchorDelay - dt);
          particle.vx += Math.cos(time * 0.55 + particle.phase) * PARTICLE_CONFIG.driftForce * 0.45;
          particle.vy += Math.sin(time * 0.45 + particle.phase) * PARTICLE_CONFIG.driftForce * 0.45;
        } else {

          const fx = particle.x * scaleX;
          const fy = particle.y * scaleY;
          const gradient = computeGradient(
            this.field,
            this.fieldMetrics.width,
            this.fieldMetrics.height,
            fx,
            fy,
          );
          const gx = gradient.dx;
          const gy = gradient.dy;
          const gradLength = Math.hypot(gx, gy) || 1;
          const nx = gx / gradLength;
          const ny = gy / gradLength;
          const tangentX = -ny;
          const tangentY = nx;
          const index =
            clamp(Math.round(fy), 0, this.fieldMetrics.height - 1) *
              this.fieldMetrics.width +
            clamp(Math.round(fx), 0, this.fieldMetrics.width - 1);
          const distance = this.field[index];
          const orbitDelta = distance - PARTICLE_CONFIG.orbitTarget;
          const orbitError = clamp(
            orbitDelta,
            -PARTICLE_CONFIG.orbitWidth * 1.35,
            PARTICLE_CONFIG.orbitWidth * 2.4,
          );
          const radialForce = -orbitError * PARTICLE_CONFIG.orbitPull;
          const seekForce =
            distance > PARTICLE_CONFIG.orbitTarget + PARTICLE_CONFIG.orbitWidth
              ? -Math.min(
                  PARTICLE_CONFIG.seekForce,
                  (distance - PARTICLE_CONFIG.orbitTarget) * 0.08,
                )
              : 0;
          const localMask = this.mask[index];
          const tangentForce =
            PARTICLE_CONFIG.tangentForce * (0.65 + localMask * 0.75);

          if (
            particle.anchorIndex == null ||
            particle.anchorIndex < 0 ||
            particle.anchorIndex >= this.orbitAnchors.length
          ) {
            this.assignAnchorIndex(particle);
          }
          const anchor =
            particle.anchorIndex >= 0 ? this.orbitAnchors[particle.anchorIndex] : null;
          let anchorForceX = 0;
          let anchorForceY = 0;
          if (anchor) {
            const ax = anchor.x - particle.x;
            const ay = anchor.y - particle.y;
            const anchorDistance = Math.hypot(ax, ay) || 1;
            if (anchorDistance < 10 || anchorDistance > 160) {
              this.assignAnchorIndex(particle);
            } else {
              anchorForceX = (ax / anchorDistance) * PARTICLE_CONFIG.anchorPull;
              anchorForceY = (ay / anchorDistance) * PARTICLE_CONFIG.anchorPull;
            }
          }

          const noiseAngle = particle.phase + time * 0.35 + particle.radius;
          const noiseX = Math.cos(noiseAngle * 1.7) * PARTICLE_CONFIG.noiseForce;
          const noiseY = Math.sin(noiseAngle * 1.3) * PARTICLE_CONFIG.noiseForce;

          particle.vx +=
            (nx * (radialForce + seekForce) +
              tangentX * tangentForce +
              anchorForceX +
              noiseX) *
            dt;
          particle.vy +=
            (ny * (radialForce + seekForce) +
              tangentY * tangentForce +
              anchorForceY +
              noiseY) *
            dt;
        }
      } else {
        particle.age += dt;
        if (particle.age >= particle.life) {
          this.triggerParticleBurst(particle, time);
          continue;
        }
        particle.vx += Math.cos(time * 0.4 + particle.phase) * PARTICLE_CONFIG.driftForce;
        particle.vy += Math.sin(time * 0.3 + particle.phase) * PARTICLE_CONFIG.driftForce;
      }

      particle.vx *= PARTICLE_CONFIG.damping;
      particle.vy *= PARTICLE_CONFIG.damping;
      const velocity = Math.hypot(particle.vx, particle.vy);
      if (velocity > PARTICLE_CONFIG.maxVelocity) {
        const scale = PARTICLE_CONFIG.maxVelocity / velocity;
        particle.vx *= scale;
        particle.vy *= scale;
      }
      if (velocity < PARTICLE_CONFIG.particleMinSpeed) {
        const scale = PARTICLE_CONFIG.particleMinSpeed / (velocity || 1);
        particle.vx *= scale;
        particle.vy *= scale;
      } else if (velocity > PARTICLE_CONFIG.particleMaxSpeed) {
        const scale = PARTICLE_CONFIG.particleMaxSpeed / velocity;
        particle.vx *= scale;
        particle.vy *= scale;
      }

      particle.x += particle.vx * dt;
      particle.y += particle.vy * dt;

      if (particle.x < -20) particle.x = width + 20;
      if (particle.x > width + 20) particle.x = -20;
      if (particle.y < -20) particle.y = height + 20;
      if (particle.y > height + 20) particle.y = -20;

      const burstProgress =
        particle.state === "bursting"
          ? clamp(particle.burstAge / Math.max(0.001, particle.burstDuration), 0, 1)
          : 0;
      const birthProgress =
        particle.state === "birthing"
          ? clamp(particle.birthAge / Math.max(0.001, particle.birthDuration), 0, 1)
          : 0;
      const lifePhase =
        particle.state === "alive"
          ? clamp(particle.age / Math.max(0.001, particle.life), 0, 1)
          : 1;
      const lifeEnvelope =
        particle.state === "alive"
          ? 0.82 + 0.18 * Math.sin(lifePhase * Math.PI)
          : particle.state === "birthing"
            ? 0.34 + Math.sin(birthProgress * Math.PI * 0.84) * (0.62 + particle.birthStrength * 0.18)
            : 1.15 - burstProgress;
      const alpha =
        particle.alpha *
        PARTICLE_CONFIG.opacity *
        DEBUG_MULTIPLIERS.opacity *
        Math.max(0, lifeEnvelope);
      const shimmer = 0.7 + 0.3 * Math.sin(time * 1.1 + particle.phase);
      const burstScale =
        particle.state === "bursting"
          ? 1 + burstProgress * 1.45 * particle.burstStrength
          : particle.state === "birthing"
            ? 2.35 - birthProgress * 1.2
            : 1;

      const [gr, gg, gb] = this.glowRgb;
      const [pr, pg, pb] = this.particleRgb;
      const glowColor = PARTICLE_DEBUG
        ? `rgba(255, 0, 170, ${PARTICLE_CONFIG.glowOpacity * DEBUG_MULTIPLIERS.glowOpacity * alpha})`
        : `rgba(${gr}, ${gg}, ${gb}, ${PARTICLE_CONFIG.glowOpacity * alpha})`;
      const particleColor = PARTICLE_DEBUG
        ? `rgba(255, 105, 235, ${alpha * shimmer})`
        : `rgba(${pr}, ${pg}, ${pb}, ${alpha * shimmer})`;
      const glowSize =
        glowRadius * 0.13 * particle.radius * DEBUG_MULTIPLIERS.glowRadius * burstScale;
      const baseRadius = particle.radius * DEBUG_MULTIPLIERS.radius * burstScale;
      renderables.push({
        particle,
        x: particle.x,
        y: particle.y,
        alpha,
        glowColor,
        particleColor,
        glowSize,
        baseRadius,
      });

      if (connectionMode === "k-nearest" || useFieldLines || useContourLines) {
        continue;
      }

      this.drawParticleRenderable(ctx, renderMode, particle, renderables[renderables.length - 1]);
    }

    if (useFieldLines) {
      this.drawParticleFieldLines(ctx, renderables, time);
    } else if (useContourLines) {
      this.drawParticleContourLines(ctx, time);
    } else if (connectionMode === "k-nearest") {
      this.drawParticleConnections(ctx, renderables);
      for (const renderable of renderables) {
        this.drawParticleRenderable(ctx, renderMode, renderable.particle, renderable);
      }
    }
  }

  drawChecker(dt, time) {
    const ctx = this.context;
    const { columns, rows } = this.getGridDimensions();
    const cellWidth = this.metrics.width / columns;
    const cellHeight = this.metrics.height / rows;
    const cellSize = Math.min(cellWidth, cellHeight);
    const moveFactor = checkerTransitionFactor(
      dt,
      Number(PARTICLE_CONFIG.particleCheckerMoveLerp || 12),
    );

    this.rebuildCheckerParticleMap();

    for (const particle of this.particles) {
      const targetActive = this.isCheckerTargetIndex(particle.gridIndex);

      if (particle.occupied) {
        particle.age += dt;
        if (particle.age >= particle.life) {
          particle.occupied = false;
          particle.respawnTimer = this.randomCheckerBirthDelay();
          particle.decayTimer = this.randomCheckerDeathDelay();
          particle.moveCooldown = Math.random() * PARTICLE_CONFIG.particleCheckerSwapInterval;
        } else if (!targetActive) {
          particle.decayTimer = Math.max(0, particle.decayTimer - dt);
          if (particle.decayTimer <= 0) {
            particle.occupied = false;
            particle.respawnTimer = this.randomCheckerBirthDelay();
            particle.decayTimer = this.randomCheckerDeathDelay();
          }
        } else {
          particle.decayTimer = this.randomCheckerDeathDelay();
        }
      } else {
        particle.respawnTimer = Math.max(0, particle.respawnTimer - dt);
        if (targetActive && particle.respawnTimer <= 0) {
          particle.occupied = true;
          particle.age = 0;
          particle.life =
            PARTICLE_CONFIG.particleLifeMin +
            Math.random() *
              (PARTICLE_CONFIG.particleLifeMax - PARTICLE_CONFIG.particleLifeMin);
          particle.decayTimer = this.randomCheckerDeathDelay();
        }
      }

      particle.moveCooldown -= dt;
      if (particle.moveCooldown <= 0) {
        const swapped = this.tryCheckerSwap(particle);
        particle.moveCooldown =
          PARTICLE_CONFIG.particleCheckerSwapInterval *
          (swapped ? 0.8 + Math.random() * 0.6 : 1.05 + Math.random() * 0.9);
      }
    }

    for (const particle of this.particles) {
      const targetCenter = checkerCellCenter(
        particle.gridIndex,
        columns,
        rows,
        this.metrics.width,
        this.metrics.height,
      );
      particle.renderX += (targetCenter.x - particle.renderX) * moveFactor;
      particle.renderY += (targetCenter.y - particle.renderY) * moveFactor;

      if (!particle.occupied) continue;
      const lifePhase = clamp(particle.age / Math.max(0.001, particle.life), 0, 1);
      const alpha =
        particle.alpha *
        PARTICLE_CONFIG.opacity *
        DEBUG_MULTIPLIERS.opacity *
        (0.82 + 0.18 * Math.sin(lifePhase * Math.PI));
      const shimmer = 0.78 + 0.22 * Math.sin(time * 1.1 + particle.phase);
      const [pr, pg, pb] = this.particleRgb;
      const particleColor = PARTICLE_DEBUG
        ? `rgba(255, 105, 235, ${alpha * shimmer})`
        : `rgba(${pr}, ${pg}, ${pb}, ${alpha * shimmer})`;

      ctx.fillStyle = particleColor;
      ctx.fillRect(
        Math.round(particle.renderX - cellSize / 2),
        Math.round(particle.renderY - cellSize / 2),
        Math.ceil(cellSize),
        Math.ceil(cellSize),
      );
    }
  }

  createPastelCellSprites() {
    const css = getComputedStyle(this.revealElement);
    const colors = ["sage", "violet", "gray", "sage", "gray", "violet"];
    const fallback = {sage: "#8B9E87", violet: "#A398BC", gray: "#99958C"};
    return colors.map((name, index) => {
      const sprite = document.createElement("canvas");
      sprite.width = sprite.height = 96;
      const ctx = sprite.getContext("2d");
      let seed = index + 117;
      const random = () => ((seed = (Math.imul(seed, 1664525) + 1013904223) >>> 0) / 4294967296);
      ctx.fillStyle = css.getPropertyValue(`--pastello-${name}`).trim() || fallback[name];
      ctx.strokeStyle = ctx.fillStyle;
      ctx.lineCap = "round";
      // Diagonal overlapping strokes remain inside the square paper cell.
      ctx.save();
      ctx.beginPath();
      ctx.rect(6, 6, 84, 84);
      ctx.clip();
      ctx.translate(48, 48);
      ctx.rotate(-Math.PI / 4 + (random() - 0.5) * 0.08);
      // Broad charcoal passes with small, seeded variations in pressure and curvature.
      for (let y = -60; y < 60; y += 12 + random() * 2) {
        const offset = y + (random() - 0.5) * 2;
        ctx.globalAlpha = 0.58 + Math.min(1, Math.abs(y) / 42) * 0.2 + random() * 0.14;
        ctx.lineWidth = 13 + random() * 3;
        ctx.beginPath();
        ctx.moveTo(-68 + random() * 3, offset);
        ctx.quadraticCurveTo((random() - 0.5) * 8, offset + (random() - 0.5) * 4,
          68 - random() * 3, offset + (random() - 0.5) * 3);
        ctx.stroke();
      }
      ctx.restore();
      ctx.globalCompositeOperation = "destination-out";
      for (let i = 0; i < 1700; i++) {
        ctx.globalAlpha = 0.16 + random() * 0.48;
        ctx.beginPath();
        ctx.arc(random() * 96, random() * 96, 0.25 + random() * 0.75, 0, Math.PI * 2);
        ctx.fill();
      }
      return sprite;
    });
  }

  rebuildPastelCells(slide) {
    const revealRect = this.revealElement.getBoundingClientRect();
    const rect = slide.getBoundingClientRect();
    const css = getComputedStyle(slide);
    const grid = parseFloat(css.getPropertyValue("--pastello-grid-size")) || 24;
    // Match the CSS background's origin and zoom, rather than fitting a viewport grid.
    const zoom = rect.width / Math.max(1, slide.offsetWidth);
    const size = grid * zoom;
    const originX = rect.left - revealRect.left;
    const originY = rect.top - revealRect.top;
    const columns = Math.floor(rect.width / size), rows = Math.floor(rect.height / size);
    const protectedRects = [...slide.querySelectorAll("h1,h2,h3,p,li,table,pre,.js-plotly-plot text")]
      .filter(el => !el.closest('.fragment:not(.visible)'))
      .map(el => el.getBoundingClientRect()).filter(r => r.width && r.height);
    const cells = [];
    const defaults = PARTICLE_THEME_PRESETS["pastel-cells"];
    const density = Number(PARTICLE_CONFIG.pastelCellDensity ?? defaults.pastelCellDensity);
    const radius = Number(PARTICLE_CONFIG.pastelCellAttentionRadius ?? defaults.pastelCellAttentionRadius) * zoom;
    for (let row = 0; row < rows; row++) for (let col = 0; col < columns; col++) {
      let seed = (row * 73856093 ^ col * 19349663 ^ 71) >>> 0;
      const random = () => ((seed = (Math.imul(seed, 1664525) + 1013904223) >>> 0) / 4294967296);
      if (random() > density) continue;
      const x = originX + col * size, y = originY + row * size;
      const fx = Math.floor((x + size / 2) * this.fieldMetrics.width / this.metrics.width);
      const fy = Math.floor((y + size / 2) * this.fieldMetrics.height / this.metrics.height);
      if (fx < 0 || fy < 0 || fx >= this.fieldMetrics.width || fy >= this.fieldMetrics.height) continue;
      const distance = this.field[fy * this.fieldMetrics.width + fx] * this.metrics.width / this.fieldMetrics.width;
      if (!Number.isFinite(distance) || distance > radius) continue;
      const screenX = x + revealRect.left, screenY = y + revealRect.top;
      if (protectedRects.some(r => screenX < r.right + 2 && screenX + size > r.left - 2 &&
        screenY < r.bottom + 2 && screenY + size > r.top - 2)) continue;
      cells.push({x, y, size, row, col, weight: 0.55 + (1 - distance / radius) * 0.45,
        phase: random(), life: 9 + random() * 7, sprite: Math.floor(random() * 6)});
    }
    this.pastelCells = cells;
    this.pastelCellsSlide = slide;
    this.pastelCellsViewport = `${this.metrics.width}:${this.metrics.height}`;
    this.pastelCellSprites ||= this.createPastelCellSprites();
  }

  drawPastelCells(time) {
    if (this.pastelCellsSlide !== this.getActiveSlide() ||
      this.pastelCellsViewport !== `${this.metrics.width}:${this.metrics.height}`) return;
    const ctx = this.context;
    const opacity = Number(PARTICLE_CONFIG.pastelCellOpacity ?? PARTICLE_THEME_PRESETS["pastel-cells"].opacity);
    for (const cell of this.pastelCells) {
      const phase = (time / cell.life + cell.phase) % 1;
      const growth = clamp(phase / 0.22, 0, 1);
      const fade = clamp((1 - phase) / 0.25, 0, 1);
      ctx.save();
      ctx.globalAlpha = opacity * cell.weight * fade;
      ctx.beginPath();
      // Sweep diagonally across the cell, following the pastel stroke direction.
      const reach = cell.size * 2 * growth;
      ctx.moveTo(cell.x, cell.y);
      ctx.lineTo(cell.x + reach, cell.y);
      ctx.lineTo(cell.x, cell.y + reach);
      ctx.closePath();
      ctx.clip();
      ctx.drawImage(this.pastelCellSprites[cell.sprite], cell.x, cell.y, cell.size, cell.size);
      ctx.restore();
    }
  }

  createPigmentSprites() {
    const css = getComputedStyle(this.revealElement);
    const palette = ["gray", "gray", "gray", "gray", "sage", "rose", "violet", "gray"];
    const fallback = {gray: "#99958C", sage: "#8B9E87", rose: "#C58E89", violet: "#A398BC"};
    // Tiny cached canvases preserve the same paper tooth as each fleck moves.
    return palette.map((name, index) => {
      const sprite = document.createElement("canvas");
      sprite.width = sprite.height = 32;
      const ctx = sprite.getContext("2d");
      let seed = 71 + index;
      const random = () => ((seed = (Math.imul(seed, 1664525) + 1013904223) >>> 0) / 4294967296);
      ctx.translate(16, 16);
      ctx.scale(1, index % 4 === 0 ? 0.32 : 0.72);
      ctx.fillStyle = css.getPropertyValue(`--pastello-${name}`).trim() || fallback[name];
      ctx.beginPath();
      for (let i = 0; i < 9; i++) {
        const angle = i * Math.PI * 2 / 9;
        const radius = 9 + random() * 4;
        const x = Math.cos(angle) * radius, y = Math.sin(angle) * radius;
        if (i) ctx.lineTo(x, y); else ctx.moveTo(x, y);
      }
      ctx.closePath();
      ctx.fill();
      ctx.globalCompositeOperation = "destination-out";
      for (let i = 0; i < 45; i++) {
        ctx.globalAlpha = 0.15 + random() * 0.4;
        ctx.beginPath();
        ctx.arc(random() * 28 - 14, random() * 28 - 14, 0.3 + random(), 0, Math.PI * 2);
        ctx.fill();
      }
      return sprite;
    });
  }

  drawPigment(dt, time) {
    this.pigmentSprites ||= this.createPigmentSprites();
    const ctx = this.context;
    const {width, height} = this.metrics;
    this.particles.forEach((particle, index) => {
      particle.age += dt;
      if (particle.age >= particle.life) {
        particle.age = 0;
        particle.x = Math.random() * width;
        particle.y = Math.random() * height;
      }
      const speed = PARTICLE_CONFIG.particleMinSpeed +
        (PARTICLE_CONFIG.particleMaxSpeed - PARTICLE_CONFIG.particleMinSpeed) * particle.radius / 2.7;
      particle.x += dt * speed * (0.65 + Math.sin(time * 0.07 + particle.phase) * 0.25);
      particle.y += dt * speed * (0.2 + Math.cos(time * 0.09 + particle.phase) * 0.25);
      if (particle.x > width + 4) particle.x = -4;
      if (particle.y > height + 4) particle.y = -4;
      if (particle.y < -4) particle.y = height + 4;
      const fade = Math.min(1, particle.age / 3, (particle.life - particle.age) / 3);
      const size = 5 + particle.radius * 2.5;
      ctx.save();
      ctx.globalAlpha = PARTICLE_CONFIG.opacity * fade * (0.65 + particle.alpha);
      ctx.translate(particle.x, particle.y);
      ctx.rotate(particle.phase + time * 0.035 * (index % 2 ? 1 : -1));
      ctx.drawImage(this.pigmentSprites[index % this.pigmentSprites.length], -size / 2, -size / 2, size, size);
      ctx.restore();
    });
  }

  drawParticleRenderable(ctx, renderMode, particle, renderable) {
    const { glowColor, particleColor, glowSize, baseRadius, x, y } = renderable;

    if (renderMode === "pixel") {
      const pixelSize = Math.max(
        1,
        Math.round(PARTICLE_CONFIG.particlePixelSize * baseRadius),
      );
      ctx.fillStyle = glowColor;
      ctx.fillRect(
        Math.round(x - glowSize * 0.7),
        Math.round(y - glowSize * 0.7),
        Math.max(pixelSize + 2, Math.round(glowSize * 1.4)),
        Math.max(pixelSize + 2, Math.round(glowSize * 1.4)),
      );
      ctx.fillStyle = particleColor;
      ctx.fillRect(
        Math.round(x - pixelSize / 2),
        Math.round(y - pixelSize / 2),
        pixelSize,
        pixelSize,
      );
    } else if (renderMode === "matrix") {
      const glyphSet =
        PARTICLE_CONFIG.particleGlyphSet ||
        "01アイウエオカキクケコABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789";
      const glyph = pickParticleGlyph(particle, glyphSet);
      const fontSize = Math.max(
        5,
        baseRadius *
          PARTICLE_CONFIG.particleGlyphScale *
          (PARTICLE_CONFIG.particleGlyphSizeFactor || 3.1),
      );
      ctx.save();
      ctx.textAlign = "center";
      ctx.textBaseline = "middle";
      ctx.font = `${fontSize}px ${PARTICLE_CONFIG.particleGlyphFontFamily}`;
      ctx.fillStyle = glowColor;
      ctx.fillText(glyph, x, y);
      ctx.fillStyle = particleColor;
      ctx.fillText(glyph, x, y);
      ctx.restore();
    } else {
      ctx.beginPath();
      ctx.fillStyle = glowColor;
      ctx.arc(x, y, glowSize, 0, Math.PI * 2);
      ctx.fill();

      ctx.beginPath();
      ctx.fillStyle = particleColor;
      ctx.arc(x, y, baseRadius, 0, Math.PI * 2);
      ctx.fill();
    }
  }

  drawParticleConnections(ctx, renderables) {
    const k = Math.max(1, Math.floor(PARTICLE_CONFIG.particleConnectionK || 1));
    const maxDistance = Math.max(8, Number(PARTICLE_CONFIG.particleConnectionMaxDistance || 120));
    const maxDistanceSq = maxDistance * maxDistance;
    const lineWidth = Math.max(
      0.3,
      Number(PARTICLE_CONFIG.particleConnectionWidth || 1) * (PARTICLE_DEBUG ? 1.8 : 1),
    );
    const seenPairs = new Set();
    const nearestNeighborSets = Array.from({ length: renderables.length }, () => new Set());

    ctx.save();
    ctx.lineCap = "round";
    ctx.lineJoin = "round";
    ctx.lineWidth = lineWidth;

    for (let i = 0; i < renderables.length; i += 1) {
      const source = renderables[i];
      const neighbors = [];
      for (let j = 0; j < renderables.length; j += 1) {
        if (i === j) continue;
        const target = renderables[j];
        const dx = target.x - source.x;
        const dy = target.y - source.y;
        const distanceSq = dx * dx + dy * dy;
        if (distanceSq > maxDistanceSq) continue;
        neighbors.push({ index: j, distanceSq });
      }

      neighbors.sort((left, right) => left.distanceSq - right.distanceSq);
      for (const neighbor of neighbors.slice(0, k)) {
        nearestNeighborSets[i].add(neighbor.index);
      }
    }

    for (let i = 0; i < renderables.length; i += 1) {
      const source = renderables[i];
      for (const neighborIndex of nearestNeighborSets[i]) {
        if (!nearestNeighborSets[neighborIndex]?.has(i)) continue;

        const a = Math.min(i, neighborIndex);
        const b = Math.max(i, neighborIndex);
        const pairKey = `${a}:${b}`;
        if (seenPairs.has(pairKey)) continue;
        seenPairs.add(pairKey);

        const target = renderables[neighborIndex];
        const dx = target.x - source.x;
        const dy = target.y - source.y;
        const distance = Math.hypot(dx, dy);
        const falloff = 1 - clamp(distance / maxDistance, 0, 1);
        const alpha =
          PARTICLE_CONFIG.particleConnectionOpacity *
          Math.min(source.alpha, target.alpha) *
          (0.3 + falloff * 0.7) *
          (PARTICLE_DEBUG ? 2.8 : 1);
        const [pr, pg, pb] = this.particleRgb;
        const lineColor = PARTICLE_DEBUG
          ? `rgba(255, 170, 245, ${clamp(alpha, 0, 0.95)})`
          : `rgba(${pr}, ${pg}, ${pb}, ${alpha})`;

        ctx.strokeStyle = lineColor;
        ctx.beginPath();
        ctx.moveTo(source.x, source.y);
        ctx.lineTo(target.x, target.y);
        ctx.stroke();
      }
    }

    ctx.restore();
  }

  drawParticleFieldLines(ctx, renderables, time) {
    const lineOpacity = Math.max(0, Number(PARTICLE_CONFIG.particleConnectionOpacity || 0.18));
    const baseWidth = Math.max(0.2, Number(PARTICLE_CONFIG.particleConnectionWidth || 1));
    const waveAmplitude = Math.max(
      0,
      Number(PARTICLE_CONFIG.particleFieldLineWaveAmplitude || 0),
    );
    const waveSpeed = Number(PARTICLE_CONFIG.particleFieldLineWaveSpeed || 0.12);
    const waveFrequency = Number(PARTICLE_CONFIG.particleFieldLineWaveFrequency || 0.18);
    const [pr, pg, pb] = this.particleRgb;
    const [gr, gg, gb] = this.glowRgb;

    ctx.save();
    ctx.lineCap = "round";
    ctx.lineJoin = "round";

    const buildAnimatedCurve = (points, curveIndex) => {
      if (waveAmplitude <= 0 || points.length < 3) return points;
      const animated = [];
      const phaseSeed = curveIndex * 0.73;
      const maxIndex = Math.max(1, points.length - 1);
      for (let i = 0; i < points.length; i += 1) {
        const current = points[i];
        const previous = points[Math.max(0, i - 1)];
        const next = points[Math.min(points.length - 1, i + 1)];
        const dx = next.x - previous.x;
        const dy = next.y - previous.y;
        const tangentLength = Math.hypot(dx, dy) || 1;
        const normalX = -dy / tangentLength;
        const normalY = dx / tangentLength;
        const lineProgress = i / maxIndex;
        const envelope = Math.sin(lineProgress * Math.PI);
        const wave =
          Math.sin(
            time * waveSpeed +
              lineProgress * Math.PI * 2 * waveFrequency * points.length +
              phaseSeed,
          ) *
          waveAmplitude *
          envelope;
        animated.push({
          x: current.x + normalX * wave,
          y: current.y + normalY * wave,
        });
      }
      return animated;
    };

    const drawSmoothPath = (points) => {
      ctx.beginPath();
      ctx.moveTo(points[0].x, points[0].y);
      for (let i = 1; i < points.length - 1; i += 1) {
        const current = points[i];
        const next = points[i + 1];
        const cx = (current.x + next.x) / 2;
        const cy = (current.y + next.y) / 2;
        ctx.quadraticCurveTo(current.x, current.y, cx, cy);
      }
      const penultimate = points[points.length - 2];
      const last = points[points.length - 1];
      ctx.quadraticCurveTo(penultimate.x, penultimate.y, last.x, last.y);
    };

    for (let curveIndex = 0; curveIndex < this.fieldLineCurves.length; curveIndex += 1) {
      const curve = this.fieldLineCurves[curveIndex];
      if (!Array.isArray(curve) || curve.length < 3) continue;
      const animatedCurve = buildAnimatedCurve(curve, curveIndex);

      const glowAlpha = Math.min(0.32, lineOpacity * 0.48) * (PARTICLE_DEBUG ? 1.9 : 1);
      const strokeAlpha = lineOpacity * (PARTICLE_DEBUG ? 1.8 : 1);

      ctx.strokeStyle = PARTICLE_DEBUG
        ? `rgba(255, 210, 250, ${clamp(glowAlpha, 0, 0.98)})`
        : `rgba(${gr}, ${gg}, ${gb}, ${glowAlpha})`;
      ctx.lineWidth = baseWidth * 2.2;
      drawSmoothPath(animatedCurve);
      ctx.stroke();

      ctx.strokeStyle = PARTICLE_DEBUG
        ? `rgba(255, 245, 255, ${clamp(strokeAlpha, 0, 0.98)})`
        : `rgba(${pr}, ${pg}, ${pb}, ${strokeAlpha})`;
      ctx.lineWidth = baseWidth;
      drawSmoothPath(animatedCurve);
      ctx.stroke();
    }

    for (const renderable of renderables) {
      const particleAlpha = clamp(renderable.alpha * 0.9, 0.12, 0.8);
      ctx.fillStyle = PARTICLE_DEBUG
        ? `rgba(255, 245, 255, ${particleAlpha})`
        : `rgba(${pr}, ${pg}, ${pb}, ${particleAlpha})`;
      ctx.beginPath();
      ctx.arc(renderable.x, renderable.y, Math.max(1.2, renderable.baseRadius * 0.85), 0, Math.PI * 2);
      ctx.fill();
    }

    ctx.restore();
  }

  drawParticleContourLines(ctx, time) {
    const lineOpacity = Math.max(0, Number(PARTICLE_CONFIG.particleConnectionOpacity || 0.18));
    const baseWidth = Math.max(0.2, Number(PARTICLE_CONFIG.particleConnectionWidth || 1));
    const outerSmoothing = Math.max(
      0,
      Math.floor(PARTICLE_CONFIG.particleContourOuterSmoothing || 2),
    );
    const waveAmplitude = Math.max(
      0,
      Number(PARTICLE_CONFIG.particleFieldLineWaveAmplitude || 0),
    ) * 0.35;
    const waveSpeed = Number(PARTICLE_CONFIG.particleFieldLineWaveSpeed || 0.12);
    const [pr, pg, pb] = this.particleRgb;
    const [gr, gg, gb] = this.glowRgb;

    ctx.save();
    ctx.lineCap = "round";

    const smoothPolyline = (points, iterations) => {
      let output = points;
      for (let iteration = 0; iteration < iterations; iteration += 1) {
        if (!Array.isArray(output) || output.length < 3) return output;
        const next = [output[0]];
        for (let i = 0; i < output.length - 1; i += 1) {
          const a = output[i];
          const b = output[i + 1];
          next.push({
            x: a.x * 0.75 + b.x * 0.25,
            y: a.y * 0.75 + b.y * 0.25,
          });
          next.push({
            x: a.x * 0.25 + b.x * 0.75,
            y: a.y * 0.25 + b.y * 0.75,
          });
        }
        next.push(output[output.length - 1]);
        output = next;
      }
      return output;
    };

    for (let i = 0; i < this.fieldLineCurves.length; i += 1) {
      const contour = this.fieldLineCurves[i];
      const segment = Array.isArray(contour?.points) ? contour.points : contour;
      if (!Array.isArray(segment) || segment.length < 2) continue;
      const levelNorm = clamp(contour?.levelNorm ?? 0.5, 0, 1);
      const outskirts = 1 - levelNorm;
      const smoothingIterations = Math.round(outerSmoothing * outskirts);
      let points = smoothingIterations > 0 ? smoothPolyline(segment, smoothingIterations) : segment;
      if (waveAmplitude > 0 && points.length >= 2) {
        const animated = [];
        for (let pointIndex = 0; pointIndex < points.length; pointIndex += 1) {
          const current = points[pointIndex];
          const previous = points[Math.max(0, pointIndex - 1)];
          const next = points[Math.min(points.length - 1, pointIndex + 1)];
          const dx = next.x - previous.x;
          const dy = next.y - previous.y;
          const length = Math.hypot(dx, dy) || 1;
          const normalX = -dy / length;
          const normalY = dx / length;
          const progress = points.length <= 1 ? 0 : pointIndex / (points.length - 1);
          const envelope = Math.sin(progress * Math.PI);
          const phase = time * waveSpeed + i * 0.11 + progress * Math.PI * 2;
          const offset = Math.sin(phase) * waveAmplitude * envelope;
          animated.push({
            x: current.x + normalX * offset,
            y: current.y + normalY * offset,
          });
        }
        points = animated;
      }

      const fade = 0.18 + levelNorm * 0.82;
      const glowAlpha = lineOpacity * (0.12 + levelNorm * 0.42);
      const strokeAlpha = lineOpacity * fade;
      const strokeWidth = baseWidth * (0.72 + levelNorm * 0.5);
      const outerShadeAlpha = lineOpacity * Math.pow(outskirts, 1.2) * 0.22;
      if (outerShadeAlpha > 0.01) {
        ctx.strokeStyle = PARTICLE_DEBUG
          ? `rgba(120, 80, 220, ${clamp(outerShadeAlpha, 0, 0.7)})`
          : `rgba(${gr}, ${gg}, ${gb}, ${outerShadeAlpha})`;
        ctx.lineWidth = Math.max(0.3, strokeWidth * (0.92 + outskirts * 0.35));
        ctx.beginPath();
        ctx.moveTo(points[0].x, points[0].y);
        for (let pointIndex = 1; pointIndex < points.length; pointIndex += 1) {
          ctx.lineTo(points[pointIndex].x, points[pointIndex].y);
        }
        ctx.stroke();
      }

      ctx.strokeStyle = PARTICLE_DEBUG
        ? `rgba(255, 210, 250, ${clamp(glowAlpha, 0, 0.98)})`
        : `rgba(${gr}, ${gg}, ${gb}, ${glowAlpha})`;
      ctx.lineWidth = strokeWidth * 1.8;
      ctx.beginPath();
      ctx.moveTo(points[0].x, points[0].y);
      for (let pointIndex = 1; pointIndex < points.length; pointIndex += 1) {
        ctx.lineTo(points[pointIndex].x, points[pointIndex].y);
      }
      ctx.stroke();

      ctx.strokeStyle = PARTICLE_DEBUG
        ? `rgba(255, 245, 255, ${clamp(strokeAlpha, 0, 0.98)})`
        : `rgba(${pr}, ${pg}, ${pb}, ${strokeAlpha})`;
      ctx.lineWidth = strokeWidth;
      ctx.beginPath();
      ctx.moveTo(points[0].x, points[0].y);
      for (let pointIndex = 1; pointIndex < points.length; pointIndex += 1) {
        ctx.lineTo(points[pointIndex].x, points[pointIndex].y);
      }
      ctx.stroke();
    }

    ctx.restore();
  }
}

function bootstrap() {
  if (window.__slideParticlesInstance) return;
  const reveal = window.Reveal;
  const revealElement = reveal?.getRevealElement?.() || document.querySelector(".reveal");
  if (!reveal || !revealElement) {
    window.setTimeout(bootstrap, 120);
    return;
  }

  if (getComputedStyle(revealElement).getPropertyValue("--slide-particles-enabled").trim() === "0" && !["pastel-dust", "pastel-cells"].includes(PARTICLE_THEME_KEY)) return;

  const instance = new SlideParticles();
  window.__slideParticlesInstance = instance;
  instance.init(reveal);
}

installDebugMarker();
bootstrap();
