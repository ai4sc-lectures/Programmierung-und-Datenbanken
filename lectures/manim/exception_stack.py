"""Manim scenes for the slides "Laufzeitfehler: Exceptions" and "Laufzeitfehler: Exceptions abfangen"
(08a_UnitTest.qmdx).

A call chain main() -> auswertung() -> mittelwert() -> division() fills the call stack. In division() a
ZeroDivisionError is raised (nenner = 0) and travels down the stack: every frame it leaves is removed. Without a handler it reaches the
bottom and the program crashes (ExceptionCrash); with a try-except ZeroDivisionError in main() it is caught there and the
program keeps running (ExceptionCaught).
Palette: light "pastello" theme (_extensions/ai4sc-style/themes/color/pastello.css).

Render, from the lectures/ directory:

    manim/render.sh manim/exception_stack.py ExceptionCrash 1200,760 images/08a_UnitTest/manim_exception_crash.mp4
    manim/render.sh manim/exception_stack.py ExceptionCaught 1200,760 images/08a_UnitTest/manim_exception_caught.mp4
"""
from manim import *
from ai4sc_style.manim_ragged import RaggedScene

config.frame_height = 7.6
config.frame_width = 12
config.background_color = "#F8F7F2"

INK = "#302F2B"
MUTED = "#68665E"
RIM = "#B9B5A6"
BLUE = "#91B5CB"
YELLOW = "#FBE9A8"
BUBBLE = "#F3F1E8"
ORANGE = "#E3A878"
RED = "#C58E89"
GREEN = "#A9C5A0"
FONT = "Helvetica Neue"

CX, WIDTH, BAR_H, STEP, BOTTOM = 0.0, 6.4, 0.58, 0.68, -1.5


def T(text, size=24, color=INK, font=FONT, **kw):
    return Text(text, font=font, font_size=size * 2, color=color, **kw).scale(0.5)


def bar(label, fill, y, width=WIDTH, size=22):
    box = Rectangle(width=width, height=BAR_H, color=INK, stroke_width=3, fill_color=fill, fill_opacity=1)
    box.move_to([CX, y, 0])
    text = T(label, size, INK, weight=BOLD).move_to([CX - width / 2 + 0.3, y, 0], aligned_edge=LEFT)
    return VGroup(box, text)


def curved_arrow(y_from, y_to):
    x = CX + WIDTH / 2 + 0.05
    return CurvedArrow([x, y_from, 0], [x, y_to, 0], angle=-PI * 0.9, color=RED, stroke_width=6, tip_length=0.2)


class _ExceptionStack(RaggedScene):
    caught = False
    names = ["main()", "auswertung()", "mittelwert()", "division()"]

    def construct(self):
        title = T("Call Stack", 26, INK, weight=BOLD).move_to([CX - WIDTH / 2, 3.2, 0], aligned_edge=LEFT)
        ys = [BOTTOM + STEP * i for i in range(len(self.names))]
        frames = [bar(n, BLUE if i else BUBBLE, ys[i]) for i, n in enumerate(self.names)]
        if self.caught:
            handler = T("try … except ZeroDivisionError", 15, MUTED, font="Menlo").move_to([CX + WIDTH / 2 - 0.3, ys[0], 0], aligned_edge=RIGHT)
            frames[0].add(handler)
        cap = None

        def caption(head, line=None):
            nonlocal cap
            g = VGroup(T(head, 22, INK, weight=BOLD), *([T(line, 18, MUTED)] if line else []))
            g.arrange(DOWN, aligned_edge=LEFT, buff=0.1).move_to([CX - WIDTH / 2, -3.35, 0], aligned_edge=LEFT)
            anims = [FadeIn(g)] + ([FadeOut(cap)] if cap else [])
            cap = g
            return anims

        self.play(FadeIn(title), run_time=0.5)
        self.play(FadeIn(frames[0], shift=DOWN * 0.3), *caption("Programmstart", "main() ruft auswertung() auf"), run_time=0.7)
        for i in range(1, len(frames)):
            line = f"{self.names[i - 1]} ruft {self.names[i]} auf" if i < len(frames) - 1 else None
            self.play(FadeIn(frames[i], shift=DOWN * 0.3),
                      *caption(f"Aufruf {self.names[i]}", line) if i == len(frames) - 1 else [], run_time=0.5)
        self.wait(0.4)

        # the exception appears above the top frame
        exc = bar("ZeroDivisionError", ORANGE, ys[-1] + STEP)
        self.play(FadeIn(exc, shift=DOWN * 0.3), *caption("ZeroDivisionError in division()", "nenner ist 0: der Programmverlauf wird unterbrochen"),
                  run_time=0.8)
        self.wait(0.6)

        # it travels down: every frame it leaves is removed
        for i in range(len(frames) - 1, 0, -1):
            arrow = curved_arrow(ys[i], ys[i - 1])
            self.play(Create(arrow), frames[i][0].animate.set_fill(RED, opacity=1), run_time=0.45)
            self.play(FadeOut(frames[i], shift=UP * 0.2), exc.animate.move_to([CX, ys[i], 0]), FadeOut(arrow),
                      *caption(f"{self.names[i]} bricht ab", "Die Exception geht an den Aufrufer weiter"),
                      run_time=0.6)
        if self.caught:
            arrow = curved_arrow(ys[1], ys[0])
            self.play(Create(arrow), run_time=0.45)
            self.play(FadeOut(arrow), frames[0][0].animate.set_fill(GREEN, opacity=1), FadeOut(exc),
                      *caption("main() fängt die Exception ab", "Das Programm läuft weiter"), run_time=0.8)
            self.wait(3)
        else:
            arrow = curved_arrow(ys[0], ys[0] - STEP)
            crash = bar("Absturz", ORANGE, ys[0] - STEP)
            self.play(Create(arrow), frames[0][0].animate.set_fill(RED, opacity=1), run_time=0.45)
            self.play(FadeOut(frames[0], shift=UP * 0.2), FadeOut(exc), FadeOut(arrow), FadeIn(crash),
                      *caption("Niemand fängt die Exception ab", "Das Programm stürzt ab"), run_time=0.8)
            self.wait(3)


class ExceptionCrash(_ExceptionStack):
    caught = False


class ExceptionCaught(_ExceptionStack):
    caught = True
