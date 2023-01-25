# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        ans = None
        cur_idx = 0

        def inorderTraversal(node):
            nonlocal cur_idx
            nonlocal ans
            if node:
                inorderTraversal(node.left)
                cur_idx += 1
                if cur_idx == k:
                    ans = node.val
                    return
                inorderTraversal(node.right)

        inorderTraversal(root)
        return ans
