class Solution:
    def isPossibleDivide(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize:
            return False

        hand = sorted(hand)

        hm = {}
        for num in hand:
            if num in hm:
                hm[num] += 1
            else:
                hm[num] = 1

        while hm:
            m = min(hm.keys())
            for i in range(m, m + groupSize):
                if i not in hm:
                    return False
                hm[i] -= 1
                if hm[i] == 0:
                    del hm[i]

        return True
