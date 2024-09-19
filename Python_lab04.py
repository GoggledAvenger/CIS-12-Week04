#Lab 4 from https://github.com/THartmanOfTheRedwoods/PyLab004

import random
import turtle

#Part 1: Drawing Basic Shapes

# Create a turtle object
t = turtle.Turtle()

def draw_square(t, length):
    """Draws a square with the given side length."""
    for _ in range(4):
        t.forward(length)
        t.left(90)

# Example usage
#draw_square(t, 100)

def draw_circle(t, radius):
    """Draws a circle with the given radius."""
    t.circle(radius)

# Example usage
#draw_circle(t, 50)

def draw_polygon(t, sides, length):
    """Draws a regular polygon with a given number of sides and side length."""
    angle = 360 / sides
    for _ in range(sides):
        t.forward(length)
        t.left(angle)

# Example usage
#draw_polygon(t, 6, 50)  # Hexagon

#Part 2: Creating Composite Shapes

def draw_pumpkin(t, x, y, radius):
    """Draws a pumpkin (orange circle) at the given (x, y) location with a green stem."""
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.fillcolor("orange")
    t.begin_fill()
    t.circle(radius)
    t.end_fill()

    # Drawing the stem
    t.penup()
    t.left(90)
    t.forward(1.9 * radius)
    t.right(90)
    t.pendown()
    t.fillcolor("green")
    t.begin_fill()
    t.left(90)  # Point upwards
    t.forward(radius // 2)
    t.left(90)
    t.forward(radius // 5)
    t.left(90)
    t.forward(radius // 2)
    t.left(90)
    t.forward(radius // 5)
    t.end_fill()

def draw_eye(t, x, y, size):
    """Draws one triangular eye at the given (x, y) position."""
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.fillcolor("yellow")
    t.begin_fill()
    draw_polygon(t, 3, size)
    t.end_fill()

def draw_mouth(t, x, y, width):
    """Draws a jagged mouth using a series of connected lines."""
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.fillcolor("yellow")
    t.begin_fill()
    t.right(60)
    for _ in range(5):  # Create a simple zigzag mouth
        t.forward(width // 5)
        t.left(120)
        t.forward(width // 5)
        t.right(120)
    t.left(60)
    t.end_fill()

#Part 3: Let the Stars Shine for You

def draw_star(t, x, y, size):
    """Draws a star at the given (x, y) position."""
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.fillcolor("white")
    t.begin_fill()
    for _ in range(5):
        t.forward(size)
        t.right(144)  # 144 degrees is the angle to form a star
    t.end_fill()

#Example usage
#draw_star(t, -100, 150, 30)  # Star in the sky
#draw_star(t, 100, 180, 20)

def draw_sky(t, num_stars):
    """Draws a starry sky with the given number of stars."""
    for _ in range(num_stars):
        x = random.randint(-300, 300)
        y = random.randint(0, 300)
        size = random.randint(10, 30)
        draw_star(t, x, y, size)

# Example usage
#draw_sky(t, 20)  # Draw 20 stars

# Hide the turtle and set speed
t.speed(0)  # 1 is slow, 10 is fast, 0 is instant
t.hideturtle()

# Create a window to draw in
# Create a new turtle screen and set its background color
screen = turtle.Screen()
screen.bgcolor("darkblue")
# Set the width and height of the screen
screen.setup(width=600, height=600)
# Clear the screen
t.clear()

#Part 4: Putting All the Incremental Development Together!

# Draw the night sky
draw_sky(t, 30)

# Draw three jack-o-lanterns
draw_pumpkin(t, -150, -250, 100)
draw_eye(t, -190, -160, 30)  # Left eye
draw_eye(t, -110, -160, 30)  # Right eye
draw_mouth(t, -190, -200, 80)  # Mouth

draw_pumpkin(t, 0, -250, 80)
draw_eye(t, -20, -170, 25)
draw_eye(t, 20, -170, 25)
draw_mouth(t, -30, -210, 60)

draw_pumpkin(t, 150, -250, 100)
draw_eye(t, 110, -160, 30)
draw_eye(t, 190, -160, 30)
draw_mouth(t, 110, -200, 80)


# Close the turtle graphics window when clicked
turtle.exitonclick()