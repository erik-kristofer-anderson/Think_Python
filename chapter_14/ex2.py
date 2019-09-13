# Write a module that imports anagram_sets and provides two new functions:
# store_anagrams should store the anagram dictionary in a "shelf";
# read_anagrams should look up a word and return a lis of
# its anagrams

import anagram_sets
import pickle


def store_anagrams(d, fout_name):
    fout = open(fout_name, 'wb')
    s = pickle.dumps(d)
    fout.write(s)

    fout.close()

def read_anagrams(word, fin_name):
    fin = open(fin_name, "rb")
    s = fin.read()
    d = pickle.loads(s)
    #print(d.keys())
    print(d[anagram_sets.signature(word)])





d = anagram_sets.all_anagrams('words.txt')
store_anagrams(d,'pickle_shelf.txt')
read_anagrams('hi', 'pickle_shelf.txt')
