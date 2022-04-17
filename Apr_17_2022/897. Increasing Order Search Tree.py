# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        arr = []

        def helper(node):
            if node:
                helper(node.left)
                arr.append(node.val)
                helper(node.right)

        helper(root)
        ans = TreeNode(arr[0])
        cur = ans
        for node in arr[1:]:
            cur.right = Tree(node.val)
            cur = cur.right
        return ans
