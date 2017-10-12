class Solution(object):
    def contagion(self, row, col, dots):
        res = 0
        for i in range(row):
            for j in range(col):
                darkness = 0
                for dot in dots:
                    # darkness = max(darkness, dot[2]-max(abs(i-dot[0]), abs(j-dot[1])))
                    darkness = max(darkness, dot[2]-(abs(i-dot[0])+abs(j-dot[1])))
                res += darkness
        return res
row = 5
col = 6
dots = [(1,0,10), (2,2,9), (2,3,5), (4,2,9)]
test = Solution()
print test.contagion(row,col,dots)
# answer should be 217
