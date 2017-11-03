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
        # each loop reduce one candidate from head
        # only consider candidates[i:]
        for i in range(len(candidates)):
            if candidates[i] == target:
                res.append(prefix+[candidates[i]])
            elif candidates[i] < target:
                self.helper(prefix+[candidates[i]], candidates[i:], target-candidates[i], res)

test = Solution()
print test.combinationSum([2,3,6,7], 7)