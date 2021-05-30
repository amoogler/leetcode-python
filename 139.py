# Recursion + Memoization
# class Solution:
#     def wordBreak(self, s: str, wordDict: List[str]) -> bool:
#         words = set(wordDict)

#         @lru_cache
#         def dfs(s: str):
#             return s in words or any(s[:i] in words and dfs(s[i:]) for i in range(1, len(s)))

#         return dfs(s)

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        words = set(wordDict)

        dp = [False] * (len(s) + 1)
        dp[0] = True

        for end in range(1, len(s) + 1):
            if any(dp[start] and s[start:end] in words for start in range(end)):
                dp[end] = True

        return dp[len(s)]
