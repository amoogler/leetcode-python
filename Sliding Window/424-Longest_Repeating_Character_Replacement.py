class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l, r, L = 0, 0, len(s)
        window = defaultdict(int)
        max_count = 0
        res = 0

        while r < L:
            window[s[r]] += 1
            max_count = max(max_count, window[s[r]])
            r += 1

            while r - l - max_count > k:
                window[s[l]] -= 1
                l += 1

            res = max(res, r - l)

        return res
