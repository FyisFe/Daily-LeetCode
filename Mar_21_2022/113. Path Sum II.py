# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def pathSum(self, root, targetSum: int):
        def isLeaf(node):
            return node.left == None and node.right == None

        ans = []
        cur = []
        cur_sum = 0

        def helper(node):
            nonlocal cur_sum
            nonlocal cur

            if not node:
                return

            cur.append(node.val)
            cur_sum += node.val

            if isLeaf(node) and cur_sum == targetSum:
                ans.append(cur.copy())

            helper(node.left)
            helper(node.right)

            cur_sum -= node.val
            cur.pop(-1)

        helper(root)

        return ans


test = TreeNode(
    5,
    TreeNode(4, TreeNode(11, TreeNode(7), TreeNode(2))),
    TreeNode(8, TreeNode(13), TreeNode(4, TreeNode(5), TreeNode(1))),
)

sol = Solution()
print(sol.pathSum(test, 22))
