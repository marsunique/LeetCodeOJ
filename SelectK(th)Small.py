class Solution(object):
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
        print nums
        print i

nums = [1,2,4,5,3]
test = Solution()
test.partition(nums)
            