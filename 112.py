class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_value = prices[0]
        max_profit = 0

        for i in range(1, len(prices)):

            if prices[i - 1] < prices[i]:
                max_profit = max(max_profit, prices[i] - min_value)
            else:
                min_value = min(min_value, prices[i])

        return max_profit
