class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        """
        If a substring of s2 has the same characters as s1, then it must be a permutation of s1.
        
        We can use a hashmap to store the characters in s1 and their counts.
        Then use a sliding window to check if the characters of the substring of s2 are a permutation of s1.
        """

        dic = {}
        for i in s1:
            if i in dic:
                dic[i] += 1
            else:
                dic[i] = 1

        for i in range(len(s2) - len(s1) + 1):
            temp = {}
            for j in s2[i : i + len(s1)]:
                if j in temp:
                    temp[j] += 1
                else:
                    temp[j] = 1

            if temp == dic:
                return True

        return False
