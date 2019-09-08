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


# for key in d.keys():
#     if len(d[key]) > 1:
#         print(d[key])

# for part c, determine which collection of 8 letters gives the most
# anagrams

import structshape

#print(d.items())
#print(structshape.structshape(d))
for item in d.items():
    #print(item)
    if len(item[0]) == 8 and len(item[1]) > 1:
        #print(item[1])
        pass

anagrams_8_letters_sorted = sorted(d.items(), key = lambda item: len(item[1]), reverse = True)
print(anagrams_8_letters_sorted[:5])
