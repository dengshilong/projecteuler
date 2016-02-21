#coding:utf-8
'''
Created on 2016年1月3日

@author: robinjia
@email: dengshilong1988@gmail.com
'''
def get_primes(n):
    primes = [True] * (n + 1)
    primes[0] = primes[1] = False
    i = 2
    while i * i <= n:
        if primes[i]:
            primes[i * i:n + 1:i] = [False] * ((n - i * i) / i + 1)
        i += 1
    return [i for i in xrange(n + 1) if primes[i]]
def smallest_multiple(n):
    primes = get_primes(n);
    result = 1
    for i in primes:
        temp = i
        while temp <= n:
            result *= i
            temp *= i
    return result
if __name__ == "__main__":
    print smallest_multiple(6)
    print smallest_multiple(10)
    print smallest_multiple(20)
        
    