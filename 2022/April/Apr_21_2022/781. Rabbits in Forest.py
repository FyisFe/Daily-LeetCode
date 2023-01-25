class Solution:
    def numRabbits(self, answers) -> int:
        hm = {}
        for ans in answers:
            if ans in hm:
                hm[ans] += 1
            else:
                hm[ans] = 1

        ans = 0
        for key in hm:
            if hm[key] % (key + 1) == 0:
                ans += (key + 1) * hm[key] // (key + 1)
            else:
                ans += (key + 1) * (hm[key] // (key + 1) + 1)

        return ans
