class Solution(object):
    def findDerangement(self, n):
        """
        :type n: int
        :rtype: int
        """
        # Reference: https://en.wikipedia.org/wiki/Derangement#Counting_derangements
        # The recursion relationship is D(n) = n-1*( D(n-1) + D(n-2) )
        MOD = 10**9+7
        d2 = 1
        d1 = 0
        # when n = 1, doesn't enter loop return d1 = D(1)
        # when n = 2, d1 = D(2), d2 = D(3), return d1 = D(2)
        # when n = 3, d1 = D(3), d2 = D(4), return d1 = D(3) 
        for i in range(3, n+2):
            d1, d2 = d2, (i-1)*(d2+d1) % MOD
        return d1

test = Solution()
print test.findDerangement(4)