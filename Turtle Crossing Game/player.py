from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    # S2.1
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.move_to_start()
        self.setheading(90)

    def move_up(self):
        self.forward(MOVE_DISTANCE)

    # S2.4

    def move_to_start(self):
        self.goto(STARTING_POSITION)

    def reached_top(self):
        if self.ycor() >= FINISH_LINE_Y:
            return True
        else:
            return False