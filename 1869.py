class Solution:
    def checkZeroOnes(self, s: str) -> bool:
        longest_1, longest_0 = 0, 0
        curr_1, curr_0 = 0, 0

        for i in range(len(s)):
            if s[i] == '1':
                curr_1 += 1
            else:
                curr_0 += 1

            if i == len(s) - 1 or s[i] != s[i + 1]:
                if s[i] == '1':
                    longest_1 = max(longest_1, curr_1)
                else:
                    longest_0 = max(longest_0, curr_0)

                curr_1, curr_0 = 0, 0

        return longest_1 > longest_0
