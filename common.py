#coding:utf-8
'''
Created on 2016年1月3日

@author: robinjia
@email: dengshilong1988@gmail.com
'''
from math import sqrt,floor
def isPrime(n):
    if n <= 1:
        return False
    if n < 4:
        return True
    if n % 2 == 0:
        return False
    if n % 3 == 0:
        return False
    r = int(floor(sqrt(n)))
    p = 5
    step = 2
    while p <= r:
        if n % p == 0:
            return False
        p = p + step
        step = 6 - step
    return True
def get_primes(n):
    primes = [True] * (n + 1)
    primes[0] = primes[1] = False
    i = 2
    while i * i <= n:
        if primes[i]:
            primes[i * i:n + 1:i] = [False] * ((n - i * i) / i + 1)
        i += 1
    return [i for i in xrange(n + 1) if primes[i]]