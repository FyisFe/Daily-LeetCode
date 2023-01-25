# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(
        self, list1: Optional[ListNode], list2: Optional[ListNode]
    ) -> Optional[ListNode]:

        dummy_head = ListNode()

        def merge(list1, list2, cur):
            if list1 is None:
                cur.next = list2
                return
            elif list2 is None:
                cur.next = list1
                return
            elif list1.val > list2.val:
                cur.next = ListNode(list2.val)
                list2 = list2.next
            else:
                cur.next = ListNode(list1.val)
                list1 = list1.next
            cur = cur.next
            merge(list1, list2, cur)

        merge(list1, list2, dummy_head)

        return dummy_head.next
