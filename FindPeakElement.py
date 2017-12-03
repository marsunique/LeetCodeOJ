class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return None
        return self.helper(0, len(nums)-1, nums)
    
    def helper(self, l, r, nums):
        mid = (l+r)/2
        if (mid-1 < 0 or nums[mid-1] < nums[mid]) and (mid+1 == len(nums) or nums[mid+1] < nums[mid]):
            return mid
        elif (mid-1 < 0 or nums[mid-1] < nums[mid]):
            # go right
            return self.helper(mid+1, r, nums)
        elif (mid+1 == len(nums) or nums[mid+1] < nums[mid]):
            # go left
            return self.helper(l, mid, nums)
        else:
            # can go either side
            return self.helper(l, mid, nums)


test  = Solution()
print test.findPeakElement([1,2,3,1])