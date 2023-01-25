# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:

        """Inorder tree traversal the binary tree and store the values in a list. The list is in ascending order."""
        """inorder_tranversal(TreeNode(2, TreeNode(1), TreeNode(3))) => [1, 2, 3]"""

        def inorder_traversal(root, lst):
            if root:
                inorder_traversal(root.left, lst)
                lst.append(root.val)
                inorder_traversal(root.right, lst)
            return lst

        """Merge two sorted lists into one sorted list."""

        def merge(lst1, lst2):
            lst = []
            while lst1 and lst2:
                if lst1[0] < lst2[0]:
                    lst.append(lst1.pop(0))
                else:
                    lst.append(lst2.pop(0))
            lst.extend(lst1)
            lst.extend(lst2)
            return lst

        return merge(inorder_traversal(root1, []), inorder_traversal(root2, []))
