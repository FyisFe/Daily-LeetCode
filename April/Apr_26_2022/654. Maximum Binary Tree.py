# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        def helper(cur):
            if not len(cur):
                return
            max_val = max(cur)
            idx = cur.index(max_val)

            root = TreeNode(max_val)
            root.left = helper(cur[:idx])
            root.right = helper(cur[idx + 1 :])

            return root
