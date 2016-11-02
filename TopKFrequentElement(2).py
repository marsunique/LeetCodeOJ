class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        dic = {}
        for num in nums:
            dic.setdefault(num, 0)
            dic[num] += 1
        dic = sorted(dic.items(), key=lambda d:d[1], reverse=True)
        dic = dic[:k]
        result = []
        for item in dic:
            result.append(item[0])
        return result

test=Solution()
nums=[1,1,1,2,2,3]
print test.topKFrequent(nums, 2)