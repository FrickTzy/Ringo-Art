from turtle import Screen, Turtle
from bicycle import Bicycle


def set_position(screen: Screen) -> None:
    screen.cv._rootwindow.geometry("+300+150")


def main() -> None:
    screen = Screen()
    screen.title("Bicycle Art  |  @kurikosancode")
    screen.bgcolor("white")
    set_position(screen=screen)
    pen = Turtle()
    pen.speed(9)
    Bicycle(screen=screen, pen=pen, position=(100, 100)).draw()
    pen.hideturtle()
    screen.exitonclick()


if __name__ == '__main__':
    main()
