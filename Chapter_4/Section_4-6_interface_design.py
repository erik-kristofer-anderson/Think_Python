import turtle
import math
bob = turtle.Turtle()



def polygon(t, n, length):
    for i in range(n):
        angle = 360 / n
        t.fd(length)
        t.lt(angle)
'''
def circle(t, r):
    # function of turtle, t, and radius, r
    circumference = 2 * math.pi * r
    n = 50
    length = circumference / n
    polygon(t, n, length)
'''

# update circle to calculate its own n
def circle(t, r):
    # function of turtle, t, and radius, r
    circumference = 2 * math.pi * r
    n = int(circumference / 3) + 3
    length = circumference / n
    polygon(t, n, length)
    print(n)


# square(bob, 100)
#polygon(bob, n = 7, length = 70)    # wrote n and length to remind
                                    # ourselves what the numbers mean

circle(bob, 100)

turtle.mainloop()
