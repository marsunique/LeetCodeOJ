class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack = []
        curNum = 0
        curStr = ''
        for char in s:
            if char.isdigit():
                curNum = curNum*10 + int(char)
            elif char == '[':
                stack.append(curStr)
                stack.append(curNum)
                curStr = ''
                curNum = 0
            elif char == ']':
                num = stack.pop()
                preStr = stack.pop()
                curStr = preStr + num*curStr
            else:
                curStr += char
        return curStr

test = Solution()
print test.decodeString('3[2[c]]')