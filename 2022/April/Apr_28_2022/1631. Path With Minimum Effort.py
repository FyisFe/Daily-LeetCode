class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:

        rows = len(heights)
        cols = len(heights[0])
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        # Use a heap, store the max diff. we find as the first element to be sorted by.
        hq = [(0, heights[0][0], 0, 0)]
        heapq.heapify(hq)
        # Mark that we visited this node.
        heights[0][0] = "#"
        while hq:
            md, prev, r, c = heapq.heappop(hq)
            heights[r][c] = "#"
            # Given the nature of our algorithm, the first option we come across at the end location
            # will be the most optimal.
            if r == rows - 1 and c == cols - 1:
                return md
            for y, x in directions:
                nr = r + y
                nc = c + x
                if 0 <= nr < rows and 0 <= nc < cols and heights[nr][nc] != "#":
                    # Take the max of the next potential move or the largest we've seen so far.
                    heapq.heappush(
                        hq,
                        (max(abs(heights[nr][nc] - prev), md), heights[nr][nc], nr, nc),
                    )

        return -1
