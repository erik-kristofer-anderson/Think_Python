# Ackerman function defined
# A(m, n) for m and n non-negative integers
# (definition in book)

# code implementation

def A(m, n):
    if m == 0:
        return n + 1
    elif m > 0 and n == 0:
        return A(m-1, 1)
    elif m > 0 and n > 0:
        return A(m - 1, A(m, n-1))
    print("hm... something went wrong")


m = 3
n = 4
print(A(m, n))

# for m = 3, n = 4, the program returns 125
# as the book says it should

# for larger m and n (including (4,0))
# there is an error:
# RecursionError: maximum recursion depth exceeded in comparison
