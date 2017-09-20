class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        s = s.strip().split(' ')
        print s
        if not s:
            return 0
        else:
            return len(s[-1])
        
test = Solution()
print test.lengthOfLastWord('a bfb  ')