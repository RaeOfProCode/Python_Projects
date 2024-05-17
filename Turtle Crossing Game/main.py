"""
1. A turtle moves forwards when you press the "Up" key. It can only move forwards, not back, left or right.
2. Cars are randomly generated along the y-axis and will move from the right edge of the screen to the left edge.
3. When the turtle hits the top edge of the screen, it moves back to the original position and the player levels up. On the next level, the car speed increases.
4. When the turtle collides with a car, it's game over and everything stops.
"""


import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

# S2.2
car_manager = CarManager()
scoreboard = Scoreboard()

# S2.1
player = Player()
screen.listen()
screen.onkey(player.move_up, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    # S2.2
    car_manager.create_car()
    car_manager.move_cars()

    # S2.3: Detect Collision with Car
    for car in car_manager.car_inventory:
        if car.distance(player) < 20:
            scoreboard.hits_car()
            game_is_on = False

    # 2.4: Detect when the turtle player reaches the top edge of the screen (reaching the FINISH_LINE_Y)
    if player.reached_top():
        player.move_to_start()
        car_manager.level_up()
        scoreboard.increase_score_level()


screen.exitonclick()