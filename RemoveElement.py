class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        index = 0
        for i in range(len(nums)):
            if nums[index] == val:
                nums.pop(index)
            else:
                index += 1
        return len(nums)
        
test = Solution()
print test.removeElement([3,2,2,1,3,6], 3)