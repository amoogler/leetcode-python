# DFS Solution
class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        def dfs(room: int):
            if room not in visited:
                visited.add(room)

                for key in rooms[room]:
                    dfs(key)

        visited = set()
        dfs(0)
        return len(visited) == len(rooms)

# BFS Solution.
class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        visited = set()
        queue = deque([0])

        while queue:
            room = queue.popleft()
            visited.add(room)

            if len(visited) == len(rooms):
                return True

            for key in rooms[room]:
                if key not in visited:
                    queue.append(key)

        return False
