class Solution:

    def __init__(self, nums: List[int]):
        self.nums = nums

    def pick(self, target: int) -> int:
        res = None
        count = 0

        for i, x in enumerate(self.nums):
            if x == target:
                count += 1
                # At each element, decide if picking that one or not based on probability
                # of entire population. If not, then you already chose before, just go with
                # it.
                chance = random.randint(1, count)

                if chance == 1:
                    res = i

        return res


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.pick(target)
