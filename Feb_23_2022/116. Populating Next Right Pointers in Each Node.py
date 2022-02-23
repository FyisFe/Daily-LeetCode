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
    def connect(self, root: "Optional[Node]") -> "Optional[Node]":
        que = []
        next_que = []

        que.append(root)

        while que[0] is not None:
            for i in range(len(que)):
                if i == len(que) - 1:
                    que[i].next = None
                else:
                    que[i].next = que[i + 1]
                next_que.append(que[i].left)
                next_que.append(que[i].right)

            que = next_que
            next_que = []

        return root
