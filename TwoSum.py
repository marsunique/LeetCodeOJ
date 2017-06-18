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

class Solution2(object):
    def twoSum(self, nums, target):
        if len(nums) < 2:
            return False
        else:
            dic = {}
            for i in range(0, len(nums)):
                if target-nums[i] in dic:
                    return [dic[target-nums[i]], i]
                else:
                    dic[nums[i]] = i

nums = [2, 7, 11, 15]
target = 9
test = Solution2()
print test.twoSum(nums, target)
