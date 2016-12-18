class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        shift = 1
        res = 0
        origin = n 
        while shift <= origin:
            if n & 1:
                res += 1
            n >>= 1
            shift <<= 1
        return res

test = Solution()
print test.hammingWeight(11)
