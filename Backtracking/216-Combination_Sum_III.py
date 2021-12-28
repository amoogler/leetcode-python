class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        res = []

        def backtrack(current: List[int], target: int, num: int) -> None:
            if len(current) == k and target == 0:
                res.append(current[:])
                return

            if target < 0:
                return

            for i in range(num, 10):
                current.append(i)
                backtrack(current, target - i, i + 1)
                current.pop()

        backtrack([], n, 1)
        return res
