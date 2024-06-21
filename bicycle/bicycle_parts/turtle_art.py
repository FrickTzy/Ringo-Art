from turtle import Screen, Turtle
from .turtle_draw import TurtleDraw
from abc import ABC, abstractmethod


class TurtleArt(ABC, TurtleDraw):
    def __init__(self, screen: Screen, pen: Turtle, position: tuple[int, int] = (0, 0),
                 stroke_size: int = 5, color: str = "black", fill_color: str = "black"):
        super().__init__(screen=screen, pen=pen, stroke_size=stroke_size, color=color)
        self.pen = pen
        self.screen = screen
        self.position = position
        self.stroke_size = stroke_size
        self.color = color
        self.fill_color = fill_color

    def _go_to_position(self):
        self._go_to(self.position)

    def _go_to(self, position: tuple[int, int]):
        self.pen.penup()
        self.pen.goto(position)
        self.pen.pendown()

    def _draw_to(self, position: tuple[int, int]):
        self.pen.pendown()
        self.pen.goto(position)
        self.pen.penup()

    def draw(self, fill_color: bool = False):
        if fill_color:
            self.pen.fillcolor(self.fill_color)
            self.pen.begin_fill()
        self._set_pen_stroke()
        self._draw_art()
        self.pen.end_fill()

    @abstractmethod
    def _draw_art(self) -> None:
        pass
