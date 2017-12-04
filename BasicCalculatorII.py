# LC 227
# Have +, -, *, /, no parenthesis
class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        s = s.replace(' ', '')
        s += '#'
        stack = []
        sign = '+'
        num = 0
        for ch in s:
            if ch.isdigit():
                num = num * 10 + int(ch)
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
                sign = ch
        return sum(stack)

test = Solution()
print test.calculate('11-6+2*3+50/10*2+12')
print test.calculate("1*2-3/4+5*6-7*8+9/10")
print test.calculate('1-3/4')
print -4/3



class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        s = s.replace(' ', '')
        s += '#'
        opnd_stack =[]
        optr_stack = []
        priority = {
            ('+','+'): True, ('+','-'): True, ('+','*'): False, ('+','/'): False,
            ('-','+'): True, ('-','-'): True, ('-','*'): False, ('-','/'): False,
            ('*','+'): True, ('*','-'): True, ('*','*'): True, ('*','/'): True,
            ('/','+'): True, ('/','-'): True, ('/','*'): True, ('/','/'): True
        }
        num = 0
        for ch in s:
            if ch.isdigit():
                num = num * 10 + int(ch)
            else:
                opnd_stack.append(num)
                num = 0
                if ch == '#':
                    break
                    
                # if optr_stack is empty, append
                if not optr_stack:
                    optr_stack.append(ch)

                # compare priority
                else:
                    for i in range(len(optr_stack)):
                        optr = optr_stack[-1]
                        # optr > ch, calculate optr
                        if priority[(optr, ch)]:
                            self.doit(opnd_stack, optr_stack)
                        else:
                            break
                    optr_stack.append(ch)

        while optr_stack:
            self.doit(opnd_stack, optr_stack)
        return opnd_stack[0]
    def doit(self, opnd_stack, optr_stack):
        num2 = opnd_stack.pop()
        num1 = opnd_stack.pop()
        optr = optr_stack.pop()
        if optr == '+':
            num1 += num2
        elif optr == '-':
            num1 -= num2
        elif optr == '*':
            num1 *= num2
        else:
            num1 /= num2
        opnd_stack.append(num1)
        
test = Solution()
print test.calculate('11-6+2*3+50/10*2+12')
print test.calculate("1*2-3/4+5*6-7*8+9/10")
