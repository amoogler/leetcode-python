class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        def backtrack(path: List[int], des_nodes: List[int]):
            if path[-1] == len(graph) - 1:
                paths.append(path[:])
                return

            for des_node in des_nodes:
                path.append(des_node)
                backtrack(path, graph[des_node])
                path.pop()

        paths = []
        backtrack([0], graph[0])
        return paths
