"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""


class Solution:
    def connect(self, root: "Node") -> "Node":
        if not root:
            return

        que = [root]

        while len(que) != 0:
            new_que = []
            for i in range(len(que)):
                que[i].next = que[i + 1] if i + 1 < len(que) else None
                if que[i].left:
                    new_que.append(que[i].left)
                if que[i].right:
                    new_que.append(que[i].right)
            que = new_que

        return root
