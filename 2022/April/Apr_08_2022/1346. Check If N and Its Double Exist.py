class Solution:
    def checkIfExist(self, arr) -> bool:
        hm = {}
        for i in arr:
            if 2 * i in hm:
                return True

            if i // 2 in hm and i % 2 == 0:
                return True

            hm[i] = 1

        return False
