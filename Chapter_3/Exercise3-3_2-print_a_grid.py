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
    do_four_times(print_horizontal_segment)
    print('+') # will create a new line

def print_horizontal_segment():
    print_plus_space()
    do_four_times(print_minus_space)

# define how to pring a vertical line
def print_vertical():
    do_four_times(print_vertical_segment)
    print('|')   # will create a new line

def print_vertical_segment():
    print('|', end = '')
    print('         ', end = '')

# make a function to do other functions repeatedly
def do_four_times(f):
    f()
    f()
    f()
    f()

# define how to print a segment
def print_section():
    print_horizontal()
    do_four_times(print_vertical)

# define how to pring the whole thing 
def print_it_all():
    do_four_times(print_section)
    print_horizontal()

print_it_all()
