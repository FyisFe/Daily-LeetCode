class Solution:
    def numberOfWays(self, s: str) -> int:

        ans = 0
        s_len = len(s)

        def dfs(idx, cur):
            nonlocal ans
            if len(cur) == 3:
                ans += 1
                return
            if idx >= s_len:
                return

            if len(cur) == 0 or cur[-1] != s[idx]:
                cur.append(s[idx])
                dfs(idx + 1, cur)
                cur.pop(-1)

            dfs(idx + 1, cur)

        dfs(0, [])


sol = Solution()
sol.numberOfWays("001101")
