# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        toRemove = head
        cur = head

        while n > 0:
            if not cur.next:
                return head.next
            cur = cur.next
            n -= 1

        while cur.next:
            cur = cur.next
            toRemove = toRemove.next

        toRemove.next = toRemove.next.next

        return head
