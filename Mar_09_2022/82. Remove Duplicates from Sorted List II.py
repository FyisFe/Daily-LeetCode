# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head):

        dummy_head = ListNode(-101, head)

        cur = dummy_head

        while cur is not None:
            if cur.next is None:
                return dummy_head.next

            next = cur.next
            flag = False
            while next.next is not None and next.val == next.next.val:
                next = next.next
                flag = True

            cur.next = next.next if flag else next
            if not flag:
                cur = cur.next
            flag = False
