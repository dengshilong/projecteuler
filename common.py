#coding:utf-8
'''
Created on 2016年1月3日

@author: robinjia
@email: dengshilong1988@gmail.com
'''
import random
from collections import defaultdict
from functools import reduce


def power_mod(a, b, m):
    r = 1
    while b:
        if b & 1:
            r = r * a % m
        a = a * a % m
        b >>= 1
    return r


def witness(n, r, d, a):
    x = power_mod(a, d, n)
    if x == 1 or x == n - 1:
        return False
    while r > 0:
        x = x ** 2 % n
        if x == n - 1:
            return False
        r -= 1
    return True


def is_prime(n, k=5):
    if n <= 1:
        return False
    r = 0
    d = n - 1
    while d & 1 == 0:
        d = d >> 1
        r += 1
    while k > 0:
        a = random.randint(2, n - 1)
        if witness(n, r, d, a):
            return False
        k -= 1
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


def load_names(filename):
    data = ''
    with open(filename) as f:
        data = f.read()
        data = ''.join(c for c in data.strip() if c != '"')
    return data.split(',')


def name_score(name):
    return sum(ord(c) - ord('A') + 1 for c in name)


def prime_factor(n):
    d = defaultdict(int)
    p = 2
    while n > 1 and n >= p:
        while n % p == 0:
            n /= p
            d[p] += 1
        p += 1
    return d


def origin_sequence(n):
    s = [i for i in str(n)]
    s.sort()
    return ''.join(s)


def totient(n):
    if n == 1:
        return 1
    d = prime_factor(n)
    r = 1
    for p, k in d.items():
        r *= (p - 1) * (p ** (k - 1))
    return r
