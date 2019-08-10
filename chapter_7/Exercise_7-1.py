import math



def mysqrt(a):
    epsilon = 0.00000000000001
    x = 1
    while True:
        #print (x)
        y = (x + a/x) / 2
        if abs(y-x) < epsilon:
            break
        x = y
    return x


mysqrt(4)

print("a   mysqrt(a))     math.sqrt(a)   diff")
print("-   ----------     ------------   ----")

for a in range(1, 10):
    a = float(a)
    print(a, end = '')
    print(" ", end = '')
    print("{:12.12f} ".format(mysqrt(a)), end = "")
    print("{:12.12f} ".format(math.sqrt(a)), end = "")
    print("{} ".format(abs(mysqrt(a) - math.sqrt(a))), end = "")
    print("")


# close enough
