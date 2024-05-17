from turtle import Turtle, Screen

t = Turtle()
t.speed(8)

def move_forwards():
    t.forward(10)

def move_backwards():
    t.backward(10)

def turn_left():
    new_heading = t.heading() + 10
    t.setheading(new_heading)


def turn_right():
    new_heading = t.heading() - 10
    t.setheading(new_heading)

def clear_screen():
    t.home()
    t.clear()


screen = Screen()
screen.listen()

screen.onkey(key="w", fun=move_forwards)

screen.onkey(key="s", fun=move_backwards)

screen.onkey(key="a", fun=turn_left)

screen.onkey(key="d", fun=turn_right)

screen.onkey(key="c", fun=clear_screen)

screen.exitonclick()