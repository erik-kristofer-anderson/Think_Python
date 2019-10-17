from objects_geom import *

p = Point(3, 4)
print('vars(p):')
print(vars(p))


def print_attributes(obj):
    for attr in vars(obj):
        print(attr, getattr(obj, attr))

print("the attributes of p are:")
print_attributes(p)
