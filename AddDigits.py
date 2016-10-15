class Solution(object):
    def addDigits(self, num):
        if num == 0:
            return 0
        else:
            return num - 9 * ((num-1)/9)

test = Solution()
print test.addDigits(0)