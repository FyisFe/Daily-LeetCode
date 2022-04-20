class Solution:
    def escapeGhosts(self, ghosts: List[List[int]], target: List[int]) -> bool:
        minTime = abs(target[0]) + abs(target[1])
        for ghost in ghosts:
            d = abs(ghost[0] - target[0]) + abs(ghost[1] - target[1])
            if d <= minTime:
                return False

        return True
