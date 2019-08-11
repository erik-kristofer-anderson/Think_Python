def count(word, letter):
    count = 0
    for character in word:
        if character == letter:
            count = count + 1
    print(count)


count('banana', 'a')
