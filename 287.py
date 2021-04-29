class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        sorted_nums = sorted(nums)
        left, right = 0, len(nums) - 1

        while left < right:
            mid = left + (right - left) // 2

            if sorted_nums[mid] > mid:
                left = mid + 1
            else:
                right = mid

        return sorted_nums[left]
