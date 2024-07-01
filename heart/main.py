from turtle import Screen, Turtle, register_shape, mainloop
from time import sleep


def set_position(screen: Screen) -> None:
    screen.cv._rootwindow.geometry("+270+150")


def draw_heart_shape():
    points = ((0.00, 0.00), (-11.49, 9.64), (-13.51, 12.45), (-13.94, 15.87), (-12.67, 19.09), (-10.03, 21.31),
              (-6.64, 22.00), (-3.34, 20.98), (-0.93, 18.50), (1.48, 20.98), (4.78, 22.00), (8.17, 21.31),
              (10.82, 19.09), (12.08, 15.87), (11.65, 12.45), (9.63, 9.64), (-1.86, -0.00))
    return points


class HeartArt:
    def __init__(self, pen: Turtle, message: str):
        self.__pen = pen
        self.__message = message
        register_shape("heart", draw_heart_shape())
        self.__setup_pen()

    def __setup_pen(self) -> None:
        self.__pen.color("red", "pink")
        self.__pen.shape("heart")
        self.__pen.pensize(15)
        self.__pen.speed(2)

    def __draw_heart(self) -> None:
        self.__pen.begin_fill()
        self.__pen.left(140)
        self.__pen.forward(352)
        self.__pen.circle(-179, 200)
        sleep(0.28)
        self.__pen.left(120)
        self.__pen.circle(-179, 200)
        self.__pen.forward(352)
        self.__pen.end_fill()

    def __write_message(self) -> None:
        self.__pen.penup()
        self.__pen.setheading(90)
        self.__pen.color("pink", "red")
        self.__pen.goto(0, 40)
        self.__pen.color("red", "pink")
        self.__pen.write(self.__message, align="center", font=("Arial", 50, "bold"))
        self.__pen.hideturtle()

    def draw(self) -> None:
        self.__pen.penup()
        self.__pen.goto(0, -230)
        self.__pen.pendown()
        self.__draw_heart()
        sleep(0.15)
        self.__write_message()


def main() -> None:
    screen = Screen()
    screen.title("Heart Art  |  @kurikosancode")
    set_position(screen=screen)
    pen = Turtle()
    heart = HeartArt(pen, message="I Love You")
    heart.draw()
    mainloop()


if __name__ == "__main__":
    main()
