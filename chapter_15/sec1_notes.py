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

for blank in blank1, blank2:
    print_point(blank)

print(distance_between_points(blank1, blank2))
