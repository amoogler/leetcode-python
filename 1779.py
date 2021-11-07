class Solution:
    def nearestValidPoint(self, x: int, y: int, points: List[List[int]]) -> int:
        current_min = float('inf')
        current_idx = -1

        for idx, (px, py) in enumerate(points):
            if px != x and py != y:
                continue

            distance = abs(px - x) + abs(py - y)

            if distance < current_min:
                current_min = distance
                current_idx = idx

        return current_idx
