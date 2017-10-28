class Solution(object):
    def maxCount(self, m, n, ops):
        """
        :type m: int
        :type n: int
        :type ops: List[List[int]]
        :rtype: int
        """
        min_x = float('inf')
        min_y = float('inf')
        for op in ops:
            min_x = min(min_x, op[0])
            min_y = min(min_y, op[1])
        return min(min_x*min_y, m*n)
