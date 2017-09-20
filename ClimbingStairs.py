class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        # DP f(n) = f(n-1) + f(n-2)
        # It essentially is Fibonacci Numbers
        if n <= 3:
            return n
        n_1 = 3
        n_2 = 2
        for i in range(4, n+1):
            print n_1, n_2
            res = n_1 + n_2
            n_1, n_2 = res, n_1 
        return res
        
test = Solution()
print test.climbStairs(5)