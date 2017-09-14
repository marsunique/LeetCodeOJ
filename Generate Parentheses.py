class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        Using recursive, like a tree
                     (
                  /     \
                (         )
              /   \
            (       )
             \
               )
               ...
        """
        res = []
        self.helper(n, 0, '', res)
        return res

    def helper(self, left_num, balance, string, res):
        """
        left_num: number of available left parenthese
        balance: difference of left and right parenthese in the string, 
        0 is balanced, can only add left
        """
        if balance == 0:
            if left_num > 0:
                self.helper(left_num-1, balance+1, string+'(', res)
            else:
                res.append(string)
        else:
            if left_num > 0:
                self.helper(left_num-1, balance+1, string+'(', res)
            self.helper(left_num, balance-1, string+')', res)

test = Solution()
print test.generateParenthesis(3)
