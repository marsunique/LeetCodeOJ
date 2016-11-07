class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        dic = {}
        res = []
        for num in nums1:
            dic.setdefault(num, 0)
            dic[num] = 1
        for num in nums2:
            if dic.has_key(num) and dic[num] > 0:
                res.append(num)
                dic[num] = 0
        return res
num1 = [1,2,2,2,3,4,5]
num2 = [2,1,3,2,3]
test = Solution()
print test.intersection(num1,num2)