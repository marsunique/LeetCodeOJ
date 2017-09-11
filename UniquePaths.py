class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        # grid = [[None] * n for i in range(m)]  //this works only because object None is immutable.
        grid = [[None for j in range(n)] for i in range(m)]
        for row in range(m):
            for col in range(n):
                if row == 0 or col == 0:
                    grid[row][col] = 1
                else:
                    grid[row][col] = grid[row-1][col] + grid[row][col-1]
        return grid[m-1][n-1]


test = Solution()
print test.uniquePaths(4,4)