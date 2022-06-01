# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        """
        Not O(1) Space, O(n) Time
        dict = {}
        while head:
            if head in dict:
                return True
            dict[head] = 1
            head = head.next

        return False
        """

        # O(1) Space, Slow and Fast pointer
        fast = head
        slow = head

        while fast and fast.next and fast.next.next:
            fast = fast.next.next
            slow = slow.next

            if fast == slow:
                return True

        return False
