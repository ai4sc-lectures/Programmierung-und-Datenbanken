(function () {
  const SCRAMBLE_SELECTOR = ".fragment.scramble, .fragment.scramble-auto";
  const SCRAMBLE_SLIDE_CLASS = "scramble-slide";
  const SCRAMBLE_AUTO_CLASS = "scramble-auto";
  const SCRAMBLE_STEPS = 12;
  const SCRAMBLE_DURATION_MS = 700;
  const MAX_SCRAMBLE_CHARS = 600;

  const COUNT_SELECTOR = ".fragment.count, .fragment.count-auto";
  const COUNT_AUTO_CLASS = "count-auto";
  const COUNT_STEPS = 30;
  const COUNT_DURATION_MS = 700;

  const lowerChars = Array.from("abcdefghijklmnopqrstuvwxyz");
  const upperChars = Array.from("ABCDEFGHIJKLMNOPQRSTUVWXYZ");
  const digitChars = Array.from("0123456789");

  const fragmentState = new WeakMap();
  let initialized = false;
  let autoTriggerTimer = 0;

  const randomFrom = (chars) => chars[Math.floor(Math.random() * chars.length)];

  const noiseChar = (char) => {
    if (/[A-Z]/.test(char)) return randomFrom(upperChars);
    if (/[a-z]/.test(char)) return randomFrom(lowerChars);
    if (/[0-9]/.test(char)) return randomFrom(digitChars);
    return char;
  };

  const getTextNodes = (root) => {
    const walker = document.createTreeWalker(root, NodeFilter.SHOW_TEXT);
    const nodes = [];

    while (walker.nextNode()) {
      const node = walker.currentNode;
      if (!node.nodeValue || node.nodeValue.length === 0) continue;
      nodes.push({
        node,
        original: node.nodeValue,
      });
    }

    return nodes;
  };

  const ensureFragmentState = (fragment) => {
    let state = fragmentState.get(fragment);
    if (state) return state;

    state = {
      textNodes: getTextNodes(fragment),
      timers: [],
    };

    fragmentState.set(fragment, state);
    return state;
  };

  const clearTimers = (state) => {
    for (const timer of state.timers) {
      window.clearTimeout(timer);
    }
    state.timers = [];
  };

  const restoreOriginalText = (fragment) => {
    const state = ensureFragmentState(fragment);
    clearTimers(state);
    for (const entry of state.textNodes) {
      entry.node.nodeValue = entry.original;
    }
  };

  const renderScrambledFrame = (state, revealCount) => {
    let remainingReveal = revealCount;
    let remainingScramble = MAX_SCRAMBLE_CHARS;

    for (const entry of state.textNodes) {
      const sourceChars = Array.from(entry.original);
      const nextChars = sourceChars.map((char, index) => {
        if (remainingReveal > 0) {
          remainingReveal -= 1;
          return sourceChars[index];
        }

        if (remainingScramble > 0) {
          remainingScramble -= 1;
          return noiseChar(char);
        }

        return sourceChars[index];
      });

      entry.node.nodeValue = nextChars.join("");
    }
  };

  const scrambleFragment = (fragment) => {
    const state = ensureFragmentState(fragment);
    const totalChars = state.textNodes.reduce(
      (count, entry) => count + Array.from(entry.original).length,
      0,
    );

    restoreOriginalText(fragment);

    if (totalChars === 0) return;

    const scrambleChars = Math.min(totalChars, MAX_SCRAMBLE_CHARS);
    renderScrambledFrame(state, 0);

    for (let step = 1; step <= SCRAMBLE_STEPS; step += 1) {
      const revealCount = Math.floor((scrambleChars * step) / SCRAMBLE_STEPS);
      const delay = (SCRAMBLE_DURATION_MS * step) / SCRAMBLE_STEPS;
      const timer = window.setTimeout(() => {
        renderScrambledFrame(state, revealCount);
      }, delay);
      state.timers.push(timer);
    }
  };

  const parseNumberInText = (text) => {
    const match = text.match(/^([^0-9-]*)(-?\d+)(.*)/);
    if (!match) return null;
    const numStr = match[2];
    const value = parseInt(numStr, 10);
    const digits = numStr.replace("-", "");
    return {
      prefix: match[1],
      value,
      suffix: match[3],
      padWidth: Math.abs(value).toString().length < digits.length ? digits.length : 0,
    };
  };

  const formatCountValue = (current, parsed) => {
    const sign = current < 0 ? "-" : parsed.value < 0 && current === 0 ? "-" : "";
    const abs = Math.abs(current).toString().padStart(parsed.padWidth, "0");
    return parsed.prefix + sign + abs + parsed.suffix;
  };

  const countFragment = (fragment) => {
    const state = ensureFragmentState(fragment);
    clearTimers(state);

    for (const entry of state.textNodes) {
      const parsed = parseNumberInText(entry.original);
      if (!parsed) continue;

      const target = parsed.value;
      entry.node.nodeValue = formatCountValue(0, parsed);

      for (let step = 1; step <= COUNT_STEPS; step++) {
        const current = Math.round(target * (step / COUNT_STEPS));
        const delay = (COUNT_DURATION_MS * step) / COUNT_STEPS;
        const timer = window.setTimeout(() => {
          entry.node.nodeValue = formatCountValue(current, parsed);
        }, delay);
        state.timers.push(timer);
      }
    }
  };

  const getFragmentsWithSameIndex = (fragment) => {
    const index = fragment.getAttribute("data-fragment-index");
    if (index === null) return [fragment];

    const slide = fragment.closest("section");
    if (!slide) return [fragment];

    return Array.from(
      slide.querySelectorAll(
        `.fragment.scramble[data-fragment-index="${index}"], .fragment.scramble-auto[data-fragment-index="${index}"]`,
      ),
    );
  };

  const getNextHiddenFragment = (slide) => {
    const fragments = Array.from(slide.querySelectorAll(".fragment"));
    for (const fragment of fragments) {
      if (!fragment.classList.contains("visible")) {
        return fragment;
      }
    }
    return null;
  };

  const isScrambleSlide = (slide) =>
    slide instanceof Element && slide.classList.contains(SCRAMBLE_SLIDE_CLASS);

  const isAutoFragment = (fragment) =>
    fragment instanceof Element &&
    (fragment.classList.contains(SCRAMBLE_AUTO_CLASS) || fragment.classList.contains(COUNT_AUTO_CLASS));

  const scheduleAutoFragment = (slide) => {
    if (!(slide instanceof Element)) return;

    window.clearTimeout(autoTriggerTimer);
    autoTriggerTimer = window.setTimeout(() => {
      const nextFragment = getNextHiddenFragment(slide);
      if (!isAutoFragment(nextFragment)) return;
      Reveal.nextFragment();
    }, 0);
  };

  const playScrambleSlide = (slide) => {
    if (!isScrambleSlide(slide)) return;
    scrambleFragment(slide);
  };

  const resetScrambleSlide = (slide) => {
    if (!isScrambleSlide(slide)) return;
    restoreOriginalText(slide);
  };

  const initScrambleFragments = () => {
    if (initialized) return;
    initialized = true;

    Reveal.on("ready", (event) => {
      const currentSlide = event.currentSlide || Reveal.getCurrentSlide();
      scheduleAutoFragment(currentSlide);
      playScrambleSlide(currentSlide);
    });

    Reveal.on("slidechanged", (event) => {
      resetScrambleSlide(event.previousSlide);
      const currentSlide = event.currentSlide || Reveal.getCurrentSlide();
      scheduleAutoFragment(currentSlide);
      playScrambleSlide(currentSlide);
    });

    Reveal.on("fragmentshown", (event) => {
      const fragment = event.fragment;
      if (!(fragment instanceof Element)) return;

      if (fragment.matches(COUNT_SELECTOR)) {
        countFragment(fragment);
      }

      if (fragment.matches(SCRAMBLE_SELECTOR)) {
        const fragments = getFragmentsWithSameIndex(fragment);
        fragments.forEach((item) => {
          item.classList.add("scramble-playing");
          scrambleFragment(item);
        });
      }

      if (isAutoFragment(fragment)) {
        scheduleAutoFragment(fragment.closest("section"));
      }
    });

    Reveal.on("fragmenthidden", (event) => {
      const fragment = event.fragment;
      if (!(fragment instanceof Element)) return;

      if (fragment.matches(COUNT_SELECTOR)) {
        restoreOriginalText(fragment);
      }

      if (fragment.matches(SCRAMBLE_SELECTOR)) {
        const fragments = getFragmentsWithSameIndex(fragment);
        fragments.forEach((item) => {
          item.classList.remove("scramble-playing");
          restoreOriginalText(item);
        });
      }
    });

    // The "ready" event has already fired when this runs (direct link to a slide,
    // or the first slide), so start the current slide here.
    if (Reveal.isReady()) {
      const currentSlide = Reveal.getCurrentSlide();
      scheduleAutoFragment(currentSlide);
      playScrambleSlide(currentSlide);
    }
  };

  const setupReveal = () => {
    if (typeof Reveal === "undefined") return;

    if (Reveal.isReady()) {
      initScrambleFragments();
    } else {
      Reveal.on("ready", () => {
        initScrambleFragments();
      });
    }
  };

  if (document.readyState === "complete") {
    setupReveal();
  } else {
    window.addEventListener("load", setupReveal, { once: true });
  }
})();
