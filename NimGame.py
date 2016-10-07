class Solution(object):
    def __init__(self):
        self.result = [None]*10000000
        self.result[1] = True
        self.result[2] = True
        self.result[3] = True
        self.result[4] = False
    def canWinNim(self, n):
        if self.result[n] != None:
            return self.result[n]
        else:
            self.result[n] = not(self.canWinNim(n-1) and self.canWinNim(n-2) and self.canWinNim(n-3))
            return self.result[n]
test = Solution()
print test.canWinNim(17)