class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        res = []
        self.helper([], candidates, target, res)
        return res
        
    def helper(self, prefix, candidates, target, res):
        can = candidates[:]
        for i in range(len(can)):
            if can[-1] == target:
                res.append(prefix+[can[-1]])
            elif can[-1] < target:
                self.helper(prefix+[can[-1]], can, target-can[-1], res)
            can.pop()

test = Solution()
print test.combinationSum([2,3,6,7], 7)