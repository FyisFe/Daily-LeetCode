class Solution:
    def floodFill(
        self, image: List[List[int]], sr: int, sc: int, newColor: int
    ) -> List[List[int]]:
        val = image[sr][sc]
        m = len(image)
        n = len(image[0])

        visited = [[False for col in range(n)] for row in range(m)]

        def dfs(row, col):
            if row < 0 or row >= m or col < 0 or col >= n:
                return
            if visited[row][col]:
                return
            visited[row][col] = True
            if image[row][col] == val:
                image[row][col] = newColor
                dfs(row, col - 1)
                dfs(row, col + 1)
                dfs(row - 1, col)
                dfs(row + 1, col)

        dfs(sr, sc)

        return image
