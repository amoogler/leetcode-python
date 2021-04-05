class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        sorted_nums = sorted(nums)
        ans = []
        
        for num in nums:
            idx = sorted_nums.index(num)
            
            while idx > 0:
                if num > sorted_nums[idx - 1]:
                    break
                else:
                    idx -= 1

            ans.append(idx)

        return ans
