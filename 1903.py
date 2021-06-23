class Solution:
    def largestOddNumber(self, num: str) -> str:
        number = num

        for i in range(len(num) - 1, -1, -1):
            if int(number[-1]) % 2 == 1:
                break

            number = number[:i]

        return number
