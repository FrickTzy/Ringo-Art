from turtle import Turtle, Screen, mainloop
from turtle_art_manager import SizedTurtleArt


class LeafArt(SizedTurtleArt):
    def __init__(self, *args, on_left_side: bool = True, **kwargs):
        super().__init__(*args, **kwargs)
        self.__on_left_side = on_left_side

    def __draw_left_leaf(self) -> None:
        self._pen.begin_fill()
        self._pen.setheading(105)
        self._pen.circle(self._get_size(size=240), 27)
        self._pen.setheading(190)
        self._pen.forward(self._get_size(40))
        self._pen.circle(self._get_size(-179), 55)
        self._pen.forward(self._get_size(120))
        self._pen.circle(self._get_size(18), 50)

        self._pen.setheading(10)
        self._pen.forward(self._get_size(120))
        self._pen.circle(self._get_size(-166), 88)
        self._pen.setheading(310)
        self._pen.circle(self._get_size(-220), 35)
        self._pen.setheading(190)
        self._pen.forward(self._get_size(10))
        self._pen.end_fill()
        self._go_to(self._get_position((-350, 230)))
        self._pen.setheading(7)
        self._pen.circle(self._get_size(-350), 53)

        self._go_to(self._get_position((-180, 208)))
        self._pen.setheading(185)
        self._pen.circle(self._get_size(-450), 10)

        self._go_to(self._get_position((-155, 200)))
        self._pen.setheading(110)
        self._pen.circle(self._get_size(280), 10)

        self._go_to(self._get_position((-110, 170)))
        self._pen.setheading(195)
        self._pen.circle(self._get_size(-250), 30)

    def __draw_right_leaf(self) -> None:
        self._pen.begin_fill()
        self._pen.setheading(75)
        self._pen.circle(self._get_size(size=-240), 27)
        self._pen.setheading(350)
        self._pen.forward(self._get_size(40))
        self._pen.circle(self._get_size(179), 55)
        self._pen.forward(self._get_size(120))
        self._pen.circle(self._get_size(-18), 50)

        self._pen.setheading(170)
        self._pen.forward(self._get_size(120))
        self._pen.circle(self._get_size(166), 88)

        self._pen.setheading(230)
        self._pen.circle(self._get_size(220), 35)
        self._pen.setheading(10)
        self._pen.forward(self._get_size(10))
        self._pen.end_fill()

        self._go_to(self._get_position((350, 230)))
        self._pen.setheading(173)
        self._pen.circle(self._get_size(350), 53)

        self._go_to(self._get_position((155, 200)))
        self._pen.setheading(70)
        self._pen.circle(self._get_size(-280), 10)

        self._go_to(self._get_position((110, 170)))
        self._pen.setheading(345)
        self._pen.circle(self._get_size(250), 30)

    def _draw_art(self) -> None:
        self._go_to_position()
        self._set_pen_stroke()
        self._pen.fillcolor(self._fill_color)
        if self.__on_left_side:
            self.__draw_left_leaf()
        else:
            self.__draw_right_leaf()


def main() -> None:
    screen = Screen()
    screen.title("Heart Art  |  @kurikosancode")
    pen = Turtle()
    heart = LeafArt(pen=pen, screen=screen, position=(100, 100), fill_color="green", size=1)
    heart.draw()
    mainloop()


if __name__ == "__main__":
    main()
