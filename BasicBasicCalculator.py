# Only have +, -, no parenthesis
def calculate1(expression):
    expression += '#'
    operand1 = None
    operand2 = None
    operator = None
    num = 0
    for ch in expression:
        if ch.isdigit():
            num = num * 10 + int(ch)
        else:
            # ch is a sign
            if operand1 is None:    # put num in op1
                operand1 = num
            else:                   # put num in op2
                operand2 = num
                if operator == '+':
                    operand1 += operand2
                else:
                    operand1 -= operand2
            # reset num, update optr to ch
            num = 0
            operator = ch         
    return operand1

print calculate1('12+85-34+11+222+234-500')


# Have +, -, *, /, no parenthesis
def calculate2(expression):
    expression += '#'
    opnd_stack =[]
    optr_stack = []
    priority = {
        ('+','+'): True, ('+','-'): True, ('+','*'): False, ('+','/'): False,
        ('-','+'): True, ('-','-'): True, ('-','*'): False, ('-','/'): False,
        ('*','+'): True, ('*','-'): True, ('*','*'): True, ('*','/'): True,
        ('/','+'): True, ('/','-'): True, ('/','*'): True, ('/','/'): True
    }
    num = 0
    for ch in expression:
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
                optr = optr_stack[-1]
                # optr > ch, calculate optr
                if priority[(optr, ch)]:
                    tmp = doit(opnd_stack, optr_stack)

                optr_stack.append(ch)

    while optr_stack:
        doit(opnd_stack, optr_stack)
    return opnd_stack[0]

def doit(opnd_stack, optr_stack):
    num2 = opnd_stack.pop()
    num1 = opnd_stack.pop()
    optr = optr_stack.pop()
    res = 0
    if optr == '+':
        res = num1 + num2
    elif optr == '-':
        res = num1 - num2
    elif optr == '*':
        res = num1 * num2
    else:
        res = num1 / num2
    opnd_stack.append(res)

print calculate2('11-6+2*3+50/10*2+12')