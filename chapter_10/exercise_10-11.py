# Two words are are "reverse pair" if each is the reverse
# of the other. Write a program that finds all the reverse pairs
# in the word list

import bisect

fin = open('words.txt')

t = []
for line in fin:
    word = line.strip()
    t.append(word)

def in_bisect(t, word):
    i = bisect.bisect_left(t, word)
    if i < len(t):
        if t[i] == word:
            return True
    return False



for word in t:
    if in_bisect(t, word[::-1]) and word != word[::-1]:
        print(word, word[::-1])
