class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        rows = len(matrix)
        cols = len(matrix[0])
        # Each element stores max length of increasing path starting on r,c
        dp = [[-1] * cols for _ in range(rows)]

        # Traverse the graph using DFS
        def dfs(r, c: int) -> int:
            # If we already have results in `dp` - return it
            if dp[r][c] >= 0:
                return dp[r][c]

            max_path_len = 0
            # Calculate max path length for all neigbours
            # Calling dfs function
            for nr, nc in [(r + 1, c), (r - 1, c), (r, c - 1), (r, c + 1)]:
                if 0 <= nr < rows and 0 <= nc < cols and matrix[nr][nc] > matrix[r][c]:
                    max_path_len = max(max_path_len, dfs(nr, nc))

            # Record path length in `dp`
            dp[r][c] = max_path_len + 1
            return dp[r][c]

        longest = 0
        for r in range(rows):
            for c in range(cols):
                longest = max(longest, dfs(r, c))

        return longest
