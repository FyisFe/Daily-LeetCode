# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        dummy_left, dummy_right = ListNode(), ListNode()
        left, right = dummy_left, dummy_right

        while head:
            if head.val < x:
                left.next = ListNode(head.val)
                left = left.next
            else:
                right.next = ListNode(head.val)
                right = right.next
            head = head.next

        left.next = dummy_right.next
        return dummy_left.next
