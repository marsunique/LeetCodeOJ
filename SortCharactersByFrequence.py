class Solution(object):
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        dic = {}
        for char in s:
            dic.setdefault(char, 0)
            dic[char] += 1
        dic = sorted(dic.items(), key=lambda d:d[1], reverse=True)
        s = ''
        for pair in dic:
            s += pair[0]*pair[1]
        return s

test=Solution()
print test.frequencySort('tree')
