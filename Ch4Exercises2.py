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

def isosceles(leg, base_angle):
    base = 2 * leg * math.sin(math.radians(90 - base_angle))
    angle = 180 - base_angle
    polyline(1, leg, angle)
    polyline(1, base, angle)
    polyline(1, leg, 2 * base_angle)

def draw_pie(n, leg):
    base_angle = 90 - 180 / n
    center_angle = 2 * base_angle
    for i in range(n):
        isosceles(leg, base_angle)
        t.left(180 - center_angle)

draw_pie(5, 50)
moveover(150)
draw_pie(6, 70)
moveover(150)
draw_pie(7, 30)

#Exercise bottom of pg52

def arc(radius, angle):
    arc_length = 2 * math.pi * radius * angle / 360
    n = 30
    length = arc_length / n
    step_angle = angle / n
    polyline(n, length, step_angle)

def petal():
    for i in range(2):
        arc(100, 100)
        t.left(80)

def draw_flower(n, radius):
    for i in range(n):
        petal()
        t.left(180 - radius)

moveover(-550)
draw_flower(9, 140)

# Close the turtle graphics window when clicked
turtle.exitonclick()