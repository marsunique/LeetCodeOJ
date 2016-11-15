class Solution(object):
    def merge(self, array, f, mid, l):
        temp = [None]*(l-f+1)
        i, j = f, mid+1
        index = 0
        while i <= mid and j <= l:
            if array[i] < array[j]:
                temp[index] = array[i]
                i += 1
                index += 1
            else:
                temp[index] = array[j]
                j += 1
                index += 1
        if i > mid:
            for k in range(j,l+1):
                temp[index] = array[k]
                index += 1
        if j > l:
            for k in range(i,mid+1):
                temp[index] = array[k]
                index += 1
        array[f:l+1] = temp
    def split(self, array, f, l):
        if f < l:
            mid = (f+l)/2
            self.split(array, f, mid)
            self.split(array, mid+1, l)
            self.merge(array, f, mid, l)
    def mergeSort(self, array):
        res = [None] * len(array)
        self.split(array, 0, len(array)-1)
        return array

test = Solution()
print test.mergeSort([5,2,3,1,4,6,8,7])
