class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""

        common_prefix = []

        for i in range(len(strs[0])):
            if any(i >= len(s) or s[i] != strs[0][i] for s in strs[1:]):
                break

            common_prefix.append(strs[0][i])

        return ''.join(common_prefix)