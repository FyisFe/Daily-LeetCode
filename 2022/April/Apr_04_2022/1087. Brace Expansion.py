class Solution:
    def expand(self, s: str):
        ans = []
        s_len = len(s) - 1

        def helper(idx, cur):
            nonlocal s_len, ans
            if idx > s_len and s[s_len] == "}":
                ans += [cur]
                return
            if idx > s_len:
                return
            if idx == s_len:
                ans += [cur + s[idx]]
            tmp = []
            if s[idx] == "{":
                idx += 1
                while s[idx] != "}":
                    if s[idx] != ",":
                        tmp.append(s[idx])
                    idx += 1

                tmp = sorted(tmp)
                for t in tmp:
                    helper(idx + 1, cur + t)
            else:
                helper(idx + 1, cur + s[idx])

        helper(0, "")
        return ans
