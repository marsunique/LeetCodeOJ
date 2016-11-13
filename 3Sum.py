# use the idea of TwoSum, check out TwoSumII.py
class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        res = []
        if len(nums) < 3:
            return res
        for i in range(len(nums)-2):
            if i != 0 and nums[i] == nums[i-1]:    # skip duplicated number
                continue
            else:
                number = 0 - nums[i]
                head = i + 1
                tail = len(nums) - 1
                while head < tail:
                    if nums[head] + nums[tail] < number:
                        head += 1
                    elif nums[head] + nums[tail] > number:
                        tail -= 1
                    else:
                        if head != i+1 and nums[head] == nums[head-1]:    # skip duplicated head
                            head += 1
                        elif tail != len(nums)-1 and nums[tail] == nums[tail+1]:    # skip duplicated tail
                            tail -= 1
                        else:
                            res.append([nums[i], nums[head], nums[tail]])
                            head += 1
                            tail -= 1
        return res
test = Solution()
print test.threeSum([0,0,0])