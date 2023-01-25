class Solution:
    def processNode(self, childNode, nxt_level_prev, nxt_level_leftmost):
        if not childNode:
            return nxt_level_prev, nxt_level_leftmost
        if nxt_level_prev:
            nxt_level_prev.next = childNode
        else:
            nxt_level_leftmost = childNode
        nxt_level_prev = childNode

        return nxt_level_prev, nxt_level_leftmost

    def connect(self, root: Optional["Node"]) -> Optional["Node"]:
        if not root:
            return root

        nxt_level_leftmost = root

        while nxt_level_leftmost:
            nxt_level_prev, cur = None, nxt_level_leftmost
            nxt_level_leftmost = None

            while cur:
                nxt_level_prev, nxt_level_leftmost = self.processNode(
                    cur.left, nxt_level_prev, nxt_level_leftmost
                )
                nxt_level_prev, nxt_level_leftmost = self.processNode(
                    cur.right, nxt_level_prev, nxt_level_leftmost
                )

                cur = cur.next
        return root
