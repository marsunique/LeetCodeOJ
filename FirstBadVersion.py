# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        # This is a variant of binary search, equivalent to search the
        # firt position of a given value.
        return self.helper(1, n)
    def helper(self, l, r):
        if l == r:
            return l
        else:
            middle = (l+r)/2
            if isBadVersion(middle):
                return self.helper(l, middle)
            else:
                return self.helper(middle+1, r)
        