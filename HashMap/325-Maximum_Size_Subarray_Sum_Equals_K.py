class Solution:
    def maxSubArrayLen(self, nums: List[int], k: int) -> int:
        table = {0: -1}
        presum = 0
        max_length = 0

        for i, num in enumerate(nums):
            presum += num

            if presum - k in table:
                max_length = max(max_length, i - table[presum - k])

            # Check existence of presum in the table, we only want to
            # keep the earliest one to ensure longest.
            if presum not in table:
                table[presum] = i

        return max_length
