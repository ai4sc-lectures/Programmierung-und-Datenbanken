"""Manim scene for the slide "Der Name im Code ist nicht der Speicher" (02c_Speicher.qmdx).

The name `a` exists only in the source code. When the program runs, Python puts the
value into a memory cell and enters the name with that cell's address in a name table.
`print(a)` follows the address to the value; `id(a)` returns the address.
Same cell style as stack_heap.py (01c/09b); same layout as the static diagrams
images/02c_Speicher/mem_*.svg (names left, memory right).
Palette: light "pastello" theme (_extensions/ai4sc-style/themes/color/pastello.css).

Render, from the lectures/ directory:

    manim/render.sh manim/variablen.py NameAdresse 1200,760 images/02c_Speicher/manim_name_adresse.mp4
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from stack_heap import *  # noqa: E402,F401,F403  (palette, T(), Matrix; 12 x 7.6 frame)

ROWS, COLS, CELL = 4, 8, 0.55
BASE = 0x1A00
OTHER_CELLS = [0, 6, 9, 15, 17, 20, 26, 29]
TARGET = 1 * COLS + 3                 # 0x1A13


def addr(i):
    r, c = divmod(i, COLS)
    return f"0x{BASE + 0x10 * r + c:04X}"


class NameAdresse(Scene):
    def construct(self):
        # source code (top left)
        src_lab = T("Quelltext", 24, INK, weight=BOLD).move_to([-5.85, 3.5, 0], aligned_edge=LEFT)
        lines = VGroup(*[T(s, 24, INK, font=MONO) for s in ["a = 21.5", "print(a)", "print(id(a))"]])
        lines.arrange(DOWN, aligned_edge=LEFT, buff=0.22).move_to([-5.5, 2.15, 0], aligned_edge=LEFT)
        src_box = SurroundingRectangle(lines, color=RIM, stroke_width=2, buff=0.25)
        src_box.stretch_to_fit_width(5.6).move_to([-3.1, 2.15, 0])
        lines.move_to(src_box.get_left() + RIGHT * 0.3, aligned_edge=LEFT)

        # memory (right): matrix of cells, row addresses on the right
        mem = Matrix(ROWS, COLS, CELL, 2.9, 2.2, BASE, label_size=13)
        for r in range(ROWS):
            mem.group[r * (COLS + 1)].next_to(mem.cells[r * COLS + COLS - 1], RIGHT, buff=0.12)
        for i in OTHER_CELLS:
            mem.cells[i].set_fill(OTHER, opacity=1)
        mem_lab = T("Speicher (laufendes Programm)", 24, INK, weight=BOLD)
        mem_lab.move_to([2.9 - COLS * CELL / 2, 2.6, 0], aligned_edge=LEFT)

        # name table (bottom left)
        tab_lab = T("Namen", 24, INK, weight=BOLD).move_to([-5.7, 0.35, 0], aligned_edge=LEFT)
        head = VGroup(Rectangle(width=1.6, height=0.55), Rectangle(width=2.4, height=0.55)).arrange(RIGHT, buff=0)
        for r in head:
            r.set_style(fill_color=OTHER, fill_opacity=1, stroke_color=RIM, stroke_width=1.5)
        head.move_to([-3.7, -0.3, 0])
        head_txt = VGroup(T("Name", 17, MUTED).move_to(head[0]), T("Adresse", 17, MUTED).move_to(head[1]))

        self.play(FadeIn(src_lab), FadeIn(src_box), FadeIn(lines), FadeIn(mem.group), FadeIn(mem_lab),
                  FadeIn(tab_lab), FadeIn(head), FadeIn(head_txt), run_time=1.0)

        cap = None

        def caption(text):
            nonlocal cap
            new = T(text, 22, MUTED).move_to([0, -3.2, 0])
            self.play(*([FadeOut(cap)] if cap else []), FadeIn(new), run_time=0.4)
            cap = new

        def mark(k):
            return SurroundingRectangle(lines[k], color=YELLOW, buff=0.08, stroke_width=4)

        # 1 a = 21.5: the value goes into a free cell ...
        hl = mark(0)
        self.play(Create(hl), run_time=0.4)
        caption("Python legt den Wert 21.5 in eine freie Speicherzelle")
        self.play(*mem.write(TARGET, "21.5", BLUE, 0.8, 14), run_time=0.9)
        self.wait(0.6)

        # ... and the name a gets that cell's address
        row = VGroup(Rectangle(width=1.6, height=0.55), Rectangle(width=2.4, height=0.55)).arrange(RIGHT, buff=0)
        for r in row:
            r.set_style(fill_color=BUBBLE, fill_opacity=1, stroke_color=RIM, stroke_width=1.5)
        row.next_to(head, DOWN, buff=0)
        name = T("a", 22, INK, font=MONO, weight=BOLD).move_to(row[0])
        adr = T(addr(TARGET), 20, INK, font=MONO).move_to(row[1])
        arrow = CurvedArrow(row[1].get_right() + RIGHT * 0.05, mem.cells[TARGET].get_left() + LEFT * 0.03,
                            angle=-0.6, color=INK, stroke_width=4, tip_length=0.2)
        caption("Der Name a bekommt die Adresse dieser Zelle")
        self.play(FadeIn(row), FadeIn(name), run_time=0.5)
        self.play(TransformFromCopy(mem.group[(TARGET // COLS) * (COLS + 1)], adr), run_time=0.8)
        self.play(Create(arrow), run_time=0.7)
        self.wait(1.0)

        # 2 print(a): look up the name, follow the address, read the value
        self.play(Transform(hl, mark(1)), run_time=0.4)
        caption("print(a): Name suchen, Adresse folgen, Wert lesen")
        self.play(Indicate(name, color=YELLOW), run_time=0.6)
        self.play(ShowPassingFlash(arrow.copy().set_color(YELLOW).set_stroke(width=8), time_width=0.6), run_time=0.8)
        self.play(Indicate(mem.cells[TARGET], color=YELLOW), run_time=0.6)
        out = T("→ 21.5", 22, MUTED, font=MONO).move_to([src_box.get_right()[0] - 0.25, lines[1].get_y(), 0],
                                                       aligned_edge=RIGHT)
        self.play(FadeIn(out), run_time=0.4)
        self.wait(0.8)

        # 3 print(id(a)): the address itself
        self.play(Transform(hl, mark(2)), run_time=0.4)
        caption("print(id(a)) gibt die Adresse aus")
        self.play(Indicate(adr, color=YELLOW), run_time=0.6)
        out2 = T("→ " + addr(TARGET), 22, MUTED, font=MONO).move_to([src_box.get_right()[0] - 0.25, lines[2].get_y(), 0],
                                                                aligned_edge=RIGHT)
        self.play(FadeIn(out2), run_time=0.4)
        self.wait(1.0)
        caption("a steht nur im Quelltext, im Programm ist a eine Adresse")
        self.wait(3)
