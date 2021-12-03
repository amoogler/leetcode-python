class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left, right = 0, len(numbers) - 1

        while left < right:
            nums_sum = numbers[left] + numbers[right]

            if nums_sum > target:
                right -= 1
            elif nums_sum < target:
                left += 1
            else:
                return [left + 1, right + 1]

        return []
