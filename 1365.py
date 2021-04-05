class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        sorted_nums = sorted(nums)
        ans = []
        
        for num in nums:
            count = 0
            
            for sorted_num in sorted_nums:
                if num > sorted_num:
                    count += 1
            
            ans.append(count)
            count = 0
        
        return ans
