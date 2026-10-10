"""Manim scene for the slide "Speicherzellen und Register" (02a_Computerhardware.qmdx).

Data flow of `z = x + y`: RAM cell -> register -> ALU -> back into the RAM cell.
Palette: light "pastello" theme (_extensions/ai4sc-style/themes/color/pastello.css).

Render, from the lectures/ directory:

    manim/render.sh manim/memory_cells.py MemoryCells 1200,800 images/02a_Computerhardware/manim_memory_cells.mp4
"""
from manim import *

config.frame_height = 8
config.frame_width = 12
config.background_color = "#F8F7F2"

INK = "#302F2B"
MUTED = "#68665E"
RIM = "#B9B5A6"
CYAN = "#91B5CB"
YELLOW = "#D6B65E"
BUBBLE = "#F3F1E8"
FONT = "Helvetica Neue"
MONO = "Menlo"


def T(text, size=24, color=INK, font=FONT, **kw):
    return Text(text, font=font, font_size=size * 2, color=color, **kw).scale(0.5)


def panel(title, x, w, h=7.2):
    frame = Rectangle(width=w, height=h, color=INK, stroke_width=3, fill_color=BUBBLE,
                      fill_opacity=0.6).move_to([x, 0, 0])
    bar = Rectangle(width=w, height=0.7, color=INK, fill_color=INK, fill_opacity=1,
                    stroke_width=3).align_to(frame, UP).align_to(frame, LEFT)
    t = T(title, 26, "#F8F7F2", weight=BOLD).move_to(bar)
    return VGroup(frame, bar, t)


def box(x, y, w, h=0.7, fill=BUBBLE):
    return Rectangle(width=w, height=h, color=RIM, fill_color=fill, fill_opacity=1,
                     stroke_width=3).move_to([x, y, 0])


class MemoryCells(Scene):
    def construct(self):
        ram = panel("RAM", -2.6, 6.2)
        cpu = panel("CPU", 3.9, 3.6)
        self.add(ram, cpu)
        self.add(T("Programm", 20, MUTED).move_to([-4.6, 2.7, 0]),
                 T("Daten (Variablen)", 20, MUTED).move_to([-3.9, -0.15, 0]))
        code = ["LOAD  R1, [0x0A10]", "LOAD  R2, [0x0A11]", "ADD   R3, R1, R2", "STORE [0x0A12], R3"]
        rows = []
        for i, c in enumerate(code):
            b = box(-2.6, 2.2 - i * 0.6, 5.8, 0.55)
            self.add(b, T(f"0x000{i+1}", 20, MUTED, font=MONO).move_to([-5.0, 2.2 - i * 0.6, 0]),
                     T(c, 20, INK, font=MONO).move_to([-3.7, 2.2 - i * 0.6, 0], aligned_edge=LEFT))
            rows.append(b)
        data = {}
        for i, (a, n, v, lab) in enumerate([("0x0A10", "x", "00000101", "x = 5"),
                                            ("0x0A11", "y", "00000011", "y = 3"),
                                            ("0x0A12", "z", "00000000", "z = ?")]):
            y = -0.7 - i * 0.7
            b = box(-2.6, y, 5.8, 0.6)
            val = T(v, 20, INK, font=MONO).move_to([-3.3, y, 0])
            note = T(lab, 20, INK).move_to([-1.2, y, 0], aligned_edge=LEFT)
            self.add(b, T(a, 20, MUTED, font=MONO).move_to([-4.9, y, 0]), val, note)
            data[n] = (b, val, note, y)
        # CPU: registers, ALU
        regs = {}
        self.add(T("Register", 20, MUTED).move_to([3.0, 2.7, 0]))
        for i, n in enumerate(["R1", "R2", "R3"]):
            y = 2.2 - i * 0.7
            b = box(3.9, y, 3.2, 0.6)
            tag = T(f"{n} =", 20, MUTED, font=MONO).move_to([2.7, y, 0])
            v = T("?" if n == "R3" else "", 20, MUTED, font=MONO).move_to([4.3, y, 0])
            self.add(b, tag, v)
            regs[n] = (b, v, y)
        alu = Rectangle(width=3.2, height=1.4, color=INK, fill_color=INK, fill_opacity=1,
                        stroke_width=3).move_to([3.9, -1.3, 0])
        alu_t = T("ALU", 26, "#F8F7F2", weight=BOLD).move_to([3.9, -1.0, 0])
        alu_s = T("R1 + R2 → R3", 20, "#F8F7F2").move_to([3.9, -1.55, 0])
        self.add(alu, alu_t, alu_s)
        self.wait(1)

        def arrow(a, b):
            return Arrow(a, b, buff=0.08, color=CYAN, stroke_width=6, tip_length=0.25,
                         max_tip_length_to_length_ratio=1, max_stroke_width_to_length_ratio=100)

        def setreg(n, v):
            b, old, y = regs[n]
            new = T(v, 20, INK, font=MONO).move_to([4.3, y, 0])
            return [b.animate.set_fill(CYAN, opacity=0.7), Transform(old, new)]

        # LOAD R1 <- x, LOAD R2 <- y
        for n, r, v in [("x", "R1", "00000101"), ("y", "R2", "00000011")]:
            b = data[n][0]
            self.play(b.animate.set_stroke(YELLOW, width=6), run_time=0.4)
            a = arrow(b.get_right(), regs[r][0].get_left())
            self.play(GrowArrow(a), run_time=0.6)
            self.play(*setreg(r, v), run_time=0.6)
            self.play(FadeOut(a), b.animate.set_stroke(RIM, width=3), run_time=0.4)
        # ADD in the ALU
        a1 = arrow(regs["R1"][0].get_bottom() + DOWN * 0.0 + RIGHT * 0.8, alu.get_top() + LEFT * 0.8)
        a2 = arrow(regs["R2"][0].get_bottom() + RIGHT * 1.2, alu.get_top() + RIGHT * 0.2)
        self.play(alu.animate.set_fill(YELLOW, opacity=1), alu_t.animate.set_color(INK),
                  alu_s.animate.set_color(INK), run_time=0.6)
        self.wait(0.6)
        self.play(*setreg("R3", "00001000"), run_time=0.7)
        self.play(alu.animate.set_fill(INK, opacity=1), alu_t.animate.set_color("#F8F7F2"),
                  alu_s.animate.set_color("#F8F7F2"), run_time=0.5)
        # STORE z <- R3
        zb, zval, znote, zy = data["z"]
        a = arrow(regs["R3"][0].get_left(), zb.get_right())
        self.play(GrowArrow(a), run_time=0.6)
        self.play(zb.animate.set_fill(CYAN, opacity=0.7),
                  Transform(zval, T("00001000", 20, INK, font=MONO).move_to(zval)),
                  Transform(znote, T("z = 8", 20, INK).move_to(znote, aligned_edge=LEFT)),
                  run_time=0.7)
        self.play(FadeOut(a), run_time=0.4)
        self.wait(2)
