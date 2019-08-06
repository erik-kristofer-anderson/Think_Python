import turtle
import math
bob = turtle.Turtle()


'''
def polygon(t, n, length):
    for i in range(n):
        angle = 360 / n
        t.fd(length)
        t.lt(angle)
'''

#start with a copy of polygon (to make an arc)
def polygon(t, r, length):
    arc_length = 2 * math.pi * r * angle / 360
    n = int(arc_length / 3) + 1
    step_length = arc_length = n
    step_angle = angle / n
    for i in range(n):
        t.fd(step_length)
        t.lt(step_angle)



# update circle to calculate its own n
def cirle(t, r):
    # function of turtle, t, and radius, r
    circumference = 2 * math.pi * r
    n = int(circumference / 3) + 3
    length = circumference / n
    polygon(t, n, length)
    print()


# square(bob, 100)
#polygon(bob, n = 7, length = 70)    # wrote n and length to remind
                                    # ourselves what the numbers mean

circle(bob, 100)

turtle.mainloop()
