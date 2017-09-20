class Solution(object):
    def getPermutation(self, nums):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        res = []
        self.helper('', nums, res)
        return res
        
    
    def helper(self, prefix, nums, res):
        if not nums:
            res.append(prefix)
        else:
            for i in range(len(nums)):
                num = nums.pop(i)
                self.helper(prefix+str(num), nums, res)
                nums.insert(i, num)

test = Solution()
print test.getPermutation([1,2,3])