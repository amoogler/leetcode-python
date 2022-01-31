# DFS + Memoization solution.
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        @lru_cache(None)
        def dfs(i, j):
            # Reach full pattern.
            if j == len(p):
                return i == len(s)

            # Match single character.
            if i < len(s) and (s[i] == p[j] or p[j] == '?'):
                if dfs(i + 1, j + 1):
                    return True
            elif p[j] == '*':
                # Match empty character.
                if dfs(i, j + 1):
                    return True

                # Match one of more characters.
                if i < len(s) and dfs(i + 1, j):
                    return True

            return False

        return dfs(0, 0)
