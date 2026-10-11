"""Manim scenes for the slides "Zwei Speicherregionen im RAM" and "Der Stack wächst mit jedem Aufruf"
(01c_Computerhardware.qmdx).

Heap and stack are matrices of memory cells. The heap hands out free cells at random, the stack
is a LIFO structure whose cells are used one after the other. Example: the recursive sum
s(n) = n + s(n - 1), s(0) = 0 (Kleiner Gauss).
Palette: light "pastello" theme (_extensions/ai4sc-style/themes/color/pastello.css).

Render, from the lectures/ directory:

    manim/render.sh manim/stack_heap.py StackHeap 1200,760 images/01c_Computerhardware/manim_stack_heap.mp4
    manim/render.sh manim/stack_heap.py CallStack 1200,760 images/01c_Computerhardware/manim_call_stack.mp4
"""
import random

from manim import *

config.frame_height = 7.6
config.frame_width = 12
config.background_color = "#F8F7F2"

INK = "#302F2B"
MUTED = "#68665E"
RIM = "#B9B5A6"
OTHER = "#DAD7CB"
BLUE = "#91B5CB"
GREEN = "#8B9E87"
YELLOW = "#D6B65E"
RED = "#C58E89"
BUBBLE = "#F3F1E8"
FONT = "Helvetica Neue"
MONO = "Menlo"


def T(text, size=24, color=INK, font=FONT, **kw):
    return Text(text, font=font, font_size=size * 2, color=color, **kw).scale(0.5)


class Matrix:
    """A matrix of memory cells; cell index i runs row by row, rows counted from the bottom if bottom_up."""

    def __init__(self, rows, cols, cell, cx, y_edge, base_addr, bottom_up=False, label_size=12):
        self.rows, self.cols, self.cell, self.bottom_up = rows, cols, cell, bottom_up
        self.cx, self.y_edge = cx, y_edge
        self.cells, self.texts = {}, {}
        self.group = VGroup()
        x_left = cx - cols * cell / 2
        for r in range(rows):
            addr = T(f"0x{base_addr + 0x10 * r:04X}", label_size, MUTED, font=MONO)
            addr.move_to([x_left - 0.1, self.pos(r * cols)[1], 0], aligned_edge=RIGHT)
            self.group.add(addr)
            for c in range(cols):
                sq = Square(cell, color=RIM, stroke_width=1.5, fill_color=BUBBLE, fill_opacity=1)
                sq.move_to(self.pos(r * cols + c, row_major=True))
                self.cells[r * cols + c] = sq
                self.group.add(sq)

    def pos(self, i, row_major=False):
        r, c = divmod(i, self.cols)
        x = self.cx - self.cols * self.cell / 2 + self.cell * (c + 0.5)
        if self.bottom_up:
            y = self.y_edge + self.cell * (r + 0.5)          # y_edge is the bottom edge
        else:
            y = self.y_edge - self.cell * (r + 0.5)          # y_edge is the top edge
        return [x, y, 0]

    def write(self, i, text, color, opacity=0.75, size=12):
        """Animations that fill cell i with a value."""
        t = T(text, size, INK, font=MONO).move_to(self.cells[i])
        self.texts[i] = t
        return [self.cells[i].animate.set_fill(color, opacity=opacity), FadeIn(t)]

    def clear(self, i):
        t = self.texts.pop(i, None)
        return [self.cells[i].animate.set_fill(BUBBLE, opacity=1)] + ([FadeOut(t)] if t else [])


class StackHeap(Scene):
    def construct(self):
        cell = 0.42
        cx = 5.9 - 8 * cell            # right edge of the matrices at x = 5.9
        heap = Matrix(10, 16, cell, cx, 3.15, 0x1000, label_size=13)
        stack = Matrix(4, 16, cell, cx, -3.5, 0x7F00, bottom_up=True, label_size=13)
        x0 = cx - 8 * cell
        heap_lab = T("Heap", 26, INK, weight=BOLD).move_to([x0, 3.55, 0], aligned_edge=LEFT)
        stack_lab = T("Stack", 26, INK, weight=BOLD).move_to([x0, -1.45, 0], aligned_edge=LEFT)
        self.play(FadeIn(heap.group), FadeIn(stack.group), FadeIn(heap_lab), FadeIn(stack_lab), run_time=1.2)

        # other data that already lives in the heap (random cells)
        rnd = random.Random(7)
        RES_CELLS = [8 * 16 + 5, 3 * 16 + 10, 6 * 16 + 7, 1 * 16 + 2, 9 * 16 + 9]      # s(0) ... s(4)
        mine = set(RES_CELLS)                      # cells for the partial results
        others = {i for i in rnd.sample(range(10 * 16), 40) if i not in mine}
        others = set(sorted(others)[:30])
        self.play(*[heap.cells[i].animate.set_fill(OTHER, opacity=1) for i in others], run_time=0.8)

        used = set()

        # formula and captions on the left
        title = T("Berechnung Kleiner Gauß", 24, INK, weight=BOLD).move_to([-5.8, 3.55, 0], aligned_edge=LEFT)
        f1 = T("s(n) = n + s(n − 1)", 30, INK).move_to([-5.8, 2.95, 0], aligned_edge=LEFT)
        self.play(FadeIn(title), FadeIn(f1), run_time=0.6)

        cap = None

        def caption(title, *lines):
            nonlocal cap
            g = VGroup(T(title, 21, INK, weight=BOLD), *[T(l, 19, MUTED) for l in lines])
            g.arrange(DOWN, aligned_edge=LEFT, buff=0.1).move_to([-5.8, -2.55, 0], aligned_edge=LEFT)
            self.play(*([FadeOut(cap)] if cap else []), FadeIn(g), run_time=0.4)
            cap = g

        # 2 recursive calls fill the stack cell by cell
        caption("Funktionsaufrufe s(4) … s(0)")
        sp = Square(cell, color=YELLOW, stroke_width=5).move_to(stack.cells[0])
        sp_lab = T("gelb: nächste freie Zelle", 14, MUTED).move_to([x0, -3.7, 0], aligned_edge=LEFT)
        self.play(Create(sp), FadeIn(sp_lab), run_time=0.5)
        lines = VGroup()
        for k, n in enumerate([4, 3, 2, 1, 0]):
            i = 2 * k
            expr = f"s({n}) = {n} + s({n - 1})" if n else "s(0) = 0"
            line = T(expr, 26, INK).move_to([-5.8, 1.5 - 0.55 * k, 0], aligned_edge=LEFT)
            lines.add(line)
            shade = 0.8 if k % 2 == 0 else 0.5
            self.play(FadeIn(line), *stack.write(i, f"n={n}", BLUE, shade, 13), *stack.write(i + 1, "ret", BLUE, shade, 13),
                      sp.animate.move_to(stack.cells[i + 2]), run_time=0.8)
        self.wait(0.8)

        # 3 return: last in, first out
        caption("Zwischenergebnisse im Heap")

        def arrow(a, b):
            return Arrow(a, b, buff=0.05, color=BLUE, stroke_width=5, tip_length=0.2,
                         max_tip_length_to_length_ratio=1, max_stroke_width_to_length_ratio=100)

        results = [0, 1, 3, 6, 10]
        for k in range(4, -1, -1):
            n = 4 - k
            i = 2 * k
            new = T(f"s({n}) = {results[n]}", 26, INK, weight=BOLD).move_to(lines[k], aligned_edge=LEFT)
            a_in = None
            if n > 0:                       # read the stored partial result s(n-1) from the heap
                a_in = arrow(heap.cells[RES_CELLS[n - 1]].get_bottom(), stack.cells[i].get_top())
                self.play(GrowArrow(a_in), run_time=0.6)
            a_out = arrow(stack.cells[i].get_top(), heap.cells[RES_CELLS[n]].get_bottom())
            self.play(*([FadeOut(a_in)] if a_in else []), GrowArrow(a_out), Transform(lines[k], new),
                      *heap.write(RES_CELLS[n], f"s{n}={results[n]}", GREEN, 0.7, 10), run_time=0.8)
            self.play(FadeOut(a_out), *stack.clear(i), *stack.clear(i + 1), sp.animate.move_to(stack.cells[i]),
                      *(heap.clear(RES_CELLS[n - 1]) if n > 0 else []), run_time=0.6)
        self.wait(0.8)
        caption("Ergebnis s(4) bleibt im Heap")
        self.wait(3)


class CallStack(Scene):
    def construct(self):
        cell, cx = 0.6, 0.0
        stack = Matrix(4, 16, cell, cx, -1.3, 0x7F00, bottom_up=True, label_size=14)
        lab = T("Stack-Größe", 28, INK, weight=BOLD).move_to([cx - 8 * cell, 1.55, 0], aligned_edge=LEFT)
        title = T("Berechnung Kleiner Gauß", 24, INK, weight=BOLD).move_to([0, 3.5, 0])
        f1 = T("s(n) = n + s(n − 1)", 32, INK).move_to([0, 2.95, 0])
        f2 = T("ohne Abbruchbedingung s(0) = 0", 24, RED).move_to([0, 2.35, 0])
        self.play(FadeIn(stack.group), FadeIn(lab), FadeIn(title), FadeIn(f1), FadeIn(f2), run_time=1.2)
        sp = Square(cell, color=YELLOW, stroke_width=5).move_to(stack.cells[0])
        self.add(sp)
        self.wait(0.5)

        total = 32                      # frames of two cells
        for k in range(total):
            n = 5 - k
            i = 2 * k
            t = max(0.6 * (0.82 ** k), 0.05)
            shade = 0.8 if k % 2 == 0 else 0.5
            nxt = stack.cells[i + 2] if i + 2 < 64 else stack.cells[63]
            self.play(*stack.write(i, f"n={n}", BLUE, shade, 14), *stack.write(i + 1, "ret", BLUE, shade, 14),
                      sp.animate.move_to(nxt), run_time=t)
        self.play(*[stack.cells[i].animate.set_fill(RED, opacity=0.8) for i in range(64)],
                  FadeOut(sp), run_time=0.8)
        err = T("RecursionError: maximum recursion depth exceeded", 28, INK, weight=BOLD, font=MONO).move_to([0, -2.5, 0])
        sub = T("Der Stack ist voll: Stack Overflow", 26, MUTED).move_to([0, -3.2, 0])
        self.play(FadeIn(err), FadeIn(sub), run_time=0.7)
        self.wait(3)
