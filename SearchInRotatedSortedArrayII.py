class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: bool
        """
        if not nums:
            return False
        return self.helper(0, len(nums)-1, nums, target)

    def helper(self, l, r, nums, target):
        if l == r:
            if nums[l] == target:
                return True
            else:
                return False
        mid = (l+r)/2
        if nums[mid] == target:
            return True
        else:
            if nums[mid] > nums[l]:
                if nums[l] <= target and target <= nums[mid]:
                    return self.helper(l, mid, nums, target)
                else:
                    return self.helper(mid+1, r, nums, target)
            if nums[mid] < nums[l]:
                if nums[mid+1] <= target and target <= nums[r]:
                    return self.helper(mid+1, r, nums, target)
                else:
                    return self.helper(l, mid, nums, target)
            if nums[mid] == nums[l]:
                return self.helper(l+1, r, nums, target)
