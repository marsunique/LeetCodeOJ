class Solution(object):
    def reverseString(self, s):
        slist = list(s)
        l = len(s)
        for i in range(0,l/2):
            temp = slist[i]
            print 'temp: ', temp
            slist[i] = slist[l-1-i]
            print slist[i]
            slist[l-1-i] = temp
        return ''.join(slist)

        # Or use slicing
        # s = s[::-1]
        # return s
test=Solution()
print test.reverseString('nihao shabi')
