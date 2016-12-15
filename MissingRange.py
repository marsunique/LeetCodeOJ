class Solution(object):
    def findMissingRanges(self, nums, lower, upper):
        """
        :type nums: List[int]
        :type lower: int
        :type upper: int
        :rtype: List[str]
        """
        nums.insert(0,lower-1)
        nums.append(upper+1)
        res = []
        for i in range(1, len(nums)):
            if nums[i] - nums[i-1] > 2:
                res.append(str(nums[i-1]+1) + '->' + str(nums[i]-1))
            elif nums[i] - nums[i-1] == 2:
                res.append(str(nums[i]-1))
        return res

test = Solution()
print test.findMissingRanges([0, 1, 3, 50, 75], 0, 99)
