# Check whether a number is power of 2.
# use bitwise operation
def powerOfTwo(n):
    tester = 1
    origin = n
    while True:
        if (n & 1):
            if tester == origin:
                return True
            else:
                return False
        else:
            n = n >> 1
            tester = tester << 1

print powerOfTwo(4096)