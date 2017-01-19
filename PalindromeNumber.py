class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False
        forward = x
        backward = 0
        while forward >= 10:
            backward = backward * 10 + forward % 10
            forward /= 10
        if backward == x / 10:
            return True
        return False

test = Solution()
print test.isPalindrome(1)