This exercise solution draws a Koch curve of length x
Here is the main function definition.
It is a recursive function that prints a fractal.

```
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
```

The image shown is for length = 300.
