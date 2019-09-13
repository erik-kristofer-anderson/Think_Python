# write a program using the algorithm in 13.7 to choose
# a random word from the book.

# first, use keys to get a list of the words in the book

# take some code for ex4b_pride.py

import string
filename = 'pride.txt'
fin = open(filename)
lines = []
for line in fin:
    lines.append(line)
lines = lines[28:-364]
words = []
for line in lines:
    #print(line)
    filtered_line = ''
    for character in line.lower():
        for char_to_remove in list(string.punctuation +'\"\'“’0123456789”—'):
            character = character.replace(char_to_remove, '')
        filtered_line += character
    for word in filtered_line.split():
        words.append(word)

# and more from ex4b
word_frequency_dict = {}
for word in words:
    if word in word_frequency_dict:
        word_frequency_dict[word] += 1
    else:
        word_frequency_dict[word] = 1



#now, get to work

items_list = word_frequency_dict.items()
cum_sum_list = []
prev = 0
for key, value in items_list:
    cum_sum_list.append(value+prev)
    prev = value + prev
#print(cum_sum_list)

# counter = 0
# for word in words:
#     counter += 1
# print(counter)



# import random
# x = random.randint(1, cum_sum_list[-1])
# import bisect
#
#
# # from ex 10.10
# def bisect_search(t, n):
#     i = bisect.bisect_left(t, n)
#     return i
#
# index = bisect_search(cum_sum_list, x)
# print(index)
# print(list(items_list)[index][0])



import random
x = random.randint(1, cum_sum_list[-1])
import bisect


# from ex 10.10
def bisect_search(t, n):
    i = bisect.bisect_left(t, n)
    return i

index = bisect_search(cum_sum_list, x)
print(index)
print(list(items_list)[index][0])



def random_words(cum_sum_list, items_list):
    """ input is cum_sum_list, items_list """

    print('here are some random words from the book')
    for i in range(100):
        x = random.randint(1, cum_sum_list[-1])
        index = bisect_search(cum_sum_list, x)
        print(list(items_list)[index][0])

random_words(cum_sum_list, items_list)
