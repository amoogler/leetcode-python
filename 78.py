class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        subsets = []
        self.helper(nums, 0, [], subsets)
        return subsets

    def helper(self, nums: List[int], start_idx: int, subset: List[int], subsets: List[List[int]]):
        subsets.append(subset)

        for i in range(start_idx, len(nums)):
            self.helper(nums, i + 1, subset + [nums[i]], subsets)
