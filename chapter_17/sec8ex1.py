""" write an add method for points that works with either
a point object or a tuple
"""
# see objects_geom.py
from objects_geom import *

A = Point(3, 5)
B = Point(1, 2)

print(A + B)
C = (-1, -1)
print(A + C)

# print(C + A)
    # TypeError: can only concatenate tuple (not "Point") to tuple
# now add __radd__ to objects.geom
print(C + A) #(2, 4)    good, it works
