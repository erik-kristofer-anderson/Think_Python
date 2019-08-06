# define a function that takes a function and calls it twice
def do_twice(f, value):
    f(value)
    f(value)

def print_spam():
    print('spam')


# defin the print_twice function copied from earlier in the chapter
def print_twice(bruce):
    print(bruce)
    print(bruce)

do_twice(print_twice, 'spam')
