class Solution(object):
    def maxKilledEnemies(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if not grid:
            return 0
        row = len(grid)
        col = len(grid[0])
        # print row, col
        res = 0
        rowKill = 0
        colKill = [0]*col
        # print colKill
        for i in range(row):
            for j in range(col):
                # calculate the number of enemies on the row between two walls
                if j == 0 or grid[i][j-1] == 'W':
                    rowKill = 0
                    k = j
                    while k < col and grid[i][k] != 'W':
                        if grid[i][k] == 'E':
                            rowKill += 1
                        k += 1
                # calculate the number of enemies on the column between two walls
                if i == 0 or grid[i-1][j] == 'W':
                    colKill[j] = 0
                    k = i
                    while k < row and grid[k][j] != 'W':
                        if grid[k][j] == 'E':
                            colKill[j] += 1
                        k += 1
                if grid[i][j] == '0':
                    res = max(res, rowKill+colKill[j])
        
        return res

test = Solution()
print test.maxKilledEnemies([['0','E','0','0'],['E','0','W','E'],['0','E','0','0']])
