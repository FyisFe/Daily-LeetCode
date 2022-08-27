class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                p = head
                q = slow
                while p != q:
                    p = p.next
                    q = q.next

                return p

        return None
