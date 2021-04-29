class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        N = len(nums)
        res = [0] * N
        start, end = 0, N - 1
        i = N - 1

        while start <= end:
            if abs(nums[start]) > abs(nums[end]):
                res[i] = nums[start] * nums[start]
                start += 1
            else:
                res[i] = nums[end] * nums[end]
                end -= 1

            i -= 1

        return res
