# Write a program that reads a file, breaks each line into words,
# strips whitespace and punctuation from the words,
# and converts them to lowercase

import string
filename = 'sample.txt'
fin = open(filename)
words = []
for line in fin:
    #print(line)
    filtered_line = ''
    for character in line.lower():
        for char_to_remove in list(string.punctuation +'\"\'“’0123456789”—'):
            character = character.replace(char_to_remove, '')
        filtered_line += character
    for word in filtered_line.split():
        words.append(word)
print(words)
