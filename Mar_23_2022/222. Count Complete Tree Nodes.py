# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        ans = 0
        if not root:
            return ans

        def countLeftHeight(node):
            ans = 0
            while node:
                ans += 1
                node = node.left
            return ans

        def countRightHeight(node):
            ans = 0
            while node:
                ans += 1
                node = node.right
            return ans

        lh = countLeftHeight(root)
        rh = countRightHeight(root)
        if lh == rh:
            return 2**lh - 1

        return 1 + self.countNodes(root.left) + self.countNodes(root.right)
