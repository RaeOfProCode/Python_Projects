from turtle import Turtle, Screen
screen = Screen()

WIDTH = 20
HEIGHT = 100


class Paddle(Turtle):

    def __init__(self, x_position, y_position):
        """Takes the x position and y position as the position of the paddle"""
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(x_position, y_position)

    def go_up(self):
        """Moves the paddle up"""
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    def go_down(self):
        """Moves the paddle down"""
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)
