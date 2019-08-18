# give me a word with three consecutive double
# double letters
# eg if committee was spelled commiittee, it would
# be one

def is_triple_double(word):
    i = 0
    while i < len(word) - 5:
        s = word[i:i+6]
        # print(s)
        if s[0] == s[1] and s[2] == s[3] and s[4] == s[5]:
            return True
        i += 1
    return False

fin = open('words.txt')

for line in fin:
    word = line.strip()
    if is_triple_double(word):
        print(word)
