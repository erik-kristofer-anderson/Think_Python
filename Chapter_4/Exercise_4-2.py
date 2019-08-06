"""
# This code is a solution to Exercise 4.2 in the book Think Python
adapted from code in the book
"""
import math
import turtle

def polyline(t, n, length, angle):
    """Draws n line segments.

    t: Turtle object
    n: number of line segments
    length: length of each segment
    angle: degrees between segments
    """
    for i in range(n):
        t.fd(length)
        t.lt(angle)

def arc(t, r, angle, arc_length):
    """Draws an arc with the given radius and angle.

    t: Turtle
    r: radius
    angle: angle subtended by the arc, in degrees
    arc_length: length of the arc
    """
    # arc_length = 2 * math.pi * r * abs(angle) / 360

    n = int((arc_length / 4)+3)
    step_length = arc_length / n
    step_angle = float(angle) / n

    polyline(t, n, step_length, step_angle)

def petal(t, petal_length, arc_radius, petal_angle):
    """ draws a petal with the given radius

    t: Turtle
    arc_radius: radius of the arcs forming the petal
    petal_length: length of the petal
    """

    arc_length = int(petal_length * 1.5)
    arc(t, arc_radius, petal_angle, petal_length )
    t.lt(180 - petal_angle)
    arc(t, arc_radius, petal_angle , petal_length)
    t.lt(180 - petal_angle)





# draw n petals of the flower while turning a total of 360 degrees
dave = turtle.Turtle()

flower_selector = 'c'
if flower_selector == 'a':
    n = 10
    petal_length = 100
    arc_radius = 100
    petal_angle = 80
if flower_selector == 'b':
    n = 7
    petal_length = 200
    arc_radius = 100
    petal_angle = 55
if flower_selector == 'c':
    n = 20
    petal_length = 200
    arc_radius = 100
    petal_angle = 20

for i in range(n):
    petal(dave, petal_length, arc_radius, petal_angle)
    dave.lt(360 / n)
dave.pu()
dave.fd(200)

turtle.mainloop()
