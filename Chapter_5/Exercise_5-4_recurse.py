"""
This is part of a solution to Exercise 5.4 of Think Python 2e
"""


def recurse(n, s):
    """ Calculates the sum of integers from 1 to n, added to s

    n: positive integer or zero
    s: any number
    """
    if n == 0:
        print(s)
    else:
        recurse(n-1, n+s)

recurse(2, 10)


"""
Part 0.
This is a rough rendition of a stack diagram for recurse(3, 0)

__main__
recurse     n = 3
            s = 0

recurse     n = 2
            s = 3

recurse     n = 1
            s = 5

recurse     n = 0
            s = 6

-----

Part 1.
if we called recourse(-1, 0), the program would
enter an infinite loop

-----

Part 2.
Write a docstring (see above in function)

"""
