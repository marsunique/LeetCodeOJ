class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # Use two passes of binary search. One for searching the first location, one for searching the last location
        if not nums:
            return [-1, -1]
        return [self.searchFirst(nums, 0, len(nums)-1, target), self.searchLast(nums, 0, len(nums)-1, target)]
        
    def searchFirst(self, nums, l, r, target):
        if l == r:
            if nums[l] == target:
                return l
            else:
                return -1
        else:
            middle = (l+r)/2
            if target <= nums[middle]:
                return self.searchFirst(nums, l, middle, target)
            else:
                return self.searchFirst(nums, middle+1, r, target)
    
    def searchLast(self, nums, l, r, target):
        if l == r:
            if nums[l] == target:
                return l
            else:
                return -1
        else:
            middle = (l+r)/2 + 1
            if target < nums[middle]:
                return self.searchLast(nums, l, middle-1, target)
            else:
                return self.searchLast(nums, middle, r, target)

test = Solution()
print test.searchRange([5,6,6,8,8,10], 8)