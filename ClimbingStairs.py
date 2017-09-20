class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
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