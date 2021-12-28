class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        sorted_candidates = sorted(candidates)

        def backtrack(current: List[int], target: int, pos: int) -> None:
            if target == 0:
                res.append(current[:])
                return

            if target < 0:
                return

            for i in range(pos, len(sorted_candidates)):
                if i > pos and sorted_candidates[i] == sorted_candidates[i - 1]:
                    continue

                current.append(sorted_candidates[i])
                backtrack(current, target - sorted_candidates[i], i + 1)
                current.pop()

        backtrack([], target, 0)
        return res
