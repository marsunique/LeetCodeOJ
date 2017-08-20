class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        res = [''] *numRows
        index = 0
        for c in s:
            res[index] += c
            if index == 0:
                step = 1
            if index == numRows-1:
                step = -1
            index += step
        return ''.join(res)

test = Solution()
print test.convert('paypalishiring', 3)