#coding:utf-8
'''
Created on 2016年1月3日

@author: robinjia
@email: dengshilong1988@gmail.com
'''
from common import is_palindrome

if __name__ == "__main__":
    result = 1
    for i in range(100, 1000):
        for j in range(i, 1000):
            temp = i * j
            if is_palindrome(temp) and temp > result:
                result = temp
    print(result)
                