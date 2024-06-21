import turtle
from .turtle_art import TurtleArt


class Seat(TurtleArt):
    __HYPOTENUSE_ANGLE, __HYPOTENUSE_LENGTH = 158, 90
    __ADJACENT_ANGLE, __ADJACENT_LENGTH = 80, 40
    __OPPOSITE_ANGLE, __OPPOSITE_LENGTH = 122, 105
    __ADDITIONAL_ANGLE = 17

    def __init__(self, screen: turtle.Screen, pen: turtle.Turtle, stroke_size: int,
                 color: str = "black", position: tuple[int, int] = (0, 0), size: float = 1, fill_color: str = "black"):
        super().__init__(screen=screen, pen=pen, position=position, color=color, stroke_size=stroke_size,
                         fill_color=fill_color)
        self.__size = size

    def _draw_art(self) -> None:
        self._go_to_position()
        self.pen.setheading(self.__HYPOTENUSE_ANGLE)
        self.pen.left(self.__ADDITIONAL_ANGLE)
        self.pen.forward(self.__get_hypotenuse_length)
        self.pen.left(self.__ADJACENT_ANGLE)
        self.pen.forward(self.__get_adjacent_length)
        self.pen.left(self.__OPPOSITE_ANGLE)
        self.pen.forward(self.__get_opposite_length)

    @property
    def __get_hypotenuse_length(self) -> int:
        return int(self.__HYPOTENUSE_LENGTH * self.__size)

    @property
    def __get_adjacent_length(self) -> int:
        return int(self.__ADJACENT_LENGTH * self.__size)

    @property
    def __get_opposite_length(self) -> int:
        return int(self.__OPPOSITE_LENGTH * self.__size)
    

def main() -> None:
    screen = turtle.Screen()
    screen.bgcolor("white")
    pen = turtle.Turtle()
    pen.speed(5)
    Seat(screen=screen, pen=pen, stroke_size=3, fill_color="yellow", size=4).draw(fill_color=True)
    pen.hideturtle()
    screen.exitonclick()


if __name__ == '__main__':
    main()
