# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        path = []

        def inorderTraversal(node: Optional[TreeNode]) -> bool:
            if node is None:
                return

            inorderTraversal(node.left)
            path.append(node.val)
            inorderTraversal(node.right)

        inorderTraversal(root)
        return all(path[i] < path[i + 1] for i in range(len(path) - 1))
