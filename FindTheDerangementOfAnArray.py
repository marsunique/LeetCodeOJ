class Solution(object):
    def findDerangement(self, n):
        """
        :type n: int
        :rtype: int
        """
        # Reference: https://en.wikipedia.org/wiki/Derangement#Counting_derangements
        # The recursion relationship is D(n) = n-1*( D(n-1) + D(n-2) )
        MOD = 10**9+7
        x2 = 1
        x1 = 0
        # when n = 1, doesn't enter loop return x1 = D(1)
        # when n = 2, x1 = D(2), x2 = D(3), return x1 = D(2)
        # when n = 3, x1 = D(3), x2 = D(4), return x1 = D(3) 
        for i in range(2, n+1):
            x1, x2 = x2, i*(x2+x1) % MOD
        return x1

test = Solution()
print test.findDerangement(4)