class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def helper(start_idx: int, subset: List[int]):
            subsets.append(subset[:])

            for i in range(start_idx, len(nums)):
                subset.append(nums[i])
                helper(i + 1, subset)
                subset.pop()

        subsets = []
        helper(0, [])
        return subsets
