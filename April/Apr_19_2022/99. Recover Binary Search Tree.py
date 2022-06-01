# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        lst = []

        def inorder_tranversal(node) -> bool:
            if node is None:
                return

            inorder_tranversal(node.left)
            lst.append(node)
            inorder_tranversal(node.right)

        inorder_tranversal(root)

        first, second = None, None

        for i in range(len(lst) - 1):
            if lst[i].val >= lst[i + 1].val:
                if first is None:
                    first = i
                else:
                    second = i + 1
        if second == None:
            lst[first].val, lst[first + 1].val = lst[first + 1].val, lst[first].val
        else:
            lst[first].val, lst[second].val = lst[second].val, lst[first].val
