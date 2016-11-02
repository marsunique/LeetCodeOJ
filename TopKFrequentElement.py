class Solution(object):
    def buildHeap(self, array):
        length = len(array)
        for i in range(length/2-1, -1, -1):
            print i
            print 'before', array
            self.Heapify(array,i)
            print 'after', array
    def Heapify(self, array, i):
        length = len(array)
        if (i+1)*2 < length:
            if array[(i+1)*2 - 1][1] > array[i][1] or array[(i+1)*2][1] > array[i][1]:
                if array[(i+1)*2 - 1][1] > array[(i+1)*2][1]:
                    bigger_child = (i+1)*2 - 1
                else:
                    bigger_child = (i+1)*2
                array[i], array[bigger_child] = array[bigger_child], array[i]
                self.Heapify(array,bigger_child)
        elif (i+1)*2-1 < length:
            if array[(i+1)*2 - 1][1] > array[i][1]:
                bigger_child = (i+1)*2 - 1
                array[i], array[bigger_child] = array[bigger_child], array[i]
                self.Heapify(array, bigger_child)
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        dic = {}
        for num in nums:
            dic.setdefault(num, 0)
            dic[num] += 1
        dic = [[key,dic[key]] for key in dic]
        print dic
        self.buildHeap(dic)
        print dic
        result = []
        for j in range(0,k):
            last = len(dic) - 1
            dic[0], dic[last] = dic[last], dic[0]
            result.append(dic.pop()[0])
            self.Heapify(dic, 0)
        return result

test=Solution()
nums=[3,2,3,1,2,4,5,5,6,7,7,8,2,3,1,1,1,10,11,5,6,2,4,7,8,5,6]
print test.topKFrequent(nums, 10)