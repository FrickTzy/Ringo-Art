from .turtle_draw import TurtleDraw


class Tube(TurtleDraw):
    def draw(self, starting_position: tuple[int, int], target_position: tuple[int, int]) -> None:
        self._set_pen_stroke()
        self.pen.penup()
        self.pen.goto(starting_position)
        self.pen.pendown()
        self.pen.goto(target_position)
        self.pen.penup()