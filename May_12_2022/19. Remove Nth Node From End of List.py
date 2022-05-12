class Solution:
    def removeNthFromEnd(self, head, n: int):
        tail = head
        size = 0
        while tail:
            size += 1
            tail = tail.next

        steps = size - n
        dummy = ListNode(0, head)
        tail = dummy
        while steps:
            steps -= 1
            tail = tail.next

        tail.next = tail.next.next
        return dummy.next
