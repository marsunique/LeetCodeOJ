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
        temp = list(dic[head])
        return [c + s for c in temp for s in self.letterCombinations(tail)]
    
test = Solution()
print test.letterCombinations('23')