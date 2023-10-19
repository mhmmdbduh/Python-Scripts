from manim import *

class pith(Scene):
    def construct(self):
        sq = Square(side_length=5,fill_opacity=0.5, fill_color=BLUE, stroke_color = GREEN)
        self.play(Create(sq), run_time=3)
        self.wait()