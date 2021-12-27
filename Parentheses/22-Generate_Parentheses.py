# Brute force solution.
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        self.N = 2 * n
        combinations = []
        self.generateAll([], 0, combinations)
        return combinations

    def generateAll(self, current: List[str], pos: int, result: List[str]) -> None:
        if pos == self.N:
            if self.isValid(current):
                result.append(''.join(current))
        else:
            # Backtracking.
            current.append('(')
            self.generateAll(current, pos + 1, result)
            del current[-1]
            current.append(')')
            self.generateAll(current, pos + 1, result)
            del current[-1]

    def isValid(self, current: str) -> bool:
        balance = 0

        for c in current:
            if c == '(':
                balance += 1
            else:
                balance -= 1

            if balance < 0:
                return False

        return balance == 0

# Improved version by validating validity before adding '(' or ')'.
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def backtrack(left: int, right: int, current: List[str]) -> None:
            if len(current) == 2 * n:
                res.append(''.join(current))
            else:
                if left < n:
                    current.append('(')
                    backtrack(left + 1, right, current)
                    current.pop()

                if right < left:
                    current.append(')')
                    backtrack(left, right + 1, current)
                    current.pop()

        backtrack(0, 0, [])
        return res
