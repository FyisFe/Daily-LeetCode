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
        ans = []
        que = [root]

        while que:
            ans.append([node.val for node in que])
            newQue = []
            for node in que:
                if node.left:
                    newQue.append(node.left)
                if node.right:
                    newQue.append(node.right)
            que = newQue
        return ans
