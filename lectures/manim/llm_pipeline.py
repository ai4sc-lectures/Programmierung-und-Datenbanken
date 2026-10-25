"""Manim scene for the slide "Ein Sprachmodell bildet Token-Folgen auf Wahrscheinlichkeiten ab"
(03d_AgentischesProgrammieren.qmdx).

Animates llm_words.svg: the words of a sentence become numbers, run through the neural network,
the next word comes out, it is appended to the sentence, the window moves one word on and
everything starts again. Numbers are illustrative.
Palette: light "pastello" theme (_extensions/ai4sc-style/themes/color/pastello.css).

Render, from the lectures/ directory:

    manim/render.sh manim/llm_pipeline.py LLMPipeline 1200,660 images/03d_AgentischesProgrammieren/manim_llm_pipeline.mp4
"""
from manim import *

config.frame_height = 6.6
config.frame_width = 12
config.background_color = "#F8F7F2"

INK = "#302F2B"
MUTED = "#68665E"
RIM = "#B9B5A6"
LINE = "#DAD7CB"
BLUE = "#91B5CB"
RED = "#C58E89"
YELLOW = "#D6B65E"
BUBBLE = "#F3F1E8"
PAPER = "#F8F7F2"
FONT = "Helvetica Neue"
MONO = "Menlo"

SENTENCE = ["Rostock", "ist", "eine", "schöne", "Stadt."]
GENERATED = ["Sie", "liegt", "an", "der", "Ostsee."]
IDS = {"Rostock": 5412, "ist": 318, "eine": 287, "schöne": 9055, "Stadt.": 2201,
       "Sie": 2764, "liegt": 4590, "an": 331, "der": 262, "Ostsee.": 18823}

ROWS = [1.5, 0.75, 0.0, -0.75, -1.5]
X_BOX, X_IN, X_H1, X_H2, X_OUT, X_RES = -5.0, -2.5, -0.7, 1.1, 2.9, 5.0
Y_TEXT, Y_TRAVEL = 2.85, -2.3


def T(text, size=24, color=INK, font=FONT, **kw):
    return Text(text, font=font, font_size=size * 2, color=color, **kw).scale(0.5)


def word_box(word, y, with_number=False):
    rect = RoundedRectangle(corner_radius=0.08, width=1.9, height=0.62, color=INK, stroke_width=2.5,
                            fill_color=BUBBLE, fill_opacity=1).move_to([X_BOX, y, 0])
    w = T(word, 18, INK).move_to([X_BOX, y + 0.1, 0])
    n = T(str(IDS[word]), 11, MUTED, font=MONO).move_to([X_BOX, y - 0.18, 0])
    if not with_number:
        n.set_opacity(0)
    return {"rect": rect, "word": w, "num": n, "grp": VGroup(rect, w, n)}


class LLMPipeline(Scene):
    def construct(self):
        # ---- network (as in llm_words.svg) -----------------------------------------------
        def layer(x, ys, fill, stroke):
            return [Circle(0.17, color=stroke, stroke_width=3 if stroke != BLUE else 0, fill_color=fill,
                           fill_opacity=1).move_to([x, y, 0]) for y in ys]

        l_in = layer(X_IN, ROWS, BUBBLE, INK)
        l_h1 = layer(X_H1, ROWS, BLUE, BLUE)
        l_h2 = layer(X_H2, ROWS, BLUE, BLUE)
        l_out = layer(X_OUT, [0.75, 0.0, -0.75], BUBBLE, INK)
        layers = [l_in, l_h1, l_h2, l_out]
        base_fill = [BUBBLE, BLUE, BLUE, BUBBLE]
        edges = VGroup()
        for a, b in zip(layers[:-1], layers[1:]):
            for na in a:
                for nb in b:
                    edges.add(Line(na.get_center(), nb.get_center(), color=LINE, stroke_width=1))
        res_box = RoundedRectangle(corner_radius=0.1, width=1.9, height=0.9, color=RED, stroke_width=3,
                                   fill_color=BUBBLE, fill_opacity=1).move_to([X_RES, 0, 0])
        res_lab = T("Nächstes Wort", 18, INK, weight=BOLD).move_to([X_RES, 0.7, 0])
        res_arrow = Arrow([X_OUT + 0.2, 0, 0], [X_RES - 0.97, 0, 0], buff=0, color=RED, stroke_width=4,
                          tip_length=0.2, max_tip_length_to_length_ratio=1, max_stroke_width_to_length_ratio=100)
        net = VGroup(edges, *[VGroup(*l) for l in layers])

        # ---- text line and input window ----------------------------------------------------
        text_words = [T(w, 24, INK) for w in SENTENCE]
        row = VGroup(*text_words).arrange(RIGHT, buff=0.18).move_to([-5.8, Y_TEXT, 0], aligned_edge=LEFT)
        text_hl = []

        boxes = [word_box(w, y) for w, y in zip(SENTENCE, ROWS)]
        in_lines = [Line([X_BOX + 0.95, y, 0], [X_IN - 0.17, y, 0], color=INK, stroke_width=1.5) for y in ROWS]

        cap = None

        def caption(title, line=""):
            nonlocal cap
            g = VGroup(T(title, 22, INK, weight=BOLD), *([T(line, 17, MUTED)] if line else []))
            g.arrange(DOWN, aligned_edge=LEFT, buff=0.08).move_to([-5.8, -3.0, 0], aligned_edge=LEFT)
            self.play(*([FadeOut(cap)] if cap else []), FadeIn(g), run_time=0.35)
            cap = g

        caption("Der Satz", "Eine Zeichenfolge aus Wörtern.")
        self.play(FadeIn(row), run_time=0.8)
        self.wait(0.8)
        self.play(FadeIn(net), *[FadeIn(l) for l in in_lines], *[FadeIn(b["grp"]) for b in boxes],
                  FadeIn(res_box), FadeIn(res_lab), run_time=1.2)
        self.wait(0.6)
        res_txt = None

        def pulse(detailed):
            """Signals run from the input words through the layers to the output."""
            t = 0.55 if detailed else 0.25
            dots = [Dot(color=YELLOW, radius=0.09).move_to([X_BOX + 0.95, y, 0]) for y in ROWS]
            self.add(*dots)
            self.play(*[d.animate.move_to([X_IN, d.get_center()[1], 0]) for d in dots], run_time=t)
            self.remove(*dots)
            for k, lay in enumerate(layers):
                self.play(*[n.animate.set_fill(YELLOW, opacity=0.95) for n in lay], run_time=t)
            self.play(l_out[1].animate.set_fill(RED, opacity=0.9), *[
                n.animate.set_fill(base_fill[0], opacity=1) for n in l_out if n is not l_out[1]], run_time=t)
            self.play(*[n.animate.set_fill(base_fill[k], opacity=1) for k, lay in enumerate(layers[:-1]) for n in lay],
                      run_time=t)

        for step, new_word in enumerate(GENERATED):
            detailed = step == 0
            words = [b["word"].text for b in boxes]
            # 1 words -> numbers
            if detailed:
                caption("Wörter werden Zahlen", "Jedes Wort hat eine Nummer im Vokabular.")
                self.play(*[b["num"].animate.set_opacity(1) for b in boxes], run_time=1.0)
                self.wait(0.8)
                caption("Die Zahlen laufen durch das Netzwerk", "Schicht für Schicht entsteht eine Vorhersage.")
            pulse(detailed)
            # 2 output
            if detailed:
                caption("Das nächste Wort kommt heraus", "Zuerst als Zahl, dann als Wort.")
            self.play(GrowArrow(res_arrow), run_time=0.4 if detailed else 0.2)
            num = T(str(IDS[new_word]), 18, INK, font=MONO).move_to(res_box)
            self.play(FadeIn(num), run_time=0.4 if detailed else 0.2)
            if detailed:
                self.wait(0.5)
            word = T(new_word, 20, INK, weight=BOLD).move_to(res_box)
            self.play(Transform(num, word), run_time=0.5 if detailed else 0.25)
            # 3 append to the text and move the window on by one word
            if detailed:
                caption("Das Wort wird angehängt", "Der Satz springt ein Wort weiter, dann beginnt es von vorn.")
            hl = Rectangle(width=0.1, height=0.1)  # placeholder to keep types simple
            new_text = T(new_word, 24, INK).next_to(row, RIGHT, buff=0.18)
            new_hl = SurroundingRectangle(new_text, color=YELLOW, buff=0.06, stroke_width=0, fill_color=YELLOW,
                                          fill_opacity=0.45)
            nb = word_box(new_word, ROWS[-1], with_number=True)
            nb["grp"].move_to([X_BOX, ROWS[-1], 0])
            nb["grp"].move_to([X_RES, 0, 0])
            nb_start = nb["grp"].copy()
            copy = word.copy()
            self.play(FadeOut(res_arrow), FadeIn(new_hl), FadeIn(new_text), run_time=0.4 if detailed else 0.2)
            path = VMobject().set_points_as_corners([[X_RES, 0, 0], [X_RES, Y_TRAVEL, 0], [X_BOX, Y_TRAVEL, 0],
                                                    [X_BOX, ROWS[-1], 0]])
            self.play(FadeOut(num), FadeIn(nb["grp"]), run_time=0.15)
            slide = [b["grp"].animate.shift(UP * 0.75) for b in boxes[1:]]
            self.play(MoveAlongPath(nb["grp"], path), *slide, boxes[0]["grp"].animate.shift(UP * 0.75).set_opacity(0),
                      run_time=1.2 if detailed else 0.6, rate_func=smooth)
            self.remove(boxes[0]["grp"])
            boxes = boxes[1:] + [nb]
            row = VGroup(*row, new_text)
            text_hl.append(new_hl)
            self.wait(0.4 if detailed else 0.1)

        caption("Das Ergebnis", "Ein Text, Wort für Wort erzeugt.")
        self.wait(3)
