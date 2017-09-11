class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        if obstacleGrid[0][0] == 1:
            return 0
        obstacleGrid[0][0] = 1
        for row in range(m):
            for col in range(n):
                if row == 0 and col == 0:
                    continue
                if obstacleGrid[row][col] == 1:
                    obstacleGrid[row][col] = 0
                else:
                    if row == 0:
                        obstacleGrid[row][col] = obstacleGrid[row][col-1]
                    elif col == 0:
                        obstacleGrid[row][col] = obstacleGrid[row-1][col]
                    else:
                        obstacleGrid[row][col] = obstacleGrid[row-1][col] + obstacleGrid[row][col-1]
        return obstacleGrid[m-1][n-1]

test = Solution()
print test.uniquePathsWithObstacles([[0,0,0],[0,1,0],[0,0,0]])