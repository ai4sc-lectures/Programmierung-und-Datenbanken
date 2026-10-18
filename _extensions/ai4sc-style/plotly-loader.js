/**
 * Plotly Loader & Helper - AMD/RequireJS-safe
 * 
 * Usage in Quarto:
 * <script type="module" src="_extensions/ai4sc-style/plotly-loader.js"></script>
 * <script type="module">
 *   await window.renderPlotlyFromJSON('myDiv', 'data/figure.json');
 * </script>
 */

/** Load Plotly once (AMD/RequireJS-safe) and expose a render helper. */
window.PLOTLY_READY = window.PLOTLY_READY || (async () => {
  // Quarto relocates this loader into site_libs; resources retain deck-relative URLs.
  const { pastelloLayout, pastelloDefaults, pastelloOptions, attachPastello, refreshPastello } = await import(
    new URL('_extensions/ai4sc-style/plotly-pastello.js', document.baseURI).href
  );
  const hasRealPlotly = () =>
    Boolean(window.Plotly?.newPlot) && !window.Plotly?.__ai4scPlotlyStub;

  if (!hasRealPlotly()) {
    // Temporarily disable AMD so Plotly attaches to window.Plotly
    const savedDefine = window.define;
    try { window.define = undefined; } catch {}
    
    await new Promise((res, rej) => {
      const s = document.createElement("script");
      s.src = "_extensions/ai4sc-style/plotly.min.js";
      s.async = false;
      s.onload = res;
      s.onerror = () => rej(new Error("Failed to load local _extensions/ai4sc-style/plotly.min.js"));
      document.head.appendChild(s);
    });
    
    if (savedDefine !== undefined) window.define = savedDefine;
  }
  
  if (!hasRealPlotly()) {
    throw new Error("Plotly global not available");
  }

  const sleep = (ms) =>
    new Promise((resolve) => {
      window.setTimeout(resolve, ms);
    });

  const nextFrame = () =>
    new Promise((resolve) => {
      window.requestAnimationFrame(() => resolve());
    });

  const isVisible = (el) => {
    if (!el) return false;
    const style = window.getComputedStyle(el);
    const rect = el.getBoundingClientRect();
    return (
      style.display !== "none" &&
      style.visibility !== "hidden" &&
      rect.width > 24 &&
      rect.height > 24
    );
  };

  const getPlotEls = (root = document) =>
    Array.from(root.querySelectorAll(".plotly-graph-div"))
      .filter((el) => el instanceof HTMLElement);

  const getOwnerSlide = (el) => el?.closest?.(".slides section");

  const isCurrentRevealSlide = (slide) => {
    if (!slide) return true;
    const current = window.Reveal?.getCurrentSlide?.();
    return !current || slide === current;
  };

  const hasStableBox = (el) => {
    if (!el) return false;
    const rect = el.getBoundingClientRect();
    const parentRect = el.parentElement?.getBoundingClientRect?.();
    return (
      rect.width > 80 &&
      rect.height > 80 &&
      (!parentRect || parentRect.width > 80)
    );
  };

  const isRenderablePlot = (el) => {
    if (!isVisible(el) || !hasStableBox(el)) return false;
    const slide = getOwnerSlide(el);
    if (slide && !isCurrentRevealSlide(slide)) return false;
    return true;
  };

  const pendingPlots = new Map();
  const activeResizes = new WeakMap();
  const activeAnimations = new WeakMap();
  const completedAnimations = new WeakMap();
  const slideActivationIds = new WeakMap();
  let flushHandle = 0;
  let slideActivationSerial = 0;

  const hasLivePlotlyGraph = (el) =>
    el instanceof HTMLElement &&
    el.isConnected &&
    el.classList?.contains("js-plotly-plot") &&
    Boolean(el._fullLayout) &&
    Boolean(el._context);

  const isBenignResizeError = (error) => {
    const message = String(error?.message || error || "");
    return (
      error instanceof TypeError &&
      (message.includes("_guiEditing") ||
        message.includes("is undefined") ||
        message.includes("is null"))
    );
  };

  const getPlotMeta = (el) => el?._fullLayout?.meta || el?.layout?.meta || null;

  const getPlotData = (el) => el?._fullData || el?.data || [];

  const markSlideActivation = (slide) => {
    if (!slide) return 0;
    const id = ++slideActivationSerial;
    slideActivationIds.set(slide, id);
    return id;
  };

  const getSlideActivation = (slide) => {
    if (!slide) return 0;
    return slideActivationIds.get(slide) || 0;
  };

  const resizePlot = async (el) => {
    if (!window.Plotly?.Plots || !isRenderablePlot(el) || !hasLivePlotlyGraph(el)) {
      return;
    }

    const existing = activeResizes.get(el);
    if (existing) {
      await existing;
      return;
    }

    const job = (async () => {
      if (!hasLivePlotlyGraph(el)) return;
      await window.Plotly.Plots.resize(el);
      refreshPastello(el);
    })();

    activeResizes.set(el, job);

    try {
      await job;
    } catch (error) {
      if (!hasLivePlotlyGraph(el) || isBenignResizeError(error)) {
        return;
      }
      console.warn("plotly-loader: resize failed", error);
    } finally {
      if (activeResizes.get(el) === job) {
        activeResizes.delete(el);
      }
    }
  };

  const stabilizePlot = async (el) => {
    if (!el) return;
    await nextFrame();
    await nextFrame();
    await resizePlot(el);
    for (const delay of [80, 220, 520]) {
      await sleep(delay);
      if (!el?.isConnected) return;
      await resizePlot(el);
    }
  };

  const stabilizeVisiblePlots = async () => {
    const slide = window.Reveal?.getCurrentSlide?.();
    const scope = slide || document;
    const plots = getPlotEls(scope);
    for (const el of plots) {
      void stabilizePlot(el);
    }
  };

  const renderDeferredPlot = async (el, job) => {
    if (!el?.isConnected || !job) return;
    try {
      const result = await originalNewPlot(...job.args);
      attachPastello(el);
      void stabilizePlot(el);
      window.setTimeout(() => {
        void animatePlotEntry(el);
      }, 120);
      job.resolve(result);
    } catch (error) {
      job.reject(error);
    } finally {
      pendingPlots.delete(el);
    }
  };

  const flushPendingPlots = async () => {
    flushHandle = 0;
    const jobs = Array.from(pendingPlots.entries());
    for (const [el, job] of jobs) {
      if (!el?.isConnected) {
        job.reject(new Error("Deferred Plotly target was removed before render"));
        pendingPlots.delete(el);
        continue;
      }
      if (!isRenderablePlot(el)) continue;
      await renderDeferredPlot(el, job);
    }
  };

  const scheduleFlushPendingPlots = (delay = 0) => {
    window.clearTimeout(flushHandle);
    flushHandle = window.setTimeout(() => {
      void flushPendingPlots();
    }, delay);
  };

  // ── AI4SC Theme Integration ────────────────────────────────────────────────
  const getAI4SCTemplate = () => {
    const reveal = document.querySelector('.reveal');
    if (!reveal) return {};
    if (pastelloOptions().enabled) return {layout: pastelloDefaults()};
    const get = (name) => getComputedStyle(reveal).getPropertyValue(name).trim();

    const paper     = get('--paper');
    const bone      = get('--bone');
    const ink       = get('--ink');
    const rebar     = get('--rebar');
    const accent    = get('--accent');
    const sigBlue    = get('--signal-blue');
    const sigBlue50    = get('--signal-blue-50');
    const sigRed    = get('--signal-red');
    const sigRed50    = get('--signal-red-50');
    const sigYellow = get('--signal-yellow');
    const sigYellow50 = get('--signal-yellow-50');
    const sigGreen   = get('--signal-green');
    const sigGreen50 = get('--signal-green-50');
    const moss700   = get('--moss-700');
    const moss500   = get('--moss-500');
    const moss300   = get('--moss-300');
    const moss100   = get('--moss-100');
    const concrete  = get('--concrete');
    const carbon    = get('--carbon');
    const plaster   = get('--plaster');

    const colorway = [sigBlue, sigBlue50, sigRed, sigRed50, sigYellow, sigYellow50, sigGreen, sigGreen50, carbon, rebar, concrete, plaster, moss700, moss300, moss500, moss100].filter(Boolean);
    const axisStyle = { gridcolor: rebar, zerolinecolor: rebar, linecolor: rebar, tickfont: { color: ink } };

    return {
      layout: {
        paper_bgcolor: paper,
        plot_bgcolor:  bone,
        colorway,
        font:   { color: ink, family: 'DINPro, Inter, ui-sans-serif, system-ui, sans-serif', size: 16 },
        title: { font: { size: 24 } },
        xaxis:  axisStyle,
        yaxis:  axisStyle,
        legend: { bgcolor: 'rgba(0,0,0,0)', bordercolor: rebar, font: { color: ink } },
      },
    };
  };

  window.getAI4SCTemplate = getAI4SCTemplate;

  const drainQueuedPlotlyCalls = async () => {
    const queue = Array.isArray(window.__plotlyCallQueue)
      ? window.__plotlyCallQueue.splice(0)
      : [];

    for (const call of queue) {
      if (!call || !call.method) continue;
      try {
        if (call.method === "newPlot") {
          const result = await window.Plotly.newPlot(...(call.args || []));
          call.resolve?.(result);
          continue;
        }

        if (call.method === "addFrames") {
          const result = await window.Plotly.addFrames(...(call.args || []));
          call.resolve?.(result);
          continue;
        }
      } catch (error) {
        call.reject?.(error);
      }
    }
  };

  const originalNewPlot = window.Plotly.newPlot.bind(window.Plotly);
  window.Plotly.newPlot = (...args) => {
    const target = args[0];
    const el =
      typeof target === "string" ? document.getElementById(target) : target;

    if (args[2]?.template === undefined) {
      args = args.slice();
      args[2] = { template: getAI4SCTemplate(), ...(args[2] || {}) };
    }

    args = args.slice();
    args[2] = pastelloLayout(args[2] || {});

    if (!(el instanceof HTMLElement)) {
      return originalNewPlot(...args);
    }

    return (async () => {
      const result = await originalNewPlot(...args);
      attachPastello(el);
      if (isRenderablePlot(el)) {
        void stabilizePlot(el);
        window.setTimeout(() => {
          void animatePlotEntry(el);
        }, 120);
      }
      return result;
    })();
  };

  // React can replace the complete layout/template and reset trace elements.
  const originalReact = window.Plotly.react.bind(window.Plotly);
  window.Plotly.react = async (target, data, layout, config) => {
    // Preserve Plotly's {data, layout, config} calling convention as well.
    if (data && !Array.isArray(data) && typeof data === "object") {
      const spec = data;
      data = spec.data;
      layout = spec.layout;
      config = spec.config;
    }
    const result = await originalReact(target, data, pastelloLayout(layout || {}), config);
    attachPastello(typeof target === "string" ? document.getElementById(target) : target);
    return result;
  };

  // Helper: render from external JSON
  window.renderPlotlyFromJSON = async (elId, url) => {
    const spec = await fetch(url).then(r => r.json());
    const el = document.getElementById(elId);
    if (!el) throw new Error(`Element #${elId} not found`);
    await Plotly.newPlot(el, spec.data, spec.layout, spec.config || {});
    if (spec.frames?.length) Plotly.addFrames(el, spec.frames);
  };

  // Plotly.js stores numeric arrays as TypedArrays (Float64Array etc.) after
  // rendering, so Array.isArray alone misses them.
  const isNumericArray = (v) =>
    Array.isArray(v) || (ArrayBuffer.isView(v) && !(v instanceof DataView));

  const buildZeroTrace = (trace) => {
    const t = trace.type || "scatter";
    const zero = {};
    if (["bar", "waterfall", "funnel"].includes(t)) {
      if (trace.orientation === "h") {
        if (isNumericArray(trace.x)) zero.x = Array.from({length: trace.x.length}, () => 0);
      } else {
        if (isNumericArray(trace.y)) zero.y = Array.from({length: trace.y.length}, () => 0);
      }
    } else if (["scatter", "scattergl", "scatterpolar"].includes(t)) {
      if (isNumericArray(trace.y)) zero.y = Array.from({length: trace.y.length}, () => 0);
    }
    return Object.keys(zero).length > 0 ? zero : null;
  };

  const animatePlotEntry = async (el) => {
    if (!hasLivePlotlyGraph(el) || !window.Plotly?.animate) return;
    const meta = getPlotMeta(el);
    if (!meta?.ai4sc_animate_on_slide) return;
    const slide = getOwnerSlide(el);
    if (slide && !isCurrentRevealSlide(slide)) return;

    const activationId = getSlideActivation(slide);
    if (activationId && completedAnimations.get(el) === activationId) return;

    const existing = activeAnimations.get(el);
    if (existing) {
      await existing;
      return;
    }

    const duration = meta.ai4sc_animate_duration ?? 700;
    const easing = meta.ai4sc_animate_easing ?? "cubic-in-out";
    const data = getPlotData(el);
    if (!data?.length) return;

    const job = (async () => {
      const indices = [];
      const zeroUpdate = {};  // restyle format: {key: [vals_per_trace, ...]}
      const fullTraces = [];  // animate format: [{key: vals}, ...]

      for (let i = 0; i < data.length; i++) {
        const trace = data[i];
        const zeroTrace = buildZeroTrace(trace);
        if (!zeroTrace) continue;
        const fullTrace = {};
        for (const [key, zeroVals] of Object.entries(zeroTrace)) {
          const val = trace[key];
          fullTrace[key] = Array.from(val);
          if (!zeroUpdate[key]) zeroUpdate[key] = [];
          zeroUpdate[key].push(zeroVals);
        }
        indices.push(i);
        fullTraces.push(fullTrace);
      }

      if (!indices.length) return;

      try {
        await window.Plotly.restyle(el, zeroUpdate, indices);
        await nextFrame();
        await window.Plotly.animate(
          el,
          {data: fullTraces, traces: indices},
          {transition: {duration, easing}, frame: {duration, redraw: true}}
        );
        if (activationId) {
          completedAnimations.set(el, activationId);
        }
      } catch {}
    })();

    activeAnimations.set(el, job);
    try {
      await job;
    } finally {
      if (activeAnimations.get(el) === job) {
        activeAnimations.delete(el);
      }
    }
  };

  const animateSlideEntry = (slide) => {
    markSlideActivation(slide);
    for (const el of getPlotEls(slide || document)) {
      void animatePlotEntry(el);
    }
  };

  const bindRevealPlotlyResize = () => {
    if (!window.Reveal?.on || window.__plotlyRevealResizeBound) return;
    window.__plotlyRevealResizeBound = true;

    const scheduleVisibleStabilize = (delay = 0) => {
      window.setTimeout(() => {
        scheduleFlushPendingPlots(0);
        void stabilizeVisiblePlots();
      }, delay);
    };

    window.Reveal.on("ready", () => {
      scheduleVisibleStabilize(80);
      window.setTimeout(
        () => animateSlideEntry(window.Reveal.getCurrentSlide()), 400
      );
    });
    window.Reveal.on("slidechanged", ({currentSlide}) => {
      scheduleVisibleStabilize(220);
      window.setTimeout(() => animateSlideEntry(currentSlide), 450);
    });
    window.Reveal.on("slidetransitionend", () => scheduleVisibleStabilize(40));
    window.Reveal.on("fragmentshown", () => scheduleVisibleStabilize(120));
    window.Reveal.on("fragmenthidden", () => scheduleVisibleStabilize(120));
    window.addEventListener("resize", () => scheduleVisibleStabilize(120));
  };

  void drainQueuedPlotlyCalls();

  bindRevealPlotlyResize();
  window.setTimeout(bindRevealPlotlyResize, 200);
  window.setTimeout(() => {
    scheduleFlushPendingPlots(0);
    void stabilizeVisiblePlots();
  }, 300);

  if (window.ResizeObserver) {
    const resizeObserver = new ResizeObserver(() => {
      scheduleFlushPendingPlots(40);
      void stabilizeVisiblePlots();
    });
    const observePlots = () => {
      getPlotEls(document).forEach((el) => {
        if (el.__plotlyResizeObserved) return;
        resizeObserver.observe(el);
        if (el.parentElement) resizeObserver.observe(el.parentElement);
        el.__plotlyResizeObserved = true;
      });
    };
    observePlots();
    window.setTimeout(observePlots, 500);
    window.setTimeout(observePlots, 1200);
  }

  return window.Plotly;
})();

// Auto-initialize on import
await window.PLOTLY_READY;
