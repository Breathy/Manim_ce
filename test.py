from manim import *
import numpy as np

config["background_color"]=GREY
class Test(Scene):
	def construct(self):


		ci=Circle(stroke_color= YELLOW_D, fill_color=BLUE_B, radius=2, stroke_width=5, fill_opacity=0.8).to_edge(UL)
		equ=TexMobject("{2}+ {3}")


		equ.next_to(ci, DOWN, buff=0.5, aligned_edge=LEFT)
		num= TexMobject("ln(2)=0.69").scale(2).next_to(equ,DOWN,buff=0.1)
		self.play(DrawBorderThenFill(ci))
		self.play(Write(equ))
		self.play(ci.animate.shift(RIGHT*3), run_time=4)
		self.play(Write(num))