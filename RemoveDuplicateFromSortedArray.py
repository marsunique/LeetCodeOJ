class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 1:
            return 1
        i = 0
        j = 1
        while j < len(nums):
            if nums[i] == nums[j]:
                del(nums[j])
            else:
                i += 1
                j += 1
        return len(nums)

test = Solution()
print test.removeDuplicates([1,1])