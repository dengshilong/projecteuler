#coding:utf-8
'''
Created on 2016年1月3日

@author: robinjia
@email: dengshilong1988@gmail.com
'''
from common import get_primes


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
    print(smallest_multiple(6))
    print(smallest_multiple(10))
    print(smallest_multiple(20))
        
    