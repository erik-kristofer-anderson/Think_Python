"""
Write a function that reads the words in words.txt and stores
them as keys in a dictionary. Values don't matter.
(Then you can use the in operator as a fast way to
check whether a string is in the dictionary.

If you did Exercise 10.10, you can compare the speed of this
implementation with the list in operator and the
bisection search)
"""

import time

fin = open('words.txt')

start = time.time()
print('forming dict:')
d = dict()
for line in fin:
    word = line.strip()
    d[word] = None
end = time.time()
print(end - start)

search_word = 'hype'
print('search_word: ', search_word)

start = time.time()
print('starting dict search:')
print(search_word in d)
end = time.time()
print(end - start)


# compare to 10.10 bisect search

import bisect

t = []
for line in fin:
    word = line.strip()
    t.append(word)

def in_bisect(t, word):
    i = bisect.bisect_left(t, word)
    print(i)
    if t[i] == word:
        return True
    else:
        return False

start = time.time()
print('starting bisect search')
print(in_bisect(t, search_word))
end = time.time()
print(end - start)

# for some reason the bisect search is not working. problem for list index
# out of range
