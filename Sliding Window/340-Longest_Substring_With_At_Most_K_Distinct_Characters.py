class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        window = defaultdict(int)
        l, r, L = 0, 0, len(s)
        res = 0

        while r < L:
            window[s[r]] += 1
            r += 1

            while len(window) > k:
                window[s[l]] -= 1

                if window[s[l]] == 0:
                    del window[s[l]]

                l += 1

            res = max(res, r - l)

        return res
