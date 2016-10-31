# Case1: the given amount is 0, the smallest possible number of coins is 0
# Case2: the given amount is smaller than c[i], look up the smallest possible number of coins without using c[i]
# Case3: the given amount is greater than or equal to c[i] and changing coins with c[i]
# Case4: the given amount is greater than or equal to c[i] and changing coins without c[i]

def coin_change(c, n):
    c.sort()    #make sure that 1 cent is the first denomination
    d = len(c)
    count = [([None]*(n+1))for i in range(d)]   #init a list
    for i in range(0,d):
        count[i][0] = 0 #case 1
        for v in range(1,n+1):
            if v < c[i]:    #case 2
                count[i][v] = count[i-1][v]
            else:
                if i == 0:  #only one denomination is left in the set which is 1 cent
                    count[i][v] = count[i][v-c[i]] + 1
                else:   #compare number of coins in case 3 & case 4
                    count[i][v] = min(count[i][v-c[i]]+1, count[i-1][v])
    print count


denominations = [4,1,3]
coin_change(denominations,6)