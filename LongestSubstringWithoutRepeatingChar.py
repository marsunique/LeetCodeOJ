class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        # use dictionary to record the last position of a character between position start and end;
        # if the character is in the dictionary and its position is bigger than start, means it is in the current substring;
        # if the character is not in the dictionary or it is in the dict but its position is smaller than start, means it is not in the current substring.
        dic = {}
        start = 0
        end = 0
        res = 0
        while end < len(s):
            if s[end] in dic and dic[s[end]] >= start:
                pos = dic[s[end]]
                dic[s[end]] = end
                res = max(end-start, res)
                start = pos + 1
            else:
                dic[s[end]] = end
            end += 1
        return max(end-start, res)

test = Solution()
print test.lengthOfLongestSubstring('abba')