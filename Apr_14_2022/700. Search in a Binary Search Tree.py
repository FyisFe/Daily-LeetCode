# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        ans = None

        def helper(node):
            nonlocal ans
            if not node:
                return
            helper(node.left)
            if node.val == val:
                ans = node
            helper(node.right)

        helper(root)
        return ans
