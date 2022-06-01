# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        ans = []
        cur = []

        def dfs(node):
            if not node:
                return

            cur.append(str(node.val))
            dfs(node.left)
            dfs(node.right)

            if node.left is None and node.right is None:
                ans.append("->".join(cur))

            cur.pop(-1)

        dfs(root)
        return ans
