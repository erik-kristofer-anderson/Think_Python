'''As an exercise, use incremental development to write a function
called hypotenuse that returns the length of the hypotenuse of a
right triangle given the lengths of the other two legs as arguments.
Record each stage of the development process as you go.
'''

# folder section_6-2_dev_steps has the
# record of the development process



# stage 3b
import math
def hypo(a, b):
    i = a ** 2 + b ** 2
    j = math.sqrt(i)
    return j

print(hypo(1, 2))
