# This problem asks us to do sampling with weight.
# Given a list of offsets(i.e. prefix sums) and a target offset, our task
# is to fit the target offset into the list so that the ascending order
# is maintained.
class Solution:

    def __init__(self, weights: List[int]):
        self.prefix_sums = []
        prefix_sum = 0

        for w in weights:
            prefix_sum += w
            self.prefix_sums.append(prefix_sum)

        self.total = prefix_sum

    def pickIndex(self) -> int:
        target = self.total * random.random()

        # Linear search.
        # for i, prefix_sum in enumerate(self.prefix_sums):
        #     if target < prefix_sum:
        #         return i

        # Binary search.
        return bisect.bisect(self.prefix_sums, target)


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()
