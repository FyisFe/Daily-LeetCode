class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        top, right, bottom, left = 0, n - 1, n - 1, 0
        ans = [[0 for col in range(n)] for row in range(n)]
        filled = 0
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        curD = 0
        x, y = 0, 0
        while filled < n * n:
            filled += 1
            ans[x][y] = filled
            if curD == 0 and y == right:
                curD += 1
                top += 1

            elif curD == 1 and x == bottom:
                curD += 1
                right -= 1

            elif curD == 2 and y == left:
                curD += 1
                bottom -= 1

            elif curD == 3 and x == top:
                curD += 1
                left += 1

            curD %= 4
            x += directions[curD][0]
            y += directions[curD][1]

        return ans
