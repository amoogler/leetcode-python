class Solution:
    def maximumSum(self, arr: List[int]) -> int:
        N = len(arr)
        dp = [[0] * 2 for _ in range(N)]
        res = float('-inf')

        # States
        # 0 - represents deletion is not happened yet
        # 1 - represents deletion has happened
        # dp[a][b] - represents max subarray at index a upon state b

        dp[0][0] = arr[0]
        dp[0][1] = float('-inf')
        res = max(res, dp[0][0], dp[0][1])

        for i in range(1, N):
            dp[i][0] = max(arr[i], dp[i - 1][0] + arr[i])
            dp[i][1] = max(dp[i - 1][0], dp[i - 1][1] + arr[i], arr[i])
            res = max(res, dp[i][0], dp[i][1])

        return res
