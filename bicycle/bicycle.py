from .bicycle_parts import Tube, BikeSeat, BikeWheel, BikeHandle, Pedal
from turtle import Screen, Turtle


class Bicycle:
    def __init__(self, screen: Screen, pen: Turtle, position: tuple[int, int] = (0, 0)):
        self.__x, self.__y = position
        self.__tube = Tube(screen=screen, pen=pen, stroke_size=12)
        self.__left_wheel = BikeWheel(
            spoke_size=3, screen=screen, pen=pen, stroke_size=12, radius=120,
            position=(self.__x - 210, self.__y - 150)
        )
        self.__right_wheel = BikeWheel(
            spoke_size=3, screen=screen, pen=pen, stroke_size=12, radius=120,
            position=(self.__x + 190, self.__y - 150)
        )
        self.__handle = BikeHandle(
            screen=screen, pen=pen, size=0.49, fill_color="red", stroke_size=3,
            position=(self.__x + 52, self.__y + 224)
        )
        self.__seat = BikeSeat(
            screen=screen, pen=pen, stroke_size=3, fill_color="red",
            size=1, position=(self.__x - 60, self.__y + 180)
        )
        self.__pedal = Pedal(
            screen=screen, pen=pen, stroke_size=12, fill_color="red",
            size=0.6, position=(self.__x - 10, self.__y - 30)
        )

    def draw(self) -> None:
        self.__left_wheel.draw()
        self.__draw_tubes()
        self.__pedal.draw()
        self.__right_wheel.draw()
        self.__tube.draw(starting_position=(self.__x + 190, self.__y - 30), target_position=(self.__x + 103, self.__y + 220))
        self.__handle.draw(fill_color=True)
        self.__seat.draw(fill_color=True)

    def __draw_tubes(self) -> None:
        tube_positions = [
            ((self.__x - 210, self.__y - 30), (self.__x - 110, self.__y + 140)),
            ((self.__x - 110, self.__y + 140), (self.__x + 125, self.__y + 140)),
            ((self.__x + 125, self.__y + 140), (self.__x - 10, self.__y - 30)),
            ((self.__x - 10, self.__y - 30), (self.__x - 200, self.__y - 30)),
            ((self.__x - 130, self.__y + 180), (self.__x + 0, self.__y - 30))
        ]
        for start, end in tube_positions:
            self.__tube.draw(starting_position=start, target_position=end)
