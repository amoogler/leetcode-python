# DFS + Backtracking solution.
class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        self.inform_time = 0

        # Build an adjaceny list to represent the tree of reporting chain.
        graph = defaultdict(list)

        for i in range(n):
            graph[manager[i]].append(i)

        self.backtrack(headID, 0, informTime, graph)
        return self.inform_time

    def backtrack(self, employee_id: int, path_sum: int, informTime: List[int], graph: defaultdict(int)) -> None:
        if not graph[employee_id]:
            self.inform_time = max(self.inform_time, path_sum)
            return

        path_sum += informTime[employee_id]

        for report_id in graph[employee_id]:
            self.backtrack(report_id, path_sum, informTime, graph)

        path_sum -= informTime[employee_id]
