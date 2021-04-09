class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        distinct = 0

        for iterator in range(len(nums)):
            if nums[distinct] != nums[iterator]:
                distinct += 1
                nums[distinct] = nums[iterator]

        return distinct + 1
