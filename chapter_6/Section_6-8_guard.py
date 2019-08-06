# example from section 6.8 of Think Python
# with guardian code to protect agains non integers and
# negative integers

def fibbonacci(n):
    if not isinstance(n, int):
        print('Factorial is only defined for integers.')
        return None
    elif n< 0:
        print('Factorila is only defined for integers.')
        return None
    elif n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibbonacci(n-1) + fibbonacci(n-2)

print(fibbonacci('fred'))
