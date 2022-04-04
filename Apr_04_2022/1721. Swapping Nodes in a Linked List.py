# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        cur = head
        count = 0
        while cur:
            count += 1
            cur = cur.next

        target = count - k

        cur = head
        cnt = 1
        front = None
        end = None
        while cur:
            if cnt == k:
                front = cur
            if cnt == target:
                end = cur
            cnt += 1
            cur = cur.next

        front.val, end.val = end.val, front.val
        return head
