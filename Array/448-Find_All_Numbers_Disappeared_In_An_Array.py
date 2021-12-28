# Intuitive solution.
class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        nums_set = set(nums)
        return [i for i in range(1, len(nums) + 1) if i not in nums_set]

# Optimized solution with linear time and constant space.
class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        for i, num in enumerate(nums):
            new_index = abs(num) - 1

            if nums[new_index] > 0:
                nums[new_index] *= -1

        res = []

        for i in range(1, len(nums) + 1):
            if nums[i - 1] > 0:
                res.append(i)

        return res
