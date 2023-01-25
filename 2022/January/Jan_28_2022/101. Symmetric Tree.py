# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def treeMatch(root1, root2):
            if not root1 and not root2:
                return True

            if (root1 and not root2) or (root2 and not root1):
                return False

            if root1.val != root2.val:
                return False

            return treeMatch(root1.left, root2.right) and treeMatch(
                root1.right, root2.left
            )

        return treeMatch(root.left, root.right)
