class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        # Variant of binary search
        if not nums:
            return 0
        return self.helper(nums, 0, len(nums)-1, target)
        
    def helper(self, nums, l, r, target):
        if l == r:
            if target == nums[l]:
                return l
            elif target < nums[l]:
                return l
            else:
                return l+1
        else:
            middle = (l+r)/2
            if target <= nums[middle]:
                return self.helper(nums, l, middle, target)
            else:
                return self.helper(nums, middle+1, r, target)

test = Solution()
print test.searchInsert([1,3,5,6], 2)