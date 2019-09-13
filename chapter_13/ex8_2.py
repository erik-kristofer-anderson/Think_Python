# more Markov analysis
# now: add a function to generate
# random text based on the markov analysis

# get the book from emma.txt

# first, define process file, adapted from
# section 13.3
import string
import random


def process_file(filename):
    """proceses the file and returns a list,
    words_in_order, which is an ordered list
    of the words in the book
    """
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


def make_markov_map(words_in_order, n):
    """ takes a list of words, words_in_order, and
    a prefix length, n, and return a dictionary,
    markov_map of the markov analysis
    """

    markov_map = {}
    for i in range(len(words_in_order) - n):
        prefix = tuple(words_in_order[i:i+n])
        suffix = words_in_order[i+n]
        if prefix not in markov_map:
            markov_map[prefix] = [suffix]
        else:
            markov_map[prefix].append(suffix)
    return markov_map



def random_prefix(markov_map):
    """selects a random prefix from the the dict,
    markov_map. returns that prefix, a tuple"""
    prefixes = list(markov_map.keys())
    prefix = prefixes[random.randint(0, len(prefixes))]
    return prefix

def radom_suffix(prefix):
    pass # TODO

def generate_text(markov_map, m, n):
    """ should generate text of length m, using
    the dict, markov_map, to suggest suffixes
    for the given prefix, with prefix length n.
    """
    generated_words = []

    prefix = random_prefix(markov_map)

    for j in range(n):
        generated_words.append(prefix[j])
        # print(generated_words)
    for i in range(m):
        candidate_suffixes = markov_map[prefix]
        suffix = random.choice(candidate_suffixes)
        #suffix = markov_map[prefix][0]  # TODO generalize to randomly selected word from the list at markov_map[prefix]

        generated_words.append(suffix)

        prefix = tuple(generated_words[-n:])
        # print(generated_words)
    return(generated_words)



words_in_order = process_file('emma.txt')

# prefix length
n = 3

markov_map = make_markov_map(words_in_order, n)

#num words to generate
m = 20
print(generate_text(markov_map, m, n))
