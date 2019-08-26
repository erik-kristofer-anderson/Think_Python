# exercise from the book think python

# write a function called nested_sum that takes a list of lists of integers
# and adds up the elements from all of the nested lists

def nested_sum(t):
    total = 0
    for t2 in t:
        for element in t2:
            total += element
    return total


t = [[1, 2], [3], [4, 5, 6]]
print(nested_sum(t))
