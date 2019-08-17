# just do the exercise from the book

from itertools import combinations




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

#print(avoids('and', ['b', 'c']))
#print(avoids('and', ['b', 'c', 'n']))

#forbidden = input("enter forbidden letters: ")
def count_allowed_words(forbidden):
    fin = open('words.txt')

    count_avoids = 0
    for line in fin:
        word = line.strip()
        if avoids(word, forbidden) == True:
            count_avoids += 1
            #count_total += 1

    return count_avoids


letter_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
comb = combinations(letter_list, 5)
letter_collections = list(comb)

most_allowed = 0
most_permissive = []
for collection in letter_collections:
    print(collection)
    x = count_allowed_words(collection)
    if x > most_allowed:
        most_permissive = collection
        most_allowed = x

print(most_permissive, "allows the most letters")
print("It allows", most_allowed, "words")
