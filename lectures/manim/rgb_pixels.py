"""Manim scene for the slide "Abbildung von Bildern im Computer" (01c_Computerhardware.qmdx).

Pixel mosaic -> zoom into 3x3 pixels -> three colour channels with numbers -> one pixel as 3 bytes.
Palette: light "pastello" theme (_extensions/ai4sc-style/themes/color/pastello.css).

Render, from the lectures/ directory:

    manim/render.sh manim/rgb_pixels.py RGBPixels 1200,800 images/01c_Computerhardware/manim_rgb_pixels.mp4
"""
from manim import *

config.frame_height = 8
config.frame_width = 12
config.background_color = "#F8F7F2"

INK = "#302F2B"
MUTED = "#68665E"
RIM = "#B9B5A6"
FONT = "Helvetica Neue"
MONO = "Menlo"
CH_BLUE, CH_GREEN, CH_RED = "#91B5CB", "#8B9E87", "#C58E89"
# rubber duck, 16 x 14 pixels; RGB values are the real colours of the pixels
PAL = {".": (207, 227, 238), "Y": (245, 208, 64), "O": (232, 118, 40), "K": (40, 40, 40),
       "W": (255, 248, 225), "w": (120, 170, 200)}
MOSAIC = ["................",
          "......YYYY......",
          ".....YYYYYY.....",
          ".....YYYKYYY....",
          ".....YYYYYOOO...",
          ".....YYYYYOOO...",
          "......YYYY......",
          ".....YYYY.......",
          "..YY.YYYYYYY....",
          ".YYYYYYYYYYYY...",
          "YYYYYYYWWYYYYY..",
          ".YYYYYYYYYYYYY..",
          "..YYYYYYYYYY....",
          "wwwwwwwwwwwwwwww"]
COLS = 16
ROWS = [3, 4, 5]
BCOLS = [8, 9, 10]
BLOCK = [[PAL[MOSAIC[r][c]] for c in BCOLS] for r in ROWS]
RED = [[px[0] for px in row] for row in BLOCK]
GREEN = [[px[1] for px in row] for row in BLOCK]
BLUE = [[px[2] for px in row] for row in BLOCK]


def hexc(rgb):
    return "#%02X%02X%02X" % rgb


def T(text, size=24, color=INK, font=FONT, **kw):
    return Text(text, font=font, font_size=size * 2, color=color, **kw).scale(0.5)


STRONG = [(208, 68, 60), (76, 154, 90), (63, 127, 191)]    # full intensity of R, G, B
PAPER = (248, 247, 242)


def tint(ch, v):
    """Paper colour at 0, the full channel colour at 255: low values look pale."""
    f = v / 255
    return hexc(tuple(round(p + (c - p) * f) for p, c in zip(PAPER, STRONG[ch])))


def grid(values, ch, cell, num_size=22):
    """One colour channel: every cell is shaded with the channel intensity (0 = pale, 255 = full colour)."""
    g = VGroup()
    for r, row in enumerate(values):
        for c, v in enumerate(row):
            sq = Square(cell, color=INK, stroke_width=2, fill_color=tint(ch, v), fill_opacity=1)
            sq.move_to([c * cell, -r * cell, 0])
            g.add(VGroup(sq, T(str(v), num_size, "#FFFFFF" if v >= 180 else INK).move_to(sq)))
    return g


def pixel_block(cell):
    """The 3 x 3 pixels in their real colours, without numbers."""
    g = VGroup()
    for r, row in enumerate(BLOCK):
        for c, px in enumerate(row):
            g.add(Square(cell, color=INK, stroke_width=2, fill_color=hexc(px), fill_opacity=1)
                  .move_to([c * cell, -r * cell, 0]))
    return g


class RGBPixels(Scene):
    def construct(self):
        cs = 0.42
        mosaic = VGroup()
        for r, row in enumerate(MOSAIC):
            for c, ch in enumerate(row):
                col = hexc(PAL[ch])
                mosaic.add(Square(cs, color=col, stroke_width=1, stroke_color="#F8F7F2",
                                  fill_color=col, fill_opacity=1).move_to([c * cs, -r * cs, 0]))
        mosaic.move_to([0, 0.3, 0])
        cap = T("Bild aus Pixeln: 16 × 14 Pixel", 26, MUTED).next_to(mosaic, DOWN, buff=0.4)
        self.play(FadeIn(mosaic), FadeIn(cap), run_time=1.2)
        self.wait(1)

        # 3x3 block (cols 7-9, rows 3-5)
        idx = [r * COLS + c for r in ROWS for c in BCOLS]
        block = VGroup(*[mosaic[i] for i in idx])
        frame = SurroundingRectangle(block, color=INK, buff=0, stroke_width=5)
        self.play(Create(frame), run_time=0.7)
        self.wait(0.6)

        # shrink the mosaic to the lower left, keep the highlighted block in view
        small = VGroup(mosaic, frame, cap)
        self.play(small.animate.scale(0.7).move_to([-3.4, -1.9, 0]), run_time=1.2)
        cell = 0.8
        zoom = pixel_block(1.0).move_to([0.3, 1.7, 0])
        zl = T("3 × 3 Pixel, vergrößert", 24, MUTED).next_to(zoom, RIGHT, buff=0.3).align_to(zoom, UP)
        line1 = DashedLine(frame.get_top(), zoom.get_corner(UL), color=INK, stroke_width=2)
        line2 = DashedLine(frame.get_right() + DOWN * 0.3, zoom.get_corner(DL), color=INK, stroke_width=2)
        self.play(FadeIn(zoom), FadeIn(zl), Create(line1), Create(line2), run_time=1.0)
        self.wait(1.5)
        gb = grid(BLUE, 2, cell, 26).move_to([-0.1, 2.3, 0])
        gg = grid(GREEN, 1, cell, 26).move_to([1.3, 1.1, 0])
        gr = grid(RED, 0, cell, 26).move_to([2.7, -0.1, 0])
        labs = []
        for g, n in [(gb, "Blau"), (gg, "Grün"), (gr, "Rot")]:
            labs.append(T(n, 26, MUTED).next_to(g, RIGHT, buff=0.25).align_to(g, UP).shift(DOWN * 0.1))
        lb, lg, lr = labs
        self.play(FadeOut(zl), run_time=0.3)
        self.play(Transform(zoom, gb), FadeIn(lb), run_time=1.0)
        self.wait(0.4)
        for g, l in [(gg, lg), (gr, lr)]:
            self.play(FadeIn(g, shift=UP * 0.4), FadeIn(l), run_time=0.9)
            self.wait(0.4)
        self.remove(line2)
        line2 = DashedLine(frame.get_right() + DOWN * 0.3, gr.get_corner(DL), color=INK, stroke_width=2)
        self.add(line2)
        self.wait(1.5)

        # one pixel: three numbers -> three bytes
        self.play(FadeOut(VGroup(zoom, gg, gr, lb, lg, lr, line1, line2, small)), run_time=0.7)
        head = T("Ein gelbes Pixel = drei Zahlen = 3 Byte = 24 Bit", 30, INK, weight=BOLD).move_to([0, 3.0, 0])
        self.play(FadeIn(head), run_time=0.5)
        data = [("Rot", 245, "11110101", CH_RED), ("Grün", 208, "11010000", CH_GREEN),
                ("Blau", 64, "01000000", CH_BLUE)]
        items = []
        for i, (n, v, bits, col) in enumerate(data):
            x = -3.8 + 3.8 * i
            sq = Square(1.1, color=INK, stroke_width=3, fill_color=col, fill_opacity=1).move_to([x, 1.2, 0])
            num = T(str(v), 40, INK, font=MONO).move_to(sq)
            lab = T(n, 26, MUTED).next_to(sq, UP, buff=0.2)
            arr = Arrow(sq.get_bottom(), [x, -0.4, 0], buff=0.1, color=INK, stroke_width=5,
                        tip_length=0.25, max_tip_length_to_length_ratio=1)
            bx = VGroup(*[Square(0.4, color=INK, stroke_width=2, fill_color="#F3F1E8", fill_opacity=1)
                          .move_to([x - 1.4 + 0.4 * k, -1.1, 0]) for k in range(8)])
            bt = VGroup(*[T(b, 26, INK, font=MONO).move_to(bx[k]) for k, b in enumerate(bits)])
            self.play(FadeIn(VGroup(sq, num, lab)), run_time=0.6)
            self.play(GrowArrow(arr), FadeIn(bx), FadeIn(bt), run_time=0.8)
            items.append(VGroup(sq, num, lab, arr, bx, bt))
            self.wait(0.5)
        full = T("11110101 11010000 01000000", 36, INK, font=MONO).move_to([0, -2.9, 0])
        self.play(FadeIn(full, shift=UP * 0.2), run_time=0.8)
        self.wait(2.5)
