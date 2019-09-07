def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

n = 36
print(fibonacci(n))




if n == 0:
    print(0)
elif n == 1:
    print(1)
else:
    print(2)
