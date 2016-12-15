class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        carry = 1
        for i in range(len(digits)-1, -1, -1):
            carry = (digits[i] + carry) / 10
            if not carry:
                digits[i] += 1
                break
            else:
                digits[i] = 0
        if carry:
            digits.insert(0, 1)
        return digits

# Solution2
class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        num = 0
        for digit in digits:
            num = num * 10 + digit
        return [int(i) for i in str(num+1)]

test = Solution()
test.plusOne([])