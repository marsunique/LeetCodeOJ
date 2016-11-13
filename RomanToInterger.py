class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        dic = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
        index = 0
        res = 0
        for index in range(len(s)):
            if index and dic[s[index]] > dic[s[index-1]]:
                res = res - 2*dic[s[index-1]] +dic[s[index]]
            else:
                res += dic[s[index]]
        return res
        
test = Solution()
print test.romanToInt('IV')