class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        res = []

        def dfs(new_s, path, res):
            if new_s is "":
                res.append(path)
                return

            if new_s[0].isdigit():
                path += new_s[0]
                dfs(new_s[1:], path, res)

            else:
                dfs(new_s[1:], path + new_s[0].lower(), res)
                dfs(new_s[1:], path + new_s[0].capitalize(), res)

        dfs(s, "", res)
        return res
