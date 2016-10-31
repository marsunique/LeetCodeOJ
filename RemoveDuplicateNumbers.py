class Solution(object):
    def removeDuplicate(self, li):
        li.sort()
        print li
        i = 0
        j = 0
        for k in range(0,len(li)):
            if i == 0:
                i += 1
                continue
            else:
                if li[i] == li[j]:
                    del(li[i])
                else:
                        j = i
                        i += 1
        return li
li = [1,2,3,3,2,4,7,4,3,4,2,1,2,2,1,1,1,1,3]
test = Solution()
print test.removeDuplicate(li)
