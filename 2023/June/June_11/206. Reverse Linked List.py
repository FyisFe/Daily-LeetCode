class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        prev = none
        cur = head

        while cur:
            nextNode = cur.next
            cur.next = prev
            prev = cur
            cur = nextNode

        return prev
