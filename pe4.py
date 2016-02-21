#coding:utf-8
'''
Created on 2016年1月3日

@author: robinjia
@email: dengshilong1988@gmail.com
'''
def isPalindrome(x):
    x = str(x)
    i = 0
    j = len(x) - 1
    while i < j:
        if x[i] != x[j]:
            return False
        i += 1
        j -= 1
    return True
    
if __name__ == "__main__":
    result = 1
    for i in xrange(100, 1000):
        for j in xrange(i, 1000):
            temp = i * j
            if isPalindrome(temp) and temp > result:
                result = temp
    print result
                