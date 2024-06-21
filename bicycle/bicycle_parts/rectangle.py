from .turtle_art import TurtleArt


class Rectangle(TurtleArt):
    def __init__(self, *args, width: int = 100, height: int = 35, **kwargs):
        super().__init__(*args, **kwargs)
        self.width = width
        self.height = height

    def _draw_art(self) -> None:
        self._go_to_position()
        for _ in range(2):
            self.pen.forward(self.width)
            self.pen.right(90)
            self.pen.forward(self.height)
            self.pen.right(90)
