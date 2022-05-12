class Solution:
    def countBattleships(self, board: List[List[str]]) -> int:
        m = len(board)
        n = len(board[0])
        ans = 0

        for r in range(m):
            for c in range(n):
                if board[r][c] == "X":
                    if r - 1 >= 0 and board[r - 1][c] == "X":
                        continue
                    if c - 1 >= 0 and board[r][c - 1] == "X":
                        continue
                    ans += 1

        return ans
