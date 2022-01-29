class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, new_color: int) -> List[List[int]]:
        self.R, self.C = len(image), len(image[0])

        if new_color != image[sr][sc]:
            self.dfs(image, sr, sc, image[sr][sc], new_color)

        return image

    def dfs(self, image: List[List[int]], sr: int, sc: int, old_color: int, new_color: int) -> None:
        if not (0 <= sr < self.R and 0 <= sc < self.C) or image[sr][sc] != old_color:
            return

        image[sr][sc] = new_color
        DIRS = ((1, 0), (-1, 0), (0, 1), (0, -1))

        for dr, dc in DIRS:
            self.dfs(image, sr + dr, sc + dc, old_color, new_color)
