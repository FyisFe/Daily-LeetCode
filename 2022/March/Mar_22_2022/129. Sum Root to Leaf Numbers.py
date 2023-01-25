# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:

        cur = ""
        ans = 0

        def dfs(node):
            nonlocal cur
            nonlocal ans
            if node is None:
                return

            cur += str(node.val)
            if node.left is None and node.right is None:
                ans += int(cur)
                cur = cur[0 : len(cur) - 1]
                return

            dfs(node.left)
            dfs(node.right)
            cur = cur[0 : len(cur) - 1]

        dfs(root)
        return ans
