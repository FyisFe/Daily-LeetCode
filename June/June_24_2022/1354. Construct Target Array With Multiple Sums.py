class Solution:
    def isPossible(self, target: List[int]) -> bool:
        maxHeap = []
        for num in target:
            heappush(maxHeap, -num)
        totalSum = sum(target)
        while maxHeap:
            top = -maxHeap[0]
            remSum = totalSum - top
            heappop(maxHeap)
            totalSum -= top
            if remSum == 1 or top == 1:
                return True
            if remSum > top or remSum == 0 or top % remSum == 0:
                return False
            heappush(maxHeap, -(top % remSum))
            totalSum += top % remSum
        return False
