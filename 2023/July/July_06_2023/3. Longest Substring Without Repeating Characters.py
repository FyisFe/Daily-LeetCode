class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0

        hm = {s[0]: 1}
        left, right = 0, 1
        ans = 1

        while right < len(s):
            if s[right] in hm:
                while s[left] != s[right]:
                    hm.pop(s[left])
                    left += 1
                left += 1
            else:
                hm[s[right]] = 1
            ans = max(ans, right - left + 1)
            right += 1

        return ans
