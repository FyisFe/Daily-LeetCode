class Solution:
    def maximumRemovals(self, s: str, p: str, removable) -> int:
        left = 0
        right = len(removable) - 1
        ans = -1

        def is_subseq(x, y):
            it = iter(y)
            return all(c in it for c in x)

        while left <= right:
            mid = left + (right - left) // 2
            s_copy = list(s)

            for i in range(mid + 1):
                s_copy[removable[i]] = ""
            s_copy = "".join(s_copy)

            if is_subseq(p, s_copy):
                ans = max(ans, mid)
                left = mid + 1
            else:
                right = mid - 1

        return ans + 1
