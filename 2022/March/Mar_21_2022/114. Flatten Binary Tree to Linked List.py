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
            currentRight = root.right
            root.right = root.left

            tmp = root
            while tmp.right:
                tmp = tmp.right
            tmp.right = currentRight

            root.left = None
            self.flatten(root.right)
