def has_no_e(word):
    if 'e' in word:
        return False
    else:
        return True

fin = open('words.txt')
count_total, count_no_e = 0, 0
for line in fin:
    word = line.strip()
    if has_no_e(word) == True:
        count_no_e += 1
    count_total += 1
    #print(count_no_e, count_total)



percentage = count_no_e / count_total * 100
print(percentage)
