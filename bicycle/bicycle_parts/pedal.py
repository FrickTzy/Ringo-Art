from .rectangle import Rectangle
from .circle import Circle
from .turtle_art import TurtleArt
from turtle import Screen, Turtle


class Pedal(TurtleArt):
    def __init__(self, *args, size: float = 1, **kwargs):
        super().__init__(*args, **kwargs)
        self.__pedal_circle = PedalCircle(screen=self.screen, pen=self.pen, size=size, pedal_position=self.position,
                                          fill_color=self.fill_color)
        self.__pedal_arm = PedalArm(screen=self.screen, pen=self.pen, size=size, position=self.position,
                                    stroke_size=self.stroke_size)
        self.__foot_rest = FootRest(screen=self.screen, pen=self.pen, size=size, pedal_position=self.position)

    def _draw_art(self) -> None:
        self.__pedal_circle.draw(fill_color=True)
        self.__pedal_arm.draw(fill_color=False)
        self.__foot_rest.draw(fill_color=True)


class PedalCircle(Circle):
    __RADIUS = 55

    def __init__(self, screen: Screen, pen: Turtle, pedal_position: tuple[int, int], size: float = 1,
                 fill_color: str = "black"):
        super().__init__(screen=screen, pen=pen, position=self.__position(pedal_position, size),
                         radius=self.__radius(size), fill_color=fill_color)

    def __position(self, pedal_position: tuple[int, int], size: float) -> tuple[int, int]:
        return pedal_position[0], pedal_position[1] - self.__radius(size)

    def __radius(self, size: float) -> int:
        return int(self.__RADIUS * size)


class PedalArm(TurtleArt):
    __PEDAL_ARM_ANGLE, __PEDAL_ARM_LENGTH = 305, 100

    def __init__(self, *args, size: float = 1, **kwargs):
        super().__init__(*args, **kwargs)
        self.__size = size

    def _draw_art(self) -> None:
        self._go_to_position()
        self.pen.setheading(self.__PEDAL_ARM_ANGLE)
        self.pen.forward(self.__PEDAL_ARM_LENGTH * self.__size)
        self.pen.setheading(0)


class FootRest(Rectangle):
    __FOOT_REST_WIDTH, __FOOT_REST_HEIGHT = 60, 15
    __FOOT_REST_X, __FOOT_REST_Y = 26, -80

    def __init__(self, screen: Screen, pen: Turtle, pedal_position: tuple[int, int], size: float = 1):
        super().__init__(screen=screen, pen=pen, width=self.__width(size), height=self.__height(size),
                         position=self.__position(size, pedal_position))

    def __width(self, size: float) -> int:
        return int(self.__FOOT_REST_WIDTH * size)

    def __height(self, size: float) -> int:
        return int(self.__FOOT_REST_HEIGHT * size)

    def __position(self, size: float, pedal_position: tuple[int, int]) -> tuple[int, int]:
        pedal_x, pedal_y = pedal_position
        return int(self.__FOOT_REST_X * size) + pedal_x, int(self.__FOOT_REST_Y * size) + pedal_y


def main() -> None:
    screen = Screen()
    screen.bgcolor("white")
    pen = Turtle()
    pen.speed(5)
    Pedal(screen=screen, pen=pen, stroke_size=12, fill_color="yellow", size=1, position=(100, 0)).draw(fill_color=False)
    pen.hideturtle()
    screen.exitonclick()


if __name__ == '__main__':
    main()