class Solution:
    def rotateTheBox(self, box):
        m = len(box)
        n = len(box[0])
        ans = []
        for c in range(n):
            cur = []
            for r in range(m - 1, -1, -1):
                cur.append(box[r][c])
            ans += [cur]

        for c in range(m):
            for r in range(n - 1, -1, -1):
                if ans[r][c] == "#":
                    target_r = None
                    for i in range(r + 1, n):
                        if ans[i][c] == ".":
                            target_r = i
                        else:
                            break
                    if target_r:
                        ans[target_r][c], ans[r][c] = ans[r][c], ans[target_r][c]

        return ans
