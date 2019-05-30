from math import ceil, sqrt, floor
import numpy as np
from time import time

## Deletes from L all numbers divisible by p that are greater than maxl
def delete_div(L, p, maxl):
    if p <= 2: return L
    f = np.where(L <= maxl)
    i = np.where(L[f] % p != 0)
    return L[i]

## Returns number of elements greater than a
def count(L, a):
    return np.size(L) - np.size(np.where(L <  a))

## Checks whether if a given number n is prime
def is_prime(n):
    if n == 1: return False
    if n <= 3: return True
    if n % 2 == 0: return False
    i = 3
    while i <= sqrt(n):
        if n % i == 0: return False
        i+=2

    return True

## Returns the counting of prime numbers in the given interval [a, b]
def primes_interval(a, b):
    p = []
    if a == 2: p.append(2)
    if a % 2 == 0: a += 1
    i = a
    while i <= b:
        if is_prime(i): p.append(i)
        i += 2

    return p

## Returns the counting of prime numbers in the given interval I = [inf, sup]
def primes_counter(inf, sup):
    # Counting of prime numbers
    # initially, takes all numbers in the interval as primes
    m = sup - inf + 1
    mv = sup//2
    maxp = floor(sqrt(sup))
    # Calculates the amount of even numbers in I
    # and removes this quantity of m
    min2 = ceil(inf/2)
    max2 = floor(sup/2)
    r = max2 - min2 + 1
    m = m - r
    # Counts all numbers in I that are divisible by 3 
    # and not divisible b 2, i.e: Non divisible by 6
    min3 = floor((inf-1)/3)
    max3 = floor(sup/3)
    r = max3 - min3 - (floor(sup/6)-floor((inf-1)/6))
    m = m - r
    # Computes only odd numbers in the interval [3, mv + 1]
    # these are the numbers such that multiplied by any prime number in P
    # lead to composite numbers in I
    L = np.arange(3,mv+1,2)
    # Deletes all numbers divisible by 3 and greater than sup/5 in L
    L = delete_div(L,3,sup/5)
    lp = 3
    P = primes_interval(5, maxp)
    # print('Primos: %d' % len(P))
    for p in P:
        minl = ceil(inf/p)
        maxl = floor(sup/p)
        L = delete_div(L, lp, maxl)
        r = count(L, minl)
        m = m - r
        lp = p

    return m
