class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        d = defaultdict(int)
        count, curr_sum = 0, 0

        for num in nums:
            curr_sum += num

            if curr_sum == k:
                count += 1

            count += d[curr_sum - k]
            d[curr_sum] += 1

        return count
