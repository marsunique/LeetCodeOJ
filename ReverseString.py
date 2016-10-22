class Solution(object):
    def reverseString(self, s):
        slist = list(s)
        l = len(s)
        for i in range(0,l/2):
            # temp = slist[i]
            # print 'temp: ', temp
            # slist[i] = slist[l-1-i]
            # print slist[i]
            # slist[l-1-i] = temp
            slist[i] = chr(ord(slist[i]) ^ ord(slist[l-1-i]))
            slist[l-1-i] = chr(ord(slist[i]) ^ ord(slist[l-1-i]))
            slist[i] = chr(ord(slist[i]) ^ ord(slist[l-1-i]))
        return ''.join(slist)

        # Or use slicing
        # s = s[::-1]
        # return s
test=Solution()
print test.reverseString('nihao shabi')

''' Reverse a string without using any extra memory:
When swaping the value of head and tail part of string, it can use XOR to swap. Like swap a, b -> a=a+b -> b=a-b -> a=a-b
slist[i] ^= slist[l-1-i]
slist[i] ^= (slist[l-1-i] ^= slist[i])
'''