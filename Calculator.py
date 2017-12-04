# similar to LC 224
# Have +, -, *, /, and '(', ')'

class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        s = s.replace(' ', '')
        res = self.helper(s)
        return res
    def helper(self, s):
        s += '#'
        stack = []
        sign = '+'
        num = 0
        i = 0
        while i < len(s):
            if s[i].isdigit():
                num = num * 10 + int(s[i])
                i += 1
            
            elif s[i] == '(':
                flag = 0
                for j in range(i, len(s)):
                    if s[j] == '(':
                        flag += 1
                    if s[j] == ')':
                        flag -= 1
                    if flag == 0:
                        break
                num = self.helper(s[i+1:j])
                i = j+1
             
            else:
                if sign == '+':
                    stack.append(num)
                elif sign == '-':
                    stack.append(-num)
                elif sign == '*':
                    temp = stack.pop()
                    stack.append(temp*num)
                elif sign == '/':
                    temp = stack.pop()
                    if temp < 0:
                        stack.append(-(abs(temp)/num))
                    else:
                        stack.append(temp/num)
                num = 0
                sign = s[i]
                i += 1
        return sum(stack)

test = Solution()
print test.calculate('11-6+2*3+50/10*2+12')
print test.calculate("1*2-3/4+5*6-7*8+9/10")
print test.calculate('1*(1+1)-4/(2-1)')