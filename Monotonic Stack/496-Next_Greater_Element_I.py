# Monotonic stack solution.
class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = []
        table = dict()

        # Build a monotonic stack and a map for num -> next greater num
        for num in nums2:
            while stack and num > stack[-1]:
                table[stack.pop()] = num

            stack.append(num)

        while stack:
            table[stack.pop()] = -1

        return [table[num] for num in nums1]
