import copy
import turtle
class Point:
    """Represents a point in 2-D space.

    Attributes: x, y
    """

class Circle:
    """Represents a circle by its center and radius

    attributes: center, a point, and radius, a number
    """

class Rectangle:
    """Represents a rectangle

    attributes: width, height, corner
    """


def print_point(p):
    print('(%g, %g)' % (p.x, p.y))

def distance_between_points(p1, p2):
    return math.sqrt((p2.x-p1.x)**2 + (p2.y - p1.y)**2)

def generate_corners(rect):
    c1 = copy.deepcopy(rect.corner)
    c2 = move_point(c1, rect.width, 0)
    c3 = move_point(c1, 0, rect.height)
    c4 = move_point(c1, rect.width, rect.height)
    return [c1, c2, c3, c4]

def move_point(p, dx, dy):
    p2 = copy.deepcopy(p)
    p.x += dx
    p.y += dy
    return p2
