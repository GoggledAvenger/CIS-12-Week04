# Ch4 Exercises

#Exercise top of pg50

from turtle import penup, pendown, forward

def jump(length):
    """Move forward length units without leaving a trail.

    Postcondition: Leaves the pen down.
    """
    penup()
    forward(length)
    pendown()

# Exercise bottom of pg50

import turtle
t = turtle.Turtle()

t.speed(5)

"""
straight code:

t.forward(length)
t.left(90)
t.forward(width)
t.left(90)
t.forward(length)
t.left(90)
t.forward(width)

as a function:

def rectangle(width,length):
    t.forward(length)
    t.left(90)
    t.forward(width)
    t.left(90)
    t.forward(length)
    t.left(90)
    t.forward(width)

encapsulated version:
    
def rectangle(width,length):
    for i in range(2):
        t.forward(length)
        t.left(90)

more efficient:
"""
def rectangle(base, width):
    for i in range(2):
        for length in (base,width):
            t.forward(length)
            t.left(90)

# rectangle(80,40)

def moveover(length):
    t.penup()
    t.forward(length)
    t.pendown()

# moveover(100)

#Exercise from top of pg51

def rhombus(length):
    for i in range(2):
        t.forward(length)
        t.left(60)
        t.forward(length)
        t.left(120)

# rhombus(50)

# moveover(100)

#Exercise from bottom of pg51

def parallelogram(base, leg, i_angle):
    for i in range(2):
        for side, angle in (base, i_angle), (leg, 180 - i_angle):
            t.forward(side)
            t.left(angle)

parallelogram(80, 40, 60)

moveover(100)

def rhombus2(base, inangle):
    parallelogram(base, base, inangle)

rhombus2(50, 60)

moveover(85)

def rect(b, h):
    parallelogram(base = b, leg = h, i_angle = 90)

rect(80, 40)

# Close the turtle graphics window when clicked
turtle.exitonclick()