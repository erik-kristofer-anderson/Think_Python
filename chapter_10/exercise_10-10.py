"""
use a bisection search to find if a given word is
in the list of words
use the bisect module
"""

import bisect

fin = open('words.txt')

t = []
for line in fin:
    word = line.strip()
    t.append(word)

def in_bisect(t, word):
    i = bisect.bisect_left(t, word)
    if t[i] == word:
        return True
    else:
        return False

word = "hyperacidic"

print(in_bisect(t, word))
