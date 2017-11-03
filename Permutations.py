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

# only produce derangement permutation
class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        original = nums[:]  # add original to compare
        self.helper([], nums, res, original)
        return res
    
    def helper(self, prefix, nums, res, original):
        if not nums:
            res.append(prefix)
        else:
            for i in range(len(nums)):
                num = nums.pop(i)
                new = prefix+[num]
                if new[-1] != original[len(new)-1]:     # only derangement
                    self.helper(prefix+[num], nums, res, original)
                nums.insert(i, num)

test = Solution()
print test.permute([1,2,3])