#coding:utf-8
'''
Created on 2016年1月3日

@author: robinjia
@email: dengshilong1988@gmail.com
'''

if __name__ == "__main__":
    n = 1000
    for a in range(1, n):
        for b in range(a + 1, n):
            if a ** 2 + b ** 2 == (n - a - b) ** 2:
                print(a * b * (n - a - b))
                exit()