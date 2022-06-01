class Solution:
    def calPoints(self, ops: List[str]) -> int:
        ans = []

        for i in ops:
            if i == "C":
                ans.pop(-1)

            elif i == "D":
                ans.append(ans[-1] * 2)

            elif i == "+":
                ans.append(ans[-1] + ans[-2])

            else:
                ans.append(int(i))

        return sum(ans)
