class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        if sum(nums) < target:
            return 0

        l, r, L = 0, 0, len(nums)
        curr_sum = 0
        ans = float('inf')

        while r < L:
            curr_sum += nums[r]
            r += 1

            while curr_sum >= target:
                ans = min(ans, r - l)
                curr_sum -= nums[l]
                l += 1

        return ans
