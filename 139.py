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

        for i in range(1, len(s) + 1):
            if any(dp[j] and s[j:i] in words for j in range(i)):
                dp[i] = True

        return dp[len(s)]
