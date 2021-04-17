class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        def backtrack(combination: List[int], start_idx: int):
            if len(combination) == k:
                combinations.append(combination[:])
                return

            for i in range(start_idx, n + 1):
                combination.append(i)
                backtrack(combination, i + 1)
                combination.pop()

        combinations = []
        backtrack([], 1)
        return combinations
