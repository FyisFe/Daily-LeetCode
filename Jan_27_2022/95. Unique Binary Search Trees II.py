# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        def helper(s, e):
            if s > e:
                return [None]

            if s == e:
                return [TreeNode(s)]

            res = []
            for i in range(s, e + 1):
                left = helper(s, i - 1)
                right = helper(i + 1, e)
                for pair in product(left, right):
                    res.append(TreeNode(i, pair[0], pair[1]))
            return res

        return helper(1, n)
