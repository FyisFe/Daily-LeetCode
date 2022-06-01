# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def removeLeafNodes(
        self, root: Optional[TreeNode], target: int
    ) -> Optional[TreeNode]:
        def isLeaf(node):
            return node.left == None and node.right == None

        def helper(node, parent_node, isLeft):
            if not node:
                return
            helper(node.left, node, True)
            helper(node.right, node, False)
            if isLeaf(node):
                if node.val == target:
                    if isLeft:
                        parent_node.left = None
                    else:
                        parent_node.right = None

        helper(root.left, root, True)
        helper(root.right, root, False)

        if root == None or (isLeaf(root) and root.val == target):
            return None

        return root
