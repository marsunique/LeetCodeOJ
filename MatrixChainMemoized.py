#This is the python implementation code of memoized version
#d is the input array. d[i-1], d[i] are numbers of rows and columns of martix A_i

import time

def Memoized_Matrix_Chain(d,s,f,m,p):
    i = s-1
    j = f-1
    #in python index of list starts from 0
    if m[i][j] < float('inf'):
        return m[i][j]
    if s == f:
        m[i][j] = 0
        return m[i][j]
    for k in range(s,f):
        r = Memoized_Matrix_Chain(d,s,k,m,p) + Memoized_Matrix_Chain(d,k+1,f,m,p) + d[s-1]*d[k]*d[f]
        if r < m[i][j]:
            m[i][j] = r
            p[i][j] = k
    return m[i][j]

if __name__ == '__main__':
    d = [5,2,4,7,3,9,7,8,6,3,7,5,5]
    length = len(d)
    m = [([float('inf')]*(length-1))for i in range(length-1)]   #talbe used to record number of multiplication
    p = [([None]*(len(d)-1))for i in range(len(d)-1)]   #table used to record the parenthese position
    sTime = time.clock()
    result = Memoized_Matrix_Chain(d, 1, len(d)-1, m, p)
    eTime = time.clock()
    print 'Number of multiplications is:', result
    print 'Table of multiplication numbers:'
    for row in m:
        print row
    print 'Table of parentese position:'
    for row in p:
        print row
    print 'Time is:', (eTime-sTime)*1000, 'ms'
