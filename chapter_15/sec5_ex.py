# start with notes from sec 1-5


# we are going to define a new type

import math
class Point:
    """Represents a point in 2-D space."""


def print_point(p):
    print('(%g, %g)' % (p.x, p.y))

def distance_between_points(p1, p2):
    return math.sqrt((p2.x-p1.x)**2 + (p2.y - p1.y)**2)

blank1 = Point()
blank2 = Point()
blank1.x, blank1.y = 2, 2
blank2.x, blank2.y = 5, 6


# for blank in blank1, blank2:
#     print_point(blank)
#
# print(distance_between_points(blank1, blank2))



# from section 3:

class Rectangle:
    """Represents a rectangle

    attributes: width, height, corner
    """

box = Rectangle()
box.width = 100.0
box.height = 200.0
box.corner = Point()
box.corner.x = 0.0
box.corner.y = 0.0

# the expression box.corner.x means, "Go to the object box refers to and select
# the attribute named corner; then go to that object and select attribute x"


# now add sec4 notes

#functions can return instances

def find_center(rect):
    p = Point()
    p.x = rect.corner.x + rect.width/2
    p.y = rect.corner.y + rect.height/2
    return p

# center = find_center(box)
# print_point(center)


# now, in section 15.5, we will write a function to modify the rectangle object

box.width = box.width + 50
box.height = box.height + 100


def grow_rectangle(rect, dwidth, dheight):
    rect.width += dwidth
    rect.height += dheight


# now, as an exercise from section 5,
# write a function named move_rectange that takes a
# Rectangle and two numbers named dx and dy
# it should move the corner by dx and dy



def move_rectangle(rect, dx, dy):
    rect.corner.x += dx
    rect.corner.y += dy

# print_point(box.corner)
#
# move_rectangle(box, 20, 50)
#
# print_point(box.corner)
