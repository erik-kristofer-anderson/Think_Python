"""
write a definition for a class named Circle with attributes center and
radius, where center is a point object and radius is a number
"""

# to start, get Point from my notes



class Point:
    """Represents a point in 2-D space.

    attributes: x, y
    """

class Circle:
    """Represents a circle by its center and radius

    attributes: center, a point, and radius, a number
    """


# instantiate a Circle object that represents a circle with its center at
# (150, 100) and radius 75
circ = Circle()
p = Point()
p.x = 150
p.y = 100
circ.center = p
circ.radius = 75

"""write a function named point_in_circle that takes a Circle and point and returns
True is the Point lies in or on the boundary of teh circle."""

# first, get dist between points from my notes
import math
def distance_between_points(p1, p2):
    return math.sqrt((p2.x-p1.x)**2 + (p2.y - p1.y)**2)

def point_in_circle(circ, p):
    if distance_between_points(circ.center, p) <= circ.radius:
        return True
    else:
        return False

# test point in circle:
def print_point(p):
    print('(%g, %g)' % (p.x, p.y))

# print_point(circ.center) # (150, 100)
# p_in = Point()
# p_in.x, p_in.y = 150, 175
# print(point_in_circle(circ, p_in)) # True
# p_in = Point()
# p_in.x, p_in.y = 160, 140
# print(point_in_circle(circ, p_in)) #True
# p_out = Point()
# p_out.x, p_out.y = 225, 175
# print(point_in_circle(circ, p_out)) #False


""" Write a function named rect_in_circle that takes a Circle and a Rectangle
and returns True if the Rectangle lied entirely in or on the boundary of the
Circle"""

# first, get rectange class from my notes

class Rectangle:
    """Represents a rectangle

    attributes: width, height, which are numbers, and corner, which is a point
    """

# if all of a rectangle's corners are within a circle, the rectangle is
# entirely within a circle

# first, generate the points of the corners
# but for that, write a function to move a point
import copy
def move_point(p, dx, dy):
    p2 = copy.deepcopy(p)
    p.x += dx
    p.y += dy
    return p2

def generate_corners(rect):
    c1 = copy.deepcopy(rect.corner)
    c2 = move_point(c1, rect.width, 0)
    c3 = move_point(c1, 0, rect.height)
    c4 = move_point(c1, rect.width, rect.height)
    return [c1, c2, c3, c4]

def rect_in_circle(rect, circ):
    for corner in generate_corners(rect):
        if point_in_circle(circ, corner) == False:
            return False
    return True

# to make things easier: define make point
def make_point(x, y):
    p = Point()
    p.x = x
    p.y = y
    return p

# # test. rect should be in circle
# rect = Rectangle()
# rect.corner = make_point(0, 0)
# rect.width = 50
# rect.height = 50
# circ = Circle()
# circ.center = make_point(0, 0)
# circ.radius = 200
# print(rect_in_circle(rect, circ))
#
# # test. rect should not be in circle
# rect = Rectangle()
# rect.corner = make_point(0, 0)
# rect.width = 200
# rect.height = 200
# circ = Circle()
# circ.center = make_point(0, 0)
# circ.radius = 200
# print(rect_in_circle(rect, circ)) #False


"""Write a function named rect_circle_overlap that takes a Circle and a
Rectangle and returns True if any of the corners of the Rectangle
fall inside the circle. (optional more challenging version: True if
any part of the Rectangle falls inside the circle)
"""
# the optional part is more geometry than programming, so I'll just study the
# solution on that


# if any of the corner points are in the circle, return true
def rect_circle_overlap(rect, circ):
    for corner in generate_corners(rect):
        if point_in_circle(circ, corner):
            return True
    return False

# test. rect should be in circle
rect = Rectangle()
rect.corner = make_point(0, 0)
rect.width = 50
rect.height = 50
circ = Circle()
circ.center = make_point(0, 0)
circ.radius = 200
print(rect_circle_overlap(rect, circ)) # True

# no corner of rect should be in circle
rect = Rectangle()
rect.corner = make_point(0, 0)
rect.width = 50
rect.height = 50
circ = Circle()
circ.center = make_point(1000, 1000)
circ.radius = 200
print(rect_circle_overlap(rect, circ)) # False
