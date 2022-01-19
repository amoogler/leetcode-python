class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        start, max_substr, letter_idx = 0, 0, dict()

        for i, letter in enumerate(s):
            if letter in letter_idx and letter_idx[letter] >= start:
                start = letter_idx[letter] + 1

            letter_idx[letter] = i
            max_substr = max(max_substr, i - start + 1)

        return max_substr

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l, r, L = 0, 0, len(s)
        window = defaultdict(int)
        res = 0

        while r < L:
            window[s[r]] += 1
            r += 1

            while len(window) < r - l:
                window[s[l]] -= 1

                if window[s[l]] == 0:
                    del window[s[l]]

                l += 1

            res = max(res, r - l)

        return res
