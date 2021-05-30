class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        strs = s.split()

        if len(pattern) != len(strs):
            return False

        str_to_pattern = dict()
        pattern_to_str = dict()

        for s, p in zip(strs, pattern):
            if (s in str_to_pattern and str_to_pattern[s] != p) or \
               (p in pattern_to_str and pattern_to_str[p] != s):
                return False

            str_to_pattern[s] = p
            pattern_to_str[p] = s

        return True
