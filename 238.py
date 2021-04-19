class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res, left, right = [1] * len(nums), nums[0], nums[len(nums) - 1]

        for i in range(1, len(nums)):
            res[i] *= left
            left *= nums[i]

        for i in range(len(nums) - 2, -1, -1):
            res[i] *= right
            right *= nums[i]

        return res
