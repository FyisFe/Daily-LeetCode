class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        if "0000" in deadends:
            return -1

        def get_children(lock):
            res = []
            for i in range(4):
                res.append(lock[0:i] + str((int(lock[i]) + 1) % 10) + lock[i + 1 :])
                res.append(
                    lock[0:i] + str((int(lock[i]) - 1 + 10) % 10) + lock[i + 1 :]
                )
            return res

        visited = set(deadends)

        queue = deque()
        queue.append(["0000", 0])

        while queue:
            lock_state, move = queue.popleft()
            if lock_state == target:
                return move
            for child_state in get_children(lock_state):
                if child_state not in visited:
                    visited.add(child_state)
                    queue.append([child_state, move + 1])
        return -1
