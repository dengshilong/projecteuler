#coding:utf-8
'''
Created on 2016年1月3日

@author: robinjia
@email: dengshilong1988@gmail.com
'''
from math import sqrt,floor

def isPrime(n):
    """判断一个数是否是素数"""
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
    """得到n以内的素数"""
    primes = [True] * (n + 1)
    primes[0] = primes[1] = False
    i = 2
    while i * i <= n:
        if primes[i]:
            primes[i * i:n + 1:i] = [False] * (int((n - i * i) / i) + 1)
        i += 1
    return [i for i in range(n + 1) if primes[i]]


def isPalindrome(x):
    """判断是否是回文数"""
    x = str(x)
    i = 0
    j = len(x) - 1
    while i < j:
        if x[i] != x[j]:
            return False
        i += 1
        j -= 1
    return True

def largest_prime_factor(n):
    p = 2
    while n > 1 and n >= p:
        while n % p == 0:
            n /= p
        if n == 1:
            return p
        p += 1
    return n