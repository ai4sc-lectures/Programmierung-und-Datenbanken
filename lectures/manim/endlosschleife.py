"""Manim scene for the slide "Was an einer Endlosschleife schiefgeht" (05c_Schleifen.qmdx).

Part 1: `while x > 0: print(x)` never changes x. The instruction pointer jumps between the two
loop lines forever, the stack cell x stays 10, the iteration counter only grows.
Part 2: `while True: daten.append(1)`. Every pass puts another object on the heap until it is full.
Palette: light "pastello" theme (_extensions/ai4sc-style/themes/color/pastello.css).

Render, from the lectures/ directory:

    manim/render.sh manim/endlosschleife.py Endlosschleife 1200,760 images/05c_Schleifen/manim_endlosschleife.mp4
"""
from manim import *

config.frame_height = 7.6
config.frame_width = 12
config.background_color = "#F8F7F2"

INK = "#302F2B"
MUTED = "#68665E"
RIM = "#B9B5A6"
BLUE = "#91B5CB"      # data
YELLOW = "#D6B65E"    # instruction pointer
RED = "#C58E89"       # problem
BUBBLE = "#F3F1E8"
FONT = "Helvetica Neue"
MONO = "Menlo"


def T(text, size=24, color=INK, font=FONT, **kw):
    return Text(text, font=font, font_size=size * 2, color=color, **kw).scale(0.5)


def code_line(text, y, x=-4.65):
    """Monospace line; Text drops leading blanks, so the indent is added as a shift."""
    indent = len(text) - len(text.lstrip())
    return T(text.strip(), 26, INK, font=MONO).move_to([x + indent * 0.2, y, 0], aligned_edge=LEFT)


def grouped(n):
    return f"{n:,}".replace(",", ".")


class Endlosschleife(Scene):
    def construct(self):
        # --- code panel (left) -----------------------------------------------------------
        panel = RoundedRectangle(width=5.6, height=2.7, corner_radius=0.15, color=RIM,
                                 fill_color=BUBBLE, fill_opacity=1, stroke_width=3).move_to([-2.3, 1.9, 0])
        ys = [2.75, 1.95, 1.15]
        code1 = ["x = 10", "while x > 0:", "    print(x)"]
        lines = VGroup(*[code_line(c, y) for c, y in zip(code1, ys)])
        head = T("Programm", 22, MUTED).next_to(panel, UP, buff=0.12).align_to(panel, LEFT)

        ip = Arrow([-5.35, 0, 0], [-5.0, 0, 0], buff=0, color=YELLOW, stroke_width=10,
                   tip_length=0.28, max_tip_length_to_length_ratio=1,
                   max_stroke_width_to_length_ratio=100)
        ip_label = T("IP", 20, MUTED, weight=BOLD)

        # --- memory (right) --------------------------------------------------------------
        stack_head = T("Stack", 22, MUTED).move_to([3.2, 3.3, 0])
        stack_cell = Rectangle(width=2.0, height=0.7, color=RIM, fill_color=BUBBLE,
                               fill_opacity=1, stroke_width=3).move_to([3.7, 2.6, 0])
        stack_name = T("x", 24, MUTED, font=MONO).next_to(stack_cell, LEFT, buff=0.2)
        stack_val = T("10", 28, INK, font=MONO).move_to(stack_cell)

        heap_head = T("Heap", 22, MUTED).move_to([3.0, 1.55, 0])
        cols, rows, cs = 10, 4, 0.42
        heap = VGroup(*[Square(cs, color=RIM, stroke_width=1.5, fill_color=BUBBLE, fill_opacity=1)
                        for _ in range(cols * rows)]).arrange_in_grid(rows, cols, buff=0)
        heap.move_to([3.2, 0.2, 0])
        heap_cells = list(heap)

        # --- counter and messages --------------------------------------------------------
        counter_label = T("Durchläufe:", 26, MUTED)
        count = ValueTracker(0)
        counter = always_redraw(lambda: T(grouped(int(count.get_value())), 34, INK, font=MONO)
                                .next_to(counter_label, RIGHT, buff=0.25))
        counter_group_pos = [-1.6, -2.1, 0]
        counter_label.move_to(counter_group_pos)

        msg1 = T("x ändert sich nie: x > 0 bleibt immer wahr.", 26, INK)
        msg1.move_to([0, -3.2, 0])
        msg2 = T("Jeder Durchlauf legt ein weiteres Objekt auf dem Heap ab.", 26, INK)
        msg2.move_to([0, -3.2, 0])
        end1 = T("Das Programm kommt nie zum Ende.", 28, RED, weight=BOLD)
        end1.move_to([0, -3.2, 0])
        end2 = T("Der Heap läuft voll: Das Programm hängt oder wird beendet.", 28, RED, weight=BOLD)
        end2.move_to([0, -3.2, 0])

        # --- part 1: x never changes -----------------------------------------------------
        self.add(panel, head, lines, stack_head, stack_cell, stack_name, stack_val,
                 heap_head, heap, counter_label, counter)
        tick = ValueTracker(0)

        def place_ip(m):
            y = ys[1] if int(tick.get_value()) % 2 == 0 else ys[2]
            m.move_to([-5.18, y, 0])

        ip.add_updater(place_ip)
        ip_label.add_updater(lambda m: m.next_to(ip, LEFT, buff=0.08))
        self.add(ip, ip_label)
        ip.move_to([-5.18, ys[1], 0])
        self.play(FadeIn(msg1), run_time=0.6)
        self.play(tick.animate.set_value(12), count.animate.set_value(120),
                  run_time=3.0, rate_func=linear)
        self.play(tick.animate.set_value(40), count.animate.set_value(1_000_000),
                  run_time=2.5, rate_func=rush_into)
        self.play(FadeOut(msg1), FadeIn(end1), run_time=0.6)
        self.wait(1.2)

        # --- part 2: the loop fills the heap ---------------------------------------------
        ip.clear_updaters()
        count.set_value(0)
        code2 = ["daten = []", "while True:", "    daten.append(1)"]
        new_lines = VGroup(*[code_line(c, y) for c, y in zip(code2, ys)])
        new_stack_name = T("daten", 22, MUTED, font=MONO).next_to(stack_cell, LEFT, buff=0.2)
        new_stack_val = T("→", 30, INK).move_to(stack_cell)
        self.play(FadeOut(end1), FadeOut(lines), FadeOut(stack_name), FadeOut(stack_val),
                  run_time=0.5)
        self.play(FadeIn(new_lines), FadeIn(new_stack_name), FadeIn(new_stack_val),
                  FadeIn(msg2), run_time=0.6)
        ip.add_updater(place_ip)
        tick.set_value(0)
        n = len(heap_cells)
        for i, c in enumerate(heap_cells):
            c.generate_target()
            c.target.set_fill(BLUE if i < n - 1 else RED, opacity=1)
        # fill the cells one after another, speeding up
        total_time = 4.0
        for i, c in enumerate(heap_cells):
            dt = total_time / n * (1.4 - i / n)
            self.play(c.animate.set_fill(BLUE, opacity=1), tick.animate.increment_value(1),
                      count.animate.increment_value(1), run_time=max(dt, 0.04), rate_func=linear)
        self.play(*[c.animate.set_fill(RED, opacity=1) for c in heap_cells], run_time=0.5)
        self.play(FadeOut(msg2), FadeIn(end2), run_time=0.6)
        self.wait(2.0)
