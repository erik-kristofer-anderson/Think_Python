# ceaser cyther

def rotate_word(word, r):
    ''' does an encoding by shifting by r through the alphabet

    word: a lower case one word string
    r:   an integer
    '''
    word = word.lower()
    cypher_word = ''
    for letter in word:

        x = ord(letter) + r
        # print('letter ', letter, 'ord(letter) ', ord(letter),'x ', x)
        if x > 122:
            x = x - 26
        if x < 97:
            x = x + 26
        cypher_letter = chr(x)
        cypher_word = cypher_word + cypher_letter
    return cypher_word

print(rotate_word('IBM', -1))


print(rotate_word('hal', 1))
