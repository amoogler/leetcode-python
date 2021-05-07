class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        total_profit = 0

        for num1, num2 in zip(prices, prices[1:]):
            if num2 > num1:
                total_profit += num2 - num1

        return total_profit
