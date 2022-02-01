class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        graph = defaultdict(set)
        seen = defaultdict(lambda: float('inf'))
        seen[src] = 0
        queue = deque([(src, -1, 0)])

        # Build a weighted directed graph.
        for u, v, w in flights:
            graph[u].add((v, w))

        # Apply Dijkstra's algorithm to find the shortest path from a
        # single source to destination in a weighted directed graph.
        while queue:
            curr_pos, stops, cost = queue.popleft()

            if curr_pos == dst or stops == k:
                continue

            for next_pos, price in graph[curr_pos]:
                new_cost = cost + price

                if new_cost < seen[next_pos]:
                    seen[next_pos] = new_cost
                    queue.append((next_pos, stops + 1, new_cost))

        return seen[dst] if seen[dst] != float('inf') else -1
