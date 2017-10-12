class Solution(object):
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        res = ''
        while n:
            r = n % 26
            if r == 0:
                res = 'Z' + res
                n = (n-1) / 26
            else:
                res = chr(ord('A') + r -1) + res
                n = n/26
        return res

test = Solution()
print test.convertToTitle(28)
