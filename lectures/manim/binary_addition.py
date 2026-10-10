"""Manim scene for the slide "Binäre Addition" (02a_Computerhardware.qmdx): 13 + 7 = 20, bit by bit.

Palette: light "pastello" theme (_extensions/ai4sc-style/themes/color/pastello.css).

Render, from the lectures/ directory:

    manim/render.sh manim/binary_addition.py BinaryAddition 1000,800 images/02a_Computerhardware/manim_binary_addition.mp4
"""
from manim import *

config.frame_height = 8
config.frame_width = 10
config.background_color = "#F8F7F2"

INK = "#302F2B"
MUTED = "#68665E"
RIM = "#B9B5A6"
GREEN = "#8B9E87"
YELLOW = "#D6B65E"
BUBBLE = "#F3F1E8"
FONT = "Helvetica Neue"
MONO = "Menlo"

XS = [-2.4, -1.2, 0.0, 1.2, 2.4]      # Bit 4 ... Bit 0
Y_HEAD, Y_CARRY, Y_A, Y_B, Y_LINE, Y_SUM, Y_TXT = 3.3, 2.2, 0.9, -0.2, -0.95, -1.75, -3.2


def T(text, size=24, color=INK, font=FONT, **kw):
    return Text(text, font=font, font_size=size * 2, color=color, **kw).scale(0.5)


def bit(v, x, y, fill=BUBBLE, stroke=RIM):
    b = Square(1.0, color=stroke, fill_color=fill, fill_opacity=1, stroke_width=3).move_to([x, y, 0])
    return VGroup(b, T(str(v), 34, INK, font=MONO).move_to(b))


class BinaryAddition(Scene):
    def construct(self):
        a = [0, 1, 1, 0, 1]   # 13
        b = [0, 0, 1, 1, 1]   # 7
        for i, x in enumerate(XS):
            self.add(T(f"Bit {4 - i}", 20, MUTED).move_to([x, Y_HEAD, 0]))
        self.add(T("Übertrag", 22, MUTED).move_to([-3.1, Y_CARRY, 0], aligned_edge=RIGHT),
                 T("13", 26, MUTED).move_to([-3.1, Y_A, 0], aligned_edge=RIGHT),
                 T("7", 26, MUTED).move_to([-3.1, Y_B, 0], aligned_edge=RIGHT),
                 T("20", 26, MUTED).move_to([-3.1, Y_SUM, 0], aligned_edge=RIGHT))
        self.add(Line([-3.0, Y_LINE, 0], [3.1, Y_LINE, 0], color=RIM, stroke_width=3))
        ra = [bit(v, x, Y_A) for v, x in zip(a, XS)]
        rb = [bit(v, x, Y_B) for v, x in zip(b, XS)]
        self.play(FadeIn(VGroup(*ra, *rb)), run_time=1)
        self.wait(0.6)

        carry = 0
        txt = None
        res = [None] * 5
        for col in range(4, -1, -1):          # index into XS, right to left
            s = a[col] + b[col] + carry
            sbit, cout = s % 2, s // 2
            hl = Rectangle(width=1.3, height=Y_CARRY - Y_SUM + 1.4, color=YELLOW, stroke_width=4,
                           fill_color=YELLOW, fill_opacity=0.15).move_to([XS[col], (Y_CARRY + Y_SUM) / 2, 0])
            parts = f"{a[col]} + {b[col]}" + (f" + {carry}" if carry else "") + f" = {s // 2}{s % 2}"
            note = f"{parts}: Summe {sbit}" + (", Übertrag 1" if cout else ", kein Übertrag")
            new_txt = T(note, 26, INK, font=MONO).move_to([0, Y_TXT, 0])
            anims = [FadeIn(hl)]
            anims.append(FadeOut(txt) if txt else Wait(0))
            anims.append(FadeIn(new_txt))
            self.play(*anims, run_time=0.5)
            txt = new_txt
            self.wait(0.5)
            r = bit(sbit, XS[col], Y_SUM, fill=GREEN, stroke=GREEN)
            r[1].set_color(INK)
            res[col] = r
            self.play(FadeIn(r, shift=DOWN * 0.3), run_time=0.5)
            if cout and col > 0:
                c = bit(1, XS[col - 1], Y_CARRY, fill=YELLOW, stroke=YELLOW)
                self.play(FadeIn(c, shift=LEFT * 0.4), run_time=0.5)
            elif cout:
                c = bit(1, XS[col] - 1.2, Y_SUM, fill=GREEN, stroke=GREEN)
                self.play(FadeIn(c, shift=LEFT * 0.4), run_time=0.5)
            self.play(FadeOut(hl), run_time=0.3)
            carry = cout
        self.play(FadeOut(txt), run_time=0.3)
        fin = T("13 + 7 = 20", 30, INK, weight=BOLD).move_to([0, Y_TXT, 0])
        self.play(FadeIn(fin), run_time=0.6)
        self.wait(2)
