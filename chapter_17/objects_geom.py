class Point:
    """Represents a point in 2-D space.

    Attributes: x, y
    """

    def __str__(self):
        return '(%d, %d)' % (self.x, self.y)

    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y

    def __add__(self, other):
        if isinstance(other, Point):
            return self.add_points(other)
        else:
            return self.add_point_tuple(other)

    def __radd__(self, other):
        return self.__add__(other)

    def add_points(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return Point(x, y)

    def add_point_tuple(self, other):
        x = self.x + other[0]
        y = self.y + other[1]
        return Point(x, y)
