class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        result = 0
        for element in s+t:
            result = result ^ ord(element)
        return chr(result)
test = Solution()
print test.findTheDifference('abcd','abecd')