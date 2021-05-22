# Recursion + Memoization
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        words = set(wordDict)

        @lru_cache
        def dfs(s: str):
            return s in words or any(s[:i] in words and dfs(s[i:]) for i in range(1, len(s)))

        return dfs(s)
