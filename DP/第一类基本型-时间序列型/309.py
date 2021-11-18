class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        N = len(prices)

        if N < 2:
            return 0

        hold, sold, sold1day = float('-inf'), 0, 0

        for i in range(N):
            prev_hold, prev_sold, prev_sold1day = hold, sold, sold1day
            price = prices[i]

            hold = max(prev_hold, prev_sold1day - price)
            sold = max(prev_hold + price, prev_sold)
            sold1day = prev_sold

        return max(0, sold)
