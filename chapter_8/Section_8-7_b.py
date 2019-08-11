def count(word, letter, start):
    count = 0
    for character in word[start:]:
        if character == letter:
            count = count + 1
    print(count)

count('banana', 'a', 2)
