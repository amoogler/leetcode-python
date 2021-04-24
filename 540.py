class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        start, end = 0, len(nums) - 1

        while start < end:
            mid = start + (end - start) // 2

            if nums[mid - 1] != nums[mid] != nums[mid + 1]:
                return nums[mid]
            elif nums[mid - 1] != nums[mid] and mid % 2 == 0: # mid is even, a,a,b,b,C,c
                start = mid + 2
            elif nums[mid - 1] != nums[mid] and mid % 2 == 1: # mid is odd, a,a,b,b,c,D,d
                end = mid - 1
            elif nums[mid] != nums[mid + 1] and mid % 2 == 0: # mid is even, a,a,b,c,C,d
                end = mid - 2
            elif nums[mid] != nums[mid + 1] and mid % 2 == 1: # mid is odd, a,a,b,b,c,C,d
                start = mid + 1

        return nums[start]