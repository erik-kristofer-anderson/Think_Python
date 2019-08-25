# this is a solution to an exercise in the book
# Think Python, 2nd ed.

# idea is to solve this puzzler: a guy and his mom
# have been in the situation that their age reversed
# equals the other's age 6 times so far
# (they are on the sixth time), and may have one or two
# more.

# how old is the guy now

# first step: find the age difference for which there
# will be 8 occurences of reversible ages

def is_palindrome(x, y):
    x = str(x).zfill(2)
    y = str(y).zfill(2)
    return x == y[::-1]


# i = starting age difference
# j = age of younger one

for i in range(100):
    counter = 0
    for j in range(100):
        if is_palindrome(j, j+i):
            counter += 1
            #print(counter)
    if counter == 8:
        print(i)
        age_diff = i

for j in range(100):
    if is_palindrome(j, j+age_diff):
        print(j,j+age_diff)
"""
inspect the output
18
2 20
13 31
24 42
35 53
46 64
57 75
68 86
79 97

I'm not sure why the 18 is there, but if I ignore that,
it looks like there are 8 entries, as there should be,
and that the gut is currently 57
"""
