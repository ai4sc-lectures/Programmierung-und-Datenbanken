"""Manim scene for the slide "Binäre Zahlen – Gleitkommazahl" (01c_Computerhardware.qmdx): -13,25 as float.

The 16 bit (IEEE 754 half precision) of the result stay visible at the bottom and are filled step by step.
Palette: light "pastello" theme (_extensions/ai4sc-style/themes/color/pastello.css).

Render, from the lectures/ directory:

    manim/render.sh manim/float_example.py FloatExample 1000,800 images/01c_Computerhardware/manim_float_example.mp4
"""
from manim import *

config.frame_height = 8
config.frame_width = 10
config.background_color = "#F8F7F2"

INK = "#302F2B"
MUTED = "#68665E"
FAINT = "#C9C6B8"
RIM = "#B9B5A6"
BLUE = "#91B5CB"
GREEN = "#8B9E87"
YELLOW = "#D6B65E"
BUBBLE = "#F3F1E8"
FONT = "Helvetica Neue"
MONO = "Menlo"

SIGN = "1"
EXP = "10010"                       # 3 + 15 = 18
MANT = "10101" + "0" * 5            # 1,10101 without the leading 1
Y_REG = -3.0
CW = 0.285                          # width of one bit cell


def T(text, size=24, color=INK, font=FONT, **kw):
    return Text(text, font=font, font_size=size * 2, color=color, **kw).scale(0.5)


def cells(digits, y, x0=-2.75, step=0.9, fill=BUBBLE, stroke=RIM):
    g = VGroup()
    for i, d in enumerate(digits):
        b = Square(0.75, color=stroke, fill_color=fill, fill_opacity=1, stroke_width=3).move_to([x0 + step * i, y, 0])
        g.add(VGroup(b, T(d, 32, INK, font=MONO).move_to(b)))
    return g


def register():
    """16 bit cells (1 | 5 | 10), all 0 at the start."""
    pos = []
    x = -4.6
    for i in range(16):
        if i in (1, 6):
            x += 0.15
        pos.append([x + 0.275, Y_REG])
        x += 0.55
    bits = []
    for x, y in pos:
        b = Square(0.55, color=RIM, fill_color=BUBBLE, fill_opacity=1, stroke_width=2).move_to([x, y, 0])
        d = T("0", 26, FAINT, font=MONO).move_to(b)
        bits.append(VGroup(b, d))
    ly = Y_REG - 0.55
    labels = VGroup(
        T("Vorzeichen", 16, MUTED).move_to([pos[0][0] - 0.275, ly, 0], aligned_edge=LEFT),
        T("Exponent (5 Bit)", 18, MUTED).move_to([(pos[1][0] + pos[5][0]) / 2 + 0.1, ly, 0]),
        T("Mantisse (10 Bit)", 18, MUTED).move_to([(pos[6][0] + pos[15][0]) / 2, ly, 0]))
    return VGroup(*bits), bits, labels


def set_bits(bits, start, digits, color):
    """Animations that write `digits` into the cells from `start` and colour them."""
    anims = []
    for k, d in enumerate(digits):
        b = bits[start + k]
        new = T(d, 26, INK, font=MONO).move_to(b[0])
        anims += [b[0].animate.set_fill(color, opacity=0.85 if d == "1" else 0.45), Transform(b[1], new)]
    return anims


class FloatExample(Scene):
    def construct(self):
        def heading(n, text):
            badge = VGroup(Circle(0.28, color=YELLOW, fill_opacity=1, stroke_width=0),
                           T(str(n), 26, INK, weight=BOLD))
            badge[1].move_to(badge[0])
            return VGroup(badge, T(text, 28, INK)).arrange(RIGHT, buff=0.25).move_to([0, 3.4, 0])

        reg_group, bits, reg_labels = register()
        self.add(reg_group, reg_labels)

        # 1 Vorzeichen
        h = heading(1, "Vorzeichen")
        num = T("−13,25", 60, INK, font=MONO).move_to([0, 2.1, 0])
        self.play(FadeIn(h), FadeIn(num), run_time=0.8)
        box = Rectangle(width=0.6, height=0.95, color=YELLOW, stroke_width=5).move_to(num[0].get_center() + 0.02 * LEFT)
        sign = T("negativ, also Vorzeichenbit = 1", 28, INK).move_to([0, 1.0, 0])
        self.play(Create(box), FadeIn(sign), run_time=0.8)
        self.play(*set_bits(bits, 0, SIGN, YELLOW), run_time=0.7)
        self.wait(1.2)

        # 2 Binärform: 13,25 = 13 + 0,25
        h2 = heading(2, "Dezimalzahl in Binärform")
        pos = T("13,25", 60, INK, font=MONO).move_to([0, 2.1, 0])
        self.play(Transform(h, h2), Transform(num, pos), FadeOut(box), FadeOut(sign), run_time=0.7)
        t13 = T("13", 60, INK, font=MONO).move_to([-2.4, 2.2, 0])
        plus = T("+", 48, MUTED).move_to([0, 2.2, 0])
        tfr = T("0,25", 60, INK, font=MONO).move_to([2.4, 2.2, 0])
        self.play(Transform(num, VGroup(t13, plus, tfr)), run_time=1.0)
        l1 = T("Ganzzahlteil", 22, MUTED).move_to([-2.4, 1.5, 0])
        l2 = T("Nachkommateil", 22, MUTED).move_to([2.4, 1.5, 0])
        self.play(FadeIn(l1), FadeIn(l2), run_time=0.5)
        self.wait(0.8)

        def digit_cells(xs, values, labels, y=0.35):
            cs = VGroup()
            for x, v, lab in zip(xs, values, labels):
                sq = Square(0.55, color=RIM, fill_color=BUBBLE, fill_opacity=1, stroke_width=3).move_to([x, y, 0])
                cs.add(VGroup(sq, T(v, 30, INK, font=MONO).move_to(sq), T(lab, 22, MUTED).move_to([x, y + 0.55, 0])))
            return cs

        left = digit_cells([-3.3, -2.7, -2.1, -1.5], "1101", ["8", "4", "2", "1"])
        self.play(FadeIn(left), run_time=0.7)
        ea = T("13 = 8 + 4 + 1", 26, INK).move_to([-2.4, -0.45, 0])
        self.play(FadeIn(ea), run_time=0.5)
        self.wait(1.0)
        right = digit_cells([2.1, 2.7], "01", ["½", "¼"])
        self.play(FadeIn(right), run_time=0.7)
        eb = T("0,25 = ¼", 26, INK).move_to([2.4, -0.45, 0])
        self.play(FadeIn(eb), run_time=0.5)
        self.wait(1.2)
        # merge into one row 1101,01
        row = cells(list("110101"), -1.4)
        dot = Dot([(-2.75 + 0.9 * 3 + -2.75 + 0.9 * 4) / 2, -1.4 - 0.45, 0], radius=0.12, color=INK)
        res = T("13,25 = 1101,01₂", 28, INK).move_to([0, -0.7, 0])
        self.play(FadeOut(VGroup(num, l1, l2, ea, eb)), run_time=0.5)
        self.play(FadeOut(left), FadeOut(right), FadeIn(row), run_time=1.0)
        self.play(FadeIn(dot), FadeIn(res), run_time=0.6)
        self.wait(1.5)

        # 3 Normieren
        h3 = heading(3, "Normieren")
        self.play(Transform(h, h3), FadeOut(res),
                  row.animate.shift(UP * 2.4), dot.animate.shift(UP * 2.4), run_time=0.8)
        note = T("Komma nach der ersten 1: 3 Stellen nach links", 28, INK).move_to([0, 2.3, 0])
        target = [(-2.75 + -2.75 + 0.9) / 2, 1.0 - 0.45, 0]
        self.play(FadeIn(note), run_time=0.5)
        self.play(dot.animate.move_to(target), run_time=1.3)
        times = T("× 2³", 44, INK).move_to([3.3, 1.0, 0])
        self.play(FadeIn(times, shift=LEFT * 0.3), run_time=0.7)
        eq = T("1101,01₂ = 1,10101₂ × 2³", 30, INK).move_to([0, -0.3, 0])
        self.play(FadeIn(eq), run_time=0.6)
        self.wait(1.5)

        # 4 Zerlegung: Exponent und Mantisse in die Bits schreiben
        h4 = heading(4, "Zerlegung")
        self.play(Transform(h, h4), FadeOut(note), FadeOut(eq), run_time=0.6)
        mant = Brace(row, DOWN, color=GREEN)
        mt = T("Mantisse m = 1,10101₂", 26, INK).next_to(mant, DOWN, buff=0.12)
        ex = Brace(times, UP, color=BLUE)
        et = T("Exponent e = 3", 26, INK).next_to(ex, UP, buff=0.12).shift(LEFT * 0.4)
        self.play(GrowFromCenter(mant), FadeIn(mt), GrowFromCenter(ex), FadeIn(et), run_time=0.8)
        self.wait(0.8)
        n_exp = T("Exponent mit Bias: 3 + 15 = 18 = 10010₂", 26, INK).move_to([0, -0.9, 0])
        self.play(FadeIn(n_exp), run_time=0.5)
        self.play(*set_bits(bits, 1, EXP, BLUE), run_time=1.0)
        self.wait(1.0)
        n_man = T("Mantisse ohne die führende 1: 10101, aufgefüllt mit Nullen", 26, INK).move_to([0, -1.55, 0])
        self.play(FadeIn(n_man), run_time=0.5)
        self.play(*set_bits(bits, 6, MANT, GREEN), run_time=1.0)
        self.wait(1.5)

        # 5 Ergebnis
        h5 = heading(5, "Ergebnis")
        fin = T("−13,25 = 1 10010 1010100000", 24, INK, font=MONO, weight=BOLD).move_to([0, 0.6, 0])
        self.play(Transform(h, h5), FadeOut(VGroup(row, dot, times, mant, mt, ex, et, n_exp, n_man)), run_time=0.6)
        self.play(FadeIn(fin), run_time=0.7)
        self.wait(2.5)
