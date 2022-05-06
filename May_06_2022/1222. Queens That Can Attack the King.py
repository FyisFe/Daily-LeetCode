class Solution:
    def queensAttacktheKing(
        self, queens: List[List[int]], king: List[int]
    ) -> List[List[int]]:

        board = [["#" for _ in range(8)] for __ in range(8)]

        for queen in queens:
            board[queen[0]][queen[1]] = "Q"

        dirc = [(-1, 0), (1, 0), (0, 1), (0, -1), (1, 1), (1, -1), (-1, 1), (-1, -1)]
        x, y = king
        ans = []
        for dx, dy in dirc:
            cx = x
            cy = y
            while True:
                nx = cx + dx
                ny = cy + dy
                if nx < 0 or nx >= 8 or ny < 0 or ny >= 8:
                    break
                if board[nx][ny] == "Q":
                    ans.append([nx, ny])
                    break
                cx = nx
                cy = ny
        return ans
