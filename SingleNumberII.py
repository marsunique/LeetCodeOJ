class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        MASK = 0xffffffff
        count = [0]*32
        for num in nums:
            for i in range(0, 32):
                if num & (1 << i):
                    count[i] += 1
        result = 0
        for i in range(0, 32):
            result |= ((count[i]%3) << i)
        if result & 1 << 31:
            return (result | ~MASK)
        return result


test = Solution()
print test.singleNumber([-2,-2,1,1,-3,1,-3,-3,-4,-2])