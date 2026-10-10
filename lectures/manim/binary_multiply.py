"""Manim scene for the slide "Binäre Multiplikation" (02a_Computerhardware.qmdx): 3 x 5 = 15 by shifting and adding.

Palette: light "pastello" theme (_extensions/ai4sc-style/themes/color/pastello.css).

Render, from the lectures/ directory:

    manim/render.sh manim/binary_multiply.py BinaryMultiply 1000,800 images/02a_Computerhardware/manim_binary_multiply.mp4
"""
from manim import *

config.frame_height = 8
config.frame_width = 10
config.background_color = "#F8F7F2"

INK = "#302F2B"
MUTED = "#68665E"
RIM = "#B9B5A6"
FAINT = "#DAD7CB"
BLUE = "#91B5CB"
GREEN = "#8B9E87"
YELLOW = "#D6B65E"
BUBBLE = "#F3F1E8"
FONT = "Helvetica Neue"
MONO = "Menlo"

XS = [-2.0, -1.0, 0.0, 1.0, 2.0]      # Bit 4 ... Bit 0
Y_HEAD, Y_A, Y_B, Y_L1, Y_TXT = 3.6, 2.7, 1.7, 1.1, 0.6
Y_ROWS = [-0.3, -1.2, -2.1]
Y_L2, Y_RES = -2.7, -3.3


def T(text, size=24, color=INK, font=FONT, **kw):
    return Text(text, font=font, font_size=size * 2, color=color, **kw).scale(0.5)


def bit(v, x, y, fill=BUBBLE, stroke=RIM, color=INK, s=0.8):
    b = Square(s, color=stroke, fill_color=fill, fill_opacity=1, stroke_width=3).move_to([x, y, 0])
    return VGroup(b, T(str(v), 30, color, font=MONO).move_to(b))


class BinaryMultiply(Scene):
    def construct(self):
        a = [0, 0, 0, 1, 1]   # 3
        b = [0, 0, 1, 0, 1]   # 5
        for i, x in enumerate(XS):
            self.add(T(f"Bit {4 - i}", 18, MUTED).move_to([x, Y_HEAD, 0]))
        lab = lambda t, y: T(t, 22, MUTED).move_to([-2.7, y, 0], aligned_edge=RIGHT)
        self.add(lab("A = 3", Y_A), lab("B = 5", Y_B))
        ra = [bit(v, x, Y_A) for v, x in zip(a, XS)]
        rb = [bit(v, x, Y_B) for v, x in zip(b, XS)]
        self.play(FadeIn(VGroup(*ra, *rb)), run_time=1)
        self.add(Line([-2.8, Y_L1, 0], [2.6, Y_L1, 0], color=RIM, stroke_width=3))
        self.wait(0.5)
        # B in powers of two
        self.play(*[rb[i][0].animate.set_fill(YELLOW, opacity=0.8) for i in (2, 4)], run_time=0.6)
        f1 = T("5 = 2² + 2⁰ = 4 + 1", 26, INK).move_to([0, Y_TXT, 0])
        self.play(FadeIn(f1), run_time=0.5)
        self.wait(1.2)
        f2 = T("3 × 5 = 3 × 4 + 3 × 1", 26, INK).move_to([0, Y_TXT, 0])
        self.play(Transform(f1, f2), run_time=0.6)
        self.wait(1.2)

        # partial products: A shifted left by k
        names = ["A << 0 = ×1", "A << 1 = ×2", "A << 2 = ×4"]
        notes = ["B[0]=1: +", "B[1]=0: –", "B[2]=1: +"]
        active = [b[4] == 1, b[3] == 1, b[2] == 1]
        rows = []
        for k in range(3):
            y = Y_ROWS[k]
            shifted = a[k:] + [0] * k
            on = active[k]
            cells = VGroup(*[
                bit(v, x, y, fill=(BLUE if (on and v) else BUBBLE), stroke=(BLUE if (on and v) else (RIM if on else FAINT)),
                    color=(INK if on else FAINT)) for v, x in zip(shifted, XS)])
            l = lab(names[k], y)
            if not on:
                l.set_color(FAINT)
            n = T(notes[k], 18, INK if on else FAINT).move_to([3.0, y, 0], aligned_edge=LEFT)
            # start unshifted and slide the whole row left by k columns
            start = VGroup(*[bit(v, x, y, fill=BUBBLE) for v, x in zip(a, XS)])
            self.play(FadeIn(start), FadeIn(l), run_time=0.5)
            if k:
                self.play(Transform(start, cells), run_time=0.8)
            else:
                self.play(Transform(start, cells), run_time=0.4)
            self.play(FadeIn(n), run_time=0.3)
            rows.append(VGroup(start, l, n))
            self.wait(0.4)

        # add the active rows
        self.add(Line([-2.8, Y_L2, 0], [2.6, Y_L2, 0], color=RIM, stroke_width=3))
        self.add(lab("Summe", Y_RES))
        res = [0, 1, 1, 1, 1]
        out = VGroup(*[bit(v, x, Y_RES, fill=GREEN, stroke=GREEN) for v, x in zip(res, XS)])
        self.play(FadeIn(out, shift=DOWN * 0.3), run_time=0.8)
        fin = T("3 × 5 = 01111 = 15", 30, INK, weight=BOLD).move_to([0, Y_TXT, 0])
        self.play(Transform(f1, fin), run_time=0.6)
        self.wait(2)
