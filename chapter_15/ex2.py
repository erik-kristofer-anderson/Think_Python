""" Write a function draw rect that takes a Turtle object and a Rectangle and
uses the Turtle to draw the rectangle. See Chapter 4 for examples using
Turtle objects
"""

# First, go review turtles in ch 4

import math
import turtle
import my_shape_classes
import my_turtle_functions


def draw_rect(t, rect):
    # move to corner (turtle starts out facing right)
    move(t, rect.corner.x)
    turn(t, 90)
    move(t, rect.corner.y)

    # mover around the Rectangle
    turn(t, -90)
    draw_line(t, rect.length)
    turn(t, 90)
    draw_line(t, rect.height)
    turn(t, 90)
    draw_line(t, rect.length)
    turn(t, 90)
    draw_line(t, rect.height)


dave = turtle.Turtle()
p = Point()
rect = Rectangle()
rect.corner = Point()
rect.corner.x = 100
rect.corner.y = -200
rect.width = 200
rect.height = 300





draw_rect(dave, rect)

turtle.mainloop()
