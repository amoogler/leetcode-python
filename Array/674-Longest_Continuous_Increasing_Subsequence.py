class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        if not nums:
            return 0

        res, curr = 1, 1

        for i in range(1, len(nums)):
            if nums[i] > nums[i - 1]:
                curr += 1
                res = max(res, curr)
            else:
                curr = 1

        return res
