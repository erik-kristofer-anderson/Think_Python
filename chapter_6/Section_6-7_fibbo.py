# copying down an example from section 6.7 of Think Python

def fibbonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + (n-2)

# comment from the book:
# if you try to follow the flow of ececution for even fairly small values
# of n, your head will explode
# but
# if you satisfy yourself that fib(n) = fib(n-1) + fib(n-2),
# and that this is correctly implemented in the program,
# then you know it will work

# for my part, I would add that you have the base case defined
# non-recursively, and that you are sure of reaching the base case
