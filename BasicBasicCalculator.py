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
