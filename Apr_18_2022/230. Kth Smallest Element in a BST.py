# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        idx = 0
        ans = -1

        def helper(node):
            if node:
                nonlocal idx
                nonlocal ans
                if idx > k:
                    return
                helper(node.left)
                idx += 1
                if idx == k:
                    ans = node.val
                    return
                helper(node.right)

        helper(root)
        return ans
