class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        for bracket in s:
            if bracket == '(' or bracket == '{' or bracket == '[':
                stack.append(bracket)
            elif stack == []:   # facing a '(', '[' or '{' but stack is empty
                return False
            elif bracket == ')':
                if stack.pop() != '(':
                    return False
            elif bracket == '}':
                if stack.pop() != '{':
                    return False
            elif bracket == ']':
                if stack.pop() != '[':
                    return False
        if len(stack):  # stack is not empty
            return False
        return True

test=Solution()
s = ['[',']','[','{','(',')','[',']','}',']']
print test.isValid(s)