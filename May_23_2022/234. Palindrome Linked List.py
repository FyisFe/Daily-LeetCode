# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        slow = fast = head

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        middle = slow

        prev, actual = None, middle

        while actual:
            nxt = actual.next
            actual.next = prev
            prev = actual
            actual = nxt

        l, r = head, prev

        while r:
            if l.val != r.val:
                return False
            l = l.next
            r = r.next

        return True
