class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ''
        res = ''
        for i in range(len(strs[0])):
            letter = strs[0][i]
            for string in strs:
                if i < len(string) and letter == string[i]:
                    continue
                else:
                    return res
            res += letter
        return res

test = Solution()
print test.longestCommonPrefix([])