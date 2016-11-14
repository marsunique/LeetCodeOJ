class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        s = '1'
        for k in range(n-1):
            temp = ''
            i = 0
            j = 0
            while j < len(s):
                if s[i] == s[j]:
                    j += 1
                    continue
                else:
                    temp = temp + str(j-i) + s[i]
                    i = j
                    j += 1
            temp = temp + str(j-i) + s[i]
            s = temp
        return s

test = Solution()
print test.countAndSay(4)