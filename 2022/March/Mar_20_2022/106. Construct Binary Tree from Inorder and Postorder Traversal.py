class Solution:
    def buildTree(self, inorder, postorder):

        inorder_index_map = {}
        for index, value in enumerate(inorder):
            inorder_index_map[value] = index

        postorder_idx = len(postorder) - 1

        def helper(inLeft, inRight):
            nonlocal postorder_idx
            if inLeft > inRight:
                return

            root = TreeNode(postorder[postorder_idx])
            postorder_idx -= 1
            if inLeft == inRight:
                return root

            root.right = helper(inorder_index_map[root.val] + 1, inRight)
            root.left = helper(inLeft, inorder_index_map[root.val] - 1)

            return root

        return helper(0, len(postorder) - 1)
