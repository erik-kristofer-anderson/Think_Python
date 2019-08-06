# define a function that takes a function and calls it twice
def do_twice(f, value):
    f(value)
    f(value)

def print_spam():
    print('spam')

# do_twice(print_spam)
