# DP
class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        length = len(s)
        dp = [([None]*length)for i in range(length)]
        for i in range(length):
            dp[i][i] = True
        start = 0
        end = 0
        for i in range(length-2, -1, -1):
            for j in range(i+1, length):
                if j - i == 1:
                    if s[i] == s[j]:
                        dp[i][j] = True
                        # update start and end position
                        if end - start < j - i:
                            start = i
                            end = j
                elif dp[i+1][j-1] and s[i] == s[j]:
                    dp[i][j] = True
                    # update start and end position
                    if end - start < j - i:
                            start = i
                            end = j
        return s[start:end+1]

# Expand from center
class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        import math
        length = len(s)
        start = 0
        end = 0
        for i in range(length-1):
            # odd
            low = i - 1
            high = i + 1
            while low >= 0 and high < length and s[low] == s[high]:
                low -= 1
                high += 1
            if high - low - 2 > end - start:
                start = low + 1
                end = high - 1
            # even
            low = i
            high = i + 1
            while low >= 0 and high < length and s[low] == s[high]:
                low -= 1
                high += 1
            if high - low - 2 > end - start:
                start = low + 1
                end = high - 1
        return s[start:end+1]

test = Solution()
print test.longestPalindrome('aaabaaaa')