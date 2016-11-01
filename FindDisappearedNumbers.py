class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        for num in nums:
            if num > 0:
                if nums[num-1] > 0:
                    nums[num-1] = -nums[num-1]
            else:
                if nums[-num-1] > 0:
                    nums[-num-1] = 0-nums[-num-1]
        index = 0
        result = []
        while index < len(nums):
            if nums[index] > 0:
                result.append(index+1)
            index += 1
        return result

test=Solution()
s=[4,3,2,7,8,2,3,1]
print test.findDisappearedNumbers(s)