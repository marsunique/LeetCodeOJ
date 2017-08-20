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
        res = 0
        for end in range(len(s)):
            if s[end] in dic and dic[s[end]] >= start:  # repeating character
                # update res
                res = max(end-start, res)
                # update new start position
                start = dic[s[end]] + 1
                # update dic
                dic[s[end]] = end
            else:
                dic[s[end]] = end
                res = max(end-start+1, res)
        return res

test = Solution()
print test.lengthOfLongestSubstring('abbac')