# DFS Recursive Solution
class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        def dfs(room: int):
            seen.add(room)

            for key in rooms[room]:
                if key not in seen:
                    dfs(key)

        seen = set()
        dfs(0)
        return len(seen) == len(rooms)

# BFS Solution
class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        visited = set()
        queue = deque([0])

        while queue:
            room = queue.popleft()
            visited.add(room)

            for key in rooms[room]:
                if key not in visited:
                    queue.append(key)

        return len(visited) == len(rooms)
