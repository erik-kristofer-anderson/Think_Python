'''
Solution to Exercise 5.6 in Think Python
'''

import turtle



def koch(t, x):
    if x < 8:
        t.fd(x)
    else:
        koch(t, x / 3)
        t.lt(60)
        koch(t, x / 3)
        t.rt(120)
        koch(t, x / 3)
        t.lt(60)
        koch(t, x / 3)

bob = turtle.Turtle()
length = 300

koch(bob, length)

turtle.mainloop()


### 5.6 1. completed sucsessfully!
