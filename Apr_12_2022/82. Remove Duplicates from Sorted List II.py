# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        cur = dummy
        while head:
            if not head.next or (head.next and head.next.val != head.val):
                cur.next = ListNode(head.val)
                cur = cur.next
                head = head.next
                continue

            while head.next and head.next.val == head.val:
                head = head.next
            head = head.next
        return dummy.next
