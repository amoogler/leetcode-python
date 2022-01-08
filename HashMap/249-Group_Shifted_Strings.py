class Solution:
    def groupStrings(self, strings: List[str]) -> List[List[str]]:
        # Build a map for pattern (e.g. diff between neighbor chars) -> a list of words.
        d = defaultdict(list)

        for s in strings:
            key = ()

            for i in range(len(s) - 1):
                key += ((ord(s[i + 1]) - ord(s[i])) % 26,) # -1 mod 26 == 25

            d[key].append(s)

        return [value for value in d.values()]
