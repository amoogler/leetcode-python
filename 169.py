# class Solution:
#     def majorityElement(self, nums: List[int]) -> int:
#         sorted_nums = sorted(nums)
#         return sorted_nums[len(nums) // 2]

# O(n) time complexity.
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        curr_majority = nums[0]
        curr_count  = 1

        for num in nums[1:]:
            if num == curr_majority:
                curr_count += 1
            else:
                if curr_count == 0:
                    curr_majority = num
                    curr_count = 1
                else:
                    curr_count -= 1

        return curr_majority
