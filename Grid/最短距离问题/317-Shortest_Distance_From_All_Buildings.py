# Solution1: Traverse from each empty space to all buildings. - Time Limited Exceeded.
class Solution:
    def shortestDistance(self, grid: List[List[int]]) -> int:
        queue = deque([])
        total_buildings = 0
        self.R, self.C = len(grid), len(grid[0])
        min_distance = float('inf')

        # Find out the total number of buildings.
        for i in range(self.R):
            for j in range(self.C):
                if grid[i][j] == 1:
                    total_buildings += 1

        # Find out the min distance sum for each empty space.
        for i in range(self.R):
            for j in range(self.C):
                if grid[i][j] == 0:
                    min_distance = min(min_distance, self.bfs(grid, i, j, total_buildings))

        if min_distance == float('inf'):
            return -1

        return min_distance

    def bfs(self, grid: List[List[int]], row: int, col: int, total_buildings: int) -> int:
        DIRS = ((-1, 0), (1, 0), (0, -1), (0, 1))
        distance_sum, buildings_reached = 0, 0
        queue = deque([(row, col)])
        seen = set()
        seen.add((row, col))
        steps = 0

        while queue and buildings_reached != total_buildings:
            queue_length = len(queue)

            for _ in range(queue_length):
                r, c = queue.popleft()

                # If this cell is a building, add distance from source to this cell.
                if grid[r][c] == 1:
                    distance_sum += steps
                    buildings_reached += 1
                    continue

                # If this cell is an empty space, traverse all directions.
                for dr, dc in DIRS:
                    nr, nc = r + dr, c + dc

                    if  (not (0 <= nr < self.R and 0 <= nc < self.C)) or \
                        (nr, nc) in seen or \
                        grid[nr][nc] == 2:
                        continue

                    seen.add((nr, nc))
                    queue.append((nr, nc))

            # After traverse 1 level, increment steps by 1.
            steps += 1

        # Optimization
        # If we did not reach all buildings, any cell visited also cannot reach all buildings.
        # Set all cells visited to 2 so we do not check them again.
        if buildings_reached != total_buildings:
            for i in range(self.R):
                for j in range(self.C):
                    if grid[i][j] == 0 and (i, j) in seen:
                        grid[i][j] = 2

            return float('inf')

        return distance_sum

# Solution2: Traverse from all buildings to each empty space.
# This is better than Solution1 when there is fewer buildings than empty spaces.
class Solution:
    def shortestDistance(self, grid: List[List[int]]) -> int:
        self.R, self.C = len(grid), len(grid[0])
        total_buildings = 0
        min_distance = float('inf')

        # Store (total_distance, buildings_count) for each cell.
        # (row, col) -> (total_distance, buildings_count)
        distances = dict()

        for i in range(self.R):
            for j in range(self.C):
                if grid[i][j] == 1:
                    total_buildings += 1
                    self.bfs(grid, distances, i, j)

        # Check all empty spaces with buildings_count equal to total_buildings
        # and find the min_distance.
        for i in range(self.R):
            for j in range(self.C):
                if (i, j) in distances and distances[(i, j)][1] == total_buildings:
                    min_distance = min(min_distance, distances[(i, j)][0])

        if min_distance == float('inf'):
            return -1

        return min_distance

    def bfs(self, grid: List[List[int]], distances: dict, row: int, col: int) -> None:
        DIRS = ((-1, 0), (1, 0), (0, -1), (0, 1))
        queue = deque([(row, col)])
        seen = set()
        seen.add((row, col))

        steps = 0

        while queue:
            queue_length = len(queue)

            for _ in range(queue_length):
                r, c = queue.popleft()

                # If this cell is an empty space, add the distance and
                # increment the count of buildings reached at this cell.
                if grid[r][c] == 0:
                    if (r, c) in distances:
                        distances[(r, c)][0] += steps
                        distances[(r, c)][1] += 1
                    else:
                        distances[(r, c)] = [steps, 1]

                # Traverse the next cells which is not a blockage.
                for dr, dc in DIRS:
                    nr, nc = r + dr, c + dc

                    if not (0 <= nr < self.R and 0 <= nc < self.C) or \
                        (nr, nc) in seen or \
                        grid[nr][nc] != 0:
                        continue

                    seen.add((nr, nc))
                    queue.append((nr, nc))

            steps += 1

# Solution3: Same idea as Solution2, with optimization.
class Solution:
    def shortestDistance(self, grid: List[List[int]]) -> int:
        DIRS = ((-1, 0), (1, 0), (0, -1), (0, 1))
        R, C = len(grid), len(grid[0])
        # Store total distance sum for each empty space cell.
        total_distance_sum = defaultdict(int)
        min_distance = float('inf')
        empty_space_value = 0

        for i in range(R):
            for j in range(C):
                # Start BFS from each building cell.
                if grid[i][j] == 1:
                    min_distance = float('inf')
                    queue = deque([(i, j)])
                    steps = 0

                    while queue:
                        steps += 1
                        queue_length = len(queue)

                        for _ in range(queue_length):
                            r, c = queue.popleft()

                            for dr, dc in DIRS:
                                nr, nc = r + dr, c + dc

                                # For each cell with value equal to empty space value,
                                # add distance and decrement the cell value by 1.
                                if not (0 <= nr < R and 0 <= nc < C) or \
                                    grid[nr][nc] != empty_space_value:
                                    continue

                                grid[nr][nc] -= 1
                                total_distance_sum[(nr, nc)] += steps
                                queue.append((nr, nc))
                                min_distance = min(min_distance, total_distance_sum[(nr, nc)])

                    empty_space_value -= 1

        return min_distance if min_distance != float('inf') else -1
