class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0

        left, right = 0, len(height) - 1
        left_max, right_max = 0, 0
        res = 0

        while left < right:
            left_max = max(height[left], left_max)
            right_max = max(height[right], right_max)

            if left_max < right_max:
                res += left_max - height[left]
                left += 1
            else:
                res += right_max - height[right]
                right -= 1

        return res
