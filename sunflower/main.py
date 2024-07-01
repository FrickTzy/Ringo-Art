import turtle
import math
from turtle_art_manager import SizedTurtleArt


class Sunflower(SizedTurtleArt):
    __PETAL_NUM = 10
    __PETAL_RADIUS = 80
    __NUMBER_OF_SEEDS = 100

    def _draw_art(self) -> None:
        self.__draw_petals()
        self.__draw_center()

    def __draw_petals(self) -> None:
        for _ in range(self.__PETAL_NUM):
            self._pen.pendown()
            self._pen.fillcolor("yellow")
            self._pen.begin_fill()
            self.__draw_petal()
            self._pen.end_fill()
            self._pen.left(360 / self.__PETAL_NUM)

    def __draw_petal(self) -> None:
        for _ in range(2):
            self._pen.circle(self._get_size(self.__PETAL_RADIUS), 90)
            self._pen.left(90)

    def __draw_center_seeds(self) -> None:
        angle = 137.5
        self._pen.penup()
        for i in range(self.__NUMBER_OF_SEEDS):
            distance = math.sqrt(i + 1) * 3
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
        self._go_to(self._get_position((0, -20)))
        self._pen.fillcolor("brown")
        self._pen.begin_fill()
        self._pen.circle(self._get_size(20))
        self._pen.end_fill()

    def __draw_outer_center(self) -> None:
        self._pen.fillcolor("dark orange")
        self._pen.begin_fill()
        self._go_to(self._get_position((0, -30)))
        self._pen.circle(self._get_size(30))
        self._pen.end_fill()


def main() -> None:
    screen = turtle.Screen()
    screen.bgcolor("sky blue")
    pen = turtle.Turtle()
    pen.color("black")
    pen.speed(20)
    pen.pensize(10)
    Sunflower(pen=pen, screen=screen, stroke_size=5, size=1.5).draw(fill_color=False)
    pen.hideturtle()
    turtle.done()


if __name__ == '__main__':
    main()
