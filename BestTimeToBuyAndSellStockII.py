class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices:
            return 0
        total_profit = 0
        profit = 0
        buy = prices[0]
        for sell in prices:
            if sell - buy < profit:
                total_profit += profit
                buy = sell
                profit = 0
            else:
                profit = sell - buy
        total_profit += profit
                
        return total_profit

test = Solution()
print test.maxProfit([6,1,3,2,4,7])