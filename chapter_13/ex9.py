# write a program that reads text from a file, counts word frequencies,
# and prints one line for each word, in descending order of
# frequency, with log f and log r
# use graphing program of your choice to plot the results and check
# whether they form a straight line. Can you estimate the value of s?


# first, get emma.text in a form that makes sense for this exercise
# we want to form a histogram with word for keys and frequency
# for values
# next we will make a sorted list of tuples, the first element in the
# tuple being a word's frequency, the second being the word itself
# the word's position in the list will determine its rank, r
# the frequency will be f, in the relation ship:

# f = cr^(-s)  or log(f) = log(c) - s*log(r)
# where r is rang of the word, f is frequency, and c and s are constants
# depending on the language and the text.


# okay. I have made the functions to prepare
# data to print a list of words ordered by rank
# with the frequency of each word printed,
# along with the word and its rank

# next, package the rank and frequency data
# for plotting
import string
import matplotlib.pyplot as plt


def process_file_emma(filename):
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

def make_hist(words_in_order):
    hist = {}
    for word in words_in_order:
        if word in hist:
            hist[word] += 1
        else:
            hist[word] = 1
    return hist

def words_sorted_by_rank(hist):
    rank_list = []
    for item in hist.items():
        key, value = item[0], item[1]
        rank_list.append((value, key))
    rank_list.sort(reverse=True)
    return rank_list

def print_ranked_words(rank_list):
    for i, item in enumerate(rank_list[:20]):
        print(i+1, item[1], item[0])

words_in_order = process_file_emma('emma.txt')
hist = make_hist(words_in_order)
rank_list = words_sorted_by_rank(hist)

# make list of ranks
ranks = list(range(1,len(rank_list)+1))
frequencies = [item[0] for item in rank_list]
#print(frequencies)

import math
log_f = []
for f in frequencies:
    f = math.log(f, 10)
    log_f.append(f)
#print(log_f)

log_r = []
for r in ranks:
    r = math.log(r, 10)
    log_r.append(r)
print(log_r)


plt.scatter(log_r, log_f)
plt.show()

# plot was succsesful
# it looks like slope, s, of -1
# and intercept, log(c) of 4.0
# approx
