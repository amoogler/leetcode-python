class Solution:
    def minAreaRect(self, points: List[List[int]]) -> int:
        min_area = float('inf')
        points_table = set()

        for x, y in points:
            points_table.add((x, y))

        for x1, y1 in points:
            for x2, y2 in points:
                if not (x1 > x2 and y1 > y2):
                    continue

                if (x1, y2) in points_table and (x2, y1) in points_table:
                    area = abs(x1 - x2) * abs(y1 - y2)

                    if area != 0:
                        min_area = min(area, min_area)

        return min_area if min_area != float('inf') else 0
