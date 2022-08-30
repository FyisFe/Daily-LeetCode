class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0  # slide window left index
        hm = {}  # character's freq
        ans = 0
        maxFreq = 0
        for i in range(len(s)):
            # i represents right index of slide window
            if s[i] in hm:
                hm[s[i]] += 1
            else:
                hm[s[i]] = 1

            maxFreq = max(maxFreq, hm[s[i]])
            if i - left - maxFreq + 1 <= k:
                ans = max(ans, i - left + 1)
            else:
                hm[s[left]] -= 1
                left += 1

        return ans
