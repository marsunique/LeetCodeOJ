class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        digit = [0 for i in range(len(num1)+len(num2))]
        for i in range(len(num1)):
            for j in range(len(num2)):
                product = (ord(num1[i])-ord('0')) * (ord(num2[j])-ord('0'))
                digit[i+j+1] += product%10
                digit[i+j] += product/10

        for i in range(len(num1)+len(num2)-1, 0, -1):
            if digit[i] >= 10:
                digit[i-1] +=  digit[i]/10
                digit[i] = digit[i]%10
        print digit
        # find first non-zero digit
        for i, num in enumerate(digit):
            if num:
                break
        return ''.join(map(str, digit[i:]))


test = Solution()
print test.multiply('123','456')