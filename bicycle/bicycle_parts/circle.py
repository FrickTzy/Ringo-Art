from .turtle_art import TurtleArt
from turtle import Screen, Turtle


class Circle(TurtleArt):
    def __init__(self, screen: Screen, pen: Turtle, radius: int, stroke_size: int = 5,
                 color: str = "black", position: tuple[int, int] = (0, 0), fill_color: str = "black"):
        super().__init__(screen=screen, pen=pen, position=position, color=color, stroke_size=stroke_size,
                         fill_color=fill_color)
        self.radius = radius

    def _draw_art(self) -> None:
        self._go_to_position()
        self.pen.circle(self.radius)

