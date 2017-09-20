class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        len_a = len(a)
        len_b = len(b)
        # use '0' to make up the shorter number
        if len_a < len_b:
            a = '0' * (len_b - len_a) + a
        else:
            b = '0' * (len_a - len_b) + b
        carry = 0
        res = ''
        for i in range(len(a)-1, -1, -1):
            cur_bit = (carry + int(a[i]) + int(b[i])) % 2
            carry = (carry + int(a[i]) + int(b[i])) / 2
            res = str(cur_bit) + res
        if carry:
            res = str(carry) + res
        return res

test = Solution()
print test.addBinary('1','1111')