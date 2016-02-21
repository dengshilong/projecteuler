#--coding: utf-8
'''
Created on 2016年1月3日

@author: long
'''


if __name__ == "__main__":
    n = 1000;
    print sum(i for i in xrange(1, n) if i % 3 == 0 or i % 5 == 0)