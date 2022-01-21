class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        l, r = 0, 0
        window = defaultdict(int)

        while r < len(s2):
            window[s2[r]] += 1
            r += 1

            while r - l > len(s1):
                window[s2[l]] -= 1

                if window[s2[l]] == 0:
                    del window[s2[l]]

                l += 1

            if len(s1) == (r - l) and Counter(s1) == window:
                return True

        return False
