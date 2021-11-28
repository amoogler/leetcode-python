class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        res = []
        sorted_nums = sorted(nums)

        for idx, num in enumerate(sorted_nums):
            if num == target:
                res.append(idx)

        return res
