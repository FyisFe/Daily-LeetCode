# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(
        self, l1: Optional[ListNode], l2: Optional[ListNode]
    ) -> Optional[ListNode]:
        ans = ListNode()
        cur = ans
        addOne = 0
        while l1 and l2:
            val = l1.val + l2.val + addOne
            cur.next = ListNode(val % 10)
            cur = cur.next

            addOne = val // 10

            l1 = l1.next
            l2 = l2.next

        while l1:
            val = l1.val + addOne
            cur.next = ListNode(val % 10)
            cur = cur.next

            addOne = val // 10

            l1 = l1.next

        while l2:
            val = l2.val + addOne
            cur.next = ListNode(val % 10)
            cur = cur.next

            addOne = val // 10

            l2 = l2.next

        if addOne == 1:
            cur.next = ListNode(1)

        return ans.next
