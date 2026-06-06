class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        for i in range(len(prices) - 1):
            l, r = i, len(prices) - 1
            while l < r:
                val = prices[r] - prices[l]
                if val > 0:
                    profit = max(profit, val)
                r -= 1 
            r = len(prices) - 1

        return profit