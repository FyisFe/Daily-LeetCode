class Solution:
    def spiralOrder(self, matrix):
        m, n = len(matrix), len(matrix[0])
        ans = []

        top, right, bottom, left = 0, n - 1, m - 1, 0
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        curD = 0
        x, y = 0, 0

        while len(ans) != m * n:
            ans.append(matrix[x][y])
            if curD == 0 and y == right:
                top += 1
                curD += 1
            elif curD == 1 and x == bottom:
                right -= 1
                curD += 1
            elif curD == 2 and y == left:
                bottom -= 1
                curD += 1
            elif curD == 3 and x == top:
                left += 1
                curD += 1

            curD %= 4
            x += directions[curD][0]
            y += directions[curD][1]

        return ans
