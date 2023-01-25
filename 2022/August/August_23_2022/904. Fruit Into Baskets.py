class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        s, hm, ans = 0, {}, 0

        for i in range(len(fruits)):
            if fruits[i] in hm:
                hm[fruits[i]] += 1
            else:
                hm[fruits[i]] = 1

            while len(hm.keys()) > 2:
                hm[fruits[s]] -= 1
                if hm[fruits[s]] == 0:
                    del hm[fruits[s]]
                s += 1

            ans = max(ans, sum(hm.values()))

        return ans
