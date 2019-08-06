'''
As an exercise, write a function is_between(x, y, z) that returns
True if x ≤ y ≤ z or False otherwise.
'''

def is_between(x, y, z):
    if x <= y <= z:
        return True
    return False

print(is_between(1, 3, 2))
