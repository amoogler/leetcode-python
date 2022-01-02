class Solution:
    def rob(self, nums: List[int]) -> int:
        # We can only rob either house 0 or house N - 1.
        # The problem is equal to rob house 0 to house N -2 or
        # rob house 1 to house N - 1.

        N = len(nums)
        dp = [[0] * 2 for _ in range(N)]

        if N == 0:
            return 0

        if N == 1:
            return nums[0]

        dp[0][0] = 0
        dp[0][1] = nums[0]

        for i in range(1, N - 1):
            dp[i][0] = max(dp[i - 1][1], dp[i - 1][0])
            dp[i][1] = dp[i - 1][0] + nums[i]

        dp1 = max(dp[N - 2][0], dp[N - 2][1])

        dp[1][0] = 0
        dp[1][1] = nums[1]

        for i in range(2, N):
            dp[i][0] = max(dp[i - 1][1], dp[i - 1][0])
            dp[i][1] = dp[i - 1][0] + nums[i]

        dp2 = max(dp[N - 1][0], dp[N - 1][1])

        return max(dp1, dp2)
