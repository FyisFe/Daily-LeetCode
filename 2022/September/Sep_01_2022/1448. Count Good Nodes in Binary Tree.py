# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        ans = 0

        def dfs(node, curMax):
            if not node:
                return
            nonlocal ans
            if node.val >= curMax:
                ans += 1
            dfs(node.left, max(curMax, node.val))
            dfs(node.right, max(curMax, node.val))

        dfs(root, -float("inf"))
        return ans
