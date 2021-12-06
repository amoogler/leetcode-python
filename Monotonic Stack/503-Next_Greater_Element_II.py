class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        self.stack = []
        self.nums = nums
        self.res = [-1] * len(nums)

        # Loop 1st time to get next greater element for regular array.
        self.findNextGreaterElement()

        # Loop 2nd time to get next greater element for circular array.
        self.findNextGreaterElement()

        return self.res

    def findNextGreaterElement(self) -> None:
        for idx, num in enumerate(self.nums):
            while self.stack and self.nums[self.stack[-1]] < num:
                self.res[self.stack.pop()] = num

            self.stack.append(idx)
