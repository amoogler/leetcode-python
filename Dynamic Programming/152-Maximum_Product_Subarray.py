class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if not nums:
            return 0

        max_sofar, min_sofar = nums[0], nums[0]
        res = max_sofar

        for num in nums[1:]:
            temp = max(max_sofar * num, min_sofar * num, num)
            min_sofar = min(min_sofar * num, max_sofar * num, num)
            max_sofar = temp
            res = max(res, max_sofar)

        return res
