# Markov analysis


# get the book from emma.txt

# first, define process file, adapted from
# section 13.3
import string

def process_file(filename):
    words_in_order = []
    fp = open(filename)
    lines = []
    for line in fp:
        lines.append(line)
    lines = lines[242:-9]
    for line in lines:
        process_line(line, words_in_order)
    return words_in_order

def process_line(line, words_in_order):
    line = line.replace('-', ' ')

    for word in line.split():
        word = word.strip(string.punctuation + string.whitespace)
        words_in_order.append(word)

words_in_order = process_file('emma.txt')
# print(words_in_order)

# prefix length
n = 2

markov_map = {}
for i in range(len(words_in_order) - n):
    prefix = tuple(words_in_order[i:i+n])
    suffix = words_in_order[i+n]
    if prefix not in markov_map:
        markov_map[prefix] = [suffix]
    else:
        markov_map[prefix].append(suffix)

print(markov_map)
