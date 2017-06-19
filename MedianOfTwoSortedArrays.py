class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        
        # Use the idea of finding K th small element in two arrays.

        total_len = len(nums1) + len(nums2)
        if total_len % 2:
            # total_len is odd
            return self.findKthSmall(nums1, nums2, total_len/2+1)
        else:
            # total_len is even
            return (self.findKthSmall(nums1, nums2, total_len/2)
                        + self.findKthSmall(nums1, nums2, total_len/2+1)) / 2.0
        

    def findKthSmall(self, nums1, nums2, k):
        len_1 = len(nums1)
        len_2 = len(nums2)
        if len_2 > len_1:
            # always make nums1 is the longer one
            return self.findKthSmall(nums2, nums1, k)
        else:
            # divide k into 2 parts, one is k/2, one is k-k/2
            k1 = k/2
            k2 = min(k - k1, len_2)

            # edge cases
            # the shorter array is []
            # k == 1
            # nums1[k1-1] and nums2[k2-1] are equal, nums2 must be longer than k-k1 (means it has enough elements).

            if len_2 == 0:
                return nums1[k-1]
            if k == 1:
                return min(nums1[0], nums2[0])
            if k-k1 <= len_2 and nums1[k1-1] == nums2[k2-1]:
                # if nums2 is longer than original k2 and nums1[k1-1] == nums2[k2-1]
                return nums1[k1-1] # nums2[k2-1]
            
            # cut the smaller part
            if nums1[k1-1] < nums2[k2-1]:
                return self.findKthSmall(nums1[k1:], nums2, k-k1)
            else:
                return self.findKthSmall(nums1, nums2[k2:], k-k2)
            
nums1 = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22]
nums2 = [0,6]
test = Solution()
print test.findMedianSortedArrays(nums1, nums2)