'''
As an exercise, write a compare function that takes two values,
x and y, and returns 1 if x > y, 0 if x == y, and -1 if x < y.
'''

def compare(x, y):
    if x > y:
        return 1
    elif x == y:
        return 0
    elif x < y:
        return -1
    return 'error'

print(compare(5, 5))
