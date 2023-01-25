class Solution:
    def numberOfSteps(self, num: int) -> int:
        res = 0

        def helper(cur):
            if not cur:
                return
            nonlocal res
            res += 1
            if cur % 2:
                helper(cur - 1)
            else:
                helper(cur // 2)

        helper(num)
        return res
