class Solution(object):
    def toDecimal(self, num):
        """
        :type num: int
        :rtype: str
        """
        # use binary form to easily handle the negative number
        res = ''
        for i in range(32):
            res = str(num&1) + res
            num = num >> 1
        return res.lstrip('0')

test = Solution()
print test.toDecimal(18)