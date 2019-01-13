#coding:utf-8
'''
Created on 2016年1月3日

@author: robinjia
@email: dengshilong1988@gmail.com
'''
from functools import reduce
from math import sqrt,floor

def is_prime(n):
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


def is_palindrome(x):
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


def product_number(s):
    return reduce(lambda x, y: x * y, s)


def product_n(n):
    if n == 0 or n == 1:
        return 1
    return product_number(range(1, n + 1))


def get_divisors(n):
    if n == 1:
        return [1]
    return [i for i in range(1, int(n/2) + 1) if n % i == 0]


def is_pandigital(n, m):
    if len(str(n)) != m:
        return False
    for i in range(1, m + 1):
        if str(i) not in str(n):
            return False
    return True