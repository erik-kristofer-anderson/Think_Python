import turtle
import math
bob = turtle.Turtle()

# code copied from book

def polyline(t, n, length, angle):
    for i in range(n):
        t.fd(length)
        t.lt(angle)

def(polygon(t, n, length)):
    angle = 360 / n
    polyline(t, n, length, angle)

def arc(t, r, angle):
    arc_length = 2 * math.pi * r * angle / 360
    n = int(arc_length / 3) + 1
    step_length = arc_length / n
    step_angle = float(angle) / n
    polyline(t, n, step_length, step_angle)

# re-write circle to use arc
def circle(t, r):
    arc(t, r, 360)

circle(bob, 100)

turtle.mainloop()
