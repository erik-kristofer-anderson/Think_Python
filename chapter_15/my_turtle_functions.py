def draw_line(t, length):
    """ Draws a line segment

    t: Turtle object
    length: length of line segment
    """
    t.pd()
    t.fd(length)

def turn(t, angle):
    """ turns a Turtle by angle degrees

    t: Turtle object
    angle: degrees of turn
    """
    t.lt(angle)

def move(t, length):
    """ Lifts the pen and moves the turtle
    forward by length

    t: Turtle object
    length: distance to move
    """
    t.pu()
    t.fd(length)


# define a function to print a polygon
def polygon(t, length, n):
    for i in range(n):
        t.fd(length)
        t.lt(360 / n)

# define a function to display a circle
def circle(t, r):
    # function of turtle, t, and radius, r
    c = 2 * 3.14159 * r
    n = 200
    polygon(t, c / n, n)
