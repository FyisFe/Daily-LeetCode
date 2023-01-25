class Solution:
    def canVisitAllRooms(self, rooms) -> bool:
        n = len(rooms)
        que = rooms[0]
        hs = set(que)
        hs.add(0)

        while que:
            new_que = []
            for key in que:
                for new_key in rooms[key]:
                    if new_key not in hs:
                        new_que.append(new_key)
                        hs.add(new_key)

            que = new_que

        return len(hs) == n
