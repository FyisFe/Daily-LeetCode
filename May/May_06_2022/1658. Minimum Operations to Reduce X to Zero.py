class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:

        # this is the subarray sum we looking for
        k = sum(nums) - x

        # edge case
        if k == 0:
            return len(nums)

        # find the max-len subarray sum equals to k

        prefix = {
            # prefix sum: leftmost index
        }

        cur = 0
        ans = float("-inf")

        for i, num in enumerate(nums):

            cur += num

            # subarray start from 0
            if cur == k:
                ans = max(ans, i + 1)

            # subarray start from index greater than 0
            elif cur - k in prefix:
                leftmost = prefix[cur - k]
                ans = max(ans, i - leftmost)

            # we only want to keep the leftmost index
            if cur not in prefix:
                prefix[cur] = i

        return len(nums) - ans if ans != float("-inf") else -1
