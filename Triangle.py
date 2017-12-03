class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        if not triangle or not triangle[0]:
            return None
        temp = [None] * len(triangle)
        for row in range(len(triangle)-1, -1, -1):
            for col in range(row+1):
                if row == len(triangle)-1:
                    temp[col] = triangle[row][col]
                else:
                    temp[col] = triangle[row][col] + min(temp[col], temp[col+1])
        return temp[0]

test = Solution()
print test.minimumTotal([[2],[3,4],[5,6,7],[4,1,8,3]])