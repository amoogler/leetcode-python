class Solution:
    def minimumDeletions(self, nums: List[int]) -> int:
        min_idx, max_idx, N = 0, 0, len(nums)

        for i, num in enumerate(nums):
            if num < nums[min_idx]:
                min_idx = i

            if num > nums[max_idx]:
                max_idx = i

        # Three cases:
        # 1. Both numbers will be removed from the front.
        # 2. Both numbers will be removed from the back.
        # 3. One number will be removed from the front,
        #    the other will be removed from the back.
        return min(max(min_idx + 1, max_idx + 1), \
                   max(N - min_idx, N - max_idx), \
                   min_idx + 1 + N - max_idx, \
                   max_idx + 1 + N - min_idx)
