class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        l, r, L = 0, 0, len(nums)
        window = defaultdict(int)
        res = 0

        while r < L:
            window[nums[r]] += 1
            r += 1

            while window[0] > k:
                window[nums[l]] -= 1
                l += 1

            res = max(res, r - l)

        return res
