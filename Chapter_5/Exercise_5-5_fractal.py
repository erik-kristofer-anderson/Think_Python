# Exercise 5.5 from Think Python

import turtle


# Read the following function and see if you can
# figure out what it does
# then run it and see if you got it right

def draw(t, length, n):
    if n == 0:
        return
    angle = 50
    t.fd(length * n)
    t.lt(angle)
    draw(t, length, n-1)
    t.rt(2 * angle)
    draw(t, length, n-1)
    t.lt(angle)
    t.bk(length * n)

# note: each turn will be 50 degrees
'''
if n = 0, nothing happens
if n = 1, it moves forward length then moves backwords length
if n = 2, it moves forward twice length, turns left angle, (moves forward length,
moves back length), turns right twice angle, (moves forward length, moves back length)
moves back twice length
if n = 3, it moves forward 3x length, turns left angle, does the n = 2 case,
turns right twice angle, does the n = 2 case, turns left angle, boes back 3x length

'''

bob = turtle.Turtle()

length= 5
n = 12

draw(bob, length, n)
turtle.mainloop()


'''
It drew a fractal, which makes sense, based
on the recursive nature of what I prediced it would do
'''
