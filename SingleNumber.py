class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        for i in range(1, len(nums)):
            nums[0] = nums[0] ^ nums[i]
        return nums[0]
            

nums = [1,2,3,4,3,2,1,4,-2,-2,-1,-1,-0,0,100032]
test = Solution()
print test.singleNumber(nums)

