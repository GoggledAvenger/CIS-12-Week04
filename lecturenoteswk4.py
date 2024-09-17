# from https://thartmanoftheredwoods.github.io/CIS-12/week_4py.html

import turtle

# Create a turtle object
t = turtle.Turtle()

# Hide the turtle and set speed
t.speed(5)  # 1 is slow, 10 is fast, 0 is instant
t.hideturtle()

# Create a window to draw in
# Create a new turtle screen and set its background color
screen = turtle.Screen()
screen.bgcolor("darkblue")
# Set the width and height of the screen
screen.setup(width=600, height=600)
# Clear the screen
t.clear()
t.color("green")



def polyline(n, length, angle):
    for i in range(n):
        t.forward(length)
        t.left(angle)

def polygon(n, length):
    angle = 360.0 / n
    polyline(n, length, angle)


def square(length):
    for i in range(4):
        t.forward(length)
        t.left(90)

square(100)

polygon(30,10)

# Close the turtle graphics window when clicked
turtle.exitonclick()