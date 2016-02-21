#coding:utf-8
'''
Created on 2016年1月3日

@author: robinjia
@email: dengshilong1988@gmail.com
'''
from common import isPrime   
if __name__ == "__main__":
    limit = 10001
    count = 1
    result = 2
    while count < limit:
        result += 1
        if isPrime(result):
            count += 1
    print result