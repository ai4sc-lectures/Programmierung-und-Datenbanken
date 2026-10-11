"""Manim scene for the slide "Der Bus transportiert Programme und Daten" (01c_Computerhardware.qmdx).

Runs the program `z = x + y` through CPU, RAM and HDD/SSD: the program is loaded from the disk into
the RAM, then the IP walks through LOAD, LOAD, ADD, STORE; instructions and data travel over the bus,
the ALU computes with registers only.
Palette: light "pastello" theme (_extensions/ai4sc-style/themes/color/pastello.css).

Render, from the lectures/ directory:

    manim/render.sh manim/bus_dataflow.py BusDataflow 1200,740 images/01c_Computerhardware/manim_bus_dataflow.mp4
"""
from manim import *

config.frame_height = 7.4
config.frame_width = 12
config.background_color = "#F8F7F2"

INK = "#302F2B"
MUTED = "#68665E"
RIM = "#B9B5A6"
BLUE = "#91B5CB"
GREEN = "#8B9E87"
YELLOW = "#D6B65E"
BUBBLE = "#F3F1E8"
PAPER = "#F8F7F2"
FONT = "Helvetica Neue"
MONO = "Menlo"

XC = -3.0                      # centre of the left column (CPU, RAM)
CORR = -2.0                    # vertical corridor between program and data in the RAM
Y_TOPCORR = -0.85              # horizontal corridor below the RAM's top edge
CPU_BOT, RAM_TOP = 0.6, -0.7
ROW_Y = [-1.45, -1.95, -2.45, -2.95]
DATA_Y = {"x": -1.6, "y": -2.3, "z": -3.0}
REG_X = {"R1": -4.5, "R2": -3.0, "R3": -1.5}


def T(text, size=24, color=INK, font=FONT, **kw):
    return Text(text, font=font, font_size=size * 2, color=color, **kw).scale(0.5)


def frame_box(x, y, w, h, fill=BUBBLE, stroke=INK, sw=4):
    return Rectangle(width=w, height=h, color=stroke, stroke_width=sw, fill_color=fill,
                     fill_opacity=1).move_to([x, y, 0])


def chip(text, color, w=None):
    t = T(text, 18, INK, font=MONO)
    r = RoundedRectangle(corner_radius=0.1, width=w or t.width + 0.35, height=0.46, color=INK,
                         stroke_width=3, fill_color=color, fill_opacity=1)
    t.move_to(r)
    return VGroup(r, t)


class BusDataflow(Scene):
    def construct(self):
        # ---- modules -------------------------------------------------------------------
        cpu = frame_box(XC, 2.0, 5.6, 2.8)
        ram = frame_box(XC, -2.15, 5.6, 2.9)
        hdd = frame_box(3.0, -2.15, 5.6, 2.9)
        bus = Line([-5.9, 0, 0], [5.9, 0, 0], color=INK, stroke_width=10)
        ends = VGroup(Dot([-5.9, 0, 0], radius=0.1, color=INK), Dot([5.9, 0, 0], radius=0.1, color=INK))
        conn_l = Line([XC, CPU_BOT, 0], [XC, RAM_TOP, 0], color=INK, stroke_width=7)
        conn_r = Line([3.0, 0, 0], [3.0, RAM_TOP, 0], color=INK, stroke_width=7)
        dots = VGroup(*[Dot([x, y, 0], radius=0.12, color=INK, fill_color=BUBBLE, fill_opacity=1, stroke_width=4)
                        for x, y in [(XC, CPU_BOT), (XC, RAM_TOP), (3.0, RAM_TOP)]])
        titles = VGroup(T("CPU", 26, INK, weight=BOLD).move_to([-5.55, 3.05, 0], aligned_edge=LEFT),
                        T("RAM", 26, INK, weight=BOLD).move_to([-5.55, -1.0, 0], aligned_edge=LEFT),
                        T("HDD/SSD", 26, INK, weight=BOLD).move_to([0.35, -1.0, 0], aligned_edge=LEFT))
        # CPU: IP, registers, ALU
        ip_lab = T("IP", 20, MUTED, font=MONO).move_to([-2.35, 3.05, 0])
        ip_box = frame_box(-1.15, 3.05, 1.5, 0.5, fill=BUBBLE, stroke=YELLOW, sw=4)
        ip_val = T("", 18, INK, font=MONO).move_to(ip_box)
        regs, reg_vals = {}, {}
        reg_items = VGroup()
        for n, x in REG_X.items():
            b = frame_box(x, 2.0, 1.3, 0.6, sw=3, stroke=RIM)
            lab = T(n, 18, MUTED, font=MONO).move_to([x, 2.52, 0])
            reg_vals[n] = T("", 22, INK, font=MONO).move_to(b)
            regs[n] = b
            reg_items.add(b, lab)
        alu = frame_box(XC, 1.05, 3.8, 0.55, fill=INK, stroke=INK, sw=3)
        alu_t = T("ALU", 20, PAPER, weight=BOLD).move_to([XC - 1.2, 1.05, 0])
        alu_s = T("R1 + R2 → R3", 18, PAPER, font=MONO).move_to([XC + 0.5, 1.05, 0])
        # RAM: program lines and data cells
        prog = ["LOAD  R1, [x]", "LOAD  R2, [y]", "ADD   R3, R1, R2", "STORE [z], R3"]
        rows = [frame_box(-4.0, y, 3.4, 0.46, sw=2, stroke=RIM) for y in ROW_Y]
        row_txt = VGroup(*[VGroup(T(f"0x000{i+1}", 14, MUTED, font=MONO).move_to([-5.45, y, 0], aligned_edge=LEFT),
                                  T(p, 16, INK, font=MONO).move_to([-4.55, y, 0], aligned_edge=LEFT))
                           for i, (p, y) in enumerate(zip(prog, ROW_Y))])
        cells, cell_vals = {}, {}
        data_items = VGroup()
        for n, y in DATA_Y.items():
            b = frame_box(-1.0, y, 1.5, 0.6, sw=3, stroke=RIM)
            cells[n] = b
            cell_vals[n] = T({"x": "x = 5", "y": "y = 3", "z": "z = ?"}[n], 20, INK, font=MONO).move_to(b)
            data_items.add(b, cell_vals[n])
        # HDD: the program file
        file_chip = chip("z = x + y", YELLOW, w=2.3).move_to([3.0, -2.45, 0])
        file_lab = T("Programm", 18, MUTED).next_to(file_chip, UP, buff=0.1)

        self.play(Create(bus), FadeIn(ends), Create(conn_l), Create(conn_r), run_time=1.0)
        self.play(FadeIn(VGroup(cpu, ram, hdd)), FadeIn(titles), run_time=0.8)
        self.add(dots)
        self.play(FadeIn(ip_lab), FadeIn(ip_box), FadeIn(reg_items), FadeIn(VGroup(alu, alu_t, alu_s)),
                  FadeIn(data_items), FadeIn(file_chip), FadeIn(file_lab), run_time=1.0)
        self.add(*reg_vals.values(), ip_val)

        cap = None

        def caption(title, lines):
            nonlocal cap
            g = VGroup(T(title, 26, INK, weight=BOLD),
                       *[T(l, 22, MUTED) for l in lines]).arrange(DOWN, aligned_edge=LEFT, buff=0.18)
            g.move_to([0.4, 2.0, 0], aligned_edge=LEFT)
            self.play(*( [FadeOut(cap)] if cap else [] ), FadeIn(g), run_time=0.4)
            cap = g

        def travel(pk, pts, t=1.0):
            path = VMobject().set_points_as_corners([[x, y, 0] for x, y in pts])
            pk.move_to(path.get_start())
            self.play(FadeIn(pk, scale=0.8), run_time=0.25)
            self.play(MoveAlongPath(pk, path), run_time=t, rate_func=linear)

        def set_ip(i):
            new = T(f"0x000{i}", 18, INK, font=MONO).move_to(ip_box)
            return Transform(ip_val, new)

        def to_cpu(row_y, color, text, extra=None):
            pk = chip(text, color)
            travel(pk, [(-2.3, row_y), (CORR, row_y), (CORR, Y_TOPCORR), (XC, Y_TOPCORR), (XC, CPU_BOT)], 1.4)
            return pk

        # ---- 1: load the program ---------------------------------------------------------
        caption("Programm laden", ["Die Festplatte liefert das Programm", "über den Bus in den RAM."])
        pk = chip("Programm", YELLOW)
        travel(pk, [(3.0, -1.7), (3.0, 0), (XC, 0), (XC, RAM_TOP - 0.15)], 2.0)
        self.play(FadeOut(pk), FadeIn(VGroup(*rows)), FadeIn(row_txt), run_time=0.6)
        self.wait(0.6)

        def hl(i, on=True):
            return rows[i].animate.set_fill(YELLOW if on else BUBBLE, opacity=0.7 if on else 1)

        def load(i, reg, var, val):
            caption(f"IP = 0x000{i+1}: {prog[i].split()[0]} {reg}, [{var}]".replace("  ", " "),
                    [f"Befehl zur CPU, dann der Wert", f"von {var} in {reg}."])
            self.play(set_ip(i + 1), hl(i), run_time=0.5)
            pk = to_cpu(ROW_Y[i], BLUE, prog[i].replace("  ", " "))
            self.play(FadeOut(pk), run_time=0.3)
            dp = chip(f"{var} = {val}", GREEN)
            travel(dp, [(-1.0, DATA_Y[var]), (CORR, DATA_Y[var]), (CORR, Y_TOPCORR), (XC, Y_TOPCORR), (XC, CPU_BOT)], 1.4)
            new = T(str(val), 22, INK, font=MONO).move_to(regs[reg])
            self.play(FadeOut(dp), regs[reg].animate.set_fill(GREEN, opacity=0.55), Transform(reg_vals[reg], new), run_time=0.5)
            self.play(hl(i, False), run_time=0.3)

        load(0, "R1", "x", 5)
        load(1, "R2", "y", 3)

        # ---- 3: ADD -----------------------------------------------------------------------
        caption("IP = 0x0003: ADD R3, R1, R2", ["Die ALU addiert die Register.", "Kein Zugriff auf den RAM."])
        self.play(set_ip(3), hl(2), run_time=0.5)
        pk = to_cpu(ROW_Y[2], BLUE, "ADD R3, R1, R2")
        self.play(FadeOut(pk), alu.animate.set_fill(YELLOW, opacity=1), alu_t.animate.set_color(INK),
                  alu_s.animate.set_color(INK), run_time=0.5)
        self.play(regs["R1"].animate.set_fill(YELLOW, opacity=0.6), regs["R2"].animate.set_fill(YELLOW, opacity=0.6),
                  run_time=0.4)
        new = T("8", 22, INK, font=MONO).move_to(regs["R3"])
        self.play(regs["R3"].animate.set_fill(GREEN, opacity=0.55), Transform(reg_vals["R3"], new), run_time=0.6)
        self.play(alu.animate.set_fill(INK, opacity=1), alu_t.animate.set_color(PAPER), alu_s.animate.set_color(PAPER),
                  regs["R1"].animate.set_fill(GREEN, opacity=0.55), regs["R2"].animate.set_fill(GREEN, opacity=0.55),
                  hl(2, False), run_time=0.5)

        # ---- 4: STORE ---------------------------------------------------------------------
        caption("IP = 0x0004: STORE [z], R3", ["Das Ergebnis geht über den Bus", "in die Zelle von z."])
        self.play(set_ip(4), hl(3), run_time=0.5)
        pk = to_cpu(ROW_Y[3], BLUE, "STORE [z], R3")
        self.play(FadeOut(pk), run_time=0.3)
        rp = chip("8", GREEN, w=0.7)
        travel(rp, [(XC, CPU_BOT), (XC, Y_TOPCORR), (CORR, Y_TOPCORR), (CORR, DATA_Y["z"]), (-1.0, DATA_Y["z"])], 1.6)
        newz = T("z = 8", 20, INK, font=MONO).move_to(cells["z"])
        self.play(FadeOut(rp), cells["z"].animate.set_fill(GREEN, opacity=0.55), Transform(cell_vals["z"], newz), run_time=0.5)
        self.play(hl(3, False), set_ip(5), run_time=0.5)
        caption("Fertig: z = x + y = 8", ["Der IP zeigt jetzt auf", "den nächsten Befehl."])
        self.wait(3)
