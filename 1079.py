class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        def backtrack(combination: List[int]):
            if combination:
                combinations.append(combination)

            for i, tile in enumerate(sorted_tiles):
                if visited[i] or \
                   i > 0 and tile == sorted_tiles[i - 1] and not visited[i - 1]:
                    continue

                visited[i] = True
                combination.append(tile)
                backtrack(combination)
                combination.pop()
                visited[i] = False

        combinations = []
        sorted_tiles = sorted(tiles)
        visited = [False] * len(tiles)
        backtrack([])
        return len(combinations)