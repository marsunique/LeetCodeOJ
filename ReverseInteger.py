class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        MAX = 0x7fffffff
        MIN = ~(0x80000000 ^ 0xffffffff)
        # use MAX and MIN to do overflow detection
        # python uses more than 32 bits to indicate a number
        # when indicate negative numbers, all higher bits are 1
        sign = cmp(x, 0)
        # get the sign of x
        x = str(sign*x)[::-1]
        x = int(x)*sign
        if MIN <= x and x <= MAX:
            return x
        return 0
        

test = Solution()
print test.reverse(-230)