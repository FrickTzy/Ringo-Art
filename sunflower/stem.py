from turtle import Turtle, Screen, done
from turtle_art_manager import TurtleArt


class Stem(TurtleArt):
    __LENGTH = 15
    __TOP, __BOTTOM = 15, 20

    def __init__(self, *args, size: float = 1, angle_range: int = 25, **kwargs):
        super().__init__(*args, **kwargs)
        self.__size = size
        self.__angle_range = angle_range

    def _draw_art(self) -> None:
        self._go_to_position()
        self._pen.pendown()
        self._pen.color("black", "green")
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
    def __length(self) -> float:
        return self.__LENGTH * self.__size

    @property
    def __top(self) -> float:
        return self.__TOP * self.__size

    @property
    def __bottom(self) -> float:
        return self.__BOTTOM * self.__size


screen = Screen()
screen.bgcolor("sky blue")

pen = Turtle()
pen.shape("turtle")
pen.color("black")
pen.speed(10)

stem_length = 250
stem_curve_radius = 30
Stem(pen=pen, screen=screen, fill_color="green", position=(0, -250), size=1.5).draw()

pen.hideturtle()
done()
