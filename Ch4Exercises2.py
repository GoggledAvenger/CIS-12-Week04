#Chapter4 Exercises

import turtle
t = turtle.Turtle()

import math

t.speed(5)

def moveover(length):
    t.penup()
    t.forward(length)
    t.pendown()

#Exercise top of pg52

def polyline(n, length, angle):
    for i in range(n):
        t.forward(length)
        t.left(angle)

def equilateral():
    polyline(3,100,120)

def isosceles(leg, bangle):
    base = 2 * leg * math.sin(math.radians(90 - bangle))
    angle = 180 - bangle
    polyline(1, leg, angle)
    polyline(1, base, angle)
    polyline(1, leg, 2 * bangle)

def draw_pie(n, leg2):
    base_angle = 90 - 180 / n
    center_angle = 2 * base_angle
    for i in range(n):
        isosceles(leg2, base_angle)
        t.left(180 - center_angle)

 draw_pie(5, 100)






#Exercise bottom of pg52


# Close the turtle graphics window when clicked
turtle.exitonclick()