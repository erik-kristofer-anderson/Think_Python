# Write a program that reads a file, breaks each line into words,
# strips whitespace and punctuation from the words,
# and converts them to lowercase

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


counter = 0
for word in words:
    counter += 1

word_frequency_dict = {}
for word in words:
    if word in word_frequency_dict:
        word_frequency_dict[word] += 1
    else:
        word_frequency_dict[word] = 1

counted_words = []
for word in word_frequency_dict:
    counted_words.append((word_frequency_dict[word], word))
counted_words.sort()
#print(counted_words)

print('num words in book:', counter)
num_distinct_words = len(set(word_frequency_dict))
print('num distinct words in book:', num_distinct_words)
