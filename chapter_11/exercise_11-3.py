# start with the version of ackermann function from exercise 6.2

def A(m, n):
    print(m, n)
    if m == 0:
        return n + 1
    elif m > 0 and n == 0:
        return A(m-1, 1)
    elif m > 0 and n > 0:
        return A(m - 1, A(m, n-1))
    print("hm... something went wrong")


m = 3
n = 10
# print(A(m, n))



# now 'memoize' it
def a_memo(m, n):
    print(m, n)
    a_dict = {}
    if m == 0:
        return n + 1
    elif m > 0 and n == 0:
        if (m, n) in a_dict:
            return a_dict[(m, n)]
        else:
            a_dict[(m, n)] = a_memo(m - 1, 1)
            return a_dict[(m, n)]
    elif m > 0 and n > 0:
        if (m, n) in a_dict:
            return a_dict[(m, n)]
        else:
            a_dict[(m, n)] = a_memo(m - 1, a_memo(m, n-1))
            return a_dict[(m, n)]

print(a_memo(m, n))
