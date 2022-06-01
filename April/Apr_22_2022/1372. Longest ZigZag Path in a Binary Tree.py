# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        ans = 0

        def helper(node, direction, depth):
            if not node:
                return
            nonlocal ans
            ans = max(ans, depth)

            if direction == "l":
                helper(node.right, "r", depth + 1)
                helper(node.left, "l", 1)

            elif direction == "r":
                helper(node.left, "l", depth + 1)
                helper(node.right, "r", 1)

        helper(root.left, "l", 1)
        helper(root.right, "r", 1)

        return ans
