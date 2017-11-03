# print out the repeated part of the division of two numbers
# Solution: find the repeated remainder

def repetend(x, y):
    dic = {}
    quotient = x/y
    remainder = x%y
    pos = 1 # record the position after decimal point
    while True:
        remainder = remainder * 10
        quotient = remainder/y
        remainder = remainder%y
        if remainder in dic:
            length = pos - dic[remainder]
            break
        else:
            dic[remainder] = pos
            pos += 1
    res = str(quotient)
    # res already has the first number, therefore loop length-1 times
    for i in range(0, length-1):
        remainder = remainder * 10
        quotient = remainder/y
        remainder = remainder%y
        res += str(quotient)
    return res

print repetend(1,7)
