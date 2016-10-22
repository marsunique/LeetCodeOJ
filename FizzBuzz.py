class Solution(object):
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        return ['FizzBuzz' if (i%15 == 0) else ('Fizz' if (i%3 == 0) else ('Buzz' if (i%5 == 0) else (str(i))))for i in range(1, n+1)]
        
test = Solution()
print test.fizzBuzz(30)
s = [1,2,3]
print i for i in s