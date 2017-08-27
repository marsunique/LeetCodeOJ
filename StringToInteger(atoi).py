class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        INT_MAX = 0x7fffffff    #INT_MAX (2147483647)
        INT_MIN = ~(0X80000000 ^ 0xffffffff)    #INT_MIN (-2147483648)
        sign = 0
        res = False
        for char in str:
            if char == ' ' and res == False and not sign:
                # there is no valid sign before this space. sign should be followed by digits
                # also there is no digits before this space
                continue
            elif (char == '+' or char == '-') and res == False:
                # there are no digits before this '+' or '-'
                if char == '+' and not sign:
                    sign = 1
                elif char == '-' and not sign:
                    sign = -1
                else:
                    # there is already a valid sign, means from here the rest of string are not considered
                    break
            elif char.isdigit():
                if res == False:
                # change res to actual digit
                    res = 0
                res = res * 10 + int(char)
            else:
                break
        if sign == 0:
            sign = 1
        if not res:
            return 0
        elif sign == 1 and res > INT_MAX:
            return INT_MAX
        elif sign == -1 and res*sign < INT_MIN:
            return INT_MIN
        else:
            return res*sign

test = Solution()
print test.myAtoi('     -1123 ds+223')
