# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        arr = []
        while head:
            arr.append(head.val)
            head = head.next

        def construct(cur_arr):
            if len(cur_arr) == 0:
                return
            if len(cur_arr) == 1:
                return TreeNode(cur_arr[0])

            mid = len(cur_arr) // 2
            root = TreeNode(cur_arr[mid])
            root.left = construct(cur_arr[:mid])
            root.right = construct(cur_arr[mid + 1 :])
            return root

        return construct(arr)
