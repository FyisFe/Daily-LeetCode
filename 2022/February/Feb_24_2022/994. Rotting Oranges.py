class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        row = len(grid)
        col = len(grid[0])

        fresh = set()
        rotten = set()
        for r in range(row):
            for c in range(col):
                if grid[r][c] == 1:
                    fresh.add((r, c))
                elif grid[r][c] == 2:
                    rotten.add((r, c))

        round = 0

        while len(fresh):
            round += 1
            changed = False
            for x, y in rotten.copy():
                for nx, ny in [[x + 1, y], [x - 1, y], [x, y + 1], [x, y - 1]]:
                    if (nx, ny) in fresh:
                        rotten.add((nx, ny))
                        fresh.remove((nx, ny))
                        changed = True
            if not changed:
                return -1
        return round
