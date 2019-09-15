""" Write a function draw rect that takes a Turtle object and a Rectangle and
uses the Turtle to draw the rectangle. See Chapter 4 for examples using
Turtle objects
"""

# First, go review turtles in ch 4

import math
import turtle
from my_shape_classes import *
from my_turtle_functions import *


# def draw_rect(t, rect):
#     # move to corner (turtle starts out facing right)
#     move(t, rect.corner.x)
#
#     turn(t, 90)
#     move(t, rect.corner.y)
#
#     # draw lines around the Rectangle
#     turn(t, -90)
#     draw_line(t, rect.width)
#     turn(t, 90)
#     draw_line(t, rect.height)
#     turn(t, 90)
#     draw_line(t, rect.width)
#     turn(t, 90)
#     draw_line(t, rect.height)
#
#
#
# p = Point()
# rect = Rectangle()
# rect.corner = Point()
# rect.corner.x = 100
# rect.corner.y = -150
# rect.width = 50
# rect.height = 100



### draw a Circle
def draw_circle(t, circ):
    move(t, circ.center.x)
    turn(t, 90)
    t.pd()
    circle(t, circ.radius)







circ = Circle()
circ.center = Point()
circ.center.x = 300
circ.center.y = 200
circ.radius = 50










dave = turtle.Turtle()
draw_circle(dave, circ)


# draw_rect(dave, rect)

turtle.mainloop()
