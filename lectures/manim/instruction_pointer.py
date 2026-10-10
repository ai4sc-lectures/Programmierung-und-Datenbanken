"""Manim scene for the slide "Instruction Pointer – Schritt für Schritt" (02a_Computerhardware.qmdx).

The IP walks through LOAD, LOAD, ADD, STORE; registers and RAM cells change with every step.
Palette: light "pastello" theme (_extensions/ai4sc-style/themes/color/pastello.css).

Render, from the lectures/ directory:

    manim/render.sh manim/instruction_pointer.py InstructionPointer 1200,800 images/02a_Computerhardware/manim_instruction_pointer.mp4
"""
from manim import *

config.frame_height = 8
config.frame_width = 12
config.background_color = "#F8F7F2"

INK = "#302F2B"
MUTED = "#68665E"
RIM = "#B9B5A6"
CYAN = "#91B5CB"      # signal-blue: data that was just written
YELLOW = "#D6B65E"    # signal-yellow: current instruction / IP
BG = "#F8F7F2"
BUBBLE = "#F3F1E8"
FONT = "Helvetica Neue"
MONO = "Menlo"


def T(text, size=24, color=INK, font=FONT, **kw):
    return Text(text, font=font, font_size=size * 2, color=color, **kw).scale(0.5)


def cell(label, value, w=1.9, h=0.8, label_size=20):
    box = Rectangle(width=w, height=h, color=RIM, fill_color=BUBBLE, fill_opacity=1, stroke_width=3)
    lab = T(label, label_size, MUTED).next_to(box, LEFT, buff=0.2)
    val = T(value, 28, INK, font=MONO).move_to(box)
    return box, lab, val


class InstructionPointer(Scene):
    def construct(self):
        code = ["LOAD  R1, [0x0A10]", "LOAD  R2, [0x0A11]", "ADD   R3, R1, R2",
                "STORE [0x0A12], R3", "..."]
        addr = ["0x0001", "0x0002", "0x0003", "0x0004", "0x0005"]
        row_h = 0.95
        top = 2.9
        rows, ys = VGroup(), []
        for i, (a, c) in enumerate(zip(addr, code)):
            y = top - i * row_h
            ys.append(y)
            bg = Rectangle(width=5.4, height=row_h - 0.1, color=RIM, fill_color=BUBBLE,
                           fill_opacity=1, stroke_width=2).move_to([-2.4, y, 0])
            ta = T(a, 22, MUTED, font=MONO).move_to([-4.4, y, 0])
            tc = T(c, 24, INK, font=MONO).move_to([-3.7, y, 0], aligned_edge=LEFT)
            rows.add(VGroup(bg, ta, tc))
        head = T("Speicher (Befehle)", 22, MUTED).move_to([-2.4, 3.65, 0])

        # IP arrow and IP register
        ip_arrow = Arrow([-5.9, ys[0], 0], [-5.2, ys[0], 0], buff=0, color=YELLOW,
                         stroke_width=10, tip_length=0.3, max_tip_length_to_length_ratio=1,
                         max_stroke_width_to_length_ratio=100)
        ip_label = T("IP", 26, INK, weight=BOLD).next_to(ip_arrow, LEFT, buff=0.1)
        ip_box = Rectangle(width=2.0, height=0.8, color=YELLOW, fill_color=BUBBLE,
                           fill_opacity=1, stroke_width=4).move_to([3.9, 3.5, 0])
        ip_tag = T("IP", 22, MUTED, font=MONO).next_to(ip_box, LEFT, buff=0.2)
        ip_val = T("0x0001", 26, INK, font=MONO).move_to(ip_box)

        # CPU registers and RAM cells (right panel)
        regs = {}
        for i, n in enumerate(["R1", "R2", "R3"]):
            box = Rectangle(width=1.4, height=0.7, color=RIM, fill_color=BUBBLE,
                            fill_opacity=1, stroke_width=3).move_to([4.2, 1.85 - i * 0.85, 0])
            lab = T(n, 20, MUTED, font=MONO).next_to(box, LEFT, buff=0.2)
            val = T("", 28, INK, font=MONO).move_to(box)
            regs[n] = (box, val, VGroup(box, lab))
        cpu_head = T("CPU-Register", 22, MUTED).move_to([3.4, 2.65, 0])
        ram = {}
        for i, (n, a) in enumerate([("x", "0x0A10"), ("y", "0x0A11"), ("z", "0x0A12")]):
            box = Rectangle(width=1.4, height=0.7, color=RIM, fill_color=BUBBLE,
                            fill_opacity=1, stroke_width=3).move_to([4.2, -1.5 - i * 0.85, 0])
            lab = T(f"{n}  {a}", 20, MUTED, font=MONO).next_to(box, LEFT, buff=0.2)
            ram[n] = (box, lab)
        ram_head = T("RAM (Daten)", 22, MUTED).move_to([3.4, -0.7, 0])

        self.play(FadeIn(head), FadeIn(rows), FadeIn(ip_box), FadeIn(ip_tag), FadeIn(ip_val),
                  FadeIn(cpu_head), FadeIn(ram_head), run_time=1)
        for n in regs:
            self.add(regs[n][2])
        for n in ram:
            self.add(*ram[n])
        # initial RAM values
        vals = {"x": "5", "y": "3"}
        ram_vals = {}
        for n, v in vals.items():
            t = T(v, 28, INK, font=MONO).move_to(ram[n][0])
            ram_vals[n] = t
            self.add(t)
        self.play(FadeIn(ip_arrow), FadeIn(ip_label), run_time=0.5)

        def hl(i):
            return rows[i][0].animate.set_fill(YELLOW, opacity=0.9)

        def unhl(i):
            return rows[i][0].animate.set_fill(BUBBLE, opacity=1)

        def set_ip(i):
            new = T(addr[i], 26, INK, font=MONO).move_to(ip_box)
            return [ip_arrow.animate.move_to([-5.55, ys[i], 0]), Transform(ip_val, new)]

        def write_reg(n, v):
            box, val, _ = regs[n]
            new = T(v, 28, INK, font=MONO).move_to(box)
            return [box.animate.set_fill(CYAN, opacity=0.7), Transform(val, new)]

        # step 1: LOAD R1
        self.play(hl(0)); self.wait(0.4)
        a1 = Arrow(ram["x"][0].get_left(), regs["R1"][0].get_right(), buff=0.1, color=CYAN,
                   stroke_width=6, tip_length=0.25)
        self.play(GrowArrow(a1), run_time=0.5)
        self.play(*write_reg("R1", "5"), run_time=0.6)
        self.play(FadeOut(a1), unhl(0), *set_ip(1), run_time=0.7)
        # step 2: LOAD R2
        self.play(hl(1)); self.wait(0.4)
        a2 = Arrow(ram["y"][0].get_left(), regs["R2"][0].get_right(), buff=0.1, color=CYAN,
                   stroke_width=6, tip_length=0.25)
        self.play(GrowArrow(a2), run_time=0.5)
        self.play(*write_reg("R2", "3"), run_time=0.6)
        self.play(FadeOut(a2), unhl(1), *set_ip(2), run_time=0.7)
        # step 3: ADD
        self.play(hl(2)); self.wait(0.4)
        self.play(regs["R1"][0].animate.set_fill(YELLOW, opacity=0.9),
                  regs["R2"][0].animate.set_fill(YELLOW, opacity=0.9), run_time=0.5)
        self.play(*write_reg("R3", "8"), run_time=0.6)
        self.play(regs["R1"][0].animate.set_fill(CYAN, opacity=0.7),
                  regs["R2"][0].animate.set_fill(CYAN, opacity=0.7), unhl(2), *set_ip(3), run_time=0.7)
        # step 4: STORE
        self.play(hl(3)); self.wait(0.4)
        a3 = Arrow(regs["R3"][0].get_right(), ram["z"][0].get_left(), buff=0.1, color=CYAN,
                   stroke_width=6, tip_length=0.25)
        self.play(GrowArrow(a3), run_time=0.5)
        zv = T("8", 28, INK, font=MONO).move_to(ram["z"][0])
        self.play(ram["z"][0].animate.set_fill(CYAN, opacity=0.7), FadeIn(zv), run_time=0.6)
        self.play(FadeOut(a3), unhl(3), *set_ip(4), run_time=0.7)
        self.wait(2)
