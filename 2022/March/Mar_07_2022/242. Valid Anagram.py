class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        dict = {}
        for s_chr in s:
            if s_chr in dict:
                dict[s_chr] += 1
            else:
                dict[s_chr] = 1

        for t_chr in t:
            if t_chr not in dict:
                return False
            dict[t_chr] -= 1

        for key in dict:
            if dict[key] != 0:
                return False

        return True
