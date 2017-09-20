class Solution(object):
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        # refer to https://discuss.leetcode.com/topic/17348/explain-like-i-m-five-java-solution-in-o-n
        # use factorial to determine each digit.
        res = ''
        nums = [i for i in range(1, n+1)]
        factorial = []
        factor = 1
        for i in range(1, n):
            factor = factor * i
            factorial.insert(0, factor)
        for factor in factorial:
            pos = (k-1)/factor
            res += str(nums.pop(pos))
            k =  k % factor
        res += str(nums.pop())
        return res


test = Solution()
print test.getPermutation(4, 3)