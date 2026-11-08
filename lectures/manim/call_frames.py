"""Manim scene for the slide "Der Stack wächst und schrumpft" (06a_Funktionen.qmdx).

Every call gets its own frame with the local names of that call. main() calls berechne_fläche(b, h):
the frame is pushed on the call stack, the local names appear, and on return the frame and its
names disappear. Palette: light "pastello" theme (_extensions/ai4sc-style/themes/color/pastello.css).

Render, from the lectures/ directory:

    manim/render.sh manim/call_frames.py CallFrames 1200,760 images/06a_Funktionen/manim_call_frames.mp4
"""
from manim import *

config.frame_height = 7.6
config.frame_width = 12
config.background_color = "#F8F7F2"

INK = "#302F2B"
MUTED = "#68665E"
RIM = "#B9B5A6"
BLUE = "#91B5CB"
YELLOW = "#FBE9A8"
BUBBLE = "#F3F1E8"
FONT = "Helvetica Neue"
MONO = "Menlo"


def T(text, size=24, color=INK, font=FONT, **kw):
    return Text(text, font=font, font_size=size * 2, color=color, **kw).scale(0.5)


CODE = [
    (0, "def berechne_fläche(breite, höhe):"),
    (1, "fläche = breite * höhe"),
    (1, "return fläche"),
    (0, ""),
    (0, "def main():"),
    (1, "b = 5"),
    (1, "h = 3"),
    (1, "ergebnis = berechne_fläche(b, h)"),
    (1, "print(ergebnis)"),
    (0, ""),
    (0, "main()"),
]
LINE_H = 0.38
CODE_X = -5.75
CODE_TOP = 2.75


class Frame:
    """A stack frame: a box with a title and rows for the local names that appear one by one."""

    ROW = 0.4

    def __init__(self, title, rows, bottom, cx=3.6, width=4.0):
        self.rows_text = rows
        self.height = 0.75 + self.ROW * rows
        self.box = Rectangle(width=width, height=self.height, color=INK, stroke_width=3, fill_color=BUBBLE, fill_opacity=1)
        self.box.move_to([cx, bottom + self.height / 2, 0])
        self.title = T(title, 22, INK, weight=BOLD).move_to(
            [cx - width / 2 + 0.25, self.box.get_top()[1] - 0.35, 0], aligned_edge=LEFT)
        self.cx, self.width = cx, width
        self.rows = {}

    def row_pos(self, i):
        return [self.cx - self.width / 2 + 0.45, self.title.get_center()[1] - 0.5 - self.ROW * i, 0]

    def mobs(self):
        return [self.box, self.title, *self.rows.values()]

    def push(self):
        return AnimationGroup(FadeIn(self.box, shift=DOWN * 0.4), FadeIn(self.title, shift=DOWN * 0.4))

    def pop(self):
        return AnimationGroup(*[FadeOut(m, shift=UP * 0.4) for m in self.mobs()])

    def add_row(self, i, text):
        t = T(text, 17, MUTED, font=MONO).move_to(self.row_pos(i), aligned_edge=LEFT)
        self.rows[i] = t
        return FadeIn(t)

    def set_row(self, i, text):
        new = T(text, 17, MUTED, font=MONO).move_to(self.row_pos(i), aligned_edge=LEFT)
        old = self.rows[i]
        self.rows[i] = new
        return ReplacementTransform(old, new)

    def active(self, on):
        return self.box.animate.set_fill(YELLOW if on else BUBBLE, opacity=1)


class CallFrames(Scene):
    def construct(self):
        # code listing on the left
        lines = []
        for k, (indent, text) in enumerate(CODE):
            if not text:
                lines.append(None)
                continue
            t = T(text, 17, INK, font=MONO).move_to(
                [CODE_X + 0.4 * indent, CODE_TOP - LINE_H * k, 0], aligned_edge=LEFT)
            lines.append(t)
        code = VGroup(*[l for l in lines if l])
        panel = RoundedRectangle(corner_radius=0.05, width=7.1, height=LINE_H * len(CODE) + 0.3,
                                 color=RIM, stroke_width=1.5, fill_color=BUBBLE, fill_opacity=0.6)
        panel.move_to([CODE_X - 0.2 + 3.55, CODE_TOP - LINE_H * (len(CODE) - 1) / 2, 0])
        hl = Rectangle(width=7.0, height=LINE_H, stroke_width=0, fill_color=BLUE, fill_opacity=0.45)
        hl.move_to([panel.get_center()[0], lines[10].get_center()[1], 0])

        def go(k):
            return hl.animate.move_to([panel.get_center()[0], lines[k].get_center()[1], 0])

        stack_lab = T("Call Stack (oben = aktiver Frame)", 20, INK, weight=BOLD).move_to([3.6, 3.25, 0])
        cap = None

        def caption(title, line=None):
            nonlocal cap
            g = VGroup(T(title, 21, INK, weight=BOLD), *([T(line, 18, MUTED)] if line else []))
            g.arrange(DOWN, aligned_edge=LEFT, buff=0.1).move_to([CODE_X, -3.05, 0], aligned_edge=LEFT)
            anims = [FadeIn(g)] + ([FadeOut(cap)] if cap else [])
            cap = g
            return anims

        bottom = -2.6
        mod = Frame("<module>", 1, bottom)
        main = Frame("main", 3, bottom + mod.height + 0.12)
        calc = Frame("berechne_fläche", 3, bottom + mod.height + main.height + 0.24)

        self.play(FadeIn(panel), FadeIn(code), FadeIn(stack_lab), run_time=0.8)
        self.play(mod.push(), mod.add_row(0, "main = Funktion"), mod.active(True),
                  *caption("Programmstart", "Der Frame <module> hält die Namen des Hauptprogramms"), run_time=0.8)
        self.wait(0.8)

        # main() is called: new frame on top
        self.play(FadeIn(hl), go(10), run_time=0.5)
        self.play(mod.active(False), main.push(), main.active(True),
                  *caption("Aufruf main()", "Neuer Frame auf dem Stack"), run_time=0.8)
        self.play(go(5), main.add_row(0, "b = 5"), run_time=0.6)
        self.play(go(6), main.add_row(1, "h = 3"), run_time=0.6)

        # berechne_fläche(b, h) is called
        self.play(go(7), main.add_row(2, "ergebnis = (noch offen)"), run_time=0.7)
        self.play(main.active(False), calc.push(), calc.active(True), go(1),
                  *caption("Aufruf berechne_fläche(b, h)", "Neuer Frame, die Parameter werden gebunden"), run_time=1.0)
        self.play(calc.add_row(0, "breite = 5"), calc.add_row(1, "höhe = 3"), run_time=0.6)
        self.wait(0.5)
        self.play(calc.add_row(2, "fläche = 15"), run_time=0.7)
        self.play(go(2), run_time=0.5)
        self.wait(0.6)

        # return: frame and local names vanish
        y1, y2 = calc.rows[2].get_center()[1], main.rows[2].get_center()[1]
        x_out = calc.box.get_right()[0]
        pts = [[x_out, y1, 0], [x_out + 0.28, y1, 0], [x_out + 0.28, y2, 0]]
        elbow = VGroup(Line(pts[0], pts[1], color=BLUE, stroke_width=5), Line(pts[1], pts[2], color=BLUE, stroke_width=5),
                       Arrow(pts[2], [x_out, y2, 0], buff=0, color=BLUE, stroke_width=5, tip_length=0.2,
                             max_tip_length_to_length_ratio=1, max_stroke_width_to_length_ratio=100))
        self.play(Create(elbow), run_time=0.8)
        self.play(calc.pop(), FadeOut(elbow), main.active(True),
                  main.set_row(2, "ergebnis = 15"), go(7),
                  *caption("Rücksprung: return fläche gibt 15 zurück", "Der Frame und mit ihm breite, höhe und fläche verschwinden"),
                  run_time=1.0)
        self.wait(0.8)
        self.play(go(8), run_time=0.5)
        out = T("15", 18, INK, font=MONO).move_to([CODE_X + 4.3, lines[8].get_center()[1], 0], aligned_edge=LEFT)
        self.play(FadeIn(out), run_time=0.4)
        self.wait(0.6)

        # main returns
        self.play(go(10), FadeOut(out), run_time=0.5)
        self.play(main.pop(), mod.active(True),
                  *caption("main() ist fertig", "Es bleibt nur <module>"), run_time=1.0)
        self.wait(3)
