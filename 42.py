# class Solution:
#     def trap(self, height: List[int]) -> int:
#         if not height:
#             return 0

#         res, L = 0, len(height)
#         left_max, right_max = [0] * L, [0] * L
#         left_max[0], right_max[L - 1] = height[0], height[L - 1]

#         for i in range(1, L):
#             left_max[i] = max(height[i], left_max[i - 1])

#         for i in range(L - 2, -1 , -1):
#             right_max[i] = max(height[i], right_max[i + 1])

#         for i in range(1, L - 1):
#             res += min(left_max[i], right_max[i]) - height[i]

#         return res

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
