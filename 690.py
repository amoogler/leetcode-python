"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        employee_table = dict()

        for e in employees:
            employee_table[e.id] = e

        queue = deque([id])
        importance = 0

        while queue:
            employee_id = queue.popleft()
            importance += employee_table[employee_id].importance

            for s_id in employee_table[employee_id].subordinates:
                queue.append(s_id)

        return importance
