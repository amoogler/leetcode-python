class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        strs = s.split()

        if len(pattern) != len(strs):
            return False

        str_to_pattern = dict()
        pattern_to_str = dict()

        for idx, (s, p) in enumerate(zip(strs, pattern)):
            if (s in str_to_pattern and str_to_pattern[s] != pattern[idx]) or \
               (p in pattern_to_str and pattern_to_str[p] != strs[idx]):
                return False

            str_to_pattern[s] = pattern[idx]
            pattern_to_str[p] = strs[idx]

        return True
