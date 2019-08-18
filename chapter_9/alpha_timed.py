# go further and try to figure out which collection of
# five letters allows the most words

from itertools import combinations
import datetime



def avoids(word, forbidden):
    """ determines if a word contains the
    letter in the string forbidden
    word: a string
    forbidden: a string of letters
    """

    for letter in forbidden:
        if letter in word:
            return False
    return True

def count_allowed_words(forbidden):
    '''
    Given a string of forbidden letters, returns
    the number of words from from the list in words.txt
    that don't contain any of those letters
    note: uses a file called words.txt

    forbidden: a string
    '''

    fin = open('words.txt')

    count_avoids = 0
    for line in fin:
        word = line.strip()
        if avoids(word, forbidden) == True:
            count_avoids += 1

    return count_avoids

# get all five letter combinations from the alphabet
letter_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
comb = combinations(letter_list, 5)
letter_collections = list(comb)

# initialize counters. most_allowed is number of words allowed
# most_permissive is the combination of letters that allowed
#the most words.
most_allowed = 0
most_permissive = []

startDT = datetime.datetime.now()

# for collection in letter_collections:
#     #print(collection)
#     x = count_allowed_words(collection)
#     if x > most_allowed:
#         most_permissive = collection
#         most_allowed = x


endDT = datetime.datetime.now()


print(most_permissive, "allows the most letters")
print("It allows", most_allowed, "words")
print('start time:', str(startDT))
print('end time:', str(endDT))
