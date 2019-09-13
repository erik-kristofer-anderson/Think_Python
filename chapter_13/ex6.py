# use set to find what words in pride and prejudice are not in
# the word list

# take some stuff from 4b_pride

fin = open('words.txt')
words_list_set = set()
for line in fin:
    word = line.strip()
    words_list_set.add(word)



import string
filename = 'pride.txt'
fin = open(filename)
lines = []
for line in fin:
    lines.append(line)
lines = lines[28:-364]
words_in_book = set()
for line in lines:
    #print(line)
    filtered_line = ''
    for character in line.lower():
        for char_to_remove in list(string.punctuation +'\"\'“’0123456789”—'):
            character = character.replace(char_to_remove, '')
        filtered_line += character
    for word in filtered_line.split():
        words_in_book.add(word)

not_in_list = words_in_book - words_list_set
print(not_in_list)
