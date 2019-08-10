# the book has an infinite series to calculate
# a numerical approximation of 1 / pi

# write a function called estimate_pi
# loop until th last term is smaller than 1e-15




def term_in_sum(k):
    top = factorial(4 * k)*(1103 + 26390 * k)
    bottom = (factorial(k) ** 4) * 396 ** (4 * k)
    result = top / bottom
    return result

def sum():
    sum_num = 0
    term = 10000000
    k = 0
    while term > 1e-15:
        term = term_in_sum(k)
        sum_num = sum_num + term
        

        k = k + 1
    return sum_num

def estimate_pi():
    return 1/(((2 * 2 ** (1 / 2)) / 9801) * sum())


# definition of factorial taken from section 6.9
def factorial(n):
    #space = ' ' * (4 * n)
    #print(space, 'factorial', n)
    if n == 0:
        #print(space, 'returning 1')
        return 1
    else:
        recurse = factorial(n-1)
        result = n * recurse
        #print(space, 'returning', result)
        return result

import math

print('estimate_pi():  ' + str(estimate_pi()))
print('math.pi:        ' + str(math.pi))
#print('difference:     ' + str(abs(math_result - estimate)))
print('difference:   ', estimate_pi() - math.pi)

# something wierd is going wrong with this
