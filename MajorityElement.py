class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Boyer-Moore Majority Vote Algorithm
        flag = 0
        majority = None
        for num in nums:
            if flag == 0:
                majority = num
                flag += 1
            elif majority == num:
                flag += 1
            else:
                flag -= 1
        return majority

test = Solution()
print test.majorityElement([1,2,3,2,2])