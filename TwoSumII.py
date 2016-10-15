class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        head = 0 
        tail = len(numbers) - 1
        while numbers[head] + numbers[tail] != target:
            if numbers[head] + numbers[tail] > target:
                tail -= 1
            else:
                head += 1
        return [head+1, tail+1]

test = Solution()
print test.twoSum([2, 7, 11, 15], 9)