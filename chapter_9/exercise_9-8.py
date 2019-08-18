
miles = list(range(0,1000000))

def is_palindrome(word):

    i = 0
    j = (len(word)-1)

    while i<j:

        if word[i] != word[j]:
            return False
        i += 1
        j -= 1
    return True


for reading in miles:
    if is_palindrome(str(reading)[2:]):
        #print(reading)
        if is_palindrome(str(reading[1:])):
            if is_palin
