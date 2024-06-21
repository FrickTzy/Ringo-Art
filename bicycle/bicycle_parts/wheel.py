import turtle
from .circle import Circle


class Wheel(Circle):
    def __init__(self, *args, spoke_size: int, **kwargs):
        super().__init__(*args, **kwargs)
        self.__spoke_size = spoke_size

    def draw(self, fill_color: bool = False):
        super().draw(fill_color=fill_color)
        self.__draw_spokes(num_spokes=20)

    def __draw_spokes(self, num_spokes: int):
        self.pen.pensize(self.__spoke_size)
        for _ in range(num_spokes):
            self._go_to((self.position[0], self.position[1] + self.radius))
            self.pen.forward(self.radius)
            self.pen.backward(self.radius)
            self.pen.right(360 / num_spokes)


def main() -> None:
    screen = turtle.Screen()
    screen.bgcolor("white")
    pen = turtle.Turtle()
    pen.speed(10)
    Wheel(spoke_size=3, screen=screen, pen=pen, stroke_size=10, radius=120, position=(-200, 0)).draw()
    Wheel(spoke_size=3, screen=screen, pen=pen, stroke_size=10, radius=120, position=(200, 0)).draw()
    pen.hideturtle()

    screen.exitonclick()


if __name__ == '__main__':
    main()
