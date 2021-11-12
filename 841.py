class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        visited = set()

        def dfs(room: int):
            if room in visited:
                return False

            visited.add(room)

            if len(visited) == len(rooms):
                return True

            for key in rooms[room]:
                if dfs(key):
                    return True

            return False

        return dfs(0)

# class Solution:
#     def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
#         visited = set()
#         queue = deque([0])

#         while queue:
#             room = queue.popleft()
#             visited.add(room)

#             if len(visited) == len(rooms):
#                 return True

#             for key in rooms[room]:
#                 if key not in visited:
#                     queue.append(key)

#         return False
