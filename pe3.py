#coding:utf-8
'''
Created on 2016年1月3日

@author: robinjia
@email: dengshilong1988@gmail.com
'''
def largest_prime_factor(n):
    p = 2
    while n > 1 and n >= p:
        while n % p == 0:
            n /= p
        if n == 1:
            return p
        p += 1
    return n
if __name__ == "__main__":
    print largest_prime_factor(600851475143)
    print largest_prime_factor(600)
    print largest_prime_factor(10)
    print largest_prime_factor(1)