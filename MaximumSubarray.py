class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        sum = 0
        res = float('-inf')
        for i in range(len(nums)):
            sum += nums[i]
            res = max(sum, res)
            if sum < 0:
                sum = 0
        return res

test = Solution()
print test.maxSubArray([-2,1,-3,4,-1,2,1,-5,4])