"""Manim scenes for the slides "Variablengültigkeit" and "Übergabe von Argumentwerten (Konzepte)"
(06a_Funktionen.qmdx).

Scope: the same name `argument` lives in two frames at once; a print reads the active frame (blue bar),
its output appears next to the line; the local names vanish on return. Same look as call_frames.py.
PassConcepts: pass-by-value copies the value, pass-by-reference shares the same data.
Palette: light "pastello" theme (_extensions/ai4sc-style/themes/color/pastello.css).

Render, from the lectures/ directory:

    manim/render.sh manim/scope_args.py Scope 1200,760 images/06a_Funktionen/manim_scope.mp4
    manim/render.sh manim/scope_args.py PassConcepts 1200,760 images/06a_Funktionen/manim_pass_concepts.mp4
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
RED = "#C58E89"
GREEN = "#8B9E87"
BUBBLE = "#F3F1E8"
FONT = "Helvetica Neue"
MONO = "Menlo"


def T(text, size=24, color=INK, font=FONT, **kw):
    return Text(text, font=font, font_size=size * 2, color=color, **kw).scale(0.5)


# ----------------------------------------------------------------------------------------------
# Scope
# ----------------------------------------------------------------------------------------------
CODE = [
    (0, "argument = 6"),
    (0, "def meine_funktion(argument):"),
    (1, "interne_variable = \"geheim\""),
    (1, "print(argument, interne_variable)"),
    (0, ""),
    (0, "meine_funktion(4)"),
    (0, "print(argument)"),
    (0, "print(interne_variable)"),
]
LINE_H = 0.4
CODE_X = -5.75
CODE_TOP = 2.7


ERROR = "#9E4A43"    # darker than RED so the error text stays readable


class Frame:
    """A stack frame: a box with a title and rows for the names that appear one by one
    (same look as manim/call_frames.py)."""

    ROW = 0.4

    def __init__(self, title, rows, bottom, cx=3.7, width=4.4):
        self.height = 0.75 + self.ROW * rows
        self.box = Rectangle(width=width, height=self.height, color=INK, stroke_width=3,
                             fill_color=BUBBLE, fill_opacity=1)
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

    def read_bar(self, i):
        """The same blue bar as the code highlight, behind the row that is being read."""
        bar = Rectangle(width=self.width - 0.2, height=self.ROW, stroke_width=0, fill_color=BLUE, fill_opacity=0.45)
        return bar.move_to([self.cx, self.row_pos(i)[1], 0])

    def active(self, on):
        return self.box.animate.set_fill(YELLOW if on else BUBBLE, opacity=1)


class Scope(Scene):
    def construct(self):
        lines = []
        for k, (indent, text) in enumerate(CODE):
            if not text:
                lines.append(None)
                continue
            lines.append(T(text, 17, INK, font=MONO).move_to(
                [CODE_X + 0.4 * indent, CODE_TOP - LINE_H * k, 0], aligned_edge=LEFT))
        code = VGroup(*[l for l in lines if l])
        panel = RoundedRectangle(corner_radius=0.05, width=7.1, height=LINE_H * len(CODE) + 0.3,
                                 color=RIM, stroke_width=1.5, fill_color=BUBBLE, fill_opacity=0.6)
        panel.move_to([CODE_X - 0.2 + 3.55, CODE_TOP - LINE_H * (len(CODE) - 1) / 2, 0])
        hl = Rectangle(width=7.0, height=LINE_H, stroke_width=0, fill_color=BLUE, fill_opacity=0.45)
        hl.move_to([panel.get_center()[0], lines[0].get_center()[1], 0])

        def go(k):
            return hl.animate.move_to([panel.get_center()[0], lines[k].get_center()[1], 0])

        def out(k, text, color=INK):
            """Output of a print, right next to its line (as in call_frames.py)."""
            t = T(text, 18, color, font=MONO, weight=BOLD if color == ERROR else NORMAL)
            return t.move_to([-0.35, lines[k].get_center()[1], 0], aligned_edge=LEFT)

        stack_lab = T("Frames (oben = aktiver Frame)", 20, INK, weight=BOLD).move_to([3.7, 3.25, 0])
        cap = None

        def caption(title, line=None):
            nonlocal cap
            g = VGroup(T(title, 21, INK, weight=BOLD), *([T(line, 18, MUTED)] if line else []))
            g.arrange(DOWN, aligned_edge=LEFT, buff=0.1).move_to([CODE_X, -3.05, 0], aligned_edge=LEFT)
            anims = [FadeIn(g)] + ([FadeOut(cap)] if cap else [])
            cap = g
            return anims

        bottom = -2.6
        mod = Frame("<module>", 2, bottom)
        loc = Frame("meine_funktion", 2, bottom + mod.height + 0.12)

        # main program
        self.play(FadeIn(panel), FadeIn(code), FadeIn(stack_lab), run_time=0.8)
        self.play(FadeIn(hl), mod.push(), mod.active(True), mod.add_row(0, "argument = 6"),
                  *caption("Programmstart", "Der Name argument liegt im Frame <module>"), run_time=0.8)
        self.wait(0.8)
        self.play(go(1), mod.add_row(1, "meine_funktion = Funktion"),
                  *caption("Definition", "Der Funktionskörper läuft noch nicht"), run_time=0.7)
        self.wait(0.8)

        # call: a new frame with its own `argument`
        self.play(go(5), run_time=0.5)
        self.play(mod.active(False), loc.push(), loc.active(True), loc.add_row(0, "argument = 4"),
                  *caption("Aufruf meine_funktion(4)", "Neuer Frame, der Parameter argument wird mit 4 gebunden"),
                  run_time=1.0)
        self.wait(0.8)
        self.play(go(2), loc.add_row(1, 'interne_variable = "geheim"'), run_time=0.7)
        self.wait(0.4)

        # print inside the function reads the active frame
        b1, b2 = loc.read_bar(0), loc.read_bar(1)
        o1 = out(3, "4 geheim")
        self.play(go(3), run_time=0.5)
        self.play(FadeIn(b1), FadeIn(b2), FadeIn(o1),
                  *caption("Ausgabe in der Funktion", "Gelesen wird im aktiven Frame: argument ist hier 4"), run_time=0.7)
        self.wait(1.2)
        self.play(FadeOut(b1), FadeOut(b2), run_time=0.3)

        # return: the frame and its names vanish
        self.play(go(5), run_time=0.5)
        self.play(loc.pop(), mod.active(True),
                  *caption("Rücksprung", "Der Frame und mit ihm argument = 4 und interne_variable verschwinden"),
                  run_time=1.0)
        self.wait(1.0)

        # back in the main program
        b3 = mod.read_bar(0)
        o2 = out(6, "6")
        self.play(go(6), run_time=0.5)
        self.play(FadeIn(b3), FadeIn(o2),
                  *caption("Zurück im Hauptprogramm", "argument ist unverändert 6"), run_time=0.7)
        self.wait(1.2)
        self.play(FadeOut(b3), run_time=0.3)

        # the local name does not exist outside
        o3 = out(7, "NameError", ERROR)
        self.play(go(7), run_time=0.5)
        self.play(FadeIn(o3), mod.box.animate.set_stroke(ERROR, width=6),
                  *caption("Außerhalb der Funktion", "In <module> gibt es keinen Namen interne_variable"), run_time=0.9)
        self.wait(0.8)
        self.play(mod.box.animate.set_stroke(INK, width=3), run_time=0.5)
        self.wait(3)


# ----------------------------------------------------------------------------------------------
# Pass by value vs. pass by reference
# ----------------------------------------------------------------------------------------------
def name_tag(name, center, width=1.5):
    box = RoundedRectangle(corner_radius=0.08, width=width, height=0.5, color=INK, stroke_width=2,
                           fill_color=BUBBLE, fill_opacity=1).move_to(center)
    lab = T(name, 17, INK, font=MONO).move_to(box)
    return VGroup(box, lab)


def value_box(text, center, w=1.1, h=0.8, fill=BUBBLE):
    box = Rectangle(width=w, height=h, color=INK, stroke_width=3, fill_color=fill, fill_opacity=1).move_to(center)
    lab = T(text, 22, INK, font=MONO).move_to(box)
    return box, lab


def addr(text, box, where=RIGHT):
    return T(text, 15, MUTED, font=MONO).next_to(box, where, buff=0.12)


CODE_TOP = 2.85   # top edge of the two function definitions below the titles
DY = -1.15        # the diagrams sit lower to make room for them


def code_block(lines, size=16, line_h=0.32, indent_w=0.4):
    """Monospace code as (indent, text) rows, left-aligned; None is a gap. Text() drops leading
    spaces, so the indentation is a shift (as in the Scope scene)."""
    rows, y = [], 0.0
    for item in lines:
        if item is None:
            y -= line_h * 0.6
            continue
        indent, text = item
        rows.append(T(text, size, MUTED, font=MONO).move_to([indent * indent_w, y, 0], aligned_edge=LEFT))
        y -= line_h
    return VGroup(*rows)


class PassConcepts(Scene):
    def construct(self):
        div = Line([0, 3.4, 0], [0, -3.5, 0], color=RIM, stroke_width=1.5)
        self.add(div)
        LX, RX = -3.0, 3.1

        # titles and code, left and right
        tl = T("Pass-by-value", 26, INK, weight=BOLD).move_to([LX, 3.3, 0])
        tr = T("Pass-by-reference", 26, INK, weight=BOLD).move_to([RX, 3.3, 0])
        cl = code_block([(0, "def ersetze_zahl(argument):"), (1, "argument = 3"), None,
                         (0, "x = 6"), (0, "ersetze_zahl(x)")])
        cl.move_to([-5.4, CODE_TOP, 0], aligned_edge=UL)
        cr = code_block([(0, "def erweitere_liste_append(argument):"), (1, "argument.append(3)"), None,
                         (0, "liste = [6]"), (0, "erweitere_liste_append(liste)")])
        cr.move_to([0.5, CODE_TOP, 0], aligned_edge=UL)
        self.play(FadeIn(tl), FadeIn(tr), FadeIn(cl), FadeIn(cr), run_time=0.8)

        zone_c = T("Aufrufer", 18, MUTED, weight=BOLD)
        zone_f = T("Funktion", 18, MUTED, weight=BOLD)

        # ---- left: value is copied ----
        zl_c = zone_c.copy().move_to([LX - 1.6, 1.55 + DY, 0])
        zl_f = zone_f.copy().move_to([LX - 1.6, -0.55 + DY, 0])
        x_tag = name_tag("x", [LX, 1.95 + DY, 0], 0.9)
        x_box, x_val = value_box("6", [LX, 1.2 + DY, 0])
        x_adr = addr("0x1A12", x_box)
        self.play(FadeIn(zl_c), FadeIn(zl_f), FadeIn(x_tag), FadeIn(x_box), FadeIn(x_val), FadeIn(x_adr), run_time=0.7)

        cap = None

        def caption(x, title, line):
            nonlocal cap
            g = VGroup(T(title, 21, INK, weight=BOLD), T(line, 18, MUTED))
            g.arrange(DOWN, aligned_edge=LEFT, buff=0.1).move_to([x - 2.5, -3.0, 0], aligned_edge=LEFT)
            return g

        capl = caption(LX, "Kopie: eigene Adresse", "Änderungen bleiben in der Funktion")
        a_tag = name_tag("argument", [LX, 0.05 + DY, 0], 1.6)
        a_box, a_val = value_box("6", [LX, -0.8 + DY, 0])
        arrow = Arrow(x_box.get_bottom(), a_tag.get_top(), buff=0.08, color=BLUE, stroke_width=5, tip_length=0.2,
                      max_tip_length_to_length_ratio=1, max_stroke_width_to_length_ratio=100)
        kopie = T("Kopie", 17, BLUE, weight=BOLD).next_to(arrow, RIGHT, buff=0.15)
        a_adr = addr("0x1A33", a_box)
        self.play(GrowArrow(arrow), FadeIn(kopie), FadeIn(a_tag), FadeIn(a_box), FadeIn(a_val), FadeIn(a_adr), run_time=1.0)
        self.wait(0.4)
        a_new = T("3", 22, INK, font=MONO).move_to(a_box)
        self.play(a_box.animate.set_fill(YELLOW, opacity=1), ReplacementTransform(a_val, a_new), run_time=0.7)
        self.play(FadeIn(capl), run_time=0.5)
        self.wait(1.0)

        # ---- right: same data is shared ----
        zr_c = zone_c.copy().move_to([RX - 2.4, 1.55 + DY, 0])
        zr_f = zone_f.copy().move_to([RX - 2.4, -0.55 + DY, 0])
        obj_box, obj_val = value_box("[6]", [RX + 1.5, 0.5 + DY, 0], w=1.9, h=0.9)
        l_tag = name_tag("liste", [RX - 1.0, 1.25 + DY, 0], 1.3)
        o_adr = addr("0x1A12", obj_box, UP)
        self.play(FadeIn(zr_c), FadeIn(zr_f), FadeIn(obj_box), FadeIn(obj_val), FadeIn(o_adr), FadeIn(l_tag), run_time=0.7)
        r1 = Arrow(l_tag.get_right(), obj_box.get_left() + UP * 0.2, buff=0.08, color=BLUE, stroke_width=5, tip_length=0.2,
                   max_tip_length_to_length_ratio=1, max_stroke_width_to_length_ratio=100)
        self.play(GrowArrow(r1), run_time=0.5)
        f_tag = name_tag("argument", [RX - 1.0, -0.3 + DY, 0], 1.6)
        r2 = Arrow(f_tag.get_right(), obj_box.get_left() + DOWN * 0.2, buff=0.08, color=BLUE, stroke_width=5, tip_length=0.2,
                   max_tip_length_to_length_ratio=1, max_stroke_width_to_length_ratio=100)
        self.play(FadeIn(f_tag), GrowArrow(r2), run_time=0.8)
        self.wait(0.4)
        new_val = T("[6, 3]", 22, INK, font=MONO).move_to(obj_box)
        self.play(obj_box.animate.set_fill(YELLOW, opacity=1), ReplacementTransform(obj_val, new_val), run_time=0.7)
        capr = caption(RX, "Alias: dieselbe Adresse", "Änderungen über beide Namen sichtbar")
        self.play(FadeIn(capr), run_time=0.5)
        self.wait(3)
