class Solution:
    def minOperations(self, nums: List[int]) -> int:
        operations_num = 0

        if len(nums) <= 1:
            return 0

        for i in range(1, len(nums)):
            if nums[i] <= nums[i - 1]:
                diff = nums[i - 1] - nums[i] + 1
                operations_num += diff
                nums[i] += diff

        return operations_num
