def LIS(s):
    n = len(s)
    print n
    l = [0]*n
    r = [None]*n
    l[0] = 1
    for i in range(0,n):
        max = 0
        for j in range(i-1,-1,-1):
            if s[j] <= s[i]:
                if max < l[j]:
                    max = l[j]
                    r[i] = j
        l[i] = max+1
    print s
    print l
    print r

LIS([1,4,2,3,1])