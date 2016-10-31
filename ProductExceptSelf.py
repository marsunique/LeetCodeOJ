class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        output = nums[:]
        record = 1
        for i in range(0, n):   #nums[i] saves the product of original nums[0]*nums[1]*...*nums[i-1] 
            if i > 0:
                record, nums[i] = nums[i], record * nums[i-1]
            else:
                record, nums[0] = nums[0], record
        record = 1
        for i in range(n-1, -1, -1):    #output[i] saves the product of original nums[n-1]*nums[n-2]*...*nums[i+1]
            if i < n-1:
                record, output[i] = output[i], record * output[i+1]
            else:
                record, output[i] = output[i], record
        for i in range(0, n):
            output[i] = nums[i] * output[i]
        return output

test=Solution()
nums=[1,2,3,4]
print test.productExceptSelf(nums)        