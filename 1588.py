class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        odd_sum, start, arr_length = 0, 0, len(arr)

        for i in range(arr_length):
            for j in range(arr_length):
                if (j - i) % 2 == 0:
                    odd_sum += sum(arr[i : j + 1])

        return odd_sum
