# Optimization with given conditions. Worst case: O(mn) upon no negative values.
class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        R, C = len(grid), len(grid[0])
        count = 0

        for i in range(R):
            for j in range(C):
                if grid[i][j] < 0:
                    count += C - j
                    break

        return count

# Binary search solution. O(mlogn)
class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        R, C = len(grid), len(grid[0])
        count = 0

        for i in range(R):
            first_neg_idx = self.reverse_bisect_right(grid[i], 0)
            print(first_neg_idx)
            count += C - first_neg_idx

        return count

    def reverse_bisect_right(self, arr: List[int], value: int) -> int:
        left, right = 0, len(arr)

        while left < right:
            mid = (left + right) // 2

            if value > arr[mid]:
                right = mid
            else:
                left = mid + 1

        return left
