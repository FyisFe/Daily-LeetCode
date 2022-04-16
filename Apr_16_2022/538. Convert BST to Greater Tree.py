# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        cur = 0

        def helper(node):
            if not node:
                return
            nonlocal cur
            helper(node.right)
            cur += node.val
            node.val = cur
            helper(node.left)

        helper(root)
        return root
