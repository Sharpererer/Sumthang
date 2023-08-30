from primePy import primes as p
from sympy import isprime
from math import sqrt

num = int(input('Enter integer: '))

def stuff(n):
    list = []
    N = n
    if isprime(n) == True:
        return n
    else:
        for prime in p.factors(n):
            while N%prime == 0:
                N = N/prime
                list += [prime]
        if N != 1:
            list += [int(N)]
        return list

print(stuff(num))