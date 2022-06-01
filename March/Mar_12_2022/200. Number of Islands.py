class Solution:
    def numIslands(self, grid):
        row = len(grid)
        col = len(grid[0])

        visited = [[False for __ in range(col)] for _ in range(row)]
        res = 0

        for i in range(row):
            for j in range(col):
                if visited[i][j] or grid[i][j] == "0":
                    continue

                res += 1
                visited[i][j] = True

                que = [[i, j]]

                while len(que) > 0:
                    item = que.pop()
                    cur_r, cur_c = item[0], item[1]

                    if (
                        cur_r + 1 < row
                        and not visited[cur_r + 1][cur_c]
                        and grid[cur_r + 1][cur_c] == "1"
                    ):
                        visited[cur_r + 1][cur_c] = True
                        que.append([cur_r + 1, cur_c])

                    if (
                        cur_r - 1 >= 0
                        and not visited[cur_r - 1][cur_c]
                        and grid[cur_r - 1][cur_c] == "1"
                    ):
                        visited[cur_r - 1][cur_c] = True
                        que.append([cur_r - 1, cur_c])

                    if (
                        cur_c - 1 >= 0
                        and not visited[cur_r][cur_c - 1]
                        and grid[cur_r][cur_c - 1] == "1"
                    ):
                        visited[cur_r][cur_c - 1] = True
                        que.append([cur_r, cur_c - 1])

                    if (
                        cur_c + 1 < col
                        and not visited[cur_r][cur_c + 1]
                        and grid[cur_r][cur_c + 1] == "1"
                    ):
                        visited[cur_r][cur_c + 1] = True
                        que.append([cur_r, cur_c + 1])
        return res
