# Backtracking + Memoization solution.
class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        total = sum(nums)
        nums = sorted(nums, reverse=True)
        self.T = total // k
        used = ['0'] * len(nums)
        memo = {}

        if total % k != 0:
            return False

        def backtrack(remain, target, start) -> bool:
            # Base cases.
            if remain == 1:
                return True

            if target < 0:
                return False

            used_string = ''.join(used)

            if used_string in memo:
                return memo[used_string]

            if target == 0:
                memo[used_string] = backtrack(remain - 1, self.T, 0)
                return memo[used_string]

            # Recusive steps.
            for i in range(start, len(nums)):
                if used[i] == '1' or nums[i] > target:
                    continue

                used[i] = '1'

                if backtrack(remain, target - nums[i], i + 1):
                    return True

                used[i] = '0'

            memo[used_string] = False
            return memo[used_string]

        return backtrack(k, self.T, 0)
