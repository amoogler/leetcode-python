class Solution:
    def findIndex(self, nums: List[int], target: int, is_leftmost: bool) -> int:
        N = len(nums)
        left, right = 0, N - 1

        while left <= right:
            mid = left + (right - left) // 2

            if nums[mid] == target:
                if is_leftmost:
                    if mid == left or nums[mid - 1] < target:
                        return mid
                    else:
                        right = mid - 1
                else:
                    if mid == right or nums[mid + 1] > target:
                        return mid
                    else:
                        left = mid + 1
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1

        return -1

    def searchRange(self, nums: List[int], target: int) -> List[int]:
        first_idx = self.findIndex(nums, target, True)
        last_idx = self.findIndex(nums, target, False)

        return [first_idx, last_idx]
