from turtle import Turtle


class Ball(Turtle):

    def __init__(self):
        """Attributes of Ball"""
        super().__init__()
        self.color("white")
        self.shape("circle")
        self.penup()
        self.move_x = 10
        self.move_y = 10
        self.move_speed = 0.1

    def move(self):
        """Moves the ball"""
        new_x = self.xcor() + self.move_x
        new_y = self.ycor() + self.move_y
        self.goto(new_x, new_y)

    def wall_bounce(self):
        """Bounces the ball when in contact with the wall"""
        self.move_y *= -1

    def paddle_bounce(self):
        """Bounces the ball when in contact with the paddle"""
        self.move_x *= -1
        self.move_speed *= 0.9

    def reset(self):
        """Resets the ball to the middle: (0,0)"""
        self.goto(0, 0)
        self.move_speed = 0.1
        self.paddle_bounce()