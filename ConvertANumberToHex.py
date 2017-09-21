class Solution(object):
    def toHex(self, num):
        """
        :type num: int
        :rtype: str
        """
        # use the binary form of a number to solve this question, 
        # therefore no need to consider about negative number, because
        # it is already stored in two's complement
        digits = ['0','1','2','3','4','5','6','7',
                    '8','9','a','b','c','d','e','f']
        if num == 0:
            return 0
        res = ''
        for i in range(8):
            res = digits[num&15] + res
            num = num >> 4
        return res.lstrip('0')
            

test = Solution()
print test.toHex(-1)