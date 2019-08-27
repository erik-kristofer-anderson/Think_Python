def histogram(s):
    d = dict()
    for c in s:
        d[c] = d.get(c, 1) + 1
    return d


s = 'implementation'
print(histogram(s))
