class Solution(object):
    def kthSmall(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        """
        if len(nums) == 1:
            return nums[0]
        else:
            pos = self.partition(nums)
            if pos == k-1:
                return nums[pos]
            elif pos > k-1:
                return self.kthSmall(nums[:pos], k)
            else:
                return self.kthSmall(nums[pos+1:], k-(pos+1))

    def partition(self, nums):
        """
        :type nums: List[int]
        """
        x = nums[-1]
        pos = -1  # the last element position that is smaller than x
        for i in range(len(nums)):
            if nums[i] <= x:
                pos += 1
                temp = nums[pos]
                nums[pos] = nums[i]
                nums[i] = temp
        return pos
k = 7
nums = [5,5,5,2,1,4,3,6,7]
test = Solution()
print test.kthSmall(nums, k)
