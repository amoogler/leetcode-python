class Solution:
    def findKDistantIndices(self, nums: List[int], key: int, k: int) -> List[int]:
        keys = [i for i in range(len(nums)) if nums[i] == key]
        res = []

        if not keys:
            return res

        for i in range(len(nums)):
            for k_idx in keys:
                if abs(i - k_idx) <= k:
                    res.append(i)
                    break

        return res
