class Solution:
    def solveNQueens(self, size):
        solutions = []
        board = [["."] * size for _ in range(size)]

        column = set()
        positive_diagonal = set()
        negative_diagonal = set()

        def backtrack(row):
            if row == size:
                solutions.append(["".join(row) for row in board])
                return

            for col in range(size):
                if (
                    col in column
                    or (row + col) in positive_diagonal
                    or (row - col) in negative_diagonal
                ):
                    continue

                column.add(col)
                positive_diagonal.add(row + col)
                negative_diagonal.add(row - col)
                board[row][col] = "Q"

                backtrack(row + 1)
                column.remove(col)
                positive_diagonal.remove(row + col)
                negative_diagonal.remove(row - col)
                board[row][col] = "."

        backtrack(0)
        return solutions
