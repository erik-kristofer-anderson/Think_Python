# start with in dict from exercise 11.1

# rework this as a function

# is a word in the dict d?
def in_dict(word, d):
    return word in d

def make_dict():
    d = {}
    fin = open('words.txt')
    for line in fin:
        word = line.strip().lower()
        d[word] = None
    return d





# now the code from the book's website to import the pronunciation dictionary

"""This module contains a code example related to

Think Python, 2nd Edition
by Allen Downey
http://thinkpython2.com

Copyright 2015 Allen Downey

License: http://creativecommons.org/licenses/by/4.0/
"""

def read_dictionary(filename='c06d.txt'):
    """Reads from a file and builds a dictionary that maps from
    each word to a string that describes its primary pronunciation.

    Secondary pronunciations are added to the dictionary with
    a number, in parentheses, at the end of the key, so the
    key for the second pronunciation of "abdominal" is "abdominal(2)".

    filename: string
    returns: map from string to pronunciation
    """
    d = dict()
    fin = open(filename)
    for line in fin:

        # skip over the comments
        if line[0] == '#': continue

        t = line.split()
        word = t[0].lower()
        pron = ' '.join(t[1:])
        d[word] = pron

    return d



d_pronounce = read_dictionary()
# for k, v in d.items():
#     pass # print(k, v)



d = make_dict()
# print(d)

del d['aah']
for word in d.keys():
    sub_word_1 = word[1:]
    sub_word_2 = word[0] + word[2:]
    if sub_word_1 in d and sub_word_2 in d and word in d_pronounce and sub_word_1 in d_pronounce and sub_word_2 in d_pronounce:
        if d_pronounce[word] == d_pronounce[sub_word_1] == d_pronounce[sub_word_2]:

            print(word, sub_word_1, sub_word_2, d_pronounce[word])
