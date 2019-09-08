# two words form a metathesis pair if you can transform one into the other
# by swapping two letters; for example, "converse" and "conserve"
# write a program that finds all of the metathesis pairs in the dictionary
# hint: don't test all pairs of words, and don't test all possible swaps

# plan: start by isolating anagrams
# then, within each anagram, compare each pair for sameness:
# if len(s) - 2 letters are the same, then it's worth testing
# if whether swapping the other two results in a metathesis pair
# actually, come to think of it, if two letters are anagrams
# and are the same in all but two letters, they must be
# metathesis pairs


def load_words(filename):
    """ loads words from a file, storing them to a list

    filename: a string, the file to be opened
    """
    fin = open(filename)
    words = []
    for line in fin:
        word = line.strip().lower()
        words.append(word)
    return words

### take code from the solution to exercise
import anagram_sets

# store to a dict, d a mapping of string
# signatures (letters of the word in order)
# to the word(s) formed by those letters


# following function modified from
# anagram_sets.print_anagram_sets_in_order
def multiple_anagrams(d):
    """ takes a dictionary, d and returns
    a list of lists, where the inner list
    contains strings that are anagrams
    of eachother. the inner lists returned
    have len() > 1
    """
    t = []
    for value in d.values(): #the value is a list of string(s)
        if len(value) > 1:
            t.append(value)
    return t

def are_similar_anagrams(pair):
    """ takes a pair of anagrams and
    determins if all but two letters
    are the same (considering position)

    pair: tuple of anagrams
    res:  boolean result that is returned
    """
    count_same = 0
    for letter1, letter2 in zip(*pair):
        if letter1 == letter2:
            count_same += 1
    return count_same == len(pair[0]) - 2

def find_similar_anagrams(anagram_list):
    """ takes a list of anagrams (strings)
    and prints out all cases
    where the word pairs are similar
    in that they have the same letters
    in all but two places
    """
    for i, word1 in enumerate(anagram_list):
        for j, word2 in enumerate(anagram_list):
            if j > i:
                test = are_similar_anagrams((word1, word2))
                if test == True:
                    print('Found one!', word1, word2)

d = anagram_sets.all_anagrams('words.txt')
anagram_lists = multiple_anagrams(d)
for anagram_list in anagram_lists:
    find_similar_anagrams(anagram_list)
