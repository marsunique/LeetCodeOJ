class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        # res = [[]]
        # for num in nums:
        #     temp = [[],[num]]
        #     res = [sub+s for sub in res for s in temp]
        # return res

        res = [[]]
        for num in nums:
            temp = [[], [num]]
            r = []
            for candidate in temp:
                for sub in res:
                    r.append(sub+candidate)
            res = r
        return res

        

test = Solution()
print test.subsets([1,2,3,4])