# 6.2 1. I can (mostly) tell what the first three functions
# do by looking at them

def first(word):
    return word[0]

def last(word):
    return word[-1]

def middle(word):
    return word[1:-1]


#print(first(""))
# causes an error


#print(last(""))
# causes and error



print(middle(""))
#prints a blank line

# 6.2 2. Write function to determine if
# word is a palindrome


def is_palindrome(word):
    if len(word) <= 1:
        return True
    elif first(word) == last(word):
        word = middle(word)
        return is_palindrome(word)
    else:
        return False






word = "amanaplanacanalpanama"
print(is_palindrome(word))
