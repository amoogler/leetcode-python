class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        N = len(nums)
        nums.sort()
        min_diff = float('inf')
        res = 0

        for i in range(N - 2):
            l, r = i + 1, N - 1

            while l < r:
                s = nums[i] + nums[l] + nums[r]

                if abs(s - target) < min_diff:
                    min_diff = abs(s - target)
                    res = s

                if s > target:
                    r -= 1
                elif s < target:
                    l += 1
                else:
                    return s
        return res
