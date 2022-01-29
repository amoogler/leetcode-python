# 1. Allocate an array to represent answer to the problem for a given state.
# 2. Find the transition between states. (i.e. transition function)
# 3. Create base case.
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        N = len(nums)
        dp = [1] * N

        for i in range(1, N):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1)

        return max(dp)
