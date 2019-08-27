"""
Write a function that reads the file words.txt and builds
a list with one element per word. write two versions
of this function, one using the append method and
one useing the idium t = t + [x]
Which takes longer to run? Why?
"""

import time

fin = open("words.txt")



def append_words(fin):
    t = []
    for line in fin:
        word = line.strip()
        t.append(word)

def concat_words(fin):
    t = []
    for line in fin:
        word = line.strip()
        t = t + [word]


print("running append words")
start = time.time()
append_words(fin)
end = time.time()

print(end - start)
#append_words(fin)))

print("running concat words")
start = time.time()
concat_words(fin)
end = time.time()

print(end - start)

# append words took 0.03 seconds
# concat words took about 1 e-05 seconds. way faster!
# why?
