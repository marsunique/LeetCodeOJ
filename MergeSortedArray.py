class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        # insert from the end of nums1
        while m and n:
            if nums1[m-1] > nums2[n-1]:
                nums1[m+n-1] = nums1[m-1]
                m -= 1
            else:
                nums1[m+n-1] = nums2[n-1]
                n -= 1
        if n:
            nums1[:n] = nums2[:n]

test = Solution()
nums1 = [1,3,4,None,None,None]
nums2 = [2,5,6]
m = 3
n = 3
test.merge(nums1,m,nums2,n)
print nums1