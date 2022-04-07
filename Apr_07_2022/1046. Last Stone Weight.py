from queue import PriorityQueue


class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        q = PriorityQueue()
        for s in stones:
            q.put(-s)

        while q.qsize() != 1:
            i = q.get()
            j = q.get()

            q.put(i - j)

        return -q.get()
