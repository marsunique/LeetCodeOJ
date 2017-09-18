class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if not nums:
            return -1
        return self.helper(nums, 0, len(nums)-1, target)
        
        
    def helper(self, nums, l, r, target):
        if l == r:
            if nums[l] == target:
                return l
            else:
                return -1
        else:
            middle = (l+r)/2
            if nums[middle] > nums[l]:      # this means that left part is sorted.
                if nums[l] <= target and target <= nums[middle]:  # target is in the left part
                    return self.helper(nums, l, middle, target)
                else:
                    return self.helper(nums, middle+1, r, target)
            else:                           # right part is sorted.
                if nums[middle+1] <= target and target <= nums[r]:
                    return self.helper(nums, middle+1, r, target)
                else:
                    return self.helper(nums, l, middle, target)
                    
test = Solution()
print test.search([4,5,6,7,0,1,2], 0)