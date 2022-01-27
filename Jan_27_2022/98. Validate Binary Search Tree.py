# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        path = []
        """If the tree is a valid Binary search tree, the inorder traversal of the tree will be ascending sorted."""

        def inorder_tranversal(node: Optional[TreeNode]) -> bool:
            if node is None:
                return

            inorder_tranversal(node.left)
            path.append(node.val)
            inorder_tranversal(node.right)

        inorder_tranversal(root)
        return all(path[i] < path[i + 1] for i in range(len(path) - 1))
