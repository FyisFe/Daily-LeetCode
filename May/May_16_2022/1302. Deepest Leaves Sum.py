class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isLeaf(self, node):
        return node.left == None and node.right == None

    def deepestLeavesSum(self, root) -> int:
        que = [root]

        while que:
            new_que = []
            res = 0
            isDeepest = True
            for node in que:
                if not self.isLeaf(node):
                    isDeepest = False
                res += node.val
                if node.left:
                    new_que.append(node.left)
                if node.right:
                    new_que.append(node.right)
            if isDeepest:
                return res
            que = new_que
