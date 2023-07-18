from functools import reduce
def mult (x, y):
    return x * y

def factorial(n):
    if n > 0:
        return reduce(mult, range(1,n+1))

def add(x,y):
    return x + y

def mean(L):
    if len(L) != 0:
        return reduce(add, L)/len(L)
    else:
        return 0

#print(factorial(5))
