from collections import deque
from typing import Deque, List, Tuple


class Solution:
    def maxResult(self, nums: List[int], k: int) -> int:
        # Complexity:
        # - Time: O(N)
        #   where N is the length of `nums`
        # - Space: O(K), worst case, O(1) best case

        n = len(nums)
        if n == 1:
            return nums[0]

        # At this point, we know there are at least 2 numbers
        idx, lastIdx = 0, n - 1
        maxScore = nums[idx] + nums[lastIdx]
        idx += 1
        while idx < lastIdx:
            num = nums[idx]
            # While scores are positive, we just move forward one step at a time
            if num >= 0:
                maxScore += num
                idx += 1
            # Otherwise, if we come to a negative strip, we first try to see if we can fully jump
            # over it; if not then we try to find the optimal way to jump through it
            else:  # `num < 0`
                negativeStripStartIdx, negativeStripEndIdx = idx, idx + 1
                while negativeStripEndIdx < lastIdx and nums[negativeStripEndIdx] < 0:
                    negativeStripEndIdx += 1
                if negativeStripEndIdx - negativeStripStartIdx >= k:
                    # The strip is too long to simply jump over it
                    # Determine the optimal way through it
                    # We use a double-ended queue, the maximum size of which will be `k`
                    scoreDeque: Deque[Tuple[int, int]] = deque(
                        [(maxScore, negativeStripStartIdx - 1)]
                    )
                    for negativeStripIdx in range(
                        negativeStripStartIdx, negativeStripEndIdx
                    ):
                        if negativeStripIdx - scoreDeque[0][1] > k:
                            scoreDeque.popleft()
                        score = nums[negativeStripIdx] + scoreDeque[0][0]
                        while scoreDeque[-1][0] <= score:
                            scoreDeque.pop()
                        scoreDeque.append((score, negativeStripIdx))
                    if negativeStripEndIdx - scoreDeque[0][1] > k:
                        scoreDeque.popleft()
                    maxScore = scoreDeque[0][0]
                idx = negativeStripEndIdx
        return maxScore
