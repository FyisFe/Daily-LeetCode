# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        max_width = 0
        arr = [root]
        idx_arr = [1]

        def getWidth(arr):
            return max(idx_arr) - min(idx_arr) + 1

        while len(arr):
            new_arr = []
            new_idx_arr = []
            max_width = max(max_width, getWidth(idx_arr))
            for (elem, idx) in zip(arr, idx_arr):
                if elem:
                    if elem.left:
                        new_arr.append(elem.left)
                        new_idx_arr.append(idx * 2)
                    if elem.right:
                        new_arr.append(elem.right)
                        new_idx_arr.append(idx * 2 + 1)
            arr = new_arr
            idx_arr = new_idx_arr

        return max_width
