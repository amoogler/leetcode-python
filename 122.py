class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0

        for num1, num2 in zip(prices, prices[1:]):
            if num2 > num1:
                max_profit += num2 - num1

        return max_profit
