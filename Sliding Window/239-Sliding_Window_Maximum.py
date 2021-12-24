# Brute force solution, time limit exceeded. Time complexity: O(nk)
# class Solution:
#     def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
#         return [max(nums[i : i + k]) for i in range(len(nums) - k + 1)]

# Monotonic queue solution.
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        queue = deque([])
        res = []

        def cleanDeque(index) -> None:
            # Remove index that will be out of sliding window.
            if queue and queue[0] == index - k:
                queue.popleft()

            # Remove the indexes of all elements which are smaller
            # than current element nums[index].
            while queue and nums[index] > nums[queue[-1]]:
                queue.pop()

        for i in range(k):
            cleanDeque(i)
            queue.append(i)

        res.append(nums[queue[0]])

        for i in range(k, len(nums)):
            cleanDeque(i)
            queue.append(i)
            res.append(nums[queue[0]])

        return res

