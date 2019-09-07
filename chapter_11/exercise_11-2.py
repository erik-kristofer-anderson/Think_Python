# use setdefault dict method to write a more
# concise version of invert_dict

d = {'a': 1, 'b': 2, 'c': 3, 'd': 3}

def invert_dic_default(d):
    inverse = dict()
    for key in d:
        print(inverse.setdefault(d[key], [key]))
    return inverse

#print(invert_dic_default(d))



###
# from the solution on line:
# http://greenteapress.com/thinkpython2/code/invert_dict.py

def invert_dict(d):
    """Inverts a dictionary, returning a lmap from val to a list of keys.

    If the mapping key->val appears in d, then in the new dictionary
    val maps to a list that includes key.

    d: dict

    returns: dict
    """
    inverse = {}
    for key in d:
        val = d[key]
        inverse.setdefault(val, []).append(key)
    return inverse

print(invert_dict(d))
