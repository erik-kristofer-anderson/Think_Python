

# define basic elements of printing
def print_plus_space():
    print('+ ', end = '')

def print_minus_space():
    print('- ', end = '')

def new_line():
    print("")

def print_space():
    prin(' ', end = '')

# define how to print a horizontal line
def print_horizontal():
    print_plus_space()
    do_four_times(print_minus_space)
    print_plus_space()
    do_four_times(print_minus_space)
    print_plus_space()
    new_line()

def print_vertical():
    print('|', end = '')
    print('         ', end = '')
    print('|', end = '')
    print('         ', end = '')
    print('|', end = '')
    new_line()



def do_four_times(f):
    f()
    f()
    f()
    f()

print_horizontal()
do_four_times(print_vertical)
print_horizontal()
do_four_times(print_vertical)
print_horizontal()
