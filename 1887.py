class Solution:
    def reductionOperations(self, nums: List[int]) -> int:
        res = 0

        sorted_nums = sorted(nums, reverse=True)
        largest = sorted_nums[0]
        smallest = sorted_nums[len(nums) - 1]
        L = len(set(nums))

        for num in sorted_nums:

            if num == smallest:
                break
            elif num != largest:
                L -= 1
                largest = num

            res += (L - 1)

        return res
