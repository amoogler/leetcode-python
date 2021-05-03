class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        sorted_arr = sorted(arr)
        min_diff = float('inf')
        res = []

        for e1, e2 in zip(sorted_arr, sorted_arr[1:]):
            min_diff = min(min_diff, e2 - e1)

        for e1, e2 in zip(sorted_arr, sorted_arr[1:]):
            if e2 - e1 == min_diff:
                res.append([e1, e2])

        return res
