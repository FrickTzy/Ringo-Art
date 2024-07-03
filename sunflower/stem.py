from turtle import Turtle, Screen, done
from turtle_art_manager import SizedTurtleArt


class StemArt(SizedTurtleArt):
    __LENGTH = 15
    __TOP, __BOTTOM = 15, 20

    def __init__(self, *args, angle_range: int = 25, **kwargs):
        super().__init__(*args, **kwargs)
        self.__angle_range = angle_range

    def _draw_art(self) -> None:
        self._go_to_position()
        self._pen.pendown()
        self._pen.color("black", self._fill_color)
        self._pen.setheading(85)
        self._pen.begin_fill()
        for _ in range(self.__angle_range):
            self._pen.forward(self.__length)
            self._pen.left(1)
        self._pen.setheading(0)
        self._pen.forward(self.__top)
        self._pen.setheading(290)
        for _ in range(self.__angle_range):
            self._pen.forward(self.__length)
            self._pen.right(1)
        self._pen.setheading(185)
        self._pen.forward(self.__bottom)
        self._pen.end_fill()

    @property
    def __length(self) -> int:
        return self._get_size(size=self.__LENGTH)

    @property
    def __top(self) -> int:
        return self._get_size(size=self.__TOP)

    @property
    def __bottom(self) -> int:
        return self._get_size(size=self.__BOTTOM)


def main() -> None:
    screen = Screen()
    screen.bgcolor("sky blue")

    pen = Turtle()
    pen.shape("turtle")
    pen.color("black")
    pen.speed(10)

    StemArt(pen=pen, screen=screen, fill_color="green", position=(0, -250), size=1.5).draw()

    pen.hideturtle()
    done()


if __name__ == '__main__':
    main()