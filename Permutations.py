class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        self.helper([], nums, res)
        return res
    
    def helper(self, prefix, nums, res):
        if not nums:
            res.append(prefix)
        else:
            for i in range(len(nums)):
                num = nums.pop(i)
                self.helper(prefix+[num], nums, res)
                nums.insert(i, num)

test = Solution()
print test.permute([1,2,3])