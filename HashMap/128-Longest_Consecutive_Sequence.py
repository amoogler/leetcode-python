class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest = 0
        nums_set = set(nums)

        for num in nums:
            if num - 1 not in nums_set:
                curr_num = num
                curr_count = 1

                while curr_num + 1 in nums_set:
                    curr_num += 1
                    curr_count += 1

                longest = max(longest, curr_count)

        return longest
