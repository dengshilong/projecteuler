#coding:utf-8
'''
Created on 2016年1月3日

@author: robinjia
@email: dengshilong1988@gmail.com
'''
from common import product_number

if __name__ == "__main__":
    board = ''
    with open('pe8.txt') as f:
        board = f.read()
    board = ''.join(board.split('\n'))
    result = 0
    for i in range(0, 1000 - 13):
        s = board[i: i + 13]
        s = [int(i) for i in s]
        p = product_number(s)
        if p > result:
            result = p
    print(result)
    