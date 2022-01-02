class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        N = len(nums)

        if N < 2:
            return N

        curr_up, curr_down = 1, 1

        for i in range(1, N):
            prev_up, prev_down = curr_up, curr_down

            if nums[i] > nums[i - 1]:
                curr_up = max(prev_up, prev_down + 1)
            elif nums[i] < nums[i - 1]:
                curr_down = max(prev_down, prev_up + 1)

        return max(curr_up, curr_down)
