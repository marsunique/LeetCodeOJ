class Solution(object):
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        res = 0
        for ch in s:
            temp = ord(ch) - ord('A') + 1
            res = res * 26 + temp
        return res

test = Solution()
print test.titleToNumber('AAA')