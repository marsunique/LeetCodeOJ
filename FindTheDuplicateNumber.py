class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # reference: https://segmentfault.com/a/1190000003817671
        # length of num is n + 1, range is 1 to n
        # find the middle of range, if count of (number < middle) > middle, search lower half range
        # else search upper half range
        low = 1 
        high =  len(nums) - 1
        while low < high:
            mid = (low + high)/2
            count = 0
            # count number small or equal to mid
            for num in nums:
                if num <= mid:
                    count += 1
            if count > mid:
                # search low half range
                high = mid
            else:
                # search upper half range
                low = mid + 1
        return low

test = Solution()
print test.findDuplicate([1,2,3,4,5,5,5,6,7])