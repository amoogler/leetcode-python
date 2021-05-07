class Solution:
    def createTargetArray(self, nums: List[int], index: List[int]) -> List[int]:
        N = len(nums)
        res = [0] * N

        for i in range(N):
            for j in range(N - 1, index[i], -1):
                res[j] = res[j - 1]

            res[index[i]] = nums[i]

        return res
