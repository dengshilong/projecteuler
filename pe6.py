#coding:utf-8
'''
Created on 2016年1月3日

@author: robinjia
@email: dengshilong1988@gmail.com
'''
def sum_square_diff(n):
    return (n * (n + 1) / 2) ** 2 - (n) * (n + 1) * (2 * n + 1) / 6
if __name__ == "__main__":
    print sum_square_diff(10)
    print sum_square_diff(100)
    