class Solution:
    def maxArea(self, height: List[int]) -> int:
        left, right = 0, len(height) - 1
        max_area = 0

        while left < right:
            l_h, r_h = height[left], height[right]
            max_area = max(max_area, min(l_h, r_h) * (right - left))

            if (l_h < r_h):
                left += 1
            else:
                right -= 1

        return max_area
