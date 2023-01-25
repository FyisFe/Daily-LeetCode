# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        hm = {}

        cur = head

        while cur:
            if cur in hm:
                return cur
            hm[cur] = 1
            cur = cur.next
