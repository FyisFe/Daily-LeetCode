# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        res = 0

        def helper(node, isLeft):
            nonlocal res
            if node is None:
                return

            if isLeft and not node.left and not node.right:
                res += node.val

            helper(node.left, True)
            helper(node.right, False)

        helper(root, False)
        return res
