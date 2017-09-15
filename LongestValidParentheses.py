class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        # use stack pop out all pairable parentheses, the difference between 
        # index of left ones are length
        stack = []
        for i in range(len(s)):
            if not stack:
                stack.append(i)
            elif s[i] != s[stack[-1]] and s[i] == ')':
                stack.pop()
            else:
                stack.append(i)
        stack.insert(0, -1)
        stack.append(len(s))
        res = 0
        for i in range(1, len(stack)):
            res = max(res, stack[i]-stack[i-1]-1)
        print stack
        return res


test = Solution()
print test.longestValidParentheses(')()())')
