# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        mid = head
        cur = head

        while cur.next and cur.next.next:
            cur = cur.next.next
            mid = mid.next

        if cur.next:
            mid = mid.next

        return mid
