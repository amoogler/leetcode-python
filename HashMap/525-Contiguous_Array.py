class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        table = {0: -1}
        max_length, count = 0, 0

        for i, num in enumerate(nums):
            if num == 1:
                count += 1
            else:
                count -= 1

            if count in table:
                max_length = max(max_length, i - table[count])
            else:
                table[count] = i

        return max_length
