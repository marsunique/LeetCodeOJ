#This is the python implementation code of recursive version
#d is the input array. d[i-1], d[i] are numbers of rows and columns of martix A_i

import time

def Recursive_Matrix_Chain(d,s,f):
    if s == f:
        return 0
    MIN = float('inf')
    for k in range(s,f):
        r = Recursive_Matrix_Chain(d,s,k) + Recursive_Matrix_Chain(d,k+1,f) + d[s-1]*d[k]*d[f]
        if r < MIN:
            MIN = r
    return MIN

if __name__ == '__main__':
    d = [5,100,2,1,3]
    sTime = time.clock()
    print 'Number of multiplications is:', Recursive_Matrix_Chain(d,1,len(d)-1)
    eTime = time.clock()
    print 'Time is:', (eTime-sTime)*1000, 'ms'
    