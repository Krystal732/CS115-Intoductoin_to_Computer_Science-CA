from math import factorial
from functools import reduce
def add(x, y):
    return x+y

def inverse(n):
    return 1.0 / n

def e(n):
    if n>=1:
        facts = map(math.factorial, range(1,n+1))
        return 1+reduce(add, map(inverse, facts))
    else:
        return "The input to e function must be a positive integer!"
    
#print("The answer of e(2) = ",e(2))
#print("The answer of e(3) = ",e(3))
#print("The answer of e(10) = ",e(10))

