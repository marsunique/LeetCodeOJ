class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices:
            return 0
        res = 0
        buy = prices[0]
        for sell in prices:
            if sell - buy < 0:
                buy = sell
            else:
                res = max(res, sell-buy)
        return res

test = Solution()
print test.maxProfit([7,5,4,2])