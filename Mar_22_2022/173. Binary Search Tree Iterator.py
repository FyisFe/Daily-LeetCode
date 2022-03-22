# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:
    def __init__(self, root: Optional[TreeNode]):
        self.inorderArr = []
        self.traverse(root)

    def next(self) -> int:
        return self.inorderArr.pop(0)

    def hasNext(self) -> bool:
        return len(self.inorderArr) != 0

    def traverse(self, node):
        if node is None:
            return

        self.traverse(node.left)
        self.inorderArr.append(node.val)
        self.traverse(node.right)


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()
