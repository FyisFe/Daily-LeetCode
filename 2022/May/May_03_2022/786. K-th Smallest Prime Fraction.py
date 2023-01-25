class Solution:
    def kthSmallestPrimeFraction(self, arr: List[int], k: int) -> List[int]:
        minHeap = []
        n = len(arr)
        x = y = 0
        for i in range(n):
            for j in range(i + 1, n):
                if arr[j] != 0:
                    heapq.heappush(minHeap, (arr[i] / arr[j], (arr[i], arr[j])))

        for _ in range(k):
            _, (x, y) = heapq.heappop(minHeap)

        return [x, y]
