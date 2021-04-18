class Solution:
    def letterCasePermutation(self, S: str) -> List[str]:
        def backtrack(permutation: List[str], depth: int):
            if depth == len(S):
                permutations.append(''.join(permutation))
                return

            permutation.append(S[depth])
            backtrack(permutation, depth + 1)
            permutation.pop()

            if S[depth].isalpha() and S[depth].isupper():
                permutation.append(S[depth].lower())
                backtrack(permutation, depth + 1)
                permutation.pop()
            elif S[depth].isalpha() and S[depth].islower():
                permutation.append(S[depth].upper())
                backtrack(permutation, depth + 1)
                permutation.pop()

        permutations = []
        backtrack([], 0)
        return permutations