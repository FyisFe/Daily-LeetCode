# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        res, que = [], [root]

        while que:
            nxt_que = []
            tmp = []

            for i in que:
                if i is not None:
                    nxt_que.append(i.left)
                    nxt_que.append(i.right)
                    tmp.append(i.val)

            que = nxt_que
            if tmp:
                res.append(tmp)

        return res
