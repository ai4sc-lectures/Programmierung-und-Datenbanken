"""Manim scene for the slide "Binäre Addition mit XOR und AND" (05a_Operatoren.qmdx).

Same example as manim/binary_addition.py (01c_Computerhardware): 13 + 7 = 20, bit by bit.
This version shows for every column which logical operations give the result:
the sum bit is A XOR B XOR Ü, the carry is (A AND B) OR (Ü AND (A XOR B)).

Palette: light "pastello" theme (_extensions/ai4sc-style/themes/color/pastello.css).

Render, from the lectures/ directory:

    manim/render.sh manim/binary_addition_logic.py BinaryAdditionLogic 1200,900 images/05a_Operatoren/manim_binary_addition_logic.mp4
"""
from manim import *

config.frame_height = 9
config.frame_width = 12
config.background_color = "#F8F7F2"

INK = "#302F2B"
MUTED = "#68665E"
RIM = "#B9B5A6"
GREEN = "#8B9E87"
YELLOW = "#D6B65E"
GREEN_TXT = "#4E6A49"
YELLOW_TXT = "#8C6D14"
BUBBLE = "#F3F1E8"
FONT = "Helvetica Neue"
MONO = "Menlo"

XS = [-2.4, -1.2, 0.0, 1.2, 2.4]      # Bit 4 ... Bit 0
Y_HEAD, Y_CARRY, Y_A, Y_B, Y_LINE, Y_SUM = 4.0, 3.0, 1.8, 0.7, -0.05, -0.85
Y_S1, Y_S2, Y_C1, Y_C2 = -2.05, -2.6, -3.35, -3.9
X_LBL = -5.4                           # left edge of the formula block
X_FORM = -3.0                          # left edge of the formulas


def T(text, size=24, color=INK, font=FONT, **kw):
    return Text(text, font=font, font_size=size * 2, color=color, **kw).scale(0.5)


def F(text, size=22, color=INK):
    """Formula line in monospace, operator keywords coloured: XOR green (sum), AND yellow (carry)."""
    return T(text, size, color, font=MONO, t2c={"XOR": GREEN_TXT, "AND": YELLOW_TXT})


def bit(v, x, y, fill=BUBBLE, stroke=RIM):
    b = Square(1.0, color=stroke, fill_color=fill, fill_opacity=1, stroke_width=3).move_to([x, y, 0])
    return VGroup(b, T(str(v), 34, INK, font=MONO).move_to(b))


def left(mob, x, y):
    return mob.move_to([x, y, 0], aligned_edge=LEFT)


class BinaryAdditionLogic(Scene):
    def construct(self):
        a = [0, 1, 1, 0, 1]   # 13
        b = [0, 0, 1, 1, 1]   # 7
        for i, x in enumerate(XS):
            self.add(T(f"Bit {4 - i}", 20, MUTED).move_to([x, Y_HEAD, 0]))
        lx = XS[0] - 0.7
        self.add(T("Übertrag Ü", 22, MUTED).move_to([lx, Y_CARRY, 0], aligned_edge=RIGHT),
                 T("A = 13", 24, MUTED).move_to([lx, Y_A, 0], aligned_edge=RIGHT),
                 T("B = 7", 24, MUTED).move_to([lx, Y_B, 0], aligned_edge=RIGHT),
                 T("20", 24, MUTED).move_to([lx, Y_SUM, 0], aligned_edge=RIGHT))
        self.add(Line([XS[0] - 0.6, Y_LINE, 0], [XS[-1] + 0.6, Y_LINE, 0], color=RIM, stroke_width=3))

        # formula block: label with colour marker, general rule, values of the current column
        mark_s = Square(0.32, color=GREEN, fill_color=GREEN, fill_opacity=1, stroke_width=0)
        mark_c = Square(0.32, color=YELLOW, fill_color=YELLOW, fill_opacity=1, stroke_width=0)
        lbl_s = VGroup(mark_s, T("Summe", 24, INK)).arrange(RIGHT, buff=0.15)
        lbl_c = VGroup(mark_c, T("Übertrag", 24, INK)).arrange(RIGHT, buff=0.15)
        left(lbl_s, X_LBL, Y_S1)
        left(lbl_c, X_LBL, Y_C1)
        rule_s = left(F("A XOR B XOR Ü"), X_FORM, Y_S1)
        rule_c = left(F("(A AND B) OR (Ü AND (A XOR B))"), X_FORM, Y_C1)

        ra = [bit(v, x, Y_A) for v, x in zip(a, XS)]
        rb = [bit(v, x, Y_B) for v, x in zip(b, XS)]
        self.play(FadeIn(VGroup(*ra, *rb)), run_time=1)
        self.play(FadeIn(VGroup(lbl_s, rule_s, lbl_c, rule_c)), run_time=0.8)
        self.wait(0.6)

        carry = 0
        vals = None
        for col in range(4, -1, -1):          # index into XS, right to left
            x, y, c = a[col], b[col], carry
            sbit = (x != y) != c
            cout = (x and y) or (c and (x != y))
            sbit, cout = int(sbit), int(bool(cout))
            assert sbit == (x + y + c) % 2 and cout == (x + y + c) // 2
            hl = Rectangle(width=1.1, height=Y_CARRY - Y_SUM + 1.25, color=YELLOW, stroke_width=4,
                           fill_color=YELLOW, fill_opacity=0.15).move_to([XS[col], (Y_CARRY + Y_SUM) / 2, 0])
            v_s = left(F(f"{x} XOR {y} XOR {c} = {sbit}", 22, INK), X_FORM, Y_S2)
            v_c = left(F(f"({x} AND {y}) OR ({c} AND ({x} XOR {y})) = {cout}", 22, INK), X_FORM, Y_C2)
            new_vals = VGroup(v_s, v_c)
            anims = [FadeIn(hl), FadeIn(new_vals)]
            if vals:
                anims.append(FadeOut(vals))
            self.play(*anims, run_time=0.5)
            vals = new_vals
            self.wait(0.8)
            r = bit(sbit, XS[col], Y_SUM, fill=GREEN, stroke=GREEN)
            self.play(FadeIn(r, shift=DOWN * 0.3), Indicate(v_s, color=GREEN_TXT, scale_factor=1.05), run_time=0.6)
            if cout and col > 0:
                cb = bit(1, XS[col - 1], Y_CARRY, fill=YELLOW, stroke=YELLOW)
                self.play(FadeIn(cb, shift=LEFT * 0.4), Indicate(v_c, color=YELLOW_TXT, scale_factor=1.05),
                          run_time=0.6)
            self.wait(0.4)
            self.play(FadeOut(hl), run_time=0.3)
            carry = cout
        # keep the values of the last column: the final frame (poster in PDF/Typst) shows rule and use
        self.wait(2.5)
