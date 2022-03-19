class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        preorder_index = 0

        inorder_index_map = {}
        for index, value in enumerate(inorder):
            inorder_index_map[value] = index

        def helper(left, right):
            nonlocal preorder_index
            if left > right:
                return None

            root_value = preorder[preorder_index]
            root = TreeNode(root_value)

            preorder_index += 1

            root.left = helper(left, inorder_index_map[root_value] - 1)
            root.right = helper(inorder_index_map[root_value] + 1, right)

            return root

        return helper(0, len(preorder) - 1)
