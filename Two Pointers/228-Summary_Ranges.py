class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        res = []
        start, end = 0, 0

        while end < len(nums):

            if end == len(nums) - 1 or nums[end] + 1 != nums[end + 1]:
                if start == end:
                    res.append(str(nums[start]))
                else:
                    res.append(str(nums[start]) + '->' + str(nums[end]))

                end += 1
                start = end
            else:
                end += 1

        return res
