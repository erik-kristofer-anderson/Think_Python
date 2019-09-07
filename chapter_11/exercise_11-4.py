# start with code from exercise 10.7

def has_duplicates(t):
    ts = sorted(t)
    for i in range(len(ts)-1):
        if ts[i] == ts[i+1]:
            return True
    return False

# implement it with a dictionary method

def has_duplicates(t):
    """takes a list as a parameter and returns True if there is any object
    that appears more than once in the list"""
    dup_dict = {}
    for element in t:
        if element in dup_dict:
            return True
        else:
            dup_dict[element] = None
    return False


t1 = [1, 2, 3, 4, 5, 6]
t2 = [1, 2, 3, 4, 5, 3, 6]

print(has_duplicates(t1))
print(has_duplicates(t2))
