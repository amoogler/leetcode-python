class Solution:
    def minSteps(self, s: str, t: str) -> int:
        s_count, t_count = Counter(s), Counter(t)
        res = 0

        for char, frequency in t_count.items():
            if frequency < s_count[char]:
                res += s_count[char] - frequency

        for char, frequency in s_count.items():
            if char not in t_count:
                res += frequency

        return res
