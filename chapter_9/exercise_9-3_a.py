# just do the exercise from the book

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

forbidden = input("enter forbidden letters: ")

fin = open('words.txt')

count_avoids, count_total = 0, 0
for line in fin:
    word = line.strip()
    if avoids(word, forbidden) == True:
        count_avoids += 1
    count_total += 1

percentage = count_avoids / count_total * 100
print(count_avoids, " words avoid the forbidden letters")
print("That's", percentage, "percent")
