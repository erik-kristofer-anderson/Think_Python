# write a program that reads a word list from
# a file and prints all the sets of
# words that are anagrams

words = []
fin = open('words.txt')
for line in fin:
    word = line.strip()
    words.append(word.lower())

d = dict()
for word in words:
    letters = tuple(sorted(word))
    if letters in d:
        d[letters].append(word)
    else:
        d[letters] = [word]
# so now we (should) have a dict, d, of lists of words,
# where the lists contain the word(s) that use that set of letters


for key in d.keys():
    if len(d[key]) > 1:
        pass # print(d[key])
#####
# now modify this program to return the list of anagram words in
# decreasing [actually I want it increasing] order of number of anagrams

import structshape

# print(structshape.structshape(d))
# from structshape: d is a dict with typle keys and values being
# lists of strings, the lists being of varying lengths

# I want to sort the items in the dict by increasing order
# of the number of strings in the list
# so there will be a len() component

# now, how do I isolate the word list
t = d.values()
t2 = []
for item in t:
    #print(t)
    if len(item) > 1:
        t2.append(item)

t2 = sorted(d.values(), key = lambda my_list: len(my_list), reverse = True)

for item in t2:
    pass
    print(item)
