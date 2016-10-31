#This is the python implementation code of dp version
#d is the input array. d[i-1], d[i] are numbers of rows and columns of martix A_i

import time

def DP_Matrix_Chain(d,s,f):
    length = len(d)
    n = length - 1
    m = [([float('inf')]*(n))for i in range(n)] #talbe used to record number of multiplication
    p = [([None]*n)for i in range(n)] #table used to record the parenthese position
    for i in range(n):
        m[i][i] = 0
    for i in range(n-2,-1,-1):  #in python index of list starts from 0, range(n-2,-1,-1) means from n-2 to 0
        for j in range(i+1,n):
            for k in range(i,j):
                r = m[i][k]+m[k+1][j]+d[i]*d[k+1]*d[j+1]
                if r < m[i][j]:
                    m[i][j] = r
                    p[i][j] = k+1
    return m[s-1][f-1], m, p   #in python index of list starts from 0

if __name__ == '__main__':
    d = [5,100,2,1,3]
    sTime = time.clock()
    result, table, parenthese_table = DP_Matrix_Chain(d, 1, len(d)-1)
    eTime = time.clock()
    print 'Number of multiplications is:',result
    print 'Table of multiplication numbers:'
    for row in table:
        print row
    print 'Table of parentese position:'
    for row in parenthese_table:
        print row
    print 'Time is:', (eTime-sTime)*1000, 'ms'
