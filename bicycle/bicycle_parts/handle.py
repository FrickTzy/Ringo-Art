import turtle
from .rectangle import Rectangle


class BikeHandle(Rectangle):
    __WIDTH = 100
    __HEIGHT = 30

    def __init__(self, *args, size: float = 1, **kwargs):
        super().__init__(*args, width=self.__width(size=size), height=self.__height(size=size), **kwargs)

    def __width(self, size: float) -> int:
        return int(self.__WIDTH * size)

    def __height(self, size: float) -> int:
        return int(self.__HEIGHT * size)


def main() -> None:
    screen = turtle.Screen()
    screen.bgcolor("white")
    pen = turtle.Turtle()
    BikeHandle(screen=screen, pen=pen, size=1.2, color="blue", stroke_size=5).draw(fill_color=True)
    pen.hideturtle()
    screen.exitonclick()


if __name__ == '__main__':
    main()
