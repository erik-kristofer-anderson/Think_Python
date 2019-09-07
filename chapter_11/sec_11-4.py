
# invert a dictionary

d = {'a': 1, 'b': 2, 'c': 3, 'd': 3}

def invert_dict(d):
    inverse = dict()
    for key in d:
        val = d[key]
        if val not in inverse:
            inverse[val] = [key]
        else:
            inverse[val].append(key)
    return inverse

print(invert_dict(d))
