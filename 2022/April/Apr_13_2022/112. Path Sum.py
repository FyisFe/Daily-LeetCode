# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def isLeaf(node):
            return node.left == None and node.right == None

        def helper(node, cur):
            if node:
                if isLeaf(node) and cur + node.val == targetSum:
                    return True
                return helper(node.left, cur + node.val) or helper(
                    node.right, cur + node.val
                )

        return helper(root, 0)
