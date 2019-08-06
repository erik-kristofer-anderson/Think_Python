import turtle
bob = turtle.Turtle()


def square(t, length):
    for i in range(4):
        t.fd(length)
        t.lt(90)


def polygon(t, n, length):
    for i in range(n):
        angle = 360 / n
        t.fd(length)
        t.lt(angle)


# square(bob, 100)
polygon(bob, n = 7, length = 70)    # wrote n and length to remind
                                    # ourselves what the numbers mean

turtle.mainloop()
