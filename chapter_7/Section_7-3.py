# rerwite the funciton below using iteration

def print_n(s, n):
    if n <= 0:
        return
    print(s)
    print_n(s, n-1)


def print_n_iter(s, n):
    while n > 0:
        print(s)
        n = n - 1
    return

print_n("hi", 3)

print_n_iter('hello', 3)

#cool, got it
