""" solution from the book
Copyright 2015 Allen Downey
"""











def make_word_dict():
    """Reads a word list and returns a dictionary."""
    d = dict()
    fin = open('words.txt')
    for line in fin:
        word = line.strip().lower()
        d[word] = None

    # have to add single letter words to the word list;
    # also, the empty string is considered a word
    for letter in ['a', 'i', '']:
        d[letter] = letter       ### I would have done d[letter] = None  Oh well
    return d


"""memo is a dictionary that maps from each word that is known to be reducible to
a list of its reducible children. It starts with the empty string.
"""

memo = {}
memo[''] = ['']


def is_reducible(word, word_dict):
    """if word is reducible, returns a list of its reducible children.

    Also adds an entry to the memo dictionary.

    A string is reducible if it has at least one child that is reducible.
    The empty string is also reducible

    word: string
    word_dict: dictionary with words as keys
    """

    # if have already checked this word, return the answer
    if word in memo:     ### doesn't he need to initialize memo somewhere?
        return memo[word]

    # check each of the children and make a list or the reducible ones
    res = []
    for child in children(word, word_dict):
        if is_reducible(child, word_dict):
            res.append(child)
    # memoize and return the result
    memo[word] = res
    return res


def children(word, word_dict):
    """Returns a list of all words that can be formed by removing one letter.

    word: string

    Returns: list of strings
    """
    res = []
    for i in range(len(word)):
        child = word[:i] + word[i+1:]
        if child in word_dict:
            res.append(child)
    return res


def all_reducible(word_dict):
    """Checks all words in the word_dict; returns a list reducible ones.

     word_dict: dictionary with words as keys
     """
    res = []
    for word in word_dict:
        t = is_reducible(word, word_dict)
        if t != []:
            res.append(word)
    return res


def print_trail(word):
    """Prints the sequence of words that reduces this word to the empty string.

    If there is more than one choice, it chooses the first.

    word: strong
    """
    if len(word) == 0:
        return
    print(word, end=' ')
    t = is_reducible(word, word_dict)
    print_trail(t[0])


def print_longest_words(word_dict):
    """Finds the longest reducible words and prints them.

    word_dict: dictionary of valid words
    """
    words = all_reducible(word_dict)

    # use DSU to sort by word length
    t = []
    for word in words:
        t.append((len(word), word))
    t.sort(reverse=True)

    # print the longest 5 words
    for _, word in t[0:5]:
        print_trail(word)
        print('\n')


if __name__ == '__main__':
    word_dict = make_word_dict()
    print_longest_words(word_dict)
