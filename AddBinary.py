class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        if len(a) < len(b):
            length = len(a)
            longer = len(b)
        else:
            length = len(b)
            longer = len(a)
        carry_bit = '0'
        res = ''
        for i in range(1,longer+1):
            if i < length+1:
                if a[-i] == '0' and b[-i] == '0':
                    res = carry_bit + res
                    carry_bit = '0'
                elif a[-i] == '1' and b[-i] == '1':
                    res = carry_bit + res
                    carry_bit = '1'
                else:
                    if carry_bit == '0':
                        res = '1' + res
                    else:
                        res = '0' + res
            else:
                if carry_bit == '0':
                    if len(a) > len(b):
                        res = a[-i] + res
                    else:
                        res = b[-i] + res
                else:
                    if len(a) > len(b):
                        if a[-i] == '0':
                            res = '1' + res
                            carry_bit = '0'
                        else:
                            res = '0' + res
                    else:
                        if b[-i] == '0':
                            res = '1' + res
                            carry_bit = '0'
                        else:
                            res = '0' + res
        if carry_bit == '1':
            res = '1' + res
        return res

test = Solution()
print test.addBinary('1','1111')