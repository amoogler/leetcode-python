class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        N = len(prices)
        dp = [[0] * 4 for _ in range(N)]

        # States:
        # 0 - hold stock1
        # 1 - sell stock1
        # 2 - hold stock2
        # 3 - sell stock2
        # dp[i][j] represents max profit at ith day when state is in j.

        dp[0][0] = -prices[0]
        dp[0][1] = float('-inf')
        dp[0][2] = float('-inf')
        dp[0][3] = float('-inf')

        for i in range(1, N):
            price = prices[i]
            dp[i][0] = max(dp[i - 1][0], -price)
            dp[i][1] = max(dp[i - 1][1], dp[i - 1][0] + price)
            dp[i][2] = max(dp[i - 1][2], dp[i - 1][1] - price)
            dp[i][3] = max(dp[i - 1][3], dp[i - 1][2] + price)

        return max(0, dp[N - 1][1], dp[N - 1][3])
