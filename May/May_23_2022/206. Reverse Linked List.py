class Solution:
    def reverseList(self, head):
        if not head or not head.next:
            return head

        def helper(last, cur):
            if cur == None:
                return last
            ans = helper(cur, cur.next)
            cur.next = last if last.val != None else None
            return ans

        return helper(ListNode(None, head), head)
