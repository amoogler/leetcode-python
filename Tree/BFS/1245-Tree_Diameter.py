class Solution:
    def treeDiameter(self, edges: List[List[int]]) -> int:
        # Build an adjacency list to represent the graph.
        graph = defaultdict(list)

        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        # Randomly pick a node A and look for furthest node B.
        queue = deque([0])
        seen = set()
        seen.add(0)
        node_B = None

        while queue:
            node = queue.popleft()

            for child in graph[node]:
                if child not in seen:
                    queue.append(child)
                    seen.add(child)

            if len(queue) == 0:
                node_B = node

        # From node B, look for furthest node C.
        queue = deque([node_B])
        seen = set()
        seen.add(node_B)
        nodes_count = 0

        while queue:
            queue_length = len(queue)

            for _ in range(queue_length):
                node = queue.popleft()

                for child in graph[node]:
                    if child not in seen:
                        queue.append(child)
                        seen.add(child)

            nodes_count += 1

        return nodes_count - 1
