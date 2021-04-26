class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        sorted_nums = sorted(nums)
        left, right = 0, len(nums) - 1

        while left < right:
            mid = left + (right - left) // 2

            if mid + 1 > sorted_nums[mid]:
                right = mid
            else:
                left = mid + 1

        return sorted_nums[left]
