class Solution:
    def letterCasePermutation(self, S: str) -> List[str]:
        def backtrack(permutation: List[str], depth: int):
            if depth == len(S):
                permutations.append(''.join(permutation))
                return

            ch = S[depth]

            permutation.append(ch)
            backtrack(permutation, depth + 1)
            permutation.pop()

            if ch.isalpha():
                if ch.isupper():
                    permutation.append(ch.lower())
                else:
                    permutation.append(ch.upper())

                backtrack(permutation, depth + 1)
                permutation.pop()

        permutations = []
        backtrack([], 0)
        return permutations