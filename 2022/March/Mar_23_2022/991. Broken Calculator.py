# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        ans = 0
        if not root:
            return ans

        que = [root]
        while que:
            new_que = []
            for i in que:
                ans += 1
                if i.left:
                    new_que.append(i.left)
                if i.right:
                    new_que.append(i.right)
            que = new_que

        return ans
