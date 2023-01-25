# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        ans = []
        que = [root]

        while que:
            new_que = []
            vals = []
            for node in que:
                if node:
                    vals.append(node.val)
                    new_que.append(node.left)
                    new_que.append(node.right)
            if vals:
                ans.append(vals)
            que = new_que

        return ans
