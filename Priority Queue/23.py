# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        heap = []
        head = curr = ListNode(-1)

        for idx, li in enumerate(lists):
            if li:
                heapq.heappush(heap, (li.val, idx))

        while heap:
            val, list_idx = heapq.heappop(heap)
            curr.next = ListNode(val)
            curr = curr.next
            lists[list_idx] = lists[list_idx].next

            if lists[list_idx]:
                heapq.heappush(heap, (lists[list_idx].val, list_idx))

        return head.next
