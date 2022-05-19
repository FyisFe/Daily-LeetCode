class Solution:
    def getLength(self, head):
        tail = head
        res = 0
        while tail:
            res += 1
            tail = tail.next
        return res

    def getIntersectionNode(
        self, headA: ListNode, headB: ListNode
    ) -> Optional[ListNode]:
        aTail = headA
        bTail = headB
        aLen = self.getLength(headA)
        bLen = self.getLength(headB)
        diff = abs(aLen - bLen)
        if aLen > bLen:
            while diff:
                diff -= 1
                aTail = aTail.next
        else:
            while diff:
                diff -= 1
                bTail = bTail.next

        while aTail:
            if aTail == bTail:
                return aTail
            aTail = aTail.next
            bTail = bTail.next
