# What is the longest English word, that remains a Valid English word,
# as you remove its letters one at a time
# can remove from any position but can't rearrange.


# first, write a function that takes a word and computes a list of
# all the words that can be formed by removing one letter

def load_word_list():
    """ opens the files words.txt, adds the words I, a, and the empty string
    and returns this as a list.
    """
    fin = open('words.txt')
    words = ['i', 'a', '']
    for line in fin:
        word = line.strip().lower()
        words.append(word)
    return words
# test load_word_list
# words = load_word_list()
# print(words) # prints a list of strings

def generate_children(word):
    """ takes a string, word, and returns a list of strings that are the
    possible words you get by removing a letter at each position of the
    string
    """
    child_list = []
    for i, letter_to_remove in enumerate(word):

        child_str = ''
        word_as_list = list(word)
        del word_as_list[i]
        for letter in word_as_list:
            child_str += letter
        child_list.append(child_str)
    return child_list

# test generate_children(word)
# word = 'hello'
# print(generate_children(word)) # ['ello', 'hllo', 'helo', 'helo', 'hell']



def is_word(word, words):
    if word in words:
        return True
    return False

# test is_word
# words = load_word_list()
# word = 'hello'
# print(is_word(word, words)) # True
# word = 'helloo'
# print(is_word(word, words)) # False

def has_child_word(word, words):
    """ return a list of the children of word.
    if no children, returns an empty list.
    """
    children = generate_children(word)
    reduced_children = []
    for child in children:
        if is_word(child, words):
            reduced_children.append(child)
    return reduced_children
# test has_child_word
# words = load_word_list()
# word = 'hello'
# print(has_child_word(word, words)) # (True, ['hell'])

# try writing a is_reducible recursive function
def is_reducible(word, words):
    # print('hi', 'word:', word)
    if word == '':
        return True
    elif is_word(word, words):
        children = generate_children(word)
        res = False
        for child in children:
            if is_reducible(child, words):
                res = True
        if res == True:
            return is_reducible(child, words)
    else:
        return False

# test is reducible('I')
words = load_word_list()
# word = ''
# print(is_reducible(word, words)) # True
# word = 'is'
# print(is_reducible(word, words)) # True

# test it on the list of words:
# words = load_word_list()
# for word in words:
#     if is_reducible_(word, words):
#         print(word)
# it is printing reducible words (yay!) but it is very slow.

# write a new function: is_reducible_memo that uses a dictionary
# to store those words we have already found to be reducible

def is_reducible_memo(word, words):
    reducible_memo = {'': True}
    if word in reducible_memo:
        return reducible_memo[word]
    elif is_word(word, words):
        children = generate_children(word)
        res = False
        for child in children:
            if is_reducible(child, words):
                res = True
            reducible_memo[child] = True
        if res == True:
            return is_reducible(child, words)
    else:
        reducible_memo[word] = False
        return False


words = load_word_list()
for word in words:
    if is_reducible_memo(word, words):
        print(word)
