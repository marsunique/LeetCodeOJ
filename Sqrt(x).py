class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        # use binary search
        return self.helper(0, x, x)

    def helper(self, l, r, x):
        if l == r:
            return l
        middle = (l + r) / 2
        if middle*middle < x and (middle+1)*(middle+1) <= x:
            return self.helper(middle+1, r, x)
        else:
            return self.helper(l, middle, x)

test = Solution()
print test.mySqrt(0)