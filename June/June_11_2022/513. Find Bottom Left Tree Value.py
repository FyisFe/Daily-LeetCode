# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        que = [root]
        res = 0
        while que:
            new_que = []
            res = que[0].val
            for node in que:
                if node.left:
                    new_que.append(node.left)
                if node.right:
                    new_que.append(node.right)
            que = new_que

        return res
