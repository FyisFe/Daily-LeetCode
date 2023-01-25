class Solution:
    def movesToStamp(self, s: str, t: str) -> List[int]:
        n, m, s, t, A = len(s), len(t), list(s), list(t), list()

        while True:
            for start in range(m - n + 1):
                for j in range(start, start + n):
                    i = j - start
                    if t[j] == "?":
                        continue
                    if s[i] != t[j]:
                        break
                else:
                    if t[start : start + n] != ["?"] * n:
                        t[start : start + n] = ["?"] * n
                        A += (start,)
                        break
            else:
                break

        return A[::-1] if t == ["?"] * m else []
