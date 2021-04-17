class Solution:
    def numberOfMatches(self, n: int) -> int:
        def countMatch(n: int) -> int:
            if n % 2 == 0:
                return n // 2, n // 2
            else:
                return (n - 1) // 2, (n - 1) // 2 + 1

        total_match = 0

        while n > 1:
            match, n = countMatch(n)
            total_match += match

        return total_match
