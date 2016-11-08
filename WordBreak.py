# This is a DP question
# str[:i] can be broken if from a index where is d[index] is true to d[i] is a word in wordDict
class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: Set[str]
        :rtype: bool
        """
        if not len(wordDict): # wordDict=[]
            return False
        d = [False] * len(s) # d[i] means str[:i] can be broken into words.
        true_index = [-1] # list that contains index where str[:index] can be broken into words. Initial:-1
        for tail in range(0,len(s)):
            for head in true_index:
                copy = s[head+1:tail+1]
                for word in wordDict:
                    if word == copy:
                        d[tail] = True
                        true_index.insert(0, tail)
                        break
                if word == copy:
                    break
        return d[len(s)-1]

test = Solution()
d = []
s = 'a'
print test.wordBreak(s,d)