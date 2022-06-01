class Solution:
    def printTree(self, root: Optional[TreeNode]) -> List[List[str]]:
        height = self.height(root) - 1
        m, n = height + 1, 2 ** (height + 1) - 1
        res = [[""] * n for _ in range(m)]

        def helper(root, r, c):
            if root is None:
                return

            res[r][c] = str(root.val)
            x = 2 ** (height - r - 1)
            helper(root.left, r + 1, c - x)
            helper(root.right, r + 1, c + x)

        helper(root, 0, (n - 1) // 2)
        return res

    def height(self, root):
        if root is None:
            return 0

        return 1 + max(self.height(root.left), self.height(root.right))
