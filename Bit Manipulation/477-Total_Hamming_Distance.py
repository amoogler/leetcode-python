class Solution:
    def totalHammingDistance(self, nums: List[int]) -> int:
        table = defaultdict(int)

        for num in nums:
            index = 0

            while num > 0:
                bit = num & 1

                if bit == 1:
                    table[index] += 1

                num >>= 1
                index += 1

        res = 0

        for i in range(32):
            res += table[i] * (len(nums) - table[i])

        return res
