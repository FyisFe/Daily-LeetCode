from collections import deque


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        ans = []
        queue = deque()

        for right in range(len(nums)):
            left = right + 1 - k

            if queue and left > 0 and nums[left - 1] == queue[0]:
                queue.popleft()

            while queue and queue[-1] < nums[right]:
                queue.pop()

            queue.append(nums[right])

            if right >= k - 1:
                ans.append(queue[0])

        return ans
