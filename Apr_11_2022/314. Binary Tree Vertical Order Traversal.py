# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        hm = {}
        que = [(root, 0)]

        while que:
            new_que = []
            for ele in que:
                node, level = ele
                if node:
                    if level in hm:
                        hm[level].append(node.val)
                    else:
                        hm[level] = [node.val]

                    new_que.append((node.left, level - 1))
                    new_que.append((node.right, level + 1))
            que = new_que
        print(hm)
        sorted_key = sorted(hm)
        ans = []
        for key in sorted_key:
            ans.append(hm[key])

        return ans
