# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        ans = []
        if not root:
            return ans

        que = [root]
        while que:
            new_que = []
            for i in que:
                if i.left:
                    new_que.append(i.left)
                if i.right:
                    new_que.append(i.right)
            ans.append(que[-1].val)
            que = new_que

        return ans
