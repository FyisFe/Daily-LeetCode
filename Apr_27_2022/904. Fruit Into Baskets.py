class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        hm = {}
        i = 0
        res = 0
        for j, fruit in enumerate(fruits):
            if fruit not in hm:
                hm[fruit] = 1
            else:
                hm[fruit] += 1
            while len(hm) > 2 and i < j:
                hm[fruits[i]] -= 1
                if hm[fruits[i]] == 0:
                    hm.pop(fruits[i], None)
                i += 1
            res = max(res, sum(hm.values()))
        return res
