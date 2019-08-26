"""
Write a functino called middle that takes a list
and returns a new list that contains all but
the first and last elements.
"""

def middle(t):
    return t[1:-1]

t = [1, 2, 3, 4]

print(middle(t))


def middle_2(t):
    t2 = []
    for i in range(1, len(t) - 1):
        t2.append(t[i])
    return t2
print(middle_2(t))
