# Check whether a number is power of 2.
# use bitwise operation
# If n is power of 2, n-1 will 0111...111
def powerOfTwo(n):
    if n <= 0:
        return False
    return not (n & n-1)

print powerOfTwo(4096)