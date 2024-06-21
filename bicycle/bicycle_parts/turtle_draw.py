from turtle import Screen, Turtle


class TurtleDraw:
    def __init__(self, screen: Screen, pen: Turtle, stroke_size: int = 5, color: str = "black"):
        self.pen = pen
        self.screen = screen
        self.stroke_size = stroke_size
        self.color = color

    def _set_pen_stroke(self):
        self.pen.pensize(self.stroke_size)