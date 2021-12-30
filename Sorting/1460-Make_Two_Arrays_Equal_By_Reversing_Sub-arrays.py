class Solution:
    def canBeEqual(self, target: List[int], arr: List[int]) -> bool:
        return all(a == b for a, b in zip(sorted(arr), sorted(target)))
