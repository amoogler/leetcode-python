class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        def reverse(nums: List[int], start: int, end: int) -> None:
            while start < end:
                nums[start], nums[end] = nums[end], nums[start]
                start += 1
                end -= 1

        N = len(nums)
        k %= N
        reverse(nums, 0, N - 1)
        reverse(nums, 0, k - 1)
        reverse(nums, k, N - 1)
