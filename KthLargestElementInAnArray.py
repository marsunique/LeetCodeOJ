# Leetcode 215. Also see SelectK(th)Small.py

class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        pos = self.partition(nums)
        if pos == k-1:
            return nums[pos]
        elif pos > k-1:
            return self.findKthLargest(nums[:pos], k)
        else:
            return self.findKthLargest(nums[pos+1:], k-pos-1)

    def partition(self, nums):
        key = nums[-1]
        pos = -1
        for i in range(len(nums)):
            if nums[i] >= key:
                pos = pos+1
                nums[pos], nums[i] = nums[i], nums[pos]
        return pos

test = Solution()
print test.findKthLargest([5,2,4,1,3,6,0],4)
