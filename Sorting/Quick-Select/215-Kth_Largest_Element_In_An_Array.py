# Heap solution, time in O(nlogk), space in O(k)
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        return heapq.nlargest(k, nums)[-1]

# Quick-select solution, time in O(n) in average case, O(n^2) in worst case.
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        self.quick_select(nums, 0, len(nums) - 1, len(nums) - k)
        return nums[len(nums) - k]

    def quick_select(self, nums, l, r, k):
        if l < r:
            p_rand = random.randint(l, r)
            p = self.partition(nums, l, r, p_rand)

            if p == k:
                return
            elif p < k:
                self.quick_select(nums, p + 1, r, k)
            else:
                self.quick_select(nums, l, p - 1, k)

    def partition(self, nums, l, r, p):
        pivot = nums[p]
        nums[p], nums[r] = nums[r], nums[p]
        le_wall = l

        for i in range(l, r):
            if nums[i] <= pivot:
                nums[le_wall], nums[i] = nums[i], nums[le_wall]
                le_wall += 1

        nums[le_wall], nums[r] = nums[r], nums[le_wall]
        return le_wall
