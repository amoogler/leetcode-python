class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        hold, sold = float('-inf'), 0

        for price in prices:
            prev_hold, prev_sold = hold, sold
            hold = max(prev_hold, prev_sold - price)
            sold = max(prev_sold, prev_hold + price - fee)

        return max(0, hold, sold)
