"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""


class Solution:
    def copyRandomList(self, head: "Optional[Node]") -> "Optional[Node]":
        hm = dict()
        dummy = Node(0)

        cur, copy_cur = head, dummy

        while cur is not None:
            copy_node = Node(cur.val)
            copy_cur.next = copy_node
            hm[cur] = copy_node

            cur, copy_cur = cur.next, copy_cur.next

        cur, copy_cur = head, dummy.next

        while cur:
            copy_cur.random = hm[cur.random] if cur.random in hm else None
            cur, copy_cur = cur.next, copy_cur.next

        return dummy.next
