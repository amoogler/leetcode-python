class Solution:
    def sortEvenOdd(self, nums: List[int]) -> List[int]:
        odds = []
        evens = []
        res = [0] * len(nums)

        for idx, num in enumerate(nums):
            if idx % 2 == 0:
                evens.append(num)
            else:
                odds.append(num)

        evens.sort()
        odds.sort()
        odds = odds[::-1]
        i = len(nums) - 1

        while i >= 0:
            if i % 2 == 0:
                res[i] = evens.pop()
            else:
                res[i] = odds.pop()

            i -= 1

        return res
