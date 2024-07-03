from turtle import Screen, Turtle, mainloop
from math import sqrt
from turtle_art_manager import SizedTurtleArt
from leaf import LeafArt
from stem import StemArt
from copy import copy


def set_position(screen: Screen) -> None:
    screen.cv._rootwindow.geometry("+270+150")


class Sunflower(SizedTurtleArt):
    __PETAL_NUM = 10
    __PETAL_RADIUS = 80
    __NUMBER_OF_SEEDS = 100
    __OUTER_CENTER_SIZE, __INNER_CENTER_SIZE = 30, 20

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        leaf_kwargs = self.__leaf_kwargs(kwargs=kwargs)
        self.__left_leaf = LeafArt(*args, on_left_side=True, **self.__left_leaf_kwargs(leaf_kwargs=leaf_kwargs))
        self.__right_leaf = LeafArt(*args, on_left_side=False, **self.__right_leaf_kwargs(leaf_kwargs=leaf_kwargs))
        self.__stem = StemArt(*args, **self.__stem_kwargs(kwargs=kwargs))

    def __leaf_kwargs(self, kwargs: dict):
        leaf_kwargs = copy(kwargs)
        leaf_kwargs["fill_color"] = "#6cc73b"
        leaf_kwargs["size"] = 0.35 * self._size
        return leaf_kwargs

    def __right_leaf_kwargs(self, leaf_kwargs: dict):
        right_leaf_kwargs = copy(leaf_kwargs)
        right_leaf_kwargs["position"] = self._get_position(position=(50, -215))
        return right_leaf_kwargs

    def __left_leaf_kwargs(self, leaf_kwargs: dict):
        left_leaf_kwargs = copy(leaf_kwargs)
        left_leaf_kwargs["position"] = self._get_position(position=(30, -197))
        return left_leaf_kwargs

    def __stem_kwargs(self, kwargs: dict):
        stem_kwargs = copy(kwargs)
        stem_kwargs["position"] = self._get_position(position=(30, -300))
        stem_kwargs["fill_color"] = "#3f9c03"
        stem_kwargs["size"] = 0.8 * self._size
        return stem_kwargs

    def _draw_art(self) -> None:
        self._pen.speed(11)
        self.__left_leaf.draw(fill_color=False)
        self.__right_leaf.draw(fill_color=False)
        self.__stem.draw(fill_color=False)
        self._go_to_position()
        self._pen.speed(10)
        self.__draw_petals()
        self.__draw_center()

    def __draw_petals(self) -> None:
        for _ in range(self.__PETAL_NUM):
            self._pen.pendown()
            self._pen.fillcolor("#ffe554")
            self.__draw_petal()
            self._pen.left(360 / self.__PETAL_NUM)

    def __draw_petal(self) -> None:
        self._pen.begin_fill()
        for _ in range(2):
            self._pen.circle(self._get_size(self.__PETAL_RADIUS), 90)
            self._pen.left(90)
        self._pen.end_fill()
        self._pen.left(25)
        self._pen.circle(self._get_size(113), 40)
        self._pen.left(180)
        self._pen.circle(self._get_size(-113), 40)
        self._pen.right(205)

    def __draw_center_seeds(self) -> None:
        angle = 137.5
        self._pen.penup()
        for i in range(self.__NUMBER_OF_SEEDS):
            distance = sqrt(i + 1) * 3
            self._pen.goto(0, 0)
            self._pen.setheading(angle * i)
            self._pen.forward(distance)
            self._pen.dot(5, "brown")
        self._pen.pendown()

    def __draw_center(self) -> None:
        self._pen.color("black")
        self.__draw_outer_center()
        self.__draw_inner_center()

    def __draw_inner_center(self) -> None:
        self._go_to(self._get_position((0, 20)))
        self._pen.fillcolor("#9a5915")
        self._pen.begin_fill()
        self._pen.circle(self._get_size(self.__INNER_CENTER_SIZE))
        self._pen.end_fill()

    def __draw_outer_center(self) -> None:
        self._pen.fillcolor("#db8d2b")
        self._pen.begin_fill()
        self._go_to(self._get_position((0, 30)))
        self._pen.circle(self._get_size(self.__OUTER_CENTER_SIZE))
        self._pen.end_fill()


def main() -> None:
    screen = Screen()
    screen.bgcolor("#67b9ea")
    set_position(screen=screen)
    screen.title("Sunflower Art  |  @kurikosancode")
    pen = Turtle()
    pen.color("black")
    Sunflower(pen=pen, screen=screen, stroke_size=5, size=1.5, position=(0, 50)).draw(fill_color=False)
    pen.hideturtle()
    mainloop()


if __name__ == '__main__':
    main()
