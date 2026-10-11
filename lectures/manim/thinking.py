"""Manim scenes for the slide "Warum nicht? → Die Modellfalle" (03d_AgentischesProgrammieren.qmdx).

Adapted from Presentations/2026/template/examples/manim/thinking.py: the palette is the light
"pastello" theme (_extensions/ai4sc-style/themes/color/pastello.css) instead of the dark cyberpunk one.

Render (portrait 9:10, matches the 450px slide columns), from the lectures/ directory:

    manim/render.sh manim/thinking.py HumanThinking 900,1000 images/03d_AgentischesProgrammieren/manim_thinking_human.mp4
    manim/render.sh manim/thinking.py LLMThinking 900,1000 images/03d_AgentischesProgrammieren/manim_thinking_llm.mp4
"""
import numpy as np
from manim import *

config.frame_height = 10
config.frame_width = 9
config.background_color = "#F8F7F2"

# pastello theme (_extensions/ai4sc-style/themes/color/pastello.css)
INK = "#302F2B"
MUTED = "#68665E"     # carbon
RIM = "#DAD7CB"
GREEN = "#8B9E87"     # signal-green
MOSS = "#52664D"      # moss-700, for green text
RED = "#C58E89"       # signal-red
CYAN = "#91B5CB"      # signal-blue: prompt / AI output
YELLOW = "#D6B65E"    # signal-yellow
BG = "#F8F7F2"
BUBBLE = "#F3F1E8"    # bone
FONT = "Helvetica Neue"


def T(text, size=26, color=INK, **kw):
    return Text(text, font=FONT, font_size=size, color=color, **kw)


def caption(num, text, color):
    n = T(f"{num}", 34, INK, weight=BOLD)
    badge = VGroup(Circle(0.28, color=color, fill_opacity=1, stroke_width=0), n)
    n.move_to(badge[0])
    label = T(text, 30, INK)
    return VGroup(badge, label).arrange(RIGHT, buff=0.25).move_to([0, 4.55, 0])


def check_mark(color=GREEN, s=0.35):
    return VMobject(color=color, stroke_width=8).set_points_as_corners(
        [[-s, 0, 0], [-s * 0.3, -s * 0.7, 0], [s, s * 0.8, 0]])


def cross_mark(color=RED, s=0.3):
    return VGroup(Line([-s, -s, 0], [s, s, 0]), Line([-s, s, 0], [s, -s, 0])).set_stroke(color, 8)


def prob_rows(cands, y0, spacing=0.8, x_bar=-2.4):
    """Next-token distribution: one row (label, bar, percent) per candidate."""
    rows = VGroup()
    for i, (w, p) in enumerate(cands):
        y = y0 - spacing * i
        lab = T(w, 24, INK).move_to([-3.7, y, 0], aligned_edge=LEFT)
        bar = Rectangle(width=7.5 * p, height=0.5, color=RED, fill_color=RED,
                        fill_opacity=0.55, stroke_width=0)
        bar.move_to([x_bar + bar.width / 2, y, 0])
        pct = T(f"{int(p * 100)} %", 22, MUTED).next_to(bar, RIGHT, buff=0.15)
        rows.add(VGroup(lab, bar, pct))
    return rows


def beam(x0, x1, y, dt, color, sw=14, arrow=1.0):
    """Beam on two supports with a point load at midspan; dt = deflection tracker."""
    d = dt.get_value()
    xm = (x0 + x1) / 2
    curve = ParametricFunction(
        lambda t: [t, y - d * np.sin(PI * (t - x0) / (x1 - x0)), 0],
        t_range=[x0, x1], color=color, stroke_width=sw)
    sup = VGroup(*[Triangle(color=INK, fill_opacity=0.0, stroke_width=3).scale(0.2)
                   .move_to([x, y - 0.3, 0]) for x in (x0, x1)])
    load = Arrow([xm, y + arrow, 0], [xm, y - d + 0.1, 0], buff=0, color=YELLOW,
                 stroke_width=6, max_tip_length_to_length_ratio=0.35)
    return VGroup(curve, sup, load)


class HumanThinking(Scene):
    def construct(self):
        # --- real-world problem (bottom) ---------------------------------
        d_real = ValueTracker(0)
        real = always_redraw(lambda: beam(-2.2, 2.2, -3.7, d_real, INK, 12, 0.75))
        real_lbl = T("Reales Problem: Balken unter Last", 22, MUTED).move_to([0, -4.65, 0])
        hx, hy = -3.55, -3.0
        head = Circle(0.5, color=INK, stroke_width=5, fill_color=BG, fill_opacity=1).move_to([hx, hy, 0])
        shoulders = Arc(radius=0.95, start_angle=0, angle=PI, color=INK, stroke_width=5
                        ).move_to([hx, -4.45, 0], aligned_edge=DOWN)
        neck = Line([hx, hy - 0.5, 0], [hx, -3.6, 0], color=INK, stroke_width=5)
        eyes = VGroup(*[Dot(radius=0.05, color=INK).move_to([hx + dx, hy + 0.08, 0]) for dx in (0.05, 0.28)])
        person = VGroup(neck, shoulders, head, eyes)
        self.play(FadeIn(real), FadeIn(real_lbl), FadeIn(person), run_time=1)

        # --- 1 mentales Modell -------------------------------------------
        cap = caption(1, "Mentales Modell", GREEN)
        cx, cy, rx, ry = 0, 1.85, 3.7, 1.4
        # equal arc-length spacing so neighbouring puffs overlap everywhere on the ellipse
        th = np.linspace(0, TAU, 2000)
        seg = np.hypot(np.diff(rx * np.cos(th)), np.diff(ry * np.sin(th)))
        cum = np.concatenate([[0], np.cumsum(seg)])
        ang = np.interp(np.linspace(0, cum[-1], 22, endpoint=False), cum, th)
        puffs = VGroup(*[Circle(0.62, color=GREEN, fill_color=BG, fill_opacity=1, stroke_width=3)
                         .move_to([cx + rx * np.cos(a), cy + ry * np.sin(a), 0]) for a in ang])
        core = Ellipse(2 * rx, 2 * ry, color=BG, fill_color=BG, fill_opacity=1, stroke_width=0
                       ).move_to([cx, cy, 0])
        trail = VGroup(*[Circle(r, color=GREEN, stroke_width=3, fill_color=BG, fill_opacity=1)
                         .move_to([x, y, 0]) for r, x, y in
                         [(0.11, -3.5, -2.1), (0.17, -3.45, -1.4), (0.25, -3.2, -0.5)]])
        d_mod = ValueTracker(0)
        model = always_redraw(lambda: beam(-2.4, 2.4, 1.85, d_mod, CYAN, 14, 1.15))
        self.play(FadeIn(cap), LaggedStart(*[GrowFromCenter(t) for t in trail], lag_ratio=0.35),
                  run_time=1.2)
        cloud = VGroup(puffs, core)
        self.play(GrowFromPoint(cloud, [-3.2, -0.5, 0]), run_time=1.0)
        self.play(TransformFromCopy(real, model), run_time=1.2)
        self.wait(0.6)

        # --- 2 abstrakte Zusammenhänge -----------------------------------
        cap2 = caption(2, "Versteht warum der Balken sich biegt", GREEN)
        react = VGroup(*[Arrow([x, 0.9, 0], [x, 1.5, 0], buff=0, color=CYAN, stroke_width=5,
                               max_tip_length_to_length_ratio=0.4) for x in (-2.4, 2.4)])
        druck = T("Druck", 22, INK).move_to([1.5, 2.5, 0])
        zug = T("Zug", 22, INK).move_to([1.5, 0.75, 0])
        self.play(ReplacementTransform(cap, cap2), run_time=0.6)
        self.play(d_mod.animate.set_value(0.55), d_real.animate.set_value(0.18),
                  run_time=1.6, rate_func=smooth)
        self.play(FadeIn(react), FadeIn(druck), FadeIn(zug), run_time=0.8)
        self.wait(0.7)

        # --- 3 kausale Schlussfolgerungen --------------------------------
        cap3 = caption(3, "Leitet Ursache und Wirkung ab", GREEN)
        boxes = VGroup()
        for s in ("Last F", "Moment M", "Durchbiegung w"):
            t = T(s, 24)
            boxes.add(VGroup(RoundedRectangle(corner_radius=0.15, width=t.width + 0.5, height=0.7,
                                              color=GREEN, stroke_width=3), t))
        boxes.arrange(RIGHT, buff=0.75).scale_to_fit_width(min(6.8, boxes.width)).move_to([0.8, -0.95, 0])
        arrows = VGroup(*[Arrow(boxes[i].get_right(), boxes[i + 1].get_left(), buff=0.08,
                                color=GREEN, stroke_width=4, max_tip_length_to_length_ratio=0.5)
                          for i in range(2)])
        self.play(ReplacementTransform(cap2, cap3), run_time=0.6)
        self.play(FadeIn(boxes[0]), run_time=0.5)
        for i in range(2):
            self.play(GrowArrow(arrows[i]), FadeIn(boxes[i + 1]), run_time=0.7)
        self.wait(0.6)

        # --- 4 rechnen & prüfen ------------------------------------------
        cap4 = caption(4, "Rechnet nach und prüft", GREEN)
        formula = T("w = F·L³ / (48·E·I) = 4,2 mm", 30).move_to([0.8, -1.8, 0])
        ok = VGroup(check_mark(), T("physikalisch plausibel", 26, MOSS)).arrange(RIGHT, buff=0.3)
        ok.move_to([0.8, -2.45, 0])
        self.play(ReplacementTransform(cap3, cap4), run_time=0.6)
        self.play(Write(formula), run_time=1.5)
        self.play(Create(ok[0]), FadeIn(ok[1]), run_time=0.8)
        self.play(Indicate(model, color=GREEN, scale_factor=1.0), run_time=0.8)
        self.wait(2.5)


class LLMThinking(Scene):
    def construct(self):
        # --- prompt as chat bubble ---------------------------------------
        prompt = T("Problem: Ein Balken biegt sich unter Last. Was passiert?", 24, INK)
        prompt.scale_to_fit_width(min(7.4, prompt.width))
        bubble = RoundedRectangle(corner_radius=0.3, width=prompt.width + 0.7, height=prompt.height + 0.6,
                                  color=MUTED, stroke_width=3, fill_color=BUBBLE, fill_opacity=1)
        bubble.move_to([0, 3.5, 0])
        prompt.move_to(bubble)
        self.play(FadeIn(bubble, scale=0.9), run_time=0.5)
        self.play(AddTextLetterByLetter(prompt), run_time=1.2)

        # --- 1 sprachliches Muster ---------------------------------------
        cap = caption(1, "Sprachliches Muster", RED)
        chips = VGroup()
        for w in ("Ein", "Balken", "biegt", "sich", "unter", "Last"):
            t = T(w, 22)
            chips.add(VGroup(RoundedRectangle(corner_radius=0.12, width=t.width + 0.35, height=0.55,
                                              color=CYAN, stroke_width=3), t))
        chips.arrange(RIGHT, buff=0.14).scale_to_fit_width(min(7.8, chips.width)).move_to([0, 2.5, 0])
        self.play(FadeIn(cap), LaggedStart(*[FadeIn(c, shift=DOWN * 0.2) for c in chips],
                                           lag_ratio=0.2), run_time=1.6)
        self.wait(0.4)

        # --- 2 kein mentales Modell --------------------------------------
        cap2 = caption(2, "Nur Korrelationen, kein Modell", RED)
        pos = {"Balken": [-2.6, 0.5], "biegen": [0.0, 0.9], "Spannung": [2.6, 0.5],
               "Last": [-1.5, -1.1], "…": [1.5, -1.1], "Träger": [0, -2.6]}
        nodes = {}
        for k, (x, y) in pos.items():
            t = T(k, 22, INK, line_spacing=0.7)
            nodes[k] = VGroup(RoundedRectangle(corner_radius=0.2, width=max(t.width + 0.4, 1.0),
                                               height=t.height + 0.3, color=CYAN, stroke_width=3,
                                               fill_color=BG, fill_opacity=1), t).move_to([x, y, 0])
        # word co-occurrence strengths (0..1)
        links = [("Balken", "biegen", 1.0), ("biegen", "Spannung", 0.6), ("Balken", "Last", 0.8),
                 ("biegen", "Last", 0.5), ("Spannung", "…", 0.4), ("Last", "…", 0.3),
                 ("Balken", "Spannung", 0.25), ("Last", "Träger", 0.7), ("…", "Träger", 0.35)]
        edges = VGroup(*[Line(nodes[a].get_center(), nodes[b].get_center(), color=CYAN,
                              stroke_width=1 + 5 * w, stroke_opacity=0.2 + 0.6 * w)
                         for a, b, w in links])
        nomodel = T("kein mentales Modell", 24, INK)
        nomodel_box = VGroup(RoundedRectangle(corner_radius=0.15, width=nomodel.width + 0.5, height=0.7,
                                              color=RED, stroke_width=3, fill_color=BG,
                                              fill_opacity=1), nomodel).move_to([0, -0.5, 0])
        self.play(ReplacementTransform(cap, cap2),
                  FadeIn(edges), LaggedStart(*[FadeIn(n) for n in nodes.values()], lag_ratio=0.15),
                  run_time=2.0)
        self.play(FadeIn(nomodel_box, scale=1.3), run_time=0.6)
        self.play(Indicate(nomodel_box, color=RED), run_time=0.8)
        self.wait(0.4)

        # --- 3 statistisch wahrscheinliches Wort -------------------------
        cap3 = caption(3, "Sagt das wahrscheinlichste Wort voraus", RED)
        # set the full sentence as one Text so the appended word sits on the same baseline
        full = T("Der Balken biegt sich durch.", 28, t2w={"durch.": BOLD})
        full.move_to([-3.7, 1.4, 0], aligned_edge=LEFT)
        cut = len("DerBalkenbiegtsich")
        sentence, winner = full[:cut], full[cut:]
        rows = prob_rows([("durch", 0.41), ("unter", 0.27), ("stark", 0.18), ("nach", 0.09)], 0.4)
        self.play(ReplacementTransform(cap2, cap3),
                  *[FadeOut(m) for m in list(nodes.values()) + [edges, nomodel_box]],
                  run_time=0.7)
        self.play(FadeIn(sentence), run_time=0.5)
        self.play(LaggedStart(*[GrowFromEdge(r[1], LEFT) for r in rows], lag_ratio=0.2),
                  FadeIn(VGroup(*[VGroup(r[0], r[2]) for r in rows])), run_time=1.6)
        self.play(rows[0][1].animate.set_fill(YELLOW, 0.9), TransformFromCopy(rows[0][0], winner),
                  run_time=0.9)
        self.play(winner.animate.set_color(INK), run_time=0.4)
        self.wait(0.4)

        # --- 4 rät die Zahl ------------------------------------------------
        cap4 = caption(4, "Rechnet nicht – rät die Zahl", RED)
        full2 = T("Die Durchbiegung beträgt 38 mm.", 28, t2w={"38 mm.": BOLD})
        full2.move_to([-3.7, 0.7, 0], aligned_edge=LEFT)
        cut2 = len("DieDurchbiegungbeträgt")
        sentence2, ans = full2[:cut2], full2[cut2:]
        num_cands = [("12 mm", 0.14), ("4,2 mm", 0.12), ("38 mm", 0.11), ("0,7 mm", 0.10), ("1,9 cm", 0.09)]
        nums = prob_rows(num_cands, -0.3, spacing=0.7, x_bar=-2.1)
        self.play(ReplacementTransform(cap3, cap4), FadeOut(rows), run_time=0.6)
        self.play(FadeIn(sentence2), run_time=0.5)
        self.play(LaggedStart(*[GrowFromEdge(r[1], LEFT) for r in nums], lag_ratio=0.15),
                  FadeIn(VGroup(*[VGroup(r[0], r[2]) for r in nums])), run_time=1.2)

        def draw(final, hops):
            """Random draw: highlight hops over the bars, slowing down, and stops on `final`."""
            for j, i in enumerate(hops + [final]):
                self.play(*[r[1].animate.set_fill(YELLOW if k == i else RED, 0.9 if k == i else 0.55)
                            for k, r in enumerate(nums)], run_time=0.07 + 0.03 * j)

        draw(2, [0, 3, 1, 4, 0, 2, 3, 1])
        self.play(TransformFromCopy(nums[2][0], ans), run_time=0.6)
        self.wait(0.3)

        # regenerate twice: same question, different numbers
        head = T("↻ neu generiert", 24, MUTED).move_to([2.4, -0.3, 0])
        self.play(FadeIn(head), run_time=0.4)
        for n, (i, hops) in enumerate([(3, [1, 4, 0, 2, 3, 1]), (0, [2, 4, 1, 3, 2])]):
            draw(i, hops)
            alt = T(num_cands[i][0], 28, INK, weight=BOLD).move_to([2.4, -1.0 - 0.7 * n, 0])
            self.play(TransformFromCopy(nums[i][0], alt), run_time=0.5)

        msg = VGroup(cross_mark(), T("Zahl geraten, nicht berechnet", 26, INK)).arrange(RIGHT, buff=0.3)
        msg.move_to([0, -4.0, 0])
        self.play(Create(msg[0]), FadeIn(msg[1]), run_time=0.8)
        self.wait(3.0)
