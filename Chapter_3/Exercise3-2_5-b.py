# define a function that takes a function and calls it twice
def do_twice(f, value):
    f(value)
    f(value)

def print_spam():
    print('spam')


# define the print_twice function copied from earlier in the chapter
def print_twice(bruce):
    print(bruce)
    print(bruce)

def do_four(f, value):
    do_twice(f, value)
    do_twice(f, value)

do_four(print_twice, 'hello!')
