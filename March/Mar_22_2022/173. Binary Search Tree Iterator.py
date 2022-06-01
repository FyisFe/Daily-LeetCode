# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:
    def __init__(self, root: Optional[TreeNode]):
        self.callStack = []
        cur = root
        while cur:
            self.callStack.append(cur)
            cur = cur.left

    def next(self) -> int:
        if len(self.callStack):
            ans = self.callStack.pop()
            cur = ans.right

            while cur:
                self.callStack.append(cur)
                cur = cur.left

            return ans.val

    def hasNext(self) -> bool:
        return len(self.ans)


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()
