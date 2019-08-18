# there are some fun abecedarian words too,
# like filmy


def is_abecedarian(word):
    word = word.lower() #just incase there are capitals
    prev = 0
    for letter in word:
        x = ord(letter)
        if x >= prev:
            prev = x
        else:
            return False
    return True

print(is_abecedarian('fis'))

fin = open('words.txt')

abc_count = 0
for line in fin:
    word = line.strip()
    if is_abecedarian(word):
        abc_count += 1
        print(word)

print(abc_count)
