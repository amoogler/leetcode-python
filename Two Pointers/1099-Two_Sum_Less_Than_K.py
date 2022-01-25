class Solution:
    def twoSumLessThanK(self, nums: List[int], k: int) -> int:
        sorted_list = sorted(nums)
        left, right = 0, len(sorted_list) - 1
        res = -1

        while left < right:
            nums_sum = sorted_list[left] + sorted_list[right]

            if nums_sum < k:
                res = max(res, nums_sum)
                left += 1
            else:
                right -= 1

        return res
