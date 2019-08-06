"""
This is a solution to exercise 5.3 in Think Python 2e.
The aim is to determine whether three give lengths can for a triangle
"""
def is_tri(a, b, c):
    if a > b + c or b > a + c or c > b + a:
        print('No')
    else:
        print('Yes')

print('Please enter the lengths of three sides of you purported triange.')
a = int(input('a: '))
b = int(input('b: '))
c = int(input('c: '))

is_tri(a, b, c)
