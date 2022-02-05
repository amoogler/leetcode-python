class Solution:
    def validSquare(self, p1: List[int], p2: List[int], p3: List[int], p4: List[int]) -> bool:
        if p1 == p2 == p3 == p4:
            return False

        def dist(a, b):
            return (a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2

        arr = [dist(p1, p2), dist(p1, p3), dist(p1, p4), dist(p2, p3), dist(p2, p4), dist(p3, p4)]
        arr.sort()

        if arr[0] == arr[1] == arr[2] == arr[3] and arr[4] == arr[5]:
            return True

        return False
