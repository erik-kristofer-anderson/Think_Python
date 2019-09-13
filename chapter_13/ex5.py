# first, take the histogram fn from section 11.2 of think python

def histogram(s):
    d = dict()
    for c in s:
        if c not in d:
            d[c] = 1
        else:
            d[c] += 1
    return d

hist = histogram('triceratops')
hist = histogram('aab')

# write a function that takes a histogram as defined
# in section 11.2 and returns a random value from the
# histo gram, chosen with probability in proportion
# to frequency
import random
def choose_from_hist(hist):
    t = []
    for key in hist:
        for i in range(hist[key]):
            t.append(key)
    return random.choice(t)


# verify the odds:
test = []
for i in range(10000):
    test.append(choose_from_hist(hist))
a, b = 0, 0
for item in test:
    if item == 'a':
        a += 1
    if item == 'b':
        b += 1
print(a, b)
