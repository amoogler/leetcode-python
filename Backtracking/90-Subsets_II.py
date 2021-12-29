class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        subsets = []
        sorted_nums = sorted(nums)

        def backtrack(subset: List[int], start_idx: int) -> None:
            subsets.append(subset[:])

            for i in range(start_idx, len(sorted_nums)):
                if i > start_idx and sorted_nums[i] == sorted_nums[i - 1]:
                    continue

                subset.append(sorted_nums[i])
                backtrack(subset, i + 1)
                subset.pop()

        backtrack([], 0)
        return subsets
