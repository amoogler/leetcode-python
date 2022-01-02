class Solution:
    def rob(self, nums: List[int]) -> int:
        N = len(nums)
        dp = [[0] * 2 for _ in range(N)]

        if N == 0:
            return 0

        if N == 1:
            return nums[0]

        dp[0][0] = 0
        dp[0][1] = nums[0]

        # dp[i][j] represents max benefit at house i when rob - 1 or not - 0.
        for i in range(1, N):
            dp[i][1] = dp[i - 1][0] + nums[i]
            dp[i][0] = max(dp[i - 1][1], dp[i - 1][0])

        return max(dp[N - 1][1], dp[N - 1][0])
