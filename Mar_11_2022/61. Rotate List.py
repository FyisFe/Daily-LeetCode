# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        def countLength(head):
            cur = head
            l = 0
            while cur is not None:
                l += 1
                cur = cur.next
            return l

        if not head:
            return None

        l = countLength(head)

        k = k % l
        if k == 0:
            return head

        i = l - k

        end = head
        for _ in range(i - 1):
            end = end.next

        new_head = end.next

        end.next = None

        cur = new_head
        while cur.next is not None:
            cur = cur.next
        cur.next = head

        return new_head
