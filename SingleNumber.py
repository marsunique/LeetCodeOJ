class Solution(object):
    def singleNumber(self, nums):
        result = 0
        for num in nums:
            result = result ^ num
        return result
num = Solution()
array = [1,2,3,4,3,2,1,4,-2,-2,-1,-1,-0,0,100032]
print num.singleNumber(array)
