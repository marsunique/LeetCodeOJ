class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        res = ''
        if not strs:
            return res
        for i in range(len(strs[0])):
            for j in range(1, len(strs)):
                if i >= len(strs[j]) or strs[0][i] != strs[j][i]:
                    return strs[0][0:i]
        return strs[0]

'''time complexity is O(mn), m is the shortest length among strs,'''
'''n is the number of strs'''

test = Solution()
print test.longestCommonPrefix([])