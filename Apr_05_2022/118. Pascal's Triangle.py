class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        ans = [[1]]

        for i in range(1, numRows):
            tmp = []

            for j in range(i + 1):
                if j == 0:
                    tmp.append(ans[i - 1][j])
                elif j == i:
                    tmp.append(ans[i - 1][j - 1])
                else:
                    tmp.append(ans[i - 1][j] + ans[i - 1][j - 1])

            ans += [tmp]

        return ans
