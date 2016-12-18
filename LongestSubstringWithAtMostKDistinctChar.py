class Solution(object):
    def lengthOfLongestSubstringKDistinct(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        if k == 0:
            return 0
        dic = {}
        res = 0
        end = 0
        # add s[end] into the dict, remove one s[start] from dict and start++
        for start in range(len(s)):
            while end < len(s):
                print start, s[start], dic, end, s[end]
                if s[end] in dic:
                    dic[s[end]] += 1
                    end += 1
                else:
                    if len(dic) < k:
                        dic.setdefault(s[end], 0)
                        dic[s[end]] += 1
                        end += 1
                    else:
                        dic[s[start]] -= 1
                        if dic[s[start]] == 0:
                            del(dic[s[start]])
                        break
            res = max(res, end-start)
        return res

test = Solution()
print test.lengthOfLongestSubstringKDistinct('abaccc',2)