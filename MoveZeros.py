class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        index = 0
        length = len(nums)
        for i in range(0,length):
            if nums[index] == 0:
                del nums[index]
                nums.append(0)
            else:
                index += 1

numbers=[1,0,2,0,3]
test=Solution()
test.moveZeroes(numbers)
print numbers