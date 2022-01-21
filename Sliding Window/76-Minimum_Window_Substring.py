class Solution:
    def minWindow(self, s: str, t: str) -> str:
        l, r, L = 0, 0, len(s)
        window = defaultdict(int)
        t_count = Counter(t)
        curr_min = float('inf')
        res = ""

        while r < L:
            window[s[r]] += 1
            r += 1

            while self.is_substring(window, t_count):
                window[s[l]] -= 1

                if window[s[l]] == 0:
                    del window[s[l]]

                l += 1

                if r - l < curr_min:
                    curr_min = r - l
                    res = s[l - 1: r]

        return res

    def is_substring(self, window: defaultdict, t_count: Counter) -> bool:
        for k in t_count:
            if t_count[k] > window[k]:
                return False

        return True
