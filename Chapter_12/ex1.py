# Exercise 12.1 from think python


# write a function called most_frequent that takes a string
# and prints the letters in decreasing order of
# frequency

# I'm not sure how to use a tuple for this, but let's
# get started


def most_common(s):
    d = dict()
    s = s.lower()
    for letter in s:
        if letter.isalpha():
            if letter in d:
                d[letter] += 1
            else:
                d[letter] = 1
    return d





# load text sample from file

fin = open('sample.txt')
s = fin.read()
d = most_common(s)
#print(d)
#print(len(d))

#print(list(d.items()))
sorted_by_num = sorted(d.items(), key = lambda tup: tup[1], reverse = True)
#print(sorted_by_num)

for t in sorted_by_num:
    print(t[0], t[1])
