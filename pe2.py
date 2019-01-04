#coding:utf-8
'''
Created on 2016年1月3日

@author: robinjia
@email: dengshilong1988@gmail.com
'''

def fibonacci(max):
    a = 1
    b = 1
    while b < max:
        a, b = b, a + b
        yield a

if __name__ == "__main__":
    n = 4000000
    print(sum(i for i in fibonacci(n) if i % 2 == 0))