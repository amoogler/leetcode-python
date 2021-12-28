class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []

        def backtrack(current: List[int], target: int, start: int) -> None:
            # Base case.
            if target == 0:
                res.append(current[:])
                return
            elif target < 0:
                return

            for i in range(start, len(candidates)):
                current.append(candidates[i])
                backtrack(current, target - candidates[i], i)
                current.pop()

        backtrack([], target, 0)
        return res
