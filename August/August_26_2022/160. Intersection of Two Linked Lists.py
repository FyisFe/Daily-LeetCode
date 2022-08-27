# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def getIntersectionNode(
        self, headA: ListNode, headB: ListNode
    ) -> Optional[ListNode]:
        m, n = 0, 0  # List A and List B length
        curA, curB = headA, headB
        while curA:
            m += 1
            curA = curA.next

        while curB:
            n += 1
            curB = curB.next

        curA, curB = headA, headB
        if m > n:
            diff = m - n
            while diff:
                diff -= 1
                curA = curA.next
        else:
            diff = n - m
            while diff:
                diff -= 1
                curB = curB.next

        while curA:
            if curA == curB:
                return curA
            curA, curB = curA.next, curB.next
