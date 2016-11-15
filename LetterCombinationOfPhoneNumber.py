# Iteration version
class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        dic = {
            '2': 'abc', 
            '3': 'def', 
            '4': 'ghi', 
            '5': 'jkl', 
            '6': 'mno', 
            '7': 'pqrs', 
            '8': 'tuv', 
            '9': 'wxyz'
        }
        if len(digits) == 0:
            return []
        res = ['']
        for digit in digits:
            if digit == '1':
                continue
            letters = dic[digit]
            res = [head + tail for head in res for tail in letters]
        return res
test = Solution()
print test.letterCombinations('23')

# Recursive version
class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        dic = {
            '2': 'abc', 
            '3': 'def', 
            '4': 'ghi', 
            '5': 'jkl', 
            '6': 'mno', 
            '7': 'pqrs', 
            '8': 'tuv', 
            '9': 'wxyz'
        }
        if len(digits) == 0:
            return []
        if len(digits) == 1:
            return [s for s in dic[digits]]
        head = digits[:1]
        tail = digits[1:]
        temp = dic[head]
        return [c + s for c in temp for s in self.letterCombinations(tail)]
    
test = Solution()
print test.letterCombinations('23')

# DFS
class Solution(object):
    def __init__(self):
        self.dic = {
            '2': 'abc', 
            '3': 'def', 
            '4': 'ghi', 
            '5': 'jkl', 
            '6': 'mno', 
            '7': 'pqrs', 
            '8': 'tuv', 
            '9': 'wxyz'
        }
    def dfs(self, digits, position, res, s):
        if position >= len(digits):
            res.append(s)
        elif digits[position] == '1':
            pass
        else:
            for letter in self.dic[digits[position]]:
                if letter != self.dic[digits[position]][0]:
                    s = s[:-1]
                    # if it's not the first letter of each figure, backtrace 1 position. e.g. a -> ad -> a(d)e
                s = s + letter
                self.dfs(digits, position+1, res, s)
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        
        if digits == '':
            return []
        res = []
        self.dfs(digits,0,res,'')
        return res
test = Solution()
print test.letterCombinations('23')