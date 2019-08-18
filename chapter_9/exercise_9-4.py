def uses_only(word, approved_letters):
    test = True
    for letter in word:
        if letter in approved_letters:
            test = True
        else:
            return False
    return test

fin = open('words.txt')

# define approved_letters
approved_letters = 'acefhlo'


for line in fin:
    word = line.strip()
    if uses_only(word, approved_letters) == True:
        print(word)
