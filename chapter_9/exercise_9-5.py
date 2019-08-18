# from this, I learned that there are a lot of fun words
# in the list of words that contain every vowel

def uses_all(word, required_letters):
    for letter in required_letters:
        if not letter in word:
            return False
    return True

fin = open('words.txt')
required_letters = 'aeiouy'
counter = 0
for line in fin:
    word = line.strip()
    if uses_all(word, required_letters):
        counter += 1
        print(word)
print("there are", counter, "words that contain all the following:", required_letters)
