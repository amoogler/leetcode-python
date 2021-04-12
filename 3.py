class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        start, max_substr, letter_idx = 0, 0, dict()

        for i, letter in enumerate(s):
            if letter in letter_idx and letter_idx[letter] >= start:
                start = letter_idx[letter] + 1

            letter_idx[letter] = i
            max_substr = max(max_substr, i - start + 1)

        return max_substr
