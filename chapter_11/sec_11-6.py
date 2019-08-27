known = {0:0, 1:1}
def fibonacci(n):
    if n in known:
        return known[n]
    res = fibonacci(n-1) + fibonacci(n-1)
    known[n] = res
    return res

n = 1000
print(fibonacci(n))
