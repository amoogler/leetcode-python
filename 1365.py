import bisect

class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        sorted_nums = sorted(nums)
        ans = []
        
        for num in nums:
            ans.append(bisect.bisect_left(sorted_nums, num))

        return ans
