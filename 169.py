# class Solution:
#     def majorityElement(self, nums: List[int]) -> int:
#         sorted_nums = sorted(nums)
#         return sorted_nums[len(nums) // 2]

# O(n) time complexity.
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = [nums[0], 1]

        for num in nums[1:]:
            if num == count[0]:
                count[1] += 1
            else:
                if count[1] == 0:
                    count[0] = num
                    count[1] = 1
                else:
                    count[1] -= 1

        return count[0]
