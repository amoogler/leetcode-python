# Top-Down Recursion + Memoization Approach
#
# class Solution:
#     def minCost(self, costs: List[List[int]]) -> int:
#         def paint_cost(n: int, color: int) -> int:
#             if (n, color) in self.memo:
#                 return self.memo[(n, color)]

#             total_cost = costs[n][color]

#             if n == len(costs) - 1:
#                 pass
#             elif color == 0:
#                 total_cost += min(paint_cost(n + 1, 1), paint_cost(n + 1, 2))
#             elif color == 1:
#                 total_cost += min(paint_cost(n + 1, 0), paint_cost(n + 1, 2))
#             elif color == 2:
#                 total_cost += min(paint_cost(n + 1, 0), paint_cost(n + 1, 1))

#             self.memo[(n, color)] = total_cost
#             return total_cost

#         if not costs:
#             return 0

#         self.memo = {}
#         return min(paint_cost(0, 0), paint_cost(0, 1), paint_cost(0, 2))

# Dynamic Programming Approach.

# class Solution:
#     def minCost(self, costs: List[List[int]]) -> int:
#         for n in range(len(costs) - 2, -1, -1):
#             # Total cost for painting nth house x(0|1|2) color.
#             costs[n][0] += min(costs[n + 1][1], costs[n + 1][2])
#             costs[n][1] += min(costs[n + 1][0], costs[n + 1][2])
#             costs[n][2] += min(costs[n + 1][0], costs[n + 1][1])

#         if not costs:
#             return 0

#         return min(costs[0])

# Dynamic Programming Approach without Modifying Input Array.

class Solution:
    def minCost(self, costs: List[List[int]]) -> int:
        if not costs:
            return 0

        previous_row = costs[-1]

        for n in range(len(costs) - 2, -1, -1):
            current_row = costs[n][:]

            current_row[0] += min(previous_row[1], previous_row[2])
            current_row[1] += min(previous_row[0], previous_row[2])
            current_row[2] += min(previous_row[0], previous_row[1])

            previous_row = current_row

        return min(previous_row)
