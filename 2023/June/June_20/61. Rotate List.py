# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        def getListLen():
            cnt, cur = 0, head
            while cur:
                cnt += 1
                cur = cur.next

            return cnt

        listLen = getListLen()
        if listLen == 0 or listLen == 1:
            return head

        k = k % listLen
        if k == 0:
            return head

        newEnd = head
        for _ in range(listLen - k - 1):
            newEnd = newEnd.next

        newHead = newEnd.next
        newEnd.next = None

        cur = newHead
        while cur.next != None:
            cur = cur.next

        cur.next = head

        return newHead
