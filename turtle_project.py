"""TODO: This is a scene of an apartment building at night, which took inspiration from the image, "Apartment building at night," created by finwal89. The scene includes the apartment windows; however, I wanted to create a dynamic scene so, I've implemented a random background and random placement of window blinds to better show the "reality" behind the scene as the windows of an apartment are not static but are occassionally closed or may differ in color. As you "Run" the program, you'd notice that the scene is always changing, much like it would in reality. In addition, in order to meet the "recursion" requirement and add more to the scene, multiple recursive trees are shown in the scene. Below is the code for the scene (multiple comments are placed that describe what is being done)."""


__author__ = "730709039"
 

# Importing:
from turtle import Turtle, colormode, done, Screen, bgcolor
import random

# Global Variables: 
SET_SPEED: int = 0
SET_SPEED_STR: str = "fastest"

# Color Palettes
shades_of_yellow_color_list: list[tuple[int, int, int]] = [(248, 222, 126), (250, 218, 94), (249, 166, 2), (255, 211, 0), (210, 181, 91), (195, 176, 145), (218, 165, 32), (252, 244, 163), (252, 209, 42), (255, 195, 11), (196, 145, 2), (252, 226, 5), (253, 165, 15), (204, 119, 34), (255, 191, 0), (238, 220, 130), (255, 253, 208), (245, 245, 220), (255, 229, 180), (239, 253, 95), (248, 228, 115), (254, 220, 86), (255, 221, 175), (206, 177, 128), (228, 211, 143)]
dark_color_list: list[tuple[int, int, int]] = [(0, 11, 17), (30, 44, 53), (54, 45, 0), (4, 0, 37), (54, 69, 79), (48, 25, 52), (52, 52, 52), (27, 18, 18), (40, 40, 43), (53, 57, 53), (4, 2, 20), (4, 2, 20), (4, 2, 20), (4, 2, 20), (4, 2, 20), (4, 2, 20), (4, 2, 20)]


# Main Code:


def main() -> None:
    """The code creates a scene of an apartment building during the night along with trees that are placed below to give the scene more detail. To show the dynamic nature of "life goes on," the background and dark window blinds are random."""
    # Turtle Variables:
    sketcher = Turtle()
    sketcher.hideturtle()
    sketcher.speed(SET_SPEED_STR)
    sketcher.color("black")
    
    # Screen Variables:
    screen = Screen()
    screen.tracer(0, 0)

    # Color Variables:
    colormode(255)
    bgcolor(255, 227, 111)

    # Procedures:

    # 1) random_background creates a random background of the apartment complex (or the inside of a window).
    random_background(sketcher, shades_of_yellow_color_list)  # Function on Line 77 - 132.

    # 2) shadow_window placed "window blinds" on random windows.
    shaded_window(sketcher, -450, 450, dark_color_list)  # Function on Line 135 - 155.

    # 3) The codes below creates the structures/baselines of the apartment building and the windows (for more detail on what they do individually find the function's docstring):
    draw_towers_vertical(sketcher, -450, 450)  # Function on Line 158 - 178.
    draw_towers_horizontal(sketcher, -450, 450)  # Function on Line 181 - 198.
    window_muntin(sketcher, -450, 450)  # Function on Line 201 - 232

    # 4) The codes below adds small details to the apartment building in order to make it appear more real and differentiable from the windows (for more detail on what they do individually find the function's docstring):
    horizontal_shadows(sketcher, -450, 450)  # Function on Line 235 - 253.
    vertical_shadows(sketcher, -450, 450)  # Function on Line 256 - 277.

    # 5) The codes below uses a single function that draws a recursive tree. This was created to add more detail and "realism" to the scene. 
    draw_tree(100, sketcher, -150, -560)  # Function on Line 280 - 297
    draw_tree(100, sketcher, -300, -550)
    draw_tree(100, sketcher, 100, -650)
    draw_tree(100, sketcher, -200, -490)
    draw_tree(100, sketcher, -200, -440)
    draw_tree(100, sketcher, 400, -550)

    # Updates the Screen:
    screen.update() 

    # Scene is completed. For more details on the individual functions, refer to the line numbers provided beside each function. 
    done()

 
# Functions of the Procedures:


def random_background(object: Turtle, color_palette: list[tuple[int, int, int]]) -> None:
    """Creates an random background that'll serve as the backbone or the "scence inside the windows" of the scene, which was created through the use of randomly drawn rectangles of varying sizes based on the color palettem chosen. Note that due to the random locations, this function does not take in an x and y coordinate and this function is simply for creating the "backbone" of the scene."""
    # 1) Creates randomly placed rectangles that are 100 x 200 in size. 
    for t in range(50):
        object.penup()
        random_color = random.choice(shades_of_yellow_color_list)
        object.fillcolor(random_color)
        object.pencolor(random_color)
        x = random.randint(-450, 450)
        y = random.randint(-450, 450)
        object.goto(x, y)
        object.pendown()
        object.begin_fill()
        for side in range(2):
            object.forward(100)
            object.left(90)
            object.forward(200)
            object.left(90)
        object.end_fill()

    # 2) Creates randomly placed rectangles that are 50 x 100 in size. 
    for t in range(150):
        object.penup()
        random_color = random.choice(shades_of_yellow_color_list)
        object.fillcolor(random_color)
        object.pencolor(random_color)
        x = random.randint(-400, 400)
        y = random.randint(-400, 400)
        object.goto(x, y)
        object.pendown()
        object.begin_fill()
        for side in range(2):
            object.forward(50)
            object.left(90)
            object.forward(100)
            object.left(90)
        object.end_fill()

    # 3) Creates randomly placed rectangles that are 10 x 20 in size. 
    for t in range(200):
        object.penup()
        random_color = random.choice(shades_of_yellow_color_list)
        object.fillcolor(random_color)
        object.pencolor(random_color)
        x = random.randint(-400, 400)
        y = random.randint(-400, 400)
        object.goto(x, y)
        object.pendown()
        object.begin_fill()
        for side in range(2):
            object.forward(10)
            object.left(90)
            object.forward(20)
            object.left(90)
        object.end_fill()


def shaded_window(object: Turtle, x: float, y: float, color_palette: list[tuple[int, int, int]]) -> None:
    """Creates "window blinds" or blocks of rectangles using the colors in the chosen color_palette in random window locations. This was done to represent the "closing of blinds" of an apartment window."""
    object.penup()
    for _ in range(20):   # Draws 20 Rows.
        for _ in range(12):   # Draw 12 Windows/Reactangles per every row.
            if random.choice([True, False]):  # For randomness, a random boolean value is randomly chosen to decide whether there should be a "window blind" there or not. 
                object.goto(x, y)
                object.pendown()
                object.begin_fill()
                for _ in range(2):   # Draws the Windows Blinds.
                    object.forward(75)
                    object.right(90)
                    object.forward(40)
                    object.right(90)
                object.end_fill()
                object.penup()
            x += 75   # Added 75 to move to the next window.
            object.color(random.choice(color_palette))  # A random window color is chosen. 
        y -= 50   # Subtracted 50 to move to the next row of Windows.
        x = -450   # Helps to reset the x-coordinate for the next row of Windows for simplicity -> broken down/simplified the code.


def draw_towers_vertical(object: Turtle, x: float, y: float) -> None:
    """Draws the the vertical lines or the columns of the towers of the apartments. This helps create one part of the apartment building and starts at (x, y) that is given."""
    object.width(20)

    object.pencolor("Black")
    for _ in range(10):  # Loops to creates vertical lines or the columns of the apartment.
        for _ in range(1): 
            object.penup()
            object.goto(x, y)
            object.setheading(0)
            object.pendown()
            object.forward(300)
            object.right(90)
            object.forward(900)
            object.right(90)
            object.forward(300)
            object.right(90)
            object.forward(900)
        x += 75
        object.goto(x, y) 


def draw_towers_horizontal(object: Turtle, x: float, y: float) -> None:
    """Draws the the horizontal lines or the rows of the towers of the apartments. This helps create the second part of the apartment building in order to separate the windows, which starts at (x, y) that is given."""
    object.width(15)

    object.pencolor("Black")
    for _ in range(16):  # Loops to create horizontal lines or the rows of the apartment. 
        for _ in range(4):
            object.penup()
            object.goto(x, y)
            object.setheading(0)
            object.pendown()
            object.forward(1000)
            object.right(90)
            object.forward(100)
            object.right(90)
            object.forward(1000)
        y -= 50


def window_muntin(object: Turtle, x: float, y: float) -> None:
    """Draws the windonw's muntin, which is two lines that separate the glass panes in the windows in order to give a window a more realist appearance."""
    object.width(5)

    # Variables for the second line that separates the glass panels. 
    x_2 = -450
    y_2 = 450

    object.pencolor("Black")
    for _ in range(12):  # Creates the first line that separates the glass panels. 
        for _ in range(1):
            object.penup()
            object.goto(x, y)
            object.setheading(0)
            object.forward(25)
            object.pendown()
            object.right(90)
            object.forward(1000)
        x += (75)
        object.penup()
        object.goto(x, y) 

        for _ in range(1):  # Creates the second line that separates the glass panels. 
            object.penup()
            object.goto(x_2, y_2)
            object.setheading(0)
            object.forward(50)
            object.pendown()
            object.right(90)
            object.forward(1000)
        x_2 += (75)
        object.penup()
        object.goto(x_2, y_2) 


def horizontal_shadows(object: Turtle, x: float, y: float) -> None:
    """Draws the the horizontal lines or the shadow of the apartments at (x, y) in order to give the apartment a more realistic appearance. On the scene it is the dark yellow-brown color above each window."""
    object.width(10)

    object.pencolor(44, 41, 29) 

    for _ in range(16):  # Creates the shadow of the apartment. 
        for _ in range(4):
            object.penup()
            object.goto(x, y)
            object.setheading(0)
            object.pendown()
            object.forward(1000)
            object.right(90)
            object.forward(100)
            object.right(90)
            object.forward(1000)
        y -= 50


def vertical_shadows(object: Turtle, x: float, y: float) -> None:
    """Draws the the vertical lines or the shadow of the apartments at (x, y) in order to give the apartmenta more realistic appearance. It is noticable on the scene due to its use to make the horizontal shadows rectangles."""
    object.width(10)

    object.pencolor(16, 14, 9)

    for _ in range(10):  # Divides the horizontal lines created by the function: horizontal_shadows.
        for _ in range(1):
            object.penup()
            object.goto(x, y)
            object.setheading(0)
            object.pendown()
            object.forward(300)
            object.right(90)
            object.forward(900)
            object.right(90)
            object.forward(300)
            object.right(90)
            object.forward(900)
        x += 75
        object.goto(x, y) 


def draw_tree(length: int, object: Turtle, x: float, y: float) -> None:
    """Draws a recursive tree on (x, y) and takes the length of the tree branches. To simplify what it does, the function starts by moving to the (x, y) position and begins to draw the branchs or lines of length "length" given, then it'll split into two smaller branches using recursion (decreasing the length each time). In order to prevent an "infinite" recursion, I've tested that the best length to stop at is 5."""
    # Variables:
    object.width(8)
    object.penup()
    object.goto(x, y)
    object.pendown()

    # Recursive Tree:
    if length > 5:
        object.forward(length)
        object.right(20)
        draw_tree(length - 15, object, object.xcor(), object.ycor())
        object.left(40)
        draw_tree(length - 15, object, object.xcor(), object.ycor())
        object.right(20)
        object.backward(length)



if __name__ == "__main__":
    main()
