class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        N = len(nums)
        dp = [[0] * 2 for _ in range(N)]
        res = 0

        # States
        # 0 - no flip yet
        # 1 - flipped
        # dp[a][b] - at index a, the max consecutive ones upon state b.

        if nums[0] == 1:
            dp[0][0] = 1
            dp[0][1] = 1
        else:
            dp[0][0] = 0
            dp[0][1] = 1

        for i in range(1, N):
            if nums[i] == 1:
                dp[i][1] = dp[i - 1][1] + 1
                dp[i][0] = dp[i - 1][0] + 1
            else:
                dp[i][1] = dp[i - 1][0] + 1
                dp[i][0] = 0

        for i in range(N):
            for j in range(2):
                res = max(res, dp[i][j])

        return res
