class Solution:
    def minDominoRotations(self, tops: List[int], bottoms: List[int]) -> int:
        MAXINT = 1000000

        def makeAllTopSame(top, bottom):
            swap = MAXINT
            for i in range(1, 7):
                tmp_swap = 0
                can = True
                for j in range(len(top)):
                    if top[j] == i:
                        continue
                    if bottom[j] == i:
                        tmp_swap += 1
                    else:
                        can = False
                        break
                if can:
                    swap = min(tmp_swap, swap)

            return swap

        tb = makeAllTopSame(tops, bottoms)
        bt = makeAllTopSame(bottoms, tops)

        if tb == MAXINT and bt == MAXINT:
            return -1

        return min(tb, bt)
