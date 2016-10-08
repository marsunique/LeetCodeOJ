class Solution(object):
    def getSum(self, a, b):
        MAX = 0x7fffffff
        #MAX number in 32 bit
        MIN = 0x80000000
        #MIN number in 32 bit, it is a negative number
        mask = 0xffffffff
        # get last 32 bits
        while b != 0:
            sum_without_carry = (a ^ b) & mask
            carry = ((a & b) << 1) & mask
            a = sum_without_carry
            b = carry
        # if a is negative, get a's 32 bits complement positive first
        # then get 32-bit positive's Python complement negative
        return a if a <= MAX else ~(a ^ mask)

test=Solution()
print test.getSum(11,-35)