# Define a new function called do_four
def do_four(f, value):
    do_twice(f, value)
    do_twice(f, value)

def do_twice(f, value):
    f(value)
    f(value)

def print_value(value):
    print(value)


do_four(print_value , '5 spams')
