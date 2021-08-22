# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger:
#    def __init__(self, value=None):
#        """
#        If value is not specified, initializes an empty list.
#        Otherwise initializes a single integer equal to value.
#        """
#
#    def isInteger(self):
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        :rtype bool
#        """
#
#    def add(self, elem):
#        """
#        Set this NestedInteger to hold a nested list and adds a nested integer elem to it.
#        :rtype void
#        """
#
#    def setInteger(self, value):
#        """
#        Set this NestedInteger to hold a single integer equal to value.
#        :rtype void
#        """
#
#    def getInteger(self):
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        :rtype int
#        """
#
#    def getList(self):
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        :rtype List[NestedInteger]
#        """

# class Solution:
#     def depthSumInverse(self, nestedList: List[NestedInteger]) -> int:
#         element_queue = deque(nestedList)
#         sum_queue = deque()
#         res = 0

#         while element_queue:
#             queue_length = len(element_queue)
#             level_sum = 0

#             for _ in range(queue_length):
#                 element = element_queue.popleft()

#                 if element.isInteger():
#                     level_sum += element.getInteger()
#                 else:
#                     element_queue.extend(element.getList())

#             sum_queue.appendleft(level_sum)

#         for idx, value in enumerate(sum_queue):
#             res += (idx + 1) * value

#         return res

class Solution:
    def depthSumInverse(self, nestedList: List[NestedInteger]) -> int:
        total = 0

        def getMaxDepth(nestedList: List[NestedInteger], depth: int):
            curr_depth = 0

            for e in nestedList:
                if not e.isInteger():
                    curr_depth = max(curr_depth, getMaxDepth(e.getList(), depth))

            return curr_depth + 1

        def dfs(nestedList: List[NestedInteger], weight: int) -> int:
            total = 0

            for e in nestedList:
                if e.isInteger():
                    total += e.getInteger() * weight
                else:
                    total += dfs(e.getList(), weight - 1)

            return total

        max_depth = getMaxDepth(nestedList, 0)
        return dfs(nestedList, max_depth)
