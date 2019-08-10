
# from the book:
# The built-ni function eval takes a string and evaluates it
# using the Python interpreter.
# Write a function called eval_loop that iteratively
# promps the user, takes the resulting input and evaluates
# it using eval, and prints the result.


import math

def eval_loop():
    while True:
        result =""
        s = input("type something: ")
        if s == 'done':
            print(result)
            break
        result = eval(s)
        print(result)

eval_loop()
