class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        # sort w in ascending order, when w is the same, sort h in descending order
        envelopes.sort(key=lambda x: (x[0], -x[1]))
        height = []
        for w, h in envelopes:
            height.append(h)

        def LIS(nums):
            n = len(nums)
            top = [0 for _ in range(n)]
            piles = 0
            for i in range(n):
                # search the most left smallest number on the top vs current number in the range
                l = 0  # current pile, every search init as 0
                r = piles  # possible future pile
                while l < r:
                    m = l + (r - l) // 2
                    if (
                        top[m] < nums[i]
                    ):  # found a larger number (the largest h < current number)
                        l = m + 1
                    else:
                        r = m

                # a new pile is required, as a larger number is found
                if l == piles:
                    piles += 1
                top[l] = nums[i]

            return piles

        return LIS(height)
