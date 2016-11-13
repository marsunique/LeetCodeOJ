class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if len(nums) < 2:
            return False
        dic = {}
        for i in range(0,len(nums)):
            if dic.has_key(nums[i]):
                return [dic[nums[i]], i]
            else:
                dic[target - nums[i]] = i 