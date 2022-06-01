class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:

        push = heapq.heappush
        pop = heapq.heappop

        dummy = ListNode()
        tail = dummy

        heap = []

        for idx in range(len(lists)):
            node = lists[idx]
            if node:
                heapq.heappush(heap, (node.val, idx, node))

        while heap:
            _, idx, node = heapq.heappop(heap)
            tail.next = node
            tail = tail.next
            node = node.next
            if node:
                heapq.heappush(heap, (node.val, idx, node))
        return dummy.next
