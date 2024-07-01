from turtle import Turtle, Screen, mainloop
from turtle_art_manager import TurtleArt


class LeafArt(TurtleArt):
    def __init__(self, *args, size: float = 1, **kwargs):
        super().__init__(*args, **kwargs)
        self.__size = size

    def __draw_leaf(self) -> None:
        self._set_pen_stroke()
        self._pen.fillcolor(self._fill_color)
        self._pen.begin_fill()
        self._pen.setheading(105)
        self._pen.circle(240 * self.__size, 27)
        self._pen.setheading(190)
        self._pen.forward(40 * self.__size)
        self._pen.circle(-179 * self.__size, 55)
        self._pen.forward(120 * self.__size)
        self._pen.circle(18 * self.__size, 50)
        self._pen.setheading(10)
        self._pen.forward(120 * self.__size)
        self._pen.circle(-166 * self.__size, 88)
        self._pen.setheading(310)
        self._pen.circle(-220 * self.__size, 35)
        self._pen.setheading(190)
        self._pen.forward(10 * self.__size)
        self._pen.end_fill()
        self._go_to(self.__get_position((-350, 230)))
        self._pen.setheading(7)
        self._pen.circle(-350 * self.__size, 53)
        self._go_to(self.__get_position((-180, 208)))
        self._pen.setheading(185)
        self._pen.circle(-450 * self.__size, 10)
        self._go_to(self.__get_position((-155, 200)))
        self._pen.setheading(110)
        self._pen.circle(280 * self.__size, 10)
        self._go_to(self.__get_position((-110, 170)))
        self._pen.setheading(195)
        self._pen.circle(-250 * self.__size, 30)

    def __get_position(self, position: tuple[int, int]) -> tuple[int, int]:
        return self._position[0] + int(position[0] * self.__size), self._position[1] + int(position[1] * self.__size)

    def _draw_art(self) -> None:
        self._go_to_position()
        self.__draw_leaf()


def main() -> None:
    screen = Screen()
    screen.title("Heart Art  |  @kurikosancode")
    pen = Turtle()
    heart = LeafArt(pen=pen, screen=screen, position=(100, 100), fill_color="green", size=0.7)
    heart.draw()
    mainloop()


if __name__ == "__main__":
    main()
