"""
two words are anagrams if you can rearrange the letters
from one to spell the other. Write a function called
that takes two strings and returns True if they are anagrams
"""

def is_anagram(s1, s2):
    return sorted(list(s1)) == sorted(list(s2))


s1 = 'akg'
s2 = 'gak'

print(is_anagram(s1, s2))

s1 = 'akf'
s2 = 'gak'

print(is_anagram(s1, s2))
