class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        MIN = 0x80000000
        MAX = 0x7fffffff
        positive = (dividend > 0) == (divisor > 0)
        dividend, divisor = abs(dividend), abs(divisor)
        res = 0
        while dividend >= divisor:
            bit = 1
            temp = divisor
            while dividend >= temp:
                dividend -= temp
                res += bit
                bit <<= 1
                temp <<= 1
        if not positive:
            return -min(res, MIN)
        else:
            return min(res, MAX)
test = Solution()
print test.divide(16, 3)