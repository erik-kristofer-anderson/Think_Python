
miles = list(range(0,1000000))

def is_palindrome(word):
    """ determines if the string word is a palindrome

    word: a string
    """

    i = 0
    j = (len(word)-1)

    while i<j:

        if word[i] != word[j]:
            return False
        i += 1
        j -= 1
    return True


for i in range(1000, len(miles)-1):
    # were the last 4 a palindrome?
    if is_palindrome(str(miles[i])[2:]):
        # for the next mile, were the last 5 a palindrome?
        if is_palindrome(str(miles[i+1])[1:]):
            # for the next mile, were the middle 6 a palindrome?
            if is_palindrome(str(miles[i+2])[1:5]):
                # for the next mile, are all six a palindrome?
                if is_palindrome(str(miles[i+3])):
                    print('yes: ', miles[i], miles[i+1], miles[i+2], miles[i+3])

# got the answer: yes:  198888 198889 198890 198891
# note: 199999 200000 200001 200002 is probably not the solution, even the the program 
# returned it because the first number has a palindrome of the last 5 numbers,
# not just the last 4.
