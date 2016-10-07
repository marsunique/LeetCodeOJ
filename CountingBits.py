class Solution(object):
    def countBits(self, num):
        List=[]
        for number in range(num+1):
            count = 0
            while number:
                remainder = number%2
                number = number/2
                if remainder:
                    count = count+1
            List.append(count)
        return List

test = Solution()
List = test.countBits(8)
print List