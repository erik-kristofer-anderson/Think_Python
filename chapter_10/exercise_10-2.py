# write a function called cumsum that takes a list
# of numbers and returns the cummulative sum;
# that is, a new list where the ith element is
# the sum of the first i + 1 elements from the
# original list

def cum_sum(t):
    t2 = []
    total = 0
    for element in t:
        total += element
        t2.append(total)
    return t2

t = [1, 2, 3]

print(cum_sum(t))
