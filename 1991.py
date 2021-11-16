class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        N = len(nums)
        left_presum, right_presum = [0] * N, [0] * N
        left, right = 0, 0

        for idx, (num1, num2) in enumerate(zip(nums, nums[::-1])):
            left_presum[idx] = left
            right_presum[N - 1 - idx] = right
            left += num1
            right += num2

        for i in range(N):
            if left_presum[i] == right_presum[i]:
                return i

        return -1
