class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        currSum = 0
        res = 0

        for i in range(k):
            currSum += nums[i]

        res = currSum / k

        for i in range(k, len(nums)):
            currSum -= nums[i - k]
            currSum += nums[i]
            res = max(res, currSum / k)

        return res
