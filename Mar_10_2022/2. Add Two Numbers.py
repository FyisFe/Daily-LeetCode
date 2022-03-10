# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(
        self, l1: Optional[ListNode], l2: Optional[ListNode]
    ) -> Optional[ListNode]:
        dummyRes = ListNode(0)
        cur = dummyRes
        carry = 0

        while l1 is not None and l2 is not None:
            res = l1.val + l2.val + carry
            carry = res // 10
            l1 = l1.next
            l2 = l2.next
            cur.next = ListNode(res % 10)
            cur = cur.next

        while l1 is not None:
            res = l1.val + carry
            carry = res // 10
            l1 = l1.next
            cur.next = ListNode(res % 10)
            cur = cur.next

        while l2 is not None:
            res = l2.val + carry
            carry = res // 10
            l2 = l2.next
            cur.next = ListNode(res % 10)
            cur = cur.next

        if carry != 0:
            cur.next = ListNode(carry)

        return dummyRes.next
