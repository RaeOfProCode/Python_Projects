from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.score = 0
        self.update()

    def increase_score_level(self):
        self.score += 1
        self.clear()
        self.update()

    def hits_car(self):
        self.goto(0, 0)
        self.write("Game Over", False, "center", FONT)

    def update(self):
        self.goto(-280, 250)
        self.write(f"Level: {self.score}", False, "left", FONT)



