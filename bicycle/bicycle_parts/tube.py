from turtle_art_manager import TurtleDraw


class Tube(TurtleDraw):
    def draw(self, starting_position: tuple[int, int], target_position: tuple[int, int]) -> None:
        self._set_pen_stroke()
        self._pen.penup()
        self._pen.goto(starting_position)
        self._pen.pendown()
        self._pen.goto(target_position)
        self._pen.penup()