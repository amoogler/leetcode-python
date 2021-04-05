class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        res = []
        pointer = n
        
        for num in nums[:n]:
            res.append(num)
            res.append(nums[pointer])
            pointer += 1
        
        return res
