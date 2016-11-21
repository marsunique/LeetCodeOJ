class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1 or len(s) < numRows:
            return s
        res = [''] * numRows
        index = 0
        step = -1
        for c in s:
            res[index] += c
            if index == numRows - 1 or index == 0:
                # change direction
                step = -step
            index += step
        return ''.join(res)

test = Solution()
print test.convert('abcd', 2)