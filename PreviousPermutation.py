class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        if not nums:
            return None
        i = 0
        k = -1
        while i < len(nums)-1:
            if nums[i+1] < nums[i]:
                k = i
            i += 1
        if k == -1:
            nums.sort(reverse=True)
            return
        else:
            l = 0
            for j in range(len(nums)-1,k,-1):
                if nums[j] < nums[k]:
                    l = j
                    break
        nums[k], nums[l] = nums[l], nums[k]
        nums[k+1:] = sorted(nums[k+1:], reverse=True)
        return

test = Solution()
a = [1,2,3,4]
test.nextPermutation(a)
print a