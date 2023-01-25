# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if root:
            cur_right = root.right
            root.right = root.left

            tail = root
            while tail.right:
                tail = tail.right
            tail.right = cur_right
            root.left = None
            self.flatten(root.right)
