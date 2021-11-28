class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        presum = { -1 : 0 }
        total = 0
        N = len(nums)
        res = []

        # Calculate pre-sum.
        for i, num in enumerate(nums):
            total += num
            presum[i] = total

        for i in range(N):
            if i - k < 0 or i + k >= N:
                res.append(-1)
            else:
                res.append((presum[i + k] - presum[i - k - 1]) // (2 * k + 1))

        return res
