class Solution:
    def tictactoe(self, moves) -> str:
        row = 3
        col = 3

        board = [["" for _ in range(col)] for __ in range(row)]
        turn = 1
        for move in moves:
            if turn == 1:
                board[move[0]][move[1]] = "X"
            else:
                board[move[0]][move[1]] = "O"

            turn = turn * -1

        # check row
        for r in range(row):
            if board[r][0] == board[r][1] == board[r][2] == "O":
                return "B"
            elif board[r][0] == board[r][1] == board[r][2] == "X":
                return "A"

        # check col
        for c in range(col):
            if board[0][c] == board[1][c] == board[2][c] == "O":
                return "B"
            elif board[0][c] == board[1][c] == board[2][c] == "X":
                return "A"

        # check diag

        if board[0][0] == board[1][1] == board[2][2]:
            if board[0][0] == "O":
                return "B"
            elif board[0][0] == "X":
                return "A"
        if board[0][2] == board[1][1] == board[2][0]:
            if board[0][2] == "O":
                return "B"
            elif board[0][2] == "X":
                return "A"

        if len(moves) == 9:
            return "Draw"

        return "Pending"
