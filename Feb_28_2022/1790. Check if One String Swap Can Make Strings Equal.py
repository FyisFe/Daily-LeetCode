class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        if s1 == s2:
            return True

        s1_list = []
        s2_list = []

        for i in range(len(s1)):
            if len(s1_list) > 2:
                return False

            if s1[i] is not s2[i]:
                s1_list.append(s1[i])
                s2_list.append(s2[i])

        return (
            len(s1_list) == 2 and s1_list[0] == s2_list[1] and s1_list[1] == s2_list[0]
        )
