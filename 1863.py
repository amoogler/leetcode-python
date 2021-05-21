class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        def backtrack(start_idx: int, subset_xor: int):
            total[0] += subset_xor

            for i in range(start_idx, len(nums)):
                subset_xor ^= nums[i]
                backtrack(i + 1, subset_xor)
                subset_xor ^= nums[i]

        total = [0]
        backtrack(0, 0)

        return total[0]
