def draw_line(t, length):
    """ Draws a line segment

    t: Turtle object
    length: length of line segment
    """
    t.pendown()
    t.fd(length)

def turn(t, angle):
    """ turns a Turtle by angle degrees

    t: Turtle object
    angle: degrees of turn
    """

def move(t, length):
    """ Lifts the pen and moves the turtle
    forward by length

    t: Turtle object
    length: distance to move
    """
    t.penup()
    t.fd(length)
