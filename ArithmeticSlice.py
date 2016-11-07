class Solution(object):
    def numberOfArithmeticSlices(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        length = len(A)
        if length < 3:
            return 0
        head = 0
        tail = 2
        count = 0
        while (head <= length - 3) and (tail <= length - 1): #the index of third last element is (length-1)-2 
            if A[tail] - A[tail-1] == A[tail-1] - A[tail-2]:
                tail += 1
            else:
                if tail - head >= 3:
                    count += self.countArithmetic(tail-head) # actually is (tail-1)-head+1
                head = tail - 1
                tail += 1
        if tail - head >= 3:
            count += self.countArithmetic(tail-head)
        return count
    
    def countArithmetic(self, length):
        return (length-1)*(length-2)/2



test=Solution()
print test.numberOfArithmeticSlices([1,2,3,8,9,10])
