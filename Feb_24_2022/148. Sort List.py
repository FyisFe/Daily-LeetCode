# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur = head
        arr = []
        while cur is not None:
            arr.append(cur.val)
            cur = cur.next

        if len(arr) is 0:
            return None

        arr = sorted(arr)
        new_head = ListNode(arr[0])
        cur = new_head

        for i in range(1, len(arr)):
            node = ListNode(arr[i])
            cur.next = node
            cur = cur.next

        return new_head
