import turtle
bob = turtle.Turtle()


# define a function that draws a square
def square(t, length):
    for i in range(4):
        t.fd(length)
        t.lt(90)

def bob_to_square():
    square(bob, length, n)

# define a function to print a polygon
def polygon(t, length, n):
    for i in range(n):
        t.fd(length)
        t.lt(360 / n)

# define a function to display a circle
def circle(t, r):
    # function of turtle, t, and radius, r
    c = 2 * 3.14159 * r
    n = 200
    polygon(bob, c / n, n)

def bob_to_square():
    pass

# define a function to display an arc of a circle
def arc(t, r, angle):
    # function of turtle, t, and radius, r
    c = 2 * 3.14159 * r
    n = 100
    partial_polygon(bob, c / n, n, angle)

# define a function to print a partial polygon as an approx to a circle
def partial_polygon(t, length, n, angle):
    for i in range(n):
        t.fd(length * angle / 360)
        t.lt(angle / n )



square(bob)
# polygon(bob, 100, 20)
# circle(bob, 10)
#arc(bob, 100, 180)
turtle.mainloop()
