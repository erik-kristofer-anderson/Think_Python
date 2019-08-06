# this is a solution to exercise 4.3 in Think Python 2e

import turtle
import math



def polyline(t, n, length, angle):
    """Draws n line segments.

    t: Turtle object
    n: number of line segments
    length: length of each segment
    angle: degrees between segments

    copied from book
    """
    for i in range(n):
        t.fd(length)
        t.lt(angle)


def polygon(t, n, length):
    """Draws a polygon with n sides.

    t: Turtle
    n: number of sides
    length: length of each side.

    copied from book
    """
    angle = 360.0/n
    polyline(t, n, length, angle)


def spokes(t, n, length):
    '''Draws the spokes within a polygon with
    n sides

    length: length of spokes
    n: number of spokes
    draws the spokes for a polygon
    '''
    for i in range(n):
        t.fd(length)
        t.lt(180)
        t.fd(length)
        t.lt(180)
        t.lt(360 / n)


def turtle_pie(t, n, length_polygon):
    """Draws turtule pies

    t: turtle_pie
    n: number of sides
    length: length of one side
    """

    # calculate
    length_spoke = abs(length_polygon / (2 * math.sin(math.radians(180 / n))))
    alpha = abs(int(((n-2) * 180) / n))
    angle = int(90 - alpha /  2)
    spokes(bob, n, length_spoke)
    bob.fd(length_spoke)
    bob.lt(90)
    bob.lt(angle)
    polygon(bob, n, length_polygon)


bob = turtle.Turtle()


turtle_pie(bob, n = 5, length_polygon = 100)

turtle.mainloop()
