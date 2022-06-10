# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # Iteration
        stack = [root]

        while stack:
            cur = stack.pop()
            if not cur:
                continue
            stack.append(cur.left)
            stack.append(cur.right)
            cur.left, cur.right = cur.right, cur.left

        return root

        # Recursion
        # def helper(node):
        #     if not node:
        #         return
        #     helper(node.left)
        #     helper(node.right)
        #     node.left, node.right = node.right, node.left
        #     return node

        # return helper(root)
