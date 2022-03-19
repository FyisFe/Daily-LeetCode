# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:

        if not root:
            return
        ans, que = [], [root]

        while que:
            new_que = []
            tmp = []
            for i in que:
                tmp.append(i.val)
                if i.left:
                    new_que.append(i.left)
                if i.right:
                    new_que.append(i.right)

            ans.append(tmp)
            que = new_que

        return reversed(ans)
