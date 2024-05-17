"""
Pong Game: Pong stimulates table tennis.

Instructions:
* Move your paddle to bounce the ball back to your opponent.
* To score points and win, make the ball pass your opponent's paddle.

Controls:
* Press the "w" and "s" keys to control the movement of the left paddle.
* Press the up and down arrow to control the movement of the right paddle.
"""

from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
import time
from scoreboard import Scoreboard

game = Turtle()
screen = Screen()


# TODO: Game Screen

# Globals
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

PADDLE_WIDTH = 20
PADDLE_HEIGHT = 100
PADDLE_X_POSITION = 350
PADDLE_Y_POSITION = 0

screen.bgcolor("black")
screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
screen.title("Pong")
screen.tracer(0)


# TODO: Paddle Movement

r_paddle = Paddle(350, 0)
l_paddle = Paddle(-350, 0)

screen.listen()

# Left Paddle controls
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")

# Right Paddle Controls
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")


# TODO: Ball Movement

ball = Ball()

# TODO: Score Tracking
scoreboard = Scoreboard()

# TODO: Updates Screen

updating = True
while updating:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    # TODO: Detect collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.wall_bounce()

    # TODO: Detect collision with paddles
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.paddle_bounce()

    # TODO Detect when paddle misses
    # Misses left paddle
    if ball.xcor() < -380:
        ball.reset()
        scoreboard.l_point()

    # Misses right paddle
    if ball.xcor() > 380:
        ball.reset()
        scoreboard.r_point()

# Added for Dashed Lines
# game.hideturtle()
# game.color("white")
# game.shape("square")
# game.pensize(3)
#
# game.penup()
# game.goto(0, 400)
# game.setheading(270)
# for _ in range(25):
#     game.forward(10)
#     game.penup()
#     game.forward(10)
#     game.pendown()

# Screen's Exit
screen.exitonclick()