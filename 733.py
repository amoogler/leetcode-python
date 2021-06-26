class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        self.color, self.newColor = image[sr][sc], newColor
        self.R, self.C = len(image), len(image[0])
        self.DIRS = ((1, 0), (-1, 0), (0, 1), (0, -1))
        self.visited = [[False] * self.C for _ in range(self.R)]
        self.dfs(image, sr, sc)
        return image

    def dfs(self, image: List[List[int]], sr: int, sc: int) -> None:
        if sr < 0 or sr >= self.R or sc < 0 or sc >= self.C or image[sr][sc] != self.color:
            return

        if self.visited[sr][sc]:
            return

        image[sr][sc] = self.newColor
        self.visited[sr][sc] = True

        for dr, dc in self.DIRS:
            self.dfs(image, sr + dr, sc + dc)
